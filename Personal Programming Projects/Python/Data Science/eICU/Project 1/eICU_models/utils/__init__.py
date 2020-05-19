
# Data manipulation
import pandas as pd
import numpy as np

# Model Saving
import joblib

from sklearn.preprocessing import binarize
from sklearn.model_selection import train_test_split

#######################################
##### APACHE COMPARISON FUNCTIONS #####
#######################################

def apache_analysis(df,version,print_values=True):
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

    # encode columns
    binarize_encode_target_columns([df])
    
    
    apache_df = {'apacheversion': version,
    'predictedicumortality': df['icu_death_prediction_label'].sum(),
    'actualicumortality': df['icu_deaths'].sum(),
    'predictedhospitalmortality':df['hosp_death_prediction_label'].sum() ,
    'actualhospitalmortality':df['hosp_deaths'].sum(),
    'predictedhospitallos':df['predictedhospitallos'].mean(),
    'unabridgedhosplos':df['unabridgedhosplos'].mean(),
    'predictediculos':df['predictediculos'].mean(),
    'unabridgedunitlos':df['unabridgedunitlos'].mean()}
    
    apacheiv_analysis = pd.DataFrame(apache_df,index = [0])

    if print_values:
        print('Analysis of APACHE {}'.format(version))
        print('Pred ICU Deaths:', np.round(df['icu_death_prediction_label'].sum(),3))
        print('ICU Deaths:',np.round(df['icu_deaths'].sum(),3))
        print('Pred Hospital Deaths:', np.round(df['hosp_death_prediction_label'].sum(),3))
        print('Hospital Deaths:',np.round(df['hosp_deaths'].sum(),3))
        print('Pred Hospital Length Of Stay:', np.round(df['predictedhospitallos'].mean(),3))
        print('Hospital Length Of Stay:',np.round(df['unabridgedhosplos'].mean(),3))
        print('Pred ICU Length Of Stay:', np.round(df['predictediculos'].mean(),3))
        print('ICU Length Of Stay:',np.round(df['unabridgedunitlos'].mean(),3))
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
    
def series_handle_na_values(series,na_value,replacement):
    """
    Vectorized handling of null values
    
    Parameters
    -----------
    series : pandas series object 
        series object holding specific data
            
    na_value : [int,string,etc..]
            the na value you want to replace
            
    replacement: [int,string,etc...]
            the value put in place for the na_value
    
    """
    series = series.values
    series = np.where(series==na_value,replacement,series)
    return series