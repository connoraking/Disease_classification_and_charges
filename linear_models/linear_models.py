# -*- coding: utf-8 -*-
"""
This file contains linear machine learning models

This includes:
    marginal linear regression
    multiple linear regression
    lasso regression
    ridge regression
    elastic net regression
    principal component regression
"""

import os
import pandas as pd

# Importing processed dataframe
path_project = "C:/Users/Conno/Documents/Career/Projects/Hospital_Charges"

os.chdir(path_project)

df = pd.read_csv("./df_processed.csv")
