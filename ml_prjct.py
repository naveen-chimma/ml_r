# -*- coding: utf-8 -*-
"""ml_prjct.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pZZ-NPYFRbHijMeITN73tnqXwKel3_Cj

* **Final Collected Data**
"""

# Base Libraries

import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('insurance.csv')

"""* **Basic Checks of Dataset**"""

# Number of rows & cols, col names non-missing values & data type

data.info()

# First 3 rows

display(data.head(3))

"""1. Data Validation"""

display(data.columns)

# Renaming Amazon Column Names using title()
data.columns = data.columns.str.title()

display(data.columns)

"""* **Already Columns are in lower case so, no need of Converting Text Columns to Lower Case **

* **Duplicated Rows Handling**
"""

display(data[data.duplicated()])
print(f"Number of Rows Duplicated: {len(data[data.duplicated()])}")

# Droping Duplicated Rows

data = data.drop_duplicates().reset_index(drop=True)

# Checking rows after droping duplicates

display(data.shape)

# Final Check

display(data[data.duplicated()])
print(f"Number of Rows Duplicated: {len(data[data.duplicated()])}")

"""* **Validation each & every column data**
    * using **unique** method in pandas dataframe
"""

# libraries

import warnings
warnings.filterwarnings("ignore")

# Function

def validate(df, col):
    print(f"Column Name: {col}")
    print()
    print(f"Number of Unique Values in Column: {df[col].nunique()}")
    print()
    print("Unique Values of Column:")
    print(df[col].unique())
    print()
    print(f"Data Type of Column: {df[col].dtype}")

data.head(2)

validate(data,'Age')

"""* Data is valid"""

validate(data,'Sex')

"""* Data is valid"""

validate(data,'Bmi')

"""* Data is valid"""

validate(data,'Children')

"""* Data is valid"""

validate(data,'Smoker')

"""* Data is valid"""

validate(data,'Region')

"""* Data is valid"""

validate(data,'Charges')

"""* **Final Validated Data**"""

# Taking Validated Data for Analysis
df = data.copy()

df.head(2)

"""* Checking Duplicated Rows After Data Validation"""

df[df.duplicated()]

df.shape

df.isnull().sum()

"""### 2. Data Understanding @ EDA (Exploratory Data Analysis):  <a id='eda'>

[Back to Top](#menu)
    
* We can get insights on dataset using Exploratory Data Analysis (EDA) methods

* EDA can be of two things,
    - Stats
        - Descriptive
    - Visual Analysis

**2.1 Analysis**

EDA is divided into major two types of analysis


Uni-Variate|Bi-Variate|Multi-Variate
---|-----|------
Data study of single column|Data study between two columns|Data Study between three or more columns

1. Univariate Analysis with Subplots
"""

# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the figure
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Age distribution
sns.histplot(df['Age'], kde=True, ax=axes[0, 0], color='blue')
axes[0, 0].set_title('Age Distribution')

# BMI distribution
sns.histplot(df['Bmi'], kde=True, ax=axes[0, 1], color='green')
axes[0, 1].set_title('BMI Distribution')

# Charges distribution
sns.histplot(df['Charges'], kde=True, ax=axes[1, 0], color='orange')
axes[1, 0].set_title('Charges Distribution')

# Children count distribution
sns.countplot(x='Children', data=df, ax=axes[1, 1], palette='pastel')
axes[1, 1].set_title('Number of Children Distribution')

plt.tight_layout()
plt.show()

"""2. Bivariate Analysis with Subplots"""

# Set up the figure
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Scatter plot: Charges vs Age
sns.scatterplot(x='Age', y='Charges', hue='Smoker', data = df, palette='coolwarm', ax=axes[0, 0])
axes[0, 0].set_title('Charges vs Age')

# Scatter plot: Charges vs BMI
sns.scatterplot(x='Bmi', y='Charges', hue='Smoker', data=df, palette='coolwarm', ax=axes[0, 1])
axes[0, 1].set_title('Charges vs BMI')

# Boxplot: Charges by Smoking Status
sns.boxplot(x='Smoker', y='Charges', data=df, palette='Set3', ax=axes[1, 0])
axes[1, 0].set_title('Charges by Smoking Status')

