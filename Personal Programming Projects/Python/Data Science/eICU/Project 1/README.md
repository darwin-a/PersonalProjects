## Introductory Machine Learning Benchmarks for Neuro ICU Patients on the eICU Critical Care Dataset [(Paper Linked)](https://github.com/darwin-a/PersonalProjects/blob/master/Personal%20Programming%20Projects/Python/Data%20Science/eICU/Project%201/Introductory%20Machine%20Learning%20Benchmarks%20for%20Neuro%20ICU%20Patients%20on%20the%20eICU%20Critical%20Care%20Dataset.pdf)

### Tl:dr
- The APACHE (Acute Physiological And Chronic Health Evaluation) IV/IVa is a tool used to risk-adjust ICU patients for ICU performance benchmarking and quality improvement analysis but it was last improved in 2006. Can we create prediction models that beat these tasks?
- Constructed LOS and mortality prediction models for patients in the Neuro ICU and compared them to the APACHE IV / APACHE IVa prediction models.
- We conclude that constructing models based on the single feature APACHE Score performs notably worse for both prediction tasks.
- Future work will include more features and more complex statistical models. 
  
## Project At A Glance

### Abstract

> Advancements in using medical data have led to the development of several different scoring systems. Some scoring systems have different specific use cases (for example the Glasgow Coma Scale (GCS) while others are for generic towards all ICU patients (APACHE, APS, MPM, etc..). These generic scoring systems are used to assess disease severity and are routinely used to predict patient outcomes (length of stay estimation and mortality probability). The world’s most widely used severity of illness scoring systems today are the APACHE IV/IVa scoring systems which were last developed around 2006-2008. This work examines the most recent APACHE scoring systems and benchmarks its performance on Neuro ICU Patients specific to the eICU Critical Care Dataset. We also construct simple linear regression and logistic regression models and compare their performances.

### Dataset Information

> [eICU Collaborative Research Database](https://eicu-crd.mit.edu/), a multi-center intensive care unit (ICU) database with high granularity data for over 200,000 admissions to ICUs monitored by eICU Programs across the United States. The database is deidentified, and includes vital sign measurements, care plan documentation, severity of illness measures, diagnosis information, treatment information, and more. 

### **Motivation** 

The APACHE (Acute Physiological And Chronic Health Evaluation) IV/IVa is a tool used to risk-adjust ICU patients for ICU performance benchmarking and quality improvement analysis. The APACHE system, among other predictors, provides estimates of the patient probability of mortality given data from the first 24 hours. It is also used for predicting an estimate for a patients length of stay (LOS).

The last time the APACHE scoring system was updated was in 2006 and is 14 years old at the creation of this project. This project is part one of a project to explore whether or not we can use Machine Learning to build a better risk-adjust scoring tool specifically for Neurologal ICU Patients.

### **Problem Statement** 

**Do the recent APACHE Scoring Systems accurately measure patient mortality and LOS for patients in the Neuro ICU in the eICU database1? Can we create better models?** In this work specifically we will be benchmarking simple linear/logistic regression models using a single feature (the APACHE Score) to predict patient mortality.

### Results

In this work we constructed LOS and mortality prediction models for patients in the Neuro ICU and compared them to the APACHE IV / APACHE IVa prediction models. We conclude that constructing models based on the single feature APACHE Score performs notably worse for both prediction tasks. 

#### Length Of Stay (LOS) Predictions

![](https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/eICU/Project%201/graphs/LOS.png)
**Length of Stay model prediction metric scores.** Regression models are matched up against APACHE IV / APACHE IVa predictions. Regression models were cross-validated 1000 times. We report the mean metric score and the standard deviation over all 1000 iterations. \*Note that standard deviation scores are not available for the APACHE prediction models.

#### Mortality Predictions

![](https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/eICU/Project%201/graphs/MORT.png)
**Mortality model prediction metric scores.** Classification models are matched up against APACHE IV / APACHE IVa predictions. Classification models were cross-validated 1000 times. We report the mean metric score and the standard deviation over all 1000 iterations. \*Note that standard deviation scores are not available for the APACHE prediction models.

### Exploratory Data Analysis

![](https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/eICU/Project%201/graphs/DEMOGRAPHICS.png)
**Demographic of the 9,997 ICU unit admissions in the database.** Note that there is a 1:1 ratio for patient-to-unit admission. Since patients can have multiple unit admissions over time only the first record of admission for a patient was taken.
  
![](https://github.com/darwin-a/PersonalProjects/blob/master/Personal%20Programming%20Projects/Python/Data%20Science/eICU/Project%201/graphs/DIAGNOSIS.png)
**Most frequent categories of APACHE diagnosis using clinically meaningful groups deﬁned in the eICU code repository**

![](https://raw.githubusercontent.com/darwin-a/PersonalProjects/b9820671f2c13d9bf1c3a8857254dabecbdefabf/Personal%20Programming%20Projects/Python/Data%20Science/eICU/Project%201/graphs/KDE%20Apache.svg)
**APACHE Score Distribution by Mortality Status.** Left graph indicates APACHE score distribution by mortality status coming out of the ICU. Right graph indicates mortality status at the end of patient admission stay. 

### Files Explained

- Notebook: Jupyter Notebook that holds all my code and analysis done on this dataset
- eICU_models: Scripts I wrote to help cut down code. Split into three different categories.
  - regression: Machine Learning functions to train models for regression problems
  - classification: Machine Learning functions to train models for classification problems.
  - utils: Dataframe cleaning/preprocessing/analysis functions. Metric scoring functions. Model saving functions.
- queries: SQL queries I wrote to analyze the [eICU Collaborative Research Database](https://eicu-crd.mit.edu/)

### Citations

| Citation |  |
| --- | --- |
| eICU Repository | https://github.com/mit-lcp/eicu-code |
| eICU Paper | https://www.nature.com/articles/sdata2018178 |
| eICU Collaborative Research Database | https://eicu-crd.mit.edu/ |

### Contact Me

| Contact Method |  |
| --- | --- |
| Professional Email | ddagunosprofessional@gmail.com |
| School Email | ddagunosschool@gmail.com |
| LinkedIn | https://www.linkedin.com/in/ddagunos/ |
