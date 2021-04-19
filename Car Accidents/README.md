# Term_Project-DSC-530

This is my term project for DSC-530

The purpose of my project is to find out the importance of different climatic factors which correspond to the accidents and accident severity. My data is a countrywide traffic accident dataset. The dataset covers 49 states of the United States, and the data are collected form February 2016 to December 2019, approximately 3 million accident records in this dataset. This project used statistical analysis to find the relaionship between climatic factors and accident severity. 

## Installation
The code requires Python versions of 3.* and general libraries.

## Project Motivation and Description
According car accidents statistics, there are nearly 6 million car accidents in the United States every year. Approximately 1.25 million people die in road crashed each year, in addition, 20-50 million people are injured, many of them even have long-term disabilities. Due to car accidents, many people lose properties, health, especially, people lose their loved ones. Thus, I determined to analyze a countywide car accident dataset. I calculated the covariance and Spearman's correlation between independent variables and dependent variable. p-Test was run to confirm the relationship between indepdent variable and dependent variable. Multiple linear regression was performed, small eigenvalue was detected, suggesting strong multicollinearity between variables.  

## Results
* Most accidents were occurred around 75, not frozen and snow days.
* Most accidents were happened in pressure 28 in, 29 in, and wind speed from 2 mph to 6 mph, not strong wind.
* Most accidents were occurred in daytime, and visibility of 10 mile.
* Then I made a PMF of visibility for severity 2 and severity 3, I could not see obviously different between them. So did the CDF of visibility. All weather-related variables have a small correlation of severity. 
* For hypothesis test, the visibility showed a correlation with severity and it is significant.  

## Limitations
Climate is geospatial correlated, therefore it would be better if the climate is analyzied state-wisely or clusters of states, as different states have different climate even though there are in the same season, the variance make it difficutl to get a precise prediction.

## Licensing, Authors, Acknowledgements
The data used for analysisi is from:
* Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. [“A Countrywide Traffic Accident Dataset.”](https://arxiv.org/abs/1906.05409), arXiv preprint arXiv:1906.05409 (2019).
* Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. [“Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights.” ](https://arxiv.org/abs/1909.09638) In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.
