# Project Name: Omaha Housing Price

The purpose of my project is to use real world house information to predict the house prices. My dataset is collected by scrapping the house information from Zillow.com. This project uses Multiple Linear Regression, Support Vector Regression and Random Forest Regression. The performance of three models were compared using metrics of mean squared error and R-squared value.

## Installation
The code requires Python versions of 3.* and general libraries.

## Project Motivation and Description
A house is one of the most valuable economic assets a person can purchase during his/her life. Thus, it is very important to make the right decision whether to buy a house or not and at the right price as well. In common, different people might have different reasons to buy houses, for example, a family has a school age kid or school age kids might be more interested in buying a house which has a good public school in the region, people do not have a big budget might look for a relatively cheap house. Also, some houses are pretty old yet still have high listed prices for sale. What are the important factors to determine the price of a house, can we accurately predict the house price with the house information? If the model is able to predict the house prices, it could be used by those people who are looking for a new house, the potential buyer could compare the listed price with the predicted price and see whether it is a good invest or not. 

### Three different models I used in this project.
* Multiple Linear Regression
* Support Vector Regression
* Random Forest Regression

In addition to evaluate how these three models can predict housing price, I used two differet performance metrics:
* Mmean Squared Error
* R-squared Value

## Results
* It can be found that livable area had an approximately linear relationship with the housing prices. I think this is in consist with common sense that the more livable area a house has, the higher of the house price will be.
* The number of bedrooms, bathrooms and garages can affect the housing prices. In general, the more bedrooms, bathrooms and garages a house has, the higher the price is. This also agrees with common sense, because more bedroom and bathrooms generally indicate a larger living area.
* The houses in school rating 10 have relatively higher prices.
* The house with window air conditions has relatively lower housing price
* Among different kinds of roof, tile roof, metal roof and flat roof have relatively higher housing prices. 
* Compared there different models, Radom Forest model performs best.

## Limitations
It is noticed the model performance is not quite good at the current stage, and I think there are multiple reasons for this:
* The model hyper parameters have not been optimized yet, grid search or randomized search with cross validation could be performed in the future to identify the best hyper parameters for the models.
* More features could be collected to complement the current dataset. It would also be interesting to increase the size of the dataset by collecting house information from east coast and west coast and see the determining factors of housing price vary with the geographical information.

## Licensing, Authors, Acknowledgements
The data used for analysis is from [Zillow](https://www.zillow.com/)
