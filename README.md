# Car Price Prediction Algorithm

## Description of Project:
The motivation behind this project is to understand the pricing of 1st hand,2nd hand, and even 3rd hand cars by dealership websites like cars24.com(an Indian Dealership website). Data scraped from the website from major metropolitan cities like Mumbai, New Delhi, Chennai, and Bengaluru.
This is **an End to End project** where the data scraped was cleaned, ingested, and validated for missing values and then inserted into SQLite Database. The Independent features here were *kilometers driven,
Fuel used, transmission type(manual or automatic), Age of the vehicle, Ownership level(1st hand,2nd hand, etc), and On road price of Car(the price which was paid after ex-showroom price and road tax)*.
The Dependent feature is the *Selling Price of the Car*.

## Machine Learning Algorithm Used:
XGBoost Regressor algorithm gave much better results compared to the others used like DecisionTree Regressor, KNN Regressor, and Lasso Regressor. Root Mean Square was the metric chosen in deciding
the model performance. 

## How to use the code:
Once cloned in your local please delete the files present in the folder Training_FileFromDB and Training_Database if you want to retrain the model from scratch. The entire flow for the code is attached in a separate file(connector diagram).
Code related to the scraper can be found in the Webscraping_Code folder.
