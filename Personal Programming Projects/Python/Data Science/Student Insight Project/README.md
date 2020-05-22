# Student Insight Project

Enclosed in this folder is all my analysis done on a real-world student dataset as well as visualizations. 

If you want my work done in creating an early failure detection algorithm click [here](https://github.com/darwin-a/PersonalProjects/tree/master/Personal%20Programming%20Projects/Python/Data%20Science/Predicting%20Student%20Success)

## Introduction

In this notebook, we will conduct exploratory data analysis using Pandas and Seaborn to find any relationships between student background and student performance in an introductory college kinematics course. We will also explore any possible reasonings to our insights and finish up with any key insights that we find. 

### Motivation

The use of machine learning and data mining techniques has exploded in recent years with the field of educational data mining making significant growth in the past two decades. Physics Education Research has benefitted from educational data mining adding to the scientific literacy tremendously. However, relatively less work was done in primarily undergraduate institutions (PUI) and minority-serving institutions. As part of an effort to provide evidence for the reproducibility of educational studies for a variety of student body as well exploring possible gender or racial gaps in student’s performance, data was collected over a year-long period for a number of introductory physics courses at this institution (both a PUI and Hispanic serving institution) to understand factors that affect students’ performance in an introductory Physics Course as well as the Force Concept Inventory

### Problem Statement

Given access to institional data on students taking an introductory calculus-based mechanics course (e.g. Gender, SAT Scores, ACT Scores, High School GPA, Math Score (when applicable), Force Concept Inventory Score, etc...), can we identify any trends in student performance and more importantly, can we find an explanation for these trends. To accomplish this task, we will use a set of real-world data collected from students enrolled in Physics 131 for the entire 2017 Academic Year at this institution.


<details>
  <summary><strong>Click to see all measures and dimensions of the dataset </strong></summary>
  
| **Measures:** continuous, quantitative values that can be aggregrated | Description |
|:---------|:-----------------|
| HS_GPA | High School GPA  |                                     
| Total_GPA | GPA Taken After College Term of the course    |                               
| SAT Verbal | SAT Verbal Score   |                              
| SAT_Math | SAT Mathematics Score  |                                  
| SAT_Total | SAT Composite Score  |                                 
| ACT English | ACT English Score   |                              
| ACT Math | ACT Mathematics Score    |                                
| ACT Reading | ACT Reading Comprehension Score      |                            
| ACT Science | ACT Science Score      |                           
| ACT Composite | Composite ACT Score    |                            
| Total GPA (at start of the Enrolled Term) | GPA at the start of the Enrolled College Term|
| MAT_Point | Grade Point received for course based on a 4-point scale
| PHY Grade | Grade Point received for course based on a 4-point scale              |                      
| FCI Pre | Force Concept Inventory Score Pre-Course                               |       
| FCI Post | Force Concept Inventory Score Post-Course|
| Student_Gain | Normalized gain on the Force Concept Inventory post-course |

|**Dimensions:** discrete, qualitative values used to categorize, segment and reveal details in data |Description |
|:-----------|:---------|
|Sex | Anatomy of an individual's reproductive system (M or F)|
|Admit Type | Admitted either as a Transfer or Freshman|
|IPEDS Ethnic Group | Ethnic Classification|
|URM Status | Under-represented Minority Status      |                       
|First Generation Status | First Generation Status    |               
|Native Freshman Cohort Year | Cohort Year     |         
|Current College | College    |                          
|Current Major | Major   |                            
|Current Subplan |      |                         
|STEM Status | STEM Status   |                              
|Pell Status | Pell Grant Status|
|MAT Catalog # | Catalog #        |                        
|MAT Course Name | Course Name    |                        
|MAT Instructor | Math Instructor made into Integer Variables for classified reasons   |                           
|MAT Enrollment Term |      |                    
|MAT Section | Section Taken|
|PHY Catalog # | Catalog #       |                         
|PHY Course Name | Course Name       |                       
|PHY Instructor | Physics Instructor made into Integer Variables for classified reasons    |                          
|PHY Enrollment Term | Term Enrolled (Summer, Fall, Winter, Spring)           |               
|PHY Section | Section Taken       |
|IT | Instruction Type (Classified as traditional, hybrid or interactive (1,2,3 respectively)|
|Class Size | 0 if Class is bigger than 100 students, 1 if less|

</details>

### Exploratory Data Analysis
