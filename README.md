# Insurance Cost Prediction Using Machine Learning

This project implements machine learning techniques to predict insurance charges based on various demographic and health-related attributes. The dataset includes features like age, BMI, and smoking status. The project evaluates model performance through metrics like Mean Squared Error (MSE) and R-squared (R²). It also explores techniques like feature engineering and model tuning to improve predictive accuracy.

## Table of contents

- `Introduction`
- `Dataset`
- `Data Preprocessing`
- `Methodology`
- `Model Evaluation`
- `Results`
- `Conclusion`

- **Introduction**

  The objective of this project is to develop a predictive model for insurance charges based on individual attributes. This involves implementing regression techniques, evaluating model performance, and identifying key factors influencing insurance costs.

**Dataset**

The dataset contains rows of samples and columns of attributes, including the target variable (charges). Key features include:

- `Age`:
 Age of the individual.
- `Bmi`: 
Body Mass Index, a measure of body fat.
- `Childrens`: 
Number of dependents.
- `Smoker`: 
Whether the individual smokes (yes/no).
- `Region`:
 Geographic region.
- `Charges`:
 Medical insurance cost (target variable).

**Data Preprocessing**

- `Missing Values:`
 Any missing values were handled through Random Imputaion.

- `Categorical Encoding:`
 Categorical features were encoded using One-Hot Encoding.

- `Feature Scaling:`
 Numerical features were scaled using Normalization to improve model performance.

 
## Methodlogy

- `Data Exploration`

Visualizations of the data distribution and correlations between features and the target variable.
### Model Development

1. `Implementation of Multiple Linear Regression.`

   In this project, we implemented multiple linear regression using Python's scikit-learn library. The following steps outline the process:
   - **Import Libraries**
First, we import the necessary libraries for data manipulation and model building.
   
   - **Load the Dataset**
Next, we load the dataset and perform initial exploration.

   - **Split the Data**

We split the dataset into training and testing sets.

   - **Train the Model**
We create an instance of the LinearRegression model and fit it to the training data.
    
  - **Make Predictions**

After training, we use the model to make predictions on the test set.

- **Evaluate the Model**
