# -*- coding: utf-8 -*-

import os
import pandas as pd
import janitor
# Reading in data 

path_project = "C:/Users/Conno/Documents/Career/Projects/Hospital_Charges"

os.chdir(path_project)

support2_path = os.path.join("data", "support2.csv")

df_raw = pd.read_csv(support2_path)

# Removing columns with more than 25% NA
df_c = df_raw.loc[:, df_raw.notna().mean() > 0.75]
df_c = df_c.dropna()


# Some pre-processing of the variables, preparing for one-hot encoding
cat_columns = ["dzclass", "dzgroup"] # removed no.co as it is an ordinarl variable

df_c[cat_columns] = df_c[cat_columns].apply(lambda x: x.astype('category'))
#df_c["num.co"] = df_c["num.co"].astype("category") # converting to categorical variable (equivalent to factor in R)
df_c = df_c.drop(columns = ["totcst"]) # these columns use "charges" in their calculations

# One-hot encoding the categorical predictors, removes first to avoid multicollinearity
df_encoded = pd.get_dummies(df_c, drop_first = True)

# Cleaning column names using pyjanitor
df_encoded = df_encoded.clean_names()

# Removing columns with near 0 variance as this will cause significant problems some certain models (neural networks specifically)
variances = df_encoded.var()
var_threshold = 0.01
cols_drop = variances[variances < var_threshold].index # removed num_co_7 thru num_co_9, race_other and sfdm2_coma_or_intub
cols_drop = cols_drop.tolist()

df_processed = df_encoded.drop(columns = cols_drop)

# Uploading as CSV
df_processed.to_csv("./df_processed.csv", index = False)
