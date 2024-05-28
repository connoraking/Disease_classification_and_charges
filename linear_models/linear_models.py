# -*- coding: utf-8 -*-
"""
This file contains linear machine learning models

This includes:
    multiple linear regression
    lasso regression
    ridge regression
    elastic net regression
    principal component regression
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

# Importing processed dataframe
path_project = "C:/Users/Conno/Documents/Career/Projects/Hospital_Charges"

os.chdir(path_project)

df = pd.read_csv("./df_processed.csv")

X = df.drop(columns = ["charges"])
y = df["charges"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 32)

# multiple regression


