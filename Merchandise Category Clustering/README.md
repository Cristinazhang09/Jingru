# Project Name: Merchandise Category Clustering
This is my course project for DSC-550 here at Bellevue University. This project is to use unsupervised methdologies to cluster taxonomy categories from different retailers to a unified taxonomy. At the current stage, I focus on the first tier taxonomy of products. TF-IDF topic modelling, TF-IDF+K-Means, and Bert-Senetence embedding+K-means clustering have been implemented.

## Installation
The code requires Python versions of 3.* and general libraries.

## Project Motivation and Description
The motivation of the project is the fact that online merchandises use different taxonomy for products, while there is a need for customer to locate the same product from different online merchandises, and there are service providers working on such a function.
The final goal of the project is unify the different product catogories from different online merchandise into the same category, or in other words, provide a label to indicate they refer to the same product. In this project, I used a simplified approach by identifying the first-tier category through unsuepervised clustering using KNN or topic modeling. Specifically, I used the BERT sentence encoding for vectorization, and I used word cloud to visulualize the identified clusters. 

## Results
The optimal number of clusters obtained through KNN was 7 using the elbow method. From the word cloud and TSNE visualization, it was found that BERT sentence encoding seperated the clusters better than the TF-IDF vectorization, which was a result of the ability to handle the semantics of short sentences using BERT sentence encoding.

