## Cluster-Based Oversampling Method for Improving Survival Prediction of Hepatocellular Carcinoma Patients - Revisited - Darwin Agunos [(Paper Linked)](https://github.com/darwin-a/PersonalProjects/blob/master/Personal%20Programming%20Projects/Python/Data%20Science/HCC%20Project/Cluster-Based%20Oversampling%20Method%20for%20Improving%20Survival%20Prediction%20of%20Hepatocellular%20Carcinoma%20Patients%20-%20Revisiited%20-%20Darwin%20Agunos.pdf)

### Tl:dr
- Created mortality prediction models for Hepatocellular Carcinoma patients than performed better than predicted by utilzing different imputation and oversampling techniques referenced in academic papers
- Neural Network Classifier paired with a 5-NN imputation technique utilizing the HEOM distance metric and K-Means SMOTE to create synthetic samples of our under-represented class yielded and Leave-One-Out Cross Validation improved over previously reported results in the following metrics
  - ~9% accuracy increase
  - ~15% AUROC score increase
  - ~17% F1 score increase
 
## Project Information

### Abstract

> Liver cancer is the sixth most frequently diagnosed cancer. According to the American Cancer Society, it is estimated that there will be 30,000 liver cancer related deaths and 40,000 new cases diagnosed. Hepatocellular Carcinoma (HCC) represents more than 90% of primary liver cancer cancers. Clinicians assess patient treatment based on previously diagnosed cases, which may not always apply to a specific patient given the genetic heterogeneity of the human population. Over the years, research studies have been developing strategies for assisting clinicians in decision making using machine learning techniques to extract knowledge from clinical data. This paper aims to add to the previous methodology of using cluster-based sampling to improve HCC survival prediction models by replicating the original work and incorporating different imputation techniques and classification algorithms. Our results are evaluated in terms of survival prediction. Our approach yielded better prediction scores previously reported, suggesting an improvement over the previous methodology used in Hepatocellular Carcinoma prediction models. 

### [Dataset Information<sup>1</sup>](https://archive.ics.uci.edu/ml/datasets/HCC+Survival)

HCC dataset was obtained at a University Hospital in Portugal and contains several demographic, risk factors, laboratory and overall survival features of 165 real patients diagnosed with HCC. The dataset contains 49 features (found below) selected according to the EASL-EORTC (European Association for the Study of the Liver - European Organisation for Research and Treatment of Cancer) Clinical Practice Guidelines, which are the current state-of-the-art on the management of HCC.

This is an heterogeneous dataset, with 23 quantitative variables, and 26 qualitative variables. Overall, missing data represents 10.22% of the whole dataset and only eight patients have complete information in all fields (4.85%). The target variables is the survival at 1 year, and was encoded as a binary variable: 0 (dies) and 1 (lives). A certain degree of class-imbalance is also present (63 cases labeled as 0 and 102 as 1).

