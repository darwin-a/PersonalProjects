# Data manipulation
import pandas as pd
import numpy as np

# Regression Metrics 
from sklearn.metrics import r2_score, mean_squared_error as mse, mean_absolute_error as mae
import joblib
from eICU_models.utils import metric_score, save_model, save_model_metadata

#######################################
##### APACHE REGRESSION FUNCTIONS #####
#######################################

def regression_scoring(y_true,y_pred,regression_metrics,optional_kwargs = {}, **kwargs):
    """
    Calculates all regression metrics stored in 
    the regression_metrics argument. Prints out
    the metric scores and also returns the
    scores to a dictionary
    
    Parameters
    -----------
    
    y_true : {array_like}
            established truth values we compare our
            prediction metrics against
            
    y_pred : {array_like}
            model predictions for that we compare 
            against the established truth
            
    regression_metrics : list 
                        List of metric functions (without the call)
                        that take in input (y_true,y_pred,**optional_kwargs)
                        
    optional_kwargs : nested dictionary, optional
                    key-value pairings of specific metrics that you want
                    written in {classification:{'key':value}}
                    
                    EXAMPLE:
                    optional_kwargs = {mean_squared_error:{'squared':False},
                                        multioutput:{'average':'weighted'}}
                        
    Returns
    -----------
    Dictionary holding regression scores
    
    
    Example
    -----------
    > regression_metrics = [r2_score,mse,mae]
    > y_true = df.loc[:,'unabridgedunitlos']
    > y_pred = df.loc[:,'predictediculos']
    > icu_los_scores = regression_scoring(y_true,y_pred,regression_metrics, average='weighted' 
    > icu_los_scores
    
    icu_los_prediction_scores
    r2_score: 0.118
    mean_squared_error: 16.640
    mean_absolute_error: 2.588
    
    {'r2_score': 0.11760667624053311,
     'mean_squared_error': 16.64014409276284,
     'mean_absolute_error': 2.5878831680942103}
     
    """
    
    # classificaiton dict to hold scores
    regression_scores = {}
    
    # for loop through classification metrics
    for metric in regression_metrics:
 
        # grab the score from the custom function
        score = metric_score(y_true,y_pred,
                            metric,optional_kwargs, **kwargs)
        
        # unpack the dictionary and append to scores dictonary
        for key, value in score.items():
            regression_scores[key] = value
            
    return regression_scores


def regression_model_cv(X_train_set,y_train_set,scaler,model,cv,print_iterations=False, save_model_data=False, model_filename=None):
    """
    Regression cross validation modeling
    
    Parameters
    -----------
    X_train_set : {sparse_matrix}  
                features matrix of shape (n_samples,n_features)
            
    y_train_set : {sparse_matrix}
                target matrix of shape (n_samples,)
            
    targets: scaler object
            pre-processing object that fits and transforms the training data
            as well as transforming the validation data
                    
    model: model object
            The Machine Learning algorithm you are using for regression predictions
            
    cv: cross validation object
    
    Returns
    -----------
    Nested list filled of regression scores given in the order
    [r2_score,mean_squared_error,mean_absolute_error]
    
    """
    
    r2_scores_lst = []
    mean_squared_error_lst = []
    mean_absolute_error_lst = []

    print(f'Number Of Splits {cv.get_n_splits()}')
    for index, (train_index,val_index) in enumerate(cv.split(X_train_set)):

        # construct training and testing sets for every split
        X_train, X_val = X_train_set[train_index], X_train_set[val_index]
        y_train, y_val = y_train_set[train_index], y_train_set[val_index]

        # Perform scaling on our training and test sets within the CV
        # to prevent data leakage
        scaler = scaler
        X_train = scaler.fit_transform(X_train.reshape(-1,1))
        X_val  = scaler.transform(X_val.reshape(-1,1))

        # predict the data
        y_pred = model.fit(X_train,y_train).predict(X_val)
        
        # grab the scores for every metric
        regression_scores = regression_scoring(y_val,y_pred,regression_metrics=[r2_score,mse,mae],print_values=False)

        # unpack the scores
        r2_scores_lst.append(regression_scores['r2_score'])
        mean_squared_error_lst.append(regression_scores['mean_squared_error'])
        mean_absolute_error_lst.append(regression_scores['mean_absolute_error'])

        # print statement every 100 iterations to let us know where we are at
        if (index+1) % 100 == 0 and print_iterations:
            print(f'Finished {index+1} Iterations')
            
    
    
     # save the model if user wants
    if save_model_data:
        if model_filename is None:
            model_filename == str(model).split('(')[0]
        else:
            # save the file
            print('model_filename')
            save_model(model,model_filename)

            # save and create metadata
            metadata = {'model':model,
                    'X_train_set':X_train_set,
                    'y_train_set':y_train_set,
                    'cv':cv,
                    'regression_scores':regression_scores}
            
            save_model_metadata(metadata,model_filename)
          
        
    return [r2_scores_lst,mean_squared_error_lst,mean_absolute_error_lst]

# Model score list

def reg_cross_val_scoring(reg_score_list,score_names,print_values=False):
    holder = {}
    score_name_index = 0
    for lst in reg_score_list:
        # create dictionary value
        holder[score_names[score_name_index]] = {'Mean' : np.mean(lst), 'Standard Deviation' : np.std(lst)}
        
        if print_values:
            print(f'{score_names[score_name_index]} - {np.mean(lst):.3f} +/- {np.std(lst):.3f}')
            
        # move up in the score name index
        score_name_index +=1
        
    return holder