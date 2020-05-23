# Student Insight Project

Enclosed in this folder is all my analysis done on a real-world student dataset as well as visualizations. 

If you want my work done in creating an early failure detection algorithm click [here](https://github.com/darwin-a/PersonalProjects/edit/master/Personal%20Programming%20Projects/Python/Data%20Science/Early%20Student%20Failure%20Detection%20Algorithm/README.md)

### Tl;dr

- EDA Project exploring real student data in a college kinematics course. Data has been de-identified.
- Goal: Explore characteristics that could potentially impact a student's physics grade and understanding of Newtonian Mechanics
<details>
  <summary><strong>Factors that could potentially impact `PHY Grade` </strong></summary>
  
- `Measures` that could influence `PHY Grade`
  - Current College GPA: r = 0.49
  - FCI Post: r = 0.42
  - FCI Pre: r = 0.38
  - ACT Composite: r = 0.33
  - HS GPA: r = 0.33
  - SAT Total: r = 0.31

- `Dimensions` that could influence `PHY Grade`
  - Gender: Males outperform Females
  - Under-represented Minority (URM) Status & Ethnicity: Non-URM students outperform URM students. `White` population outperforms all Non-URM students. `Hispanic` population outperforms URM students. On average, no one scores above or at a 3.0 (B)
  - First Generation Status: Non-First Generation Students do better than First Generation Students. Males still outperform females
  - Instruction Type: `Interactive Teaching` shows that students perform better in both `PHY Grade` & `FCI Post`
  - Professor: Professors who have the same `Instruction Type` have `PHY Grades` that vary largely (see below)
</details>

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

### Some Exploratory Data Analysis (Physics Grade Distributions, Pre/Post Force Concept Inventory (FCI) Scores)
*<small>Note: FCI is a measure of a student's understanding of Newtonian Mechanics. Used to assess student's understanding of Newtonian Mechanics post-course</small>*


####  Preliminary Analysis Pre-Course & Correlation Plot

<p align="center"><img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/score_distributions.png" width = 700><p>

- The true mean for **SAT Composite Scores** is 1145.35 ±  148.19
- The true mean for **ACT Composite Scores** lies between 25.56 ± 4.09
- Students initially do very poorly on the **FCI Pre Test** with a mean score of 12.56 ± 6.36
- Students do better on the **FCI Post Test** with a mean score of 15.99 ± 6.65. However, this average is scoring a **53% on the test** indicating most students do come out of the course understanding  Newtonian Mechanics

<p align="center"><img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/CORRELATION_PLOT.png" width = 1200><p>
  
- `Measures` that could influence `PHY Grade`
  - Current College GPA: r = 0.49
  - FCI Post: r = 0.42
  - FCI Pre: r = 0.38
  - ACT Composite: r = 0.33
  - HS GPA: r = 0.33
  - SAT Total: r = 0.31

- `Dimensions` that could influence `PHY Grade`
  - Gender: Males outperform Females
  - Under-represented Minority (URM) Status & Ethnicity: Non-URM students outperform URM students. `White` population outperforms all Non-URM students. `Hispanic` population outperforms URM students. On average, no one scores above or at a 3.0 (B)
  - First Generation Status: Non-First Generation Students do better than First Generation Students. Males still outperform females
  - Instruction Type: `Interactive Teaching` shows that students perform better in both `PHY Grade` & `FCI Post`
  - Professor: Professors who have the same `Instruction Type` have `PHY Grades` that vary largely (see below)


#### By Gender

<p align="center"><img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/PHY_Grade_Sex.png" width = 600><p>

<p float="left" align='center'>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/FCI_Pre_Sex.png" width = 450>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/FCI_Post_Sex.png" width = 450>
<p>

<p align="center"><img src="https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/gender_table.png" width=500><p>

#### By Minority Status

<p align="center"><img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/URM_STATS_PHY.png" width = 1000><p>

<p align="center"><img src="https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/URM_table.png" width=700><p>
 
<p float="left" align='center'>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/URM_STATS_FCI_PRE.png" width = 450>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/URM_STATS_FCI_Post.png" width = 450>
<p>
  

#### By First Generation Status and Gender


<p align="center"><img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/First_Generation_PHY.png" width = 1000><p>

<p align="center"><img src="https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/first_gen_table.png" width=700><p>
 
<p float="left" align='center'>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/FIRSTGEN_FCIPRE.png" width = 450>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/FIRSTGEN_FCIPOST.png" width = 450>
<p>

#### By Instruction Type
  
 <p float="left" align='center'>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/INSTRUCTION_TYPE_PHYGRADE.png" width = 450>
  <img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/FCI_Student_Gain_IT.png" width = 450>
<p>

<p align="center"><img src="https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/IT_table.png" width=500><p>
 
##### By Instruction Type and Professor
 
<p align="center"><img src = "https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/INSTRUCTION_TYPE_PHYGRADE_BY_INSTRUCTOR.png" width = 1200><p>

<p align="center"><img src="https://raw.githubusercontent.com/darwin-a/PersonalProjects/master/Personal%20Programming%20Projects/Python/Data%20Science/Student%20Insight%20Project/images/IT_by_instructor_table.png" width=500><p>
  
### Contact Me

| Contact Method |  |
| --- | --- |
| Professional Email | ddagunosprofessional@gmail.com |
| School Email | ddagunosschool@gmail.com |
| LinkedIn | https://www.linkedin.com/in/ddagunos/ |