A detailed description of the HCC dataset (feature's type/scale, range, mean/mode and missing data percentages) provided at the end


### **Motivation** 

Liver cancer is the sixth most frequently diagnosed cancer, and, particularly Hepatocellular Carcinoma (HCC) represents more than 90% of primarily liver cancers. Clinicians assess each patient's treatment on the bases of evidence-based medicine, which may or may not apply to a specific patient, given biological variability among individuals. Over the years, research studies have been developing strategies for assisting clinicians in decising making using computational methods to extract knowledge from the clinical data. However, some of these studies have limitations that have not been addressed yet such as the presence of missing data or the heterogeneity between patients.

This work aims to tackle these limitations

### **Problem Statement** 

**Can we develop a mortality prediction model that can outperform previous results in the context of Hepatocellular Carcinoma patients?** More specifically, we will be comparing different sampling, imputation and statistical learning models against results from six years prior. This paper branches the gap between the [original HCC prediction paper (mpublished 2016 in the Journal of Biomedical Informatics)](https://www.sciencedirect.com/science/article/pii/S1532046415002063) and recent advances in [statistical imputation (published 2019 in the HDSR)](https://hdsr.mitpress.mit.edu/pub/ct67j043)

### Results

Our approach for mortality prediction models yielded better scores previously reported, suggesting an improvement over the previous methodology used in Hepatocellular Carcinoma prediction models. More specifically, the use of a Neural Network Classifier paired with a 5-NN imputation technique utilizing the HEOM distance metric and K-Means SMOTE to create synthetic samples of our under-represented class yielded and Leave-One-Out Cross Validation yielded a
- **~9% accuracy increase**
- **~15% AUROC score increase**
- **~17% F1 score increase**

For more information on methodology, results and background information the paper I wrote is [linked here](https://github.com/darwin-a/PersonalProjects/blob/master/Personal%20Programming%20Projects/Python/Data%20Science/HCC%20Project/Cluster-Based%20Oversampling%20Method%20for%20Improving%20Survival%20Prediction%20of%20Hepatocellular%20Carcinoma%20Patients%20-%20Revisiited%20-%20Darwin%20Agunos.pdf)

#### Mortality Predictions

<p align="center">
<img src="https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/HCC%20Project/images/results_table.png" width="500"></p>
 <p align="center"><strong>Performance metrics for each approach and classifier</strong></p>


### Files Explained

- HCC Project: Jupyter Notebook that holds all my code and analysis done on this dataset
- research papers: A few academic papers I read to do this project
- Cluster-Based Oversampling Method for Improving Survival Prediction of Hepatocellular Carcinoma Patients - Revisiited - Darwin Agunos: Paper I wrote conveying all of my work
- data: data I used for this project. Available on both Kaggle and the UCI repository
- graphs: AUROC, Confusion Matrices pictures for each classifier with each method
- images: images used to readme/jupyter notebook

### Citations

[<sup>1</sup>HCC Survival Data Set](https://archive.ics.uci.edu/ml/datasets/HCC+Survival) <br>
[<sup>2</sup>Miriam Seoane Santos, Pedro Henriques Abreu, Pedro J Garcia-Laencina, Adelia Simao, Armando Carvalho, A new cluster-based oversampling method for improving survival prediction of hepatocellular carcinoma patients, Journal of biomedical informatics, 58, 49-59, 2015](https://www.sciencedirect.com/science/article/pii/S1532046415002063)<br>
[<sup>3</sup>Machine Learning with Statistical Imputation for Predicting Drug Approvals](https://hdsr.mitpress.mit.edu/pub/ct67j043) <br>
[<sup>4</sup>American Cancer Society](https://www.cancer.org/research/cancer-facts-statistics/all-cancer-facts-figures/cancer-facts-figures-2012.html) <br>
[<sup>5</sup>American Cancer Society](https://www.cancer.org/content/dam/cancer-org/research/cancer-facts-and-statistics/annual-cancer-facts-and-figures/2020/cancer-facts-and-figures-2020.pdf) <br>
[<sup>6</sup>Synthetic Minority Oversampling Technique](http://rikunert.com/SMOTE_explained) <br>
[<sup>7</sup>K-Nearest-Neighbors Algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) <br>
[<sup>8</sup>StatQuest Explaining KNN](https://www.youtube.com/watch?v=HVXime0nQeI&feature=emb_title)  <br>
[<sup>9</sup>Heterogeneous Euclidean-Overlap Metric](https://towardsdatascience.com/the-proper-way-of-handling-mixed-type-data-state-of-the-art-distance-metrics-505eda236400) <br>
[<sup>10</sup>GAP Statistic](https://statweb.stanford.edu/~gwalther/gap) <br>
[<sup>11</sup>K-means clustering](https://towardsdatascience.com/k-means-clustering-8e1e64c1561c) <br>
[<sup>12</sup>AUC](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5) <br>
[<sup>13</sup>F-Measure](https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9) <br>
[<sup>14</sup>Predicting Drug Approvals: Supplementary Materials Paper](https://hdsr.mitpress.mit.edu/pub/dno70rhw?readingCollection=72befc2a) <br>
[<sup>15</sup>Linear Digressions](http://lineardigressions.com/episodes/2019/11/17/using-machine-learning-to-predict-drug-approvals) <br>
[<sup>16</sup>Sci-Kit Learn](https://scikit-learn.org/stable/whats_new/v0.22.html) <br>
[<sup>17</sup>Distython](https://towardsdatascience.com/distython-5de10f342c93) <br>
[<sup>18</sup>AutoImpute](https://kearnz.github.io/autoimpute-tutorials/)

### Contact Me

| Contact Method |  |
| --- | --- |
| Professional Email | ddagunosprofessional@gmail.com |
| School Email | ddagunosschool@gmail.com |
| LinkedIn | https://www.linkedin.com/in/ddagunos/ |


### Dataset Information Table

|**Prognostic Factors**|Description|Type/Scale|Range|Mean or Mode|Missingness (%)|
|:------------------:|:------------------------------------------------|:----------:|:------------:|:-----------:|:-------------:|
|**Gender**|Gender (nominal)|Qualitative/dichotomous|0/1|1|0|
|**Symptoms**|Symptons (nominal)|Qualitative/dichotomous|0/1|1|10.91|
|**Alcohol**|Alcohol (nominal)|Qualitative/dichotomous|0/1|1|0|
|**HBsAg**|Hepatitis B Surface Antigen (nominal)|Qualitative/dichotomous|0/1|0|10.3|
|**HBeAg**|Hepatitis B e Antigen (nominal)|Qualitative/dichotomous|0/1|0|23.64|
|**HBcAb**|Hepatitis B Core Antibody (nominal) |Qualitative/dichotomous|0/1|0|14.55|
|**HCVAb**|Hepatitis C Virus Antibody (nominal)|Qualitative/dichotomous|0/1|0|5.45|
|**Cirrhosis**|Degenerative disease of the liver (nominal)|Qualitative/dichotomous|0/1|1|0|
|**Endemic Countries**|Relating to the Country (nominal)|Qualitative/dichotomous|0/1|0|23.64|
|**Smoking**|Does the patient smoke? (nominal)|Qualitative/dichotomous|0/1|1|24.85|
|**Diabetes**|Is the patient diabetic? (nominal)|Qualitative/dichotomous|0/1|0|1.82|
|**Obesity**|Is the patient obese (nominal)|Qualitative/dichotomous| 0/1| 0| 6.06|
|**Hemochromatosis**|Disorder where too much iron builds up in your body(nominal) |Qualitative/dichotomous|0/1|0|13.94|
|**AHT**| Arterial Hypertension (nominal) |Qualitative/dichotomous|0/1|0|1.82|
|**CRI**| Chronic Renal Insufficiency(nominal)   |Qualitative/dichotomous|0/1|0|1.21|
|**HIV**|Human Immunodeficiency Virus    (nominal)  |Qualitative/dichotomous|0/1|0|8.48|
|**NASH**|Nonalcoholic Steatohepatitis (nominal)  |Qualitative/dichotomous|0/1|0|13.33|
|**Esophageal Varices**|Presence of abnormal, dilated veins in the food pipe (nominal)    |Qualitative/dichotomous|0/1|1|31.52|
|**Splenomegaly**|Enlarged spleen(nominal)   |Qualitative/dichotomous|0/1|1|9.03|
|**Portal Hypertension**| Increase of blood pressure within a system of veins (nominal)|Qualitative/dichotomous|0/1|1|6.67|
|**Portal Vein Thrombosis**| Blood clot of the portal vein(nominal)  |Qualitative/dichotomous|0/1|1|1.82|
|**Liver Metasis**| Cancerous tumor that has spread to the liver from a cancer that started in another place in the body (nominal)  |Qualitative/dichotomous|0/1|0|2.42|
|**Radiological Hallmark**| Radiological Characteristic Present (nominal)   |Qualitative/dichotomous|0/1|0|1.21|
|**Age at diagnosis**| Age of diagnosis (integer) |Quantitative/ratio|20-93|64.69|0
|**Grams/day**| Grams of Alcohol per day(continuous)  |Quantitative/ratio|0-500|71.01|29.09
|**Packs/year**|Packs of cigarettes per year (continuous)   |Quantitative/ratio|0-510|20.46|32.12
|**Performance Status**| Performance status (ordinal)  |Qualitative/ordinal|0,1,2,3,4|0|0
|**Encefalopathy**|Medical term used to describe disease that affects brain structure or function (ordinal)  |Qualitative/ordinal|1,2,3|1|0.61
|**Ascites**|Excess level of fluid built up in the abdomen (ordinal)  |Qualitative/ordinal|1,2,3|1|1.21
|**INR**| International Normalized Ratio. Test to see how well blood clots (continuous)  |Quantitative/ratio|0.84-4.82|1.42|2.42
|**AFP**| Alpha-Fetoprotein. Important fetal serum protein that doubles as a tumor marker in adults. (continuous)     |Quantitative/ratio|1.2-1,810,346|19299.95|4.85
|**Hemoglobin**| Red protein responsible for the transportation of oxygen in the blood of vertebrates (continuous)    |Quantitative/ratio|5-18.7|12.88|1.82
|**MCV**| Mean Corpusucular Volume. Measure of the average volkume of a red blood corpuscle (continuous)  |Quantitative/ratio|69.5-119.6|95.12|1.82
|**Leukocytes**|White blood cell count (continuous)   |Quantitative/ratio|2.2-13,000|1473.96|1.82
|**Platelets**| Components that help blood to clot (continuous) |Quantitative/ratio|1.71-459,000|113206.44|1.82
|**Albumin**|Presence of proteins that are soluble in water (continuous)    |Quantitative/ratio|1.9-4.9|3.45|3.64
|**Total Bil**|Total Bilirubin. Orange-yellow pigment formed in the liver from te breakdown of hemoglobin (continuous)      |Quantitative/ratio|0.3-40.5|3.09|3.03
|**ALT**|Alanine transaminase. Catalyzes the two parts of the alanine cycle. (continuous)   |Quantitative/ratio|11-420|67.09|2.42
|**AST**|Aspartate transaminase. Pyridoxal phosphate. Ratio of AST/ALT commonly measures as biomarkers for liver health (continuous)    |Quantitative/ratio|17-553|69.38|1.826
|**GGT**|Gamma glutamyl transferase. Enzyme that catalyzes the transfer of gamma-glutamyl functional groups (continuous)   |Quantitative/ratio|23-1575|268.03|1.82
|**ALP**|Alkanine phosphatse. Enzyme found in bile ducts, bone, intestine, placenta and tumors. (continuous)   |Quantitative/ratio|1.28-980|212.21|1.82
|**TP**|Total proteins. Measures the total amount of albumin and globulin in the body. (continuous)    |Quantitative/ratio|3.9-102|8.96|6.67
|**Creatinine**| Waste product that comes from wear and tear on the muscles of the body (continuous)   |Quantitative/ratio|0.2-7.6|1.13|4.24
|**Number of Nodules**|Amount of abnormally grown tissues (integer)   |Quantitative/ratio|0-5|2.74|1.21
|**Major Dimension**|Length of nodule (continuous)  |Quantitative/ratio|1.5-22|6.85|12.12
|**Dir. Bil**|Amount of conjugated bilirubin that travels from the liver to the small intestine (continuous)    |Quantitative/ratio|0.1-29.3|1.93|26.67
|**Iron**|Iron (continuous)   |Quantitative/ratio|0-224|85.6|47.88
|**Sat**| Oxygen Saturation (continuous)  |Quantitative/ratio|0-126|37.03|48.48
|**Ferritin**| Ferritin (continuous)   |Quantitative/ratio|0-2230|439|48.48|Qualitative/dichotomous|0/1|0|6.06|







