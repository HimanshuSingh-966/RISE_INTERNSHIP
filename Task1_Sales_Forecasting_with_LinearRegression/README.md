# Sales Forecasting with Linear Regression
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task1_Sales_Forecasting_with_LinearRegression)

This repository contains a project focused on forecasting sales using a Linear Regression model. The project involves data preprocessing, outlier removal, and model training to predict future sales based on historical data.

## Project Overview

The primary objective of this project is to build a predictive model that can forecast sales. This is achieved by cleaning and preparing raw sales data and then applying a Linear Regression algorithm to learn patterns and make predictions.

## Datasets

-   `preprocessing/Online_Sales_Data.csv`: The initial raw dataset containing online sales information.
-   `Cleaned_sales_data.csv`: The final, processed dataset used for training the model. This dataset is the result of the preprocessing and cleaning steps.

## Methodology

The project is structured into two main phases: Data Preprocessing and Modeling.

### 1. Data Preprocessing

The raw sales data undergoes a series of cleaning and transformation steps to prepare it for the modeling phase. These steps are detailed in the notebooks within the `preprocessing/` directory.

-   **`preprocessing/1_data_preprocessing.ipynb`**: This notebook handles the initial data cleaning tasks such as handling missing values, correcting data types, and feature engineering.
-   **`preprocessing/2_outlier_removing.ipynb`**: This notebook focuses on identifying and removing outliers from the dataset to improve model performance and accuracy.

### 2. Modeling

-   **`sales_forecasting.ipynb`**: This notebook contains the core logic for the sales forecasting model. It loads the `Cleaned_sales_data.csv`, splits the data into training and testing sets, trains a Linear Regression model, and evaluates its performance.

## How to Run the Project

To replicate the project, follow these steps:

1.  Clone the repository to your local machine.
2.  Ensure you have a Python environment with necessary libraries such as Pandas, NumPy, Scikit-learn, and Jupyter Notebook installed.
3.  Navigate to the `Task1_Sales_Forecasting_with_LinearRegression/` directory.
4.  To understand the data preparation process, run the notebooks in the `preprocessing/` directory sequentially:
    -   `1_data_preprocessing.ipynb`
    -   `2_outlier_removing.ipynb`
5.  Run the `sales_forecasting.ipynb` notebook to train the model and see the forecasting results.