# Boxplot: Charges by Region
sns.boxplot(x='Region', y='Charges', data=df, palette='Set2', ax=axes[1, 1])
axes[1, 1].set_title('Charges by Region')

plt.tight_layout()
plt.show()

"""3. Multivariate Analysis with Subplots


"""

# Pair plot for numerical variables
sns.pairplot(df, hue='Smoker', palette='coolwarm')
plt.suptitle('Pairplot Analysis', y=1.02)
plt.show()

# Correlation matrix with heatmap
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Charges vs Region colored by Smoking Status
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Charges', hue='Smoker', data=df, palette='Set2')
plt.title('Average Charges by Region and Smoking Status')
plt.xlabel('Region')
plt.ylabel('Average Charges')
plt.legend(title='Smoker')
plt.show()

"""### 3. Handling Missing Values & Outliers<a id='naout'>

    
**3.1 NaN (missing data in columns)**
"""

df.isnull().sum()

"""### No need of handling missing values, beacause there are no null values present in given data

**3.2 Outliers Handling**

* Numeric data which does not fit to col data
"""

import plotly.express as px

def outlier_detect(df):
    for col in df.describe().columns:
        print("Column:",col)
        print("------------------------------------------------")
        print("Boxplot For Outlier Identification:")
        px.box(df[col], orientation='h', width=600, height=300, ).show()
        print()
        Q1 = df.describe().at['25%',col]
        Q3 = df.describe().at['75%',col]
        IQR = Q3 - Q1
        LTV = Q1 - 1.5 * IQR
        UTV = Q3 + 1.5 * IQR

        print("********* Outlier Data Points *******")
        print()
        lowerout = []
        upperout = []

        for val in df[col]:
            if val<LTV:
                if val not in lowerout:
                    lowerout.append(val)
            elif val>UTV:
                if val not in upperout:
                    upperout.append(val)

        lowerout.sort()
        upperout.sort()

        print("Lower Outliers:")
        print(lowerout)
        print()
        print()
        print("Upper Outliers:")
        print(upperout)
        print()
        print("===============================================")
        print()

def outlier_replacement(df):
    for col in df.describe().columns:
        print("Column:",col)
        print("------------------------------------------------")
        Q1 = df.describe().at['25%',col]
        Q3 = df.describe().at['75%',col]
        IQR = Q3 - Q1
        LTV = Q1 - 1.5 * IQR
        UTV = Q3 + 1.5 * IQR

        # replacement vals (any one of the below)

        # median
        median = df[col].median()

        # Ltv, Utv
        low_bound = LTV
        high_bound = UTV

        # 5th & 95th
        fifth = df[col].quantile(0.05)
        ninetyfifth = df[col].quantile(0.95)

        print("Replacing Outliers with 5th percentile for lower Outliers, 95th percentile for Upper Outliers....")
        print("Adjust the module code for any other replacements.........")
        print()

        # mask method is used to replace the values
        df[col] = df[col].mask(df[col]<LTV, round(fifth)) # replacing the lower outlier with 5th percentile value
        df[col] = df[col].mask(df[col]>UTV, round(ninetyfifth)) # replacing the outlier with 95th percentile value

outlier_detect(df)

"""### @  Predictive Modeling<a id='pm'>"""

df.head(4)

"""#### Predictive Modeling on Price Data
    
* Above data will be given to a machine learning model , where the model will be trained on column data price with other column data and estimate price for given laptop data
    
* predictive modeling is sending data to a algorithm as input columns(x) along with one output column data (y), training y data with x
    
    model: y~x -> y = f(x)+e

**Input (x) and output(y) column for modeling from data**<a id='xy'>
"""

X = df.drop('Charges', axis = 1)
y = df['Charges']

X.head(2)

y.head(2)

"""* ** Feature Modification**"""

# Selecting Object Type Cols

X.select_dtypes("O")

X.select_dtypes("O").columns

import sklearn
from sklearn.preprocessing import LabelEncoder
for col in X.select_dtypes("O").columns:
    Le = LabelEncoder()
    X[col] = Le.fit_transform(X[col])

"""## Train - Test Split"""

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(X,y,test_size=0.25,random_state=42)

xtrain.shape, xtest.shape

xtrain.head(2)

xtest.head(2)

ytrain.shape, ytest.shape

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

X_train.shape, X_test.shape

X_train.head(2)

X_test.head(2)

y_train.shape, y_test.shape

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.metrics import r2_score, root_mean_squared_error,mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR

# Linear Regression
def linear_regression_algo(X_train, X_test, y_train, y_test):
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    y_train_pred = reg.predict(X_train)
    y_test_pred = reg.predict(X_test)

    cv_scores = cross_val_score(reg, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

# Lasso Regression
def lasso_regression_algo(X_train, X_test, y_train, y_test):
    la = Lasso(alpha=0.2)
    la.fit(X_train, y_train)
    y_train_pred = la.predict(X_train)
    y_test_pred = la.predict(X_test)

    cv_scores = cross_val_score(la, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

# Ridge Regression
def ridge_regression_algo(X_train, X_test, y_train, y_test):
    rg = Ridge(alpha=0.2)
    rg.fit(X_train, y_train)
    y_train_pred = rg.predict(X_train)
    y_test_pred = rg.predict(X_test)

    cv_scores = cross_val_score(rg, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

# polynomial
def poly_regression_performance(X_train, X_test, y_train, y_test, degree=2):
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train)
    y_train_pred = poly_model.predict(X_train_poly)
    y_test_pred = poly_model.predict(X_test_poly)
    cv_scores = cross_val_score(poly_model, X_train_poly, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    print(f"\n------------ Polynomial Regression (Degree {degree}) Performance -------------\n")
    print(f"Train R2: {train_r2:.4f} | Train RMSE: {train_rmse:.4f}")
    print(f"Test R2:  {test_r2:.4f} | Test RMSE:  {test_rmse:.4f}")
    print(f"CV Mean R2: {cv_mean:.4f} | CV Std R2: {cv_std:.4f}")

# random Forest Regressor
def random_forest_regression_algo(X_train, X_test, y_train, y_test):
    rf = RandomForestRegressor(n_estimators=100, random_state=20)
    rf.fit(X_train, y_train)
    y_train_pred = rf.predict(X_train)
    y_test_pred = rf.predict(X_test)

    cv_scores = cross_val_score(rf, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

# decision tree Regressor
def decision_tree_regression_algo(X_train, X_test, y_train, y_test):
    dt = DecisionTreeRegressor(random_state=42)
    dt.fit(X_train, y_train)
    y_train_pred = dt.predict(X_train)
    y_test_pred = dt.predict(X_test)

    cv_scores = cross_val_score(dt, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

# Svr
def SVR_algo(X_train, X_test, y_train, y_test):
    svr = SVR(kernel='rbf')
    svr.fit(X_train, y_train)
    y_train_pred = svr.predict(X_train)
    y_test_pred = svr.predict(X_test)

    cv_scores = cross_val_score(svr, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

# Adaboost
def Adaboost_algo(X_train, X_test, y_train, y_test):
    adr = AdaBoostRegressor(n_estimators=100, learning_rate=0.5, random_state=42)
    adr.fit(X_train, y_train)
    y_train_pred = adr.predict(X_train)
    y_test_pred = adr.predict(X_test)

    cv_scores = cross_val_score(adr, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

# KNN
def knn_algo(X_train, X_test, y_train, y_test):
    knn = KNeighborsRegressor(n_neighbors=11)
    knn.fit(X_train, y_train)
    y_train_pred = knn.predict(X_train)
    y_test_pred = knn.predict(X_test)

    cv_scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='r2')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)

    print(f'\n------------ Train Performance -------------\n')
    print(f"Train R2 score is: {r2_score(y_train, y_train_pred)}")
    print(f"Train RMSE score is: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")

    print(f'\n------------ Test Performance -------------\n')
    print(f"Test R2 score is: {r2_score(y_test, y_test_pred)}")
    print(f"Test RMSE score is: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")

    print(f'\n------------ Cross Validation Performance -------------\n')
    print(f"CV Mean R2 score is: {cv_mean}")
    print(f"CV Std R2 score is: {cv_std}")

def calling(X_train, X_test, y_train, y_test):
  print('------------Linear----------------')
  linear_regression_algo(X_train, X_test, y_train, y_test)
  print('------------lasso----------------')
  lasso_regression_algo(X_train, X_test, y_train, y_test)
  print('------------ridge----------------')
  ridge_regression_algo(X_train, X_test, y_train, y_test)
  print('------------random forest----------------')
  random_forest_regression_algo(X_train, X_test, y_train, y_test)
  print('------------decision tree----------------')
  decision_tree_regression_algo(X_train, X_test, y_train, y_test)
  print('------------svr--------------------------')
  SVR_algo(X_train, X_test, y_train, y_test)
  print('------------adaboost---------------------')
  Adaboost_algo(X_train, X_test, y_train, y_test)
  print('------------poly--------------------------')
  poly_regression_performance(X_train, X_test, y_train, y_test, degree=2)
  print('-------------knn-------------------------')
  knn_algo(X_train, X_test, y_train, y_test)

calling(X_train, X_test, y_train, y_test)

def bias_variance_tradeoff(r2_train, r2_test):
    if r2_train > 0.8 and r2_test > 0.8:
        return "Good Fit"
    elif r2_train < 0.5 and r2_test < 0.5:
        return "Underfitting"
    elif r2_train - r2_test > 0.2:
        return "Overfitting"
    else:
        return "Balanced"

models = {
    'Linear': LinearRegression(),
    'Lasso': Lasso(alpha=0.2),
    'Ridge': Ridge(alpha=0.2),
    'Polynomial': PolynomialFeatures(degree=2),
    'Random_Forest': RandomForestRegressor(n_estimators=100),
    'Decision_Tree': DecisionTreeRegressor(random_state=20),
    'SVR': SVR(kernel='rbf'),
    'AdaBoost': AdaBoostRegressor(n_estimators=100, learning_rate=0.5, random_state=42),
    'KNN': KNeighborsRegressor(n_neighbors=11)
}
result = []
for model_name, model in models.items():
    if model_name == 'Polynomial':
        poly = PolynomialFeatures(degree=2)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)
        reg = LinearRegression()
        reg.fit(X_train_poly, y_train)
        y_train_pred = reg.predict(X_train_poly)
        y_test_pred = reg.predict(X_test_poly)
        cv_mean = np.mean(cross_val_score(reg, X_train_poly, y_train, cv=5, scoring='r2'))
    else:
        model.fit(X_train, y_train)
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        cv_mean = np.mean(cross_val_score(model, X_train, y_train, cv=5, scoring='r2'))
    result.append([
        model_name,
        model,
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred),
        np.sqrt(mean_squared_error(y_train, y_train_pred)),
        np.sqrt(mean_squared_error(y_test, y_test_pred)),
        cv_mean,
    ])
result_df = pd.DataFrame(result, columns=['Model', 'Algorithm', 'Train R2', 'Test R2', 'Train RMSE', 'Test RMSE', 'CV_Score'])

result_df['Bias_Variance_Tradeoff'] = result_df.apply(
    lambda row: bias_variance_tradeoff(row['Train R2'], row['Test R2']), axis=1
)
result_df

# Checking Price Distribution to Understand RMSE

df.Charges.describe()

"""#### Model Deployment<a id='dep'>


"""

# Module

import joblib

# Saving above mentioned object files

joblib.dump(data, "asc.pkl")
joblib.dump(ridge, "reflapprice_ari.pkl")

"""####  Real Time Prediction<a id='pred'>"""

def real_time_prediction(model, input_data):
    # Predict the value for given features using the trained model
    prediction = model.predict([input_data])  # Ensure input is in the right format (2D array)
    return prediction[0]  # Return the predicted value

# Example real-time input data (age, bmi, children, sex, smoker, region)
real_time_input = [40, 28.5, 2, 1, 0, 1]  # Example: age=40, bmi=28.5, 2 children, male, non-smoker, northeast region

# Real-time prediction
predicted_charge = real_time_prediction(model, real_time_input)
print(f"Predicted Insurance Charges for the given input: {predicted_charge:.2f}")