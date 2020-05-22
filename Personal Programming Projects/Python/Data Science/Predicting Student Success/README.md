# Machine Learning With Student Data

## Quick Intro

Enclosed is a Jupyter Notebook for some research done at an institution. I've added noise so the real data but the idea still persists. This work uses Machine Learning Models to predict student success in a calculus-based kinematics course.

If you want to see some Exploratory Data Analysis on this project I go in-depth [here](https://github.com/darwin-a/PersonalProjects/tree/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project)

## Problem Statement

Given access to institutional data on students taking an introductory calculus-based kinematics course (e.g. Gender, SAT Scores, ACT Scores, High School GPA, Math Score (when applicable), Force Concept Inventory Scores, etc...) can we predict whether or not a student can be successful.

## Approach

I used several features (College GPA, SAT Scores, etc...) to predict our target variable (student success) and split the data into tresting and training groups. I then created a naive baseline to which I would compare my machine earning models against. I implemented several machine learning algorithms such as Random Forest, Logistic Regression, Support Vector Machine and Neural Networks to model and fit our data. To quantify our models I used the metrics of model accuracy, model classification report (F1 Score, Precision, Accuracy Between Classes, Recall), model confusion matrix, model ROC Curve and AUC score.

## Result

In this notebook I implemented Logistic Regression, Random Forest, Support Vector Machine and Neural Network models for a machine learning supervised classification task. The best result using only institutional variables : **Random Forest w/ AUC Score: 0.7669, Model Accuracy Score : 83.46%, F1 Score : 0.79**

## Importance

The use of machine learning and data mining techniques has exploded in recent years with the field of educational data mining making significant growth in the past two decades. No work has been done at this institution, a primarily undergraduate institution with a variety of ethnic backgrounds. This work will serve as the baseline for all future Machine Learning work at this institution. Predicting student success has many use cases and will ultimately benefit both the students and professors in creating instructional techniques/habits that will gear students towards better/more efficient course performance.

*Note*
The PDF file is a reference to another work for Machine Learning done at a **different institution**. This can be used as a reference for context. 
