# Project Name: Wine Quality
The purpose of this project is to provide a model to predict the quality of red wine based the properties like acidity, pH, density, sulfur dioxide, etc. 
## Installation
The code requires R.

## Project Motivation and Description
The motivation of this project is to answer whether the quality of wine can be predicted from its physical quantities or not. The features provided include acidity (fixed, volatile), sugar content, sulfur dioxide content, density, pH value, sulphates, alcohol, etc. The features are correlated. This project also provides a good platform to practice R programming as well as statistical analysis.
There are 6 levels of wine quality, and the data is very imbalanced, making it difficult for prediction.
## Results
From EDA, features correlations were identified, which was understandable, since acidity and pH are obviously close related;
Features were selected by using the significant independent variables, namely, volatile acidity, chlorides, total sulfur dioxide, sulphates and alcohol;
Multiple linear regression model was trained using R, the accuracy on test was 41%, which was not so bad for a 6 classes task, however, model performance could be improved through through under-sampling or up-sampling regarding the imblanced dataset. Also, more complex model may also provide a chance to achieve a better model accuracy.
