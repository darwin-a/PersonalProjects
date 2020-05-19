# Data manipulation
import pandas as pd
import numpy as np

# Classification Metrics
from sklearn.metrics import (classification_report as cr, roc_auc_score as auroc, 
                             average_precision_score as prc, accuracy_score as acc, confusion_matrix as cm)

# Model Saving
import joblib

from eICU_models.utils import metric_score, save_model, save_model_metadata

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

def classification_model_cv(X_train_set,y_train_set,scaler,model,cv,print_iterations=False, save_model_data=False, model_filename=None):
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
            
    # save the model if user wants
    if save_model_data:
        if model_filename is None:
            model_filename == str(model).split('(')[0]
        else:
            # save the file
            save_model(model,model_filename)

            # save and create metadata
            metadata = {'model':model,
                       'X_train_set':X_train_set,
                       'y_train_set':y_train_set,
                       'cv':cv,
                       'classification_scores':classification_scores}

            save_model_metadata(metadata,model_filename)
        
    
    return [cr_lst,auroc_lst,prc_lst,acc_lst,cm_lst]


# Model score list

def classification_cross_val_scoring(class_score_list,score_names_class,class_cm=None,print_values=False,get_cm_metrics=False):
    score_holder = {}
    score_name_index = 0
    
    
    for lst in class_score_list:
        # create dictionary value
        score_holder[score_names_class[score_name_index]] = {'Mean' : np.mean(lst), 'Standard Deviation' : np.std(lst)}
        
        if print_values:
            print(f'{score_names_class[score_name_index]} - {np.mean(lst):.3f} +/- {np.std(lst):.3f}')
            
        # move up in the score name index
        score_name_index +=1
        
    # for classification confuson matrix
    
    if class_cm is not None:
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
                
        if get_cm_metrics:
            # create metric holders
            sensitivity_list = []
            specificity_list = []
            ppv_list = []
            npv_list = []

            # Loop through each matrix and append metric scores to list
            for confusion_matrix in class_cm:
                cm_metrics = confusion_matrix_metrics(confusion_matrix)

                sensitivity_list.append(cm_metrics[0])
                specificity_list.append(cm_metrics[1])
                ppv_list.append(cm_metrics[2])
                npv_list.append(cm_metrics[3])

            
            score_holder['confusion_matrix_metrics'] = {'Sensitivity': {'Mean' : np.mean(sensitivity_list), 'Standard Deviation' : np.std(sensitivity_list)},
                                                        'Specificity': {'Mean' : np.mean(specificity_list), 'Standard Deviation' : np.std(specificity_list)},
                                                        'PPV': {'Mean' : np.mean(ppv_list), 'Standard Deviation' : np.std(ppv_list)},
                                                        'NPV': {'Mean' : np.mean(npv_list), 'Standard Deviation' : np.std(npv_list)}}

            if print_values:
                for metric,scores in score_holder['confusion_matrix_metrics'].items():
                    print(f"{metric} - {scores['Mean']:.3f} +/- {scores['Standard Deviation']:.3f}")

    return score_holder


def confusion_matrix_metrics(cm):
    """

    Parameters
    ----------
    cm : ndarray of shape (n_classes, n_classes) 
        scikit-learn confusion matrix object

    Returns
    -----------
    list containing confusion matrix
    sensitivity, specificity, ppv, npv
    """

    tn, fp, fn, tp = cm.ravel()
    
    # sensitivity -TP/P
    sensitivity = tp/(tp+fn)

    # specificity - TN/N
    specificity = tn/(tn+fp)

    # precision / positive predictive value - TP/(TP+FP)
    ppv = tp/(tp+fp) 

    # negative predictive value - TN/(TN+FN)
    npv = tn/(tn+fn)

    return [sensitivity,specificity,ppv,npv]


