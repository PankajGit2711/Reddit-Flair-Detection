# Reddit-Flair-Detection (https://reddit-application-flair.herokuapp.com/)

Reddit Flair Detection is an web-based application for detecting reddit flairs tag based on thier features like title, content, url.
This is project is the solution for the assignment given by MIDAS Labs - IIIT Delhi

The Project is done in by using two methods and thus divided into two parts:

1. Method - 1:- Uses Data Scrapped from Simple PRAW module and various Machine Learning Algorithms
2. Method - 2:- Uses Data Scrapped from Pushshift API Wrapper of PRAW module and Various Machine Learning & Deep Learning Algorithms

## Directory Structure

The Directory Structure for both of the methods along with their description of files is decribed below:

### Method - 1

  1. [Web-App](https://github.com/PankajGit2711/Reddit-Flair-Detection/tree/master/Method%20-%201/Web_App) - Contains the files for flask web application.
  2. [Data Scrapping](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%201/1.%20Data%20Scrapping.ipynb) - Contains the Code for Scrapping Reddit Data Using Simple PRAW Library.
  3. [Data Cleaning](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%201/2.%20Data%20Cleaning.ipynb) - Contains the code for cleaning the collected data.
  4. [Exploratory Data Analysis](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%201/3.%20Exploratory%20Data%20Analysis.ipynb) - Contains the code for Data Analysis.
  5. [Modelling](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%201/4.%20Modelling.ipynb) - Contains the code for testing various Machine Learning Models on the reddit data collected.
  6. [Cleaned Reddit Data](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%201/Cleaned%20Reddit%20Data.csv) - CSV File of Cleaned reddit data collected by using PRAW Library of shape (961, 9).
  7. [Reddit Data](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%201/Reddit%20Data.csv) - Contains the collected reddit data(Uncleaned data) of shape (961, 9) .
  

### Method - 2

  1. [Alternate Scrapping](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%202/1.%20Alternate%20Scrapping.ipynb) - Contains the Code for Scrapping Reddit Data Using Pushshift API Wrapper of PRAW Library.
  2. [Alternate Cleaning](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%202/2.%20Alternate%20Cleaning.ipynb) - Contains the code for cleaning the collected data.
  3. [Alternate EDA](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%202/3.%20Alternate%20EDA.ipynb) - Contains the code for Data Analysis.
  4. [Alternate Modelling(Deep Learning)](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%202/4.%20Alternate%20Modelling(Deep%20Learning).ipynb) - Contains the code for testing LSTM Model on the reddit data collected.
  4. [Alternate Modelling(Machine Learning)](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%202/4.%20Alternate%20Modelling(Machine%20Learning).ipynb) - Contains the code for testing various Machine Learning Models on the reddit data collected.
  5. [Cleaned Reddit Data AS](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%202/Cleaned%20Reddit%20Data%20AS.csv) - Contains the collected reddit data by using Pushshift API Wrapper of PRAW Library of shape (21605, 9) .
  6. [Reddit Data AS](https://github.com/PankajGit2711/Reddit-Flair-Detection/blob/master/Method%20-%202/Cleaned%20Reddit%20Data%20AS.csv) - Contains the collected reddit data (uncleaned data) of shape (21605, 9).
  
## Results

The Results Obtained After running various Machine Learning and Deep Learning Models on the collected data of both the methods are listed below

### Method - 1

#### Title as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest Classifier   | 0.8134715025      |
| Naive Bayes Classifier     | 0.6580310880      |
| SGD Classifier             | 0.8497409326      |
| MLP Classifier             | 0.6994818652      |
| Logistic Regression        | 0.7616580310      |
| XGB Classifier             | 0.8031088082      |
| Linear SVM Classifier      | 0.8652849740      |

#### Content as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest Classifier   | 0.4093264248      |
| Naive Bayes Classifier     | 0.3937823834      |
| SGD Classifier             | 0.2849740932      |
| MLP Classifier             | 0.4352331606      |
| Logistic Regression        | 0.3834196891      |
| XGB Classifier             | 0.4404145077      |
| Linear SVM Classifier      | 0.4507772020      |


#### Title + Content + URL as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest Classifier   | 0.8186528497      |
| Naive Bayes Classifier     | 0.6476683937      |
| SGD Classifier             | 0.8808290155      |
| MLP Classifier             | 0.7668393782      |
| Logistic Regression        | 0.7720207253      |
| XGB Classifier             | 0.8860103626      |
| Linear SVM Classifier      | **0.8860103626**  |

Note:- Highlighted Model From the table is used in the deployment.

### Method - 2

#### Deep Learning Models

| Deep Learning Algorithms | Features              | Training Accuracy | Testing Accuracy | Training Loss | Validation loss |
| -------------            | -----------           | ----------        | ---------------- | ------------- | --------------- |
| Long Short Term Memory   | Title + Content + URL | 0.8215            | 0.4954           | 0.5276        | 2.2310          |

#### Title as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest Classifier   | 0.5460434983      |
| Naive Bayes Classifier     | 0.4583526145      |
| SGD Classifier             | 0.5590004627      |
| MLP Classifier             | 0.4361406756      |
| Logistic Regression        | 0.4567329939      |
| XGB Classifier             | 0.4946783896      |
| Linear SVM Classifier      | 0.5388708931      |

#### URL as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest Classifier   | 0.3250809810      |
| Naive Bayes Classifier     | 0.3498380379      |
| SGD Classifier             | 0.3773715872      |
| MLP Classifier             | 0.1008792225      |
| Logistic Regression        | 0.3776029615      |
| XGB Classifier             | 0.3507635354      |
| Linear SVM Classifier      | 0.3776029615      |

#### Content as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest Classifier   | 0.4079130032      |
| Naive Bayes Classifier     | 0.4030541416      |
| SGD Classifier             | 0.4143914854      |
| MLP Classifier             | 0.4055992596      |
| Logistic Regression        | 0.4136973623      |
| XGB Classifier             | 0.4157797316      |
| Linear SVM Classifier      | 0.4178621008      |


#### Title + Content + URL as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest Classifier   | 0.5226746876      |
| Naive Bayes Classifier     | 0.4201758445      |
| SGD Classifier             | 0.5691809347      |
| MLP Classifier             | 0.4666820916      |
| Logistic Regression        | 0.5583063396      |
| XGB Classifier             | 0.4944470152      |
| Linear SVM Classifier      | 0.5696436834      |


## Libraries Used 
The Libraries Used in the devlopment of both methods are listed below:

### Method - 1

* [Numpy](http://https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [SK-Learn](https://scikit-learn.org/stable/)
* [NLTK](https://www.nltk.org/)
* [PRAW](https://praw.readthedocs.io/en/latest/)

### Method - 2

* [Numpy](http://https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [SK-Learn](https://scikit-learn.org/stable/)
* [NLTK](https://www.nltk.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [PRAW](https://praw.readthedocs.io/en/latest/)
* [PSAW](https://psaw.readthedocs.io/en/latest/)

## Refrences

Below are the refrences that I used in order to complete this project:-

1. [How to scrape data from Reddit](http://www.storybench.org/how-to-scrape-reddit-with-python/)
2. [Multi Class Text Classification with LSTM using TensorFlow 2.0](https://towardsdatascience.com/multi-class-text-classification-with-lstm-using-tensorflow-2-0-d88627c10a35)
3. [PSAW Documentation](https://psaw.readthedocs.io/en/latest/)

