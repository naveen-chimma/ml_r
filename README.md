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

# Insurance Cost Prediction Using Machine Learning

This project analyzes an insurance dataset to predict costs using machine learning techniques. The notebook includes steps for data preprocessing, exploratory data analysis (EDA), model building, and evaluation.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Development](#model-development)
- [Results](#results)
- [Conclusion](#conclusion)

## Introduction

The objective of this project is to predict insurance costs based on customer features, including demographic and health-related attributes. The project explores various machine learning models to achieve the best predictive accuracy.

## Dataset

The dataset contains the following columns:
- **age:** Age of the policyholder.
- **sex:** Gender of the policyholder.
- **bmi:** Body mass index.
- **children:** Number of children covered by insurance.
- **smoker:** Whether the policyholder is a smoker.
- **region:** Residential region of the policyholder.
- **charges:** Insurance cost (target variable).

## Data Preprocessing

1. **Handling Missing Values:** Checked and managed missing data.
2. **Validation:** Verified data integrity using pandas' `unique` method.
3. **Encoding Categorical Data:** Applied encoding for `sex`, `smoker`, and `region` columns.
4. **Scaling:** Standardized numerical features using normalization techniques.

## Exploratory Data Analysis (EDA)

- Visualized data distributions and correlations.
- Identified trends between features and the target variable.

## Model Development

- Implemented machine learning models for prediction:
  - Linear Regression
  - Regularized Regression (Lasso and Ridge)
- Evaluated models using metrics such as R² and Mean Squared Error (MSE).

## Results

- Achieved **R² Score:** 0.089 (train), 0.029 (test).
- MSE on test set: 989,558,744.54.

## Conclusion

This project highlights the importance of data preprocessing and regularization in predicting insurance costs. Future work could include:
- Exploring advanced algorithms like Random Forest or Gradient Boosting.
- Incorporating additional features for better predictive power.

---

### How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/insurance-prediction.git
   cd insurance-prediction
