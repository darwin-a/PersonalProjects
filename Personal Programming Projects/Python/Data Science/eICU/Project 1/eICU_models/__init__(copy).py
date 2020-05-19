"""
-------------------------------------------------------------------
Title: Functions for Ad-Hoc Analysis/Machine Learning for the eICU Database
Description: More detailed description explaining the purpose.
eICU version: N/A
References: N/A. 
------------------------------------------------------------------
"""
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:51:57 2020 - My Birthday!

@author: ddagu - ddagunosschool@gmail.com

eICU_models
===========

Provides
    1. Functions for Plug and Play Analysis of eICU Data
        - : Some functions are tailored for a specific purpose and as such, columns are 
        - : already defined and will only work under certain conditions. 
    2. Functions for creating training and testing dataframes
    3. ML Functions for CV testing and scoring for both regression and classification problems

TO ADD:
    1. Support For Neural Networks
    2. Fix metric score generation
        - CV Models are hard coded for the specific metrics given

Notebook Reference:
    - All functions have been used my work for the eICU dataset and are available on the github
      for examples. 
"""

# Data manipulation
import pandas as pd
import numpy as np

# Classification Metrics
from sklearn.metrics import (classification_report as cr, roc_auc_score as auroc, 
                             average_precision_score as prc, accuracy_score as acc, confusion_matrix as cm)

# Regression Metrics 
from sklearn.metrics import r2_score, mean_squared_error as mse, mean_absolute_error as mae

# Model Saving
import joblib


#######################################
##### APACHE COMPARISON FUNCTIONS #####
#######################################

def apache_analysis(df,version,print=True):
    """
    Analysis comparing predicted mortality and length of stay predictions
    to established ground truth for an APACHE version.  

    NOTE: No column names have been changed from the SQL database
          so this will not work if you have changed any relevant columns

          Here is a list
          : actualicumortality
          : actualhospitalmortality
          : apacheversion
          : predictedicumortality
          : predictedhospitalmortality
          : predictedhospitallos
          : unabridgedhosplos
          : predictediculos
          : unabridgedunitlos

          Mortality Predictions

    Parameters
    ----------
    df : pandas dataframe object
        dataframe object grabbed from SQL Queries. More specifically
        SQL Query # 
        Query Reference Here : 

    version : string
        string indicating APACHE Version, i.e. 'IV' or 'IVa'

    Returns
    -------
    pandas dataframe object
        dataframe object returning comparisons between Mortality/LOS predictions
        to established ground truth for an apache version.

    Example
    -------

    # concatenate both versions through the function
    > analysis = pd.concat([apache_analysis(apacheiv,'IV'),apache_analysis(apacheiva,'IVa')],axis=1)
    > analysis

    apacheversion	                IV	            IVa
    predictedicumortality	    813.098367	    740.337009
    actualicumortality	        463.000000	    463.000000
    predictedhospitalmortality	1365.558676	    1263.459066
    actualhospitalmortality	    846.000000	    846.000000
    predictedhospitallos	    97671.142437	103577.745953
    unabridgedhosplos	        81548.184200	81548.184200
    predictediculos	            35387.274613	41183.602045
    unabridgedunitlos	        34898.196600	34898.196600
    """
    # Lets drop NA values
    df.dropna(inplace=True)

    # map values actual icu deaths and hospital deaths
    df['icu_deaths']=df['actualicumortality'].map(lambda status: 0 if status == 'ALIVE' else 1)
    df['hosp_deaths'] = df['actualhospitalmortality'].map(lambda status: 0 if status == 'ALIVE' else 1)
    
    apache_df = {'apacheversion': version,
    'predictedicumortality': df['predictedicumortality'].sum(),
    'actualicumortality': df['icu_deaths'].sum(),
    'predictedhospitalmortality':df['predictedhospitalmortality'].sum() ,
    'actualhospitalmortality':df['hosp_deaths'].sum(),
    'predictedhospitallos':df['predictedhospitallos'].sum(),
    'unabridgedhosplos':df['unabridgedhosplos'].sum(),
    'predictediculos':df['predictediculos'].sum(),
    'unabridgedunitlos':df['unabridgedunitlos'].sum()}
    
    apacheiv_analysis = pd.DataFrame(apache_df,index = [0])

    if print:
        print('Analysis of APACHE {}'.format(version))
        print('Pred ICU Deaths:', df['predictedicumortality'].sum())
        print('ICU Deaths:',df['icu_deaths'].sum())
        print('Pred Hospital Deaths:', df['predictedhospitalmortality'].sum())
        print('Hospital Deaths:',df['hosp_deaths'].sum())
        print('Pred Hospital Length Of Stay:', df['predictedhospitallos'].sum())
        print('Hospital Length Of Stay:',df['unabridgedhosplos'].sum())
        print('Pred ICU Length Of Stay:', df['predictediculos'].sum())
        print('ICU Length Of Stay:',df['unabridgedunitlos'].sum())
        print('')

    return apacheiv_analysis.set_index('apacheversion').T


# lets create an error dictionary

def grab_error(df):
    """
    Grab the percent error in predictions. We get error as
    (theoretical-actual)/actual.

    NOTE : Used with the output of the apache_analysis function

    Parameters
    ----------
     df : pandas dataframe object
        dataframe object that was returned from the apache_analysis function

    Returns
    -------
    pandas dataframe object
        dataframe object with errors

    Example
    -------
    > err_df = grab_error(analysis)
    > err_df = round(err_df*100,2
    > err_df

                            IV	     IVa
    icu_mortality_error	    75.62	59.90
    hosp_mortality_error	61.41	49.35
    hosp_los_error	        19.77	27.01
    icu_los_error	        1.40	18.01
    """
    
    
    # create error dict
    error_dict = {}
    
    for version in df.columns:
        df_version = df.loc[:,version]
        # find test error
        icu_mortality_error = (df_version['predictedicumortality']-df_version['actualicumortality'])/df_version['actualicumortality']
        hosp_mortality_error = (df_version['predictedhospitalmortality']-df_version['actualhospitalmortality'])/df_version['actualhospitalmortality']
        hosp_los_error=(df_version['predictedhospitallos']-df_version['unabridgedhosplos'])/df_version['unabridgedhosplos']
        icu_los_error=(df_version['predictediculos']-df_version['unabridgedunitlos'])/df_version['unabridgedunitlos']
        
        version_dict = {'icu_mortality_error':icu_mortality_error,
                      'hosp_mortality_error':hosp_mortality_error,
                        'hosp_los_error': hosp_los_error,
                      'icu_los_error':icu_los_error}
        
        # append version to error_dict
        error_dict[version] = version_dict
    
    return pd.DataFrame(error_dict)

def binarize_encode_target_columns(apache_df_list):
    """
    Function to binarize predictions and encode the actual 
    target columns for the apache prediction tables
    
    NOTE - all column names are the same names for when
    they were queried from the database. Will not work
    if you have renamed
    
    predictedicumortality,predictedhospitalmortality
    actualicumortality,actualhospitalmortality.
    
    If you have, please rename them back or change
    them directly from this function.
    
    Parameters
    ------------
    apache_df_list: list of dataframe objects 
                    The dataframes for which we will be performing
                    the operations on, given that
                    
    Returns
    ------------
    None, directly makes changes to the dataframes listed in 
    apache_df_list. Four new columns will be added
    
    icu_death_prediction_label : class labels from the 
                                 predictedicumortality column
                                 
    hosp_death_predictions_label : class labels from the 
                                   predictedhospitalmortality column
                                   
    icu_deaths : class labels for the actualicumortality column
    
    hosp_deaths : class labels for the actualhospitalmortality column
    
    """
    # Grab the dataframes
    apache_df_list = apache_df_list

    # set the threshold
    threshold = 0.5

    # loop through the dataframes binarize predictions and encode labels for established truth
    for df in apache_df_list:
        # binarize predictions
        icu_death_predictions = binarize(df['predictedicumortality'].values.reshape(-1,1), threshold=threshold)
        hosp_death_predictions = binarize(df['predictedhospitalmortality'].values.reshape(-1,1), threshold=threshold)
        df['icu_death_prediction_label'] = icu_death_predictions
        df['hosp_death_prediction_label'] = hosp_death_predictions

        # encode lobels for actual data
        df['icu_deaths']=df['actualicumortality'].map(lambda status: 0 if status == 'ALIVE' else 1)
        df['hosp_deaths'] = df['actualhospitalmortality'].map(lambda status: 0 if status == 'ALIVE' else 1)


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


def regression_model_cv(X_train_set,y_train_set,scaler,model,cv,print_iterations=False, filename = ''):
    """
    Automate splitting dataframes into training and testing dataframes.
    The training dataframe is used for model selection and cross validation.
    The testing dataframe is used for model evaluation
    
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

        # save the data in a joblib file
        
        
        # grab the scores for every metric
        regression_scores = regression_scoring(y_val,y_pred,regression_metrics=[r2_score,mse,mae],print_values=False)

        # unpack the scores
        r2_scores_lst.append(regression_scores['r2_score'])
        mean_squared_error_lst.append(regression_scores['mean_squared_error'])
        mean_absolute_error_lst.append(regression_scores['mean_absolute_error'])

        # print statement every 100 iterations to let us know where we are at
        if (index+1) % 100 == 0 and print_iterations:
            print(f'Finished {index+1} Iterations')
            
    # save the model if user specified gave a filename
    
    if filename == '':
        pass
    else:
        # save the file
        save_model(model,filename)
        
        # save and create metadata
        metadata = {'model':model,
                   'X_train_set':X_train_set,
                   'y_train_set':y_train_set,
                   'cv':cv,
                   'regression_scores':regression_scores}
        
        save_model_metadata(metadata,filename)
        
        
        
    return [r2_scores_lst,mean_squared_error_lst,mean_absolute_error_lst]

# Model score list

def reg_cross_val_scoring(reg_score_list,score_names,print_values=False):
    holder = {}
    score_name_index = 0
    for lst in reg_score_list:
        # create dictionary value
        holder[score_names[score_name_index]] = {'Mean' : np.mean(lst), 'Standard Deviation' : np.std(lst)}
        
        if print_values:
            print(f'{score_names[score_name_index]} - Mean: {np.mean(lst):.3f} +/- {np.std(lst):.3f}')
            
        # move up in the score name index
        score_name_index +=1
        
    return holder

#######################################
### APACHE CLASSIFICATION FUNCTIONS ###
#######################################

def classification_scoring(y_true,y_pred_labels,y_pred_probabilities,
                       classification_label_metrics,classification_probability_metrics, optional_kwargs = {}, **kwargs):
    """
    Function to print and store the scores for 
    all relevant classification scores within a list. 
    If your results seem off or flipped, check to make sure
    that your labels for your classes are correct for your
    workflow, i.e. choosing the right class for 
    predicted probabilities.
    
    
    y_true : {array_like}
            established truth values we compare our
            prediction metrics against
            
    y_pred_label : {array_like}
            model label predictions that we compare 
            against the established truth
            
    y_pred_probabilities : {array_like}
                            model probability predictions that we compare 
                            against the established truth. 
            
    classification_label_metrics : list 
                        List of metric functions (without the call)
                        that take in labels for the
                        predicted input (y_true,y_pred_labels, **optional_kwargs)
                        
    
    classificatio_probability_metrics : list 
                        List of metric functions (without the call)
                        that take in probabilities or labels for the
                        predicted input. (y_true,y_pred_probabilities, **optional_kwargs)
                        
    optional_kwargs : nested dictionary, optional
                    key-value pairings of specific metrics that you want
                    written in {classification:{'key':value}}
                    
                    EXAMPLE:
                    optional_kwargs = {classification_report:{'output_dict':True},
                                        roc_auc_score:{'average':'weighted'}}
                        
    Returns
    -----------
    Dictionary holding classification scores
    
    EXAMPLE OUTPUT
    
    {'roc_auc_score': 0.7331094896656479,
     'average_precision_score': 0.21008780368014515}
    """
    
    
    # classificaiton dict to hold scores
    classification_scores = {}
    
    # for loop through classification metrics
    for metric in classification_label_metrics:
 
        # grab the score
        score = metric_score(y_true,y_pred_labels,
                                         metric,optional_kwargs, **kwargs)
        
        # unpack the dictionary and append to scores dictonary
        for key, value in score.items():
            classification_scores[key] = value

       
        
    # the same workflow applies to the probability metrics
    for metric in classification_probability_metrics:
        
        score = metric_score(y_true,y_pred_probabilities,
                                            metric,optional_kwargs, **kwargs)
        for key, value in score.items():
            classification_scores[key] = value


    return classification_scores


# MODEL TRAINING 
from sklearn.metrics import (classification_report as cr, roc_auc_score as auroc, 
                             average_precision_score as prc, accuracy_score as acc, confusion_matrix as cm)

def classification_model_cv(X_train_set,y_train_set,scaler,model,cv,print_iterations=False, filename=''):
    """
    Automate splitting dataframes into training and testing dataframes.
    The training dataframe is used for model selection and cross validation.
    The testing dataframe is used for model evaluation
    
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
    
    cr_lst = []
    auroc_lst = []
    prc_lst = []
    acc_lst = []
    cm_lst = []

    print(f'Number Of Splits {cv.get_n_splits()}')
    
    try:
        split = cv.split(X_train_set)
    except TypeError as e:
        pass
    else:
        split = cv.split(X_train_set,y_train_set)
        
        
    for index, (train_index,val_index) in enumerate(split):

        # construct training and testing sets for every split
        X_train, X_val = X_train_set[train_index], X_train_set[val_index]
        y_train, y_val = y_train_set[train_index], y_train_set[val_index]

        # Perform scaling on our training and test sets within the CV
        # to prevent data leakage
        scaler = scaler
        X_train = scaler.fit_transform(X_train.reshape(-1,1))
        X_val  = scaler.transform(X_val.reshape(-1,1))
        
        # ravel training and validation data
        y_train, y_val = y_train.ravel(), y_val.ravel()

        # predict the data
        y_pred_labels = model.fit(X_train,y_train).predict(X_val)
        y_pred_probabilities = model.fit(X_train,y_train).predict_proba(X_val)
        
        # grab the positive probabilities
        positive_class_index = np.argmax(model.classes_)
        y_pred_probabilities = y_pred_probabilities[:,[positive_class_index]]
        
        # grab the scores for every metric
        classification_scores = classification_scoring(y_val,y_pred_labels, y_pred_probabilities,
                                                       classification_label_metrics=[cr,acc,cm],
                                                       classification_probability_metrics=[auroc,prc],
                                                       print_values=False)
        
        
        # unpack the scores
        cr_lst.append(classification_scores['classification_report'])
        auroc_lst.append(classification_scores['roc_auc_score'])
        prc_lst.append(classification_scores['average_precision_score'])
        acc_lst.append(classification_scores['accuracy_score'])
        cm_lst.append(classification_scores['confusion_matrix'])

                                                                                
                                                                                

        # print statement every 100 iterations to let us know where we are at
        if (index+1) % 100 == 0 and print_iterations:
            print(f'Finished {index+1} Iterations')
            
    # save the model if user specified gave a filename
    
    if filename == '':
        pass
    else:
        # save the file
        save_model(model,filename)
        
        # save and create metadata
        metadata = {'model':model,
                   'X_train_set':X_train_set,
                   'y_train_set':y_train_set,
                   'cv':cv,
                   'classification_scores':classification_scores}
        
        save_model_metadata(metadata,filename)
        
    
    return [cr_lst,auroc_lst,prc_lst,acc_lst,cm_lst]


# Model score list

def classification_cross_val_scoring(class_score_list,class_cm,score_names_class,print_values=False):
    score_holder = {}
    score_name_index = 0
    
    
    for lst in class_score_list:
        # create dictionary value
        score_holder[score_names_class[score_name_index]] = {'Mean' : np.mean(lst), 'Standard Deviation' : np.std(lst)}
        
        if print_values:
            print(f'{score_names_class[score_name_index]} - Mean: {np.mean(lst):.3f} +/- {np.std(lst):.3f}')
            
        # move up in the score name index
        score_name_index +=1
        
    # for classification confuson matrix
    
    try:
        # initialize array to hold the confusion matris values
        x = np.array([['',''],['','']],dtype ='object')
        
        # loop through each index and grab the mean and std
        for row in range(2):
            for col in range(2):

                mean_score = np.mean(np.array(class_cm), axis=0)[row][col]
                std = np.std(np.array(class_cm), axis=0)[row][col]
                string =  f'{mean_score:.3f} +/- {std:.3f}'
                x[row][col] = string

        # add that to score holder
        score_holder['confusion_matrix'] = np.array(x)

        if print_values:
            print(f'Confusion Matrix : {np.array(x)}')

    except:
        pass
            
    return score_holder


#######################################
####### APACHE Utility FUNCTIONS ######
#######################################

def metric_score(y_true,y_pred, metric, optional_kwargs = {}, print_values=False):
    """
    Metric scoring helping function. Works with regression metrics
    and classification metrics that require either labels or probabilities.
    Can be used independently but is necessary for the classification_scoring
    and regression_scoring functions
    
    Parameters
    -----------
    y_true : {array_like}
        established truth values we compare our
        prediction metrics against
            
    y_pred : {array_like}
            model predictions that we compare against the established truth. 
            Can be continuous (regression), labels (classification), probabilities (classification)
            
    metric: regression or classification metric object
            e.g. classification_report, r2_score
    
    optional_kwargs : nested dictionary, optional
                    key-value pairings of specific metrics that you want
                    written in {classification:{'key':value}}
                    
                    EXAMPLE:
                    optional_kwargs = {classification_report:{'output_dict':True}}
                    
    Returns
    -----------
    dictionary object holding metric_name as key and metric score as value
    
    Example Output
    -------------------
    
    For Classification:
    
    > metric_score(y_true,y_pred,roc_auc_score)
    
    'roc_auc_score': 0.7331094896656479
    
    Regression:
    
    > metric_score(y_true,y_pred,r2_score)
    
    {'r2_score': 0.11760667624053311}
     
    > metric_score (y_true,y_pred,mean_squared_error)
    {mean_squared_error': 16.64014409276284}
    
    """
    
    # if you passed in optional_kwargs then we'll go through them here
        # if not we'll do default scoring
    metric_name = str(metric).split()[1]
    if metric in optional_kwargs:
        print(f'{metric_name} with optional arguments {optional_kwargs[metric]}')
        score = metric(y_true,y_pred, **optional_kwargs[metric])
    else:
        score = metric(y_true,y_pred)


    # try/except block to catch error if metric doesnt print out a number
    # as it prints different metric score form than the other metrics
    if print_values:
        try:
            print(metric_name + f': {score:.3f}')
        except:
            print(metric_name + f': \n {score:}')

    return {metric_name:score}


def train_test_dataframes(df,features,targets, **kwargs):
    """
    Automate splitting dataframes into training and testing dataframes.
    The training dataframe is used for model selection and cross validation.
    The testing dataframe is used for model evaluation
    
    Parameters
    -----------
    df : dataframe object 
        dataframe object holding all relevant features and targets
            
    features : [list of strings]
            list of column names that will be used to predict the targets
            
    targets: [list of strings]
            list of column names that you are trying to predict
                    
    **kwargs: keyword arguments
              The only keyword arguments allowed here are arguments for sklearn's
              train_test_split()
    Returns
    -----------
    Training and testing dataframe objects respectively. Column names
    are ordered from inputted features to inputted targets.
    
    Example Code
    -------------------
    
    x = [[num,num+1] for num in range(8)]
    y = [0 if num < 4 else 1 for num in range(8)]
    data = {'features':x,
           'targets':y}
    df = pd.DataFrame(data)

    features = ['features']
    targets = ['targets']

    train_df, test_df = train_test_dataframes(df=df,features=features,
                                                targets=targets, test_size=0.2, random_state=1)
    """
    
    df = df

    features_df = df.loc[:,features].values
    targets_df = df.loc[:,targets].values
    
    X_train, X_test, y_train, y_test = train_test_split(features_df,targets_df,**kwargs)
    
    # lets store our testing results in a "vault" that we'll only use towards the end
    X_test = X_test
    X_test = pd.DataFrame(X_test,columns=features)
    y_test = pd.DataFrame(y_test,columns=targets)
    test_df = pd.concat([X_test,y_test],axis=1)
    
    # lets do the same with our validation data
    # lets store our testing results in a "vault" that we'll only use towards the end
    X_train = X_train
    X_train = pd.DataFrame(X_train,columns=features)
    y_train = pd.DataFrame(y_train,columns=targets)
    train_df = pd.concat([X_train,y_train],axis=1)
    
    return train_df, test_df

def save_model(model,filename):
    """
    save model using joblib

    Parameters
    ----------
    model : scikit learn object
    filename : string
        name of the file
    """
    joblib.dump(model,filename)
    
def save_model_metadata(metadata,filename):
    """
    save model using joblib

    Parameters
    ----------
    metadata : dictionary object holding relevant metadata
               for a specific training model

               EX: # create metadata
                    metadata = {'model':model,
                                'X_train_set':X_train_set,
                                'y_train_set':y_train_set,
                                'cv':cv,
                                'regression_scores':regression_scores}
    filename : string
        name of the file
    """
    filename = filename + ' metadata'
    joblib.dump(metadata,filename)



