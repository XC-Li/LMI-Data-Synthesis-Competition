
# coding: utf-8

import os
import argparse
parser = argparse.ArgumentParser(description='Execute Xgboost H2O Pipeline')
parser.add_argument('-f','--filepath', help='filepath to data set', required=True)
args = vars(parser.parse_args())
input_filePath = args['filepath']
if not input_filePath:
    input_filePath = "data.xlsx"




# coding: utf-8
import pandas as pd
# These lines set up the plotting funstionality and formatting.
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
matplotlib.use('Agg', warn = False)
#get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np


from sklearn.metrics import accuracy_score, precision_score, recall_score

from sklearn.model_selection import train_test_split

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import itertools
#!pip install h2o
import h2o
h2o.init()
from h2o.automl import H2OAutoML


# read data
def reading_data(file_name):
    if file_name.endswith(".csv"):

        df = pd.read_csv(file_name) 
    else:
        df = pd.read_excel(file_name,thousands = ",") #seperations in thousands
    # remove features:
    not_include_features = ["MOU", "MOU Title", "Title", "Department", "Record Number", "POBP",
                            "p_grade","benefit","e_type"]
    selected_features = [i for i in df.columns if i not in not_include_features]
    X_selected = df.loc[:,selected_features]
    # data imputation:
    X_selected["p_dep"] = X_selected["p_dep"].fillna(X_selected["p_dep"].mean())
    X_selected["Lump Sum Pay"] = X_selected["Lump Sum Pay"].fillna(0)
    X_selected["Rate"] = X_selected["Rate"].fillna(X_selected["Rate"].mean())
    X_selected["o_pay"] = X_selected["o_pay"].fillna(X_selected["o_pay"].median())
    final_df = X_selected
    return final_df



df = reading_data(input_filePath) 
print("========================================================")
print("The data after imputation (head 5)")
print(df.head(5))
print("========================================================")


def h2o_pred(test):
    h2oTest = h2o.H2OFrame(test)
    saved_model = h2o.load_model(os.getcwd()+"/XGBoost_1_AutoML_20181105_211213")
    preds = saved_model.predict(h2oTest)
    preds = preds.as_data_frame()
    print(saved_model.model_performance(h2oTest))
    print("========================================================")
    print("Saving prediction into csv file")
    preds.to_csv("test_predict.csv")
    return preds
  

#Saved Residual plot
def residual_plot(y_pred, y_test):
    # transform y_test and y_pred as dataframe:
    tf = y_test.to_frame().reset_index(drop=True)
    new_df = pd.DataFrame()
    new_df["y_test"] = tf
    new_df["y_test_pred"] = y_pred
    # substraction two columns to compute residuals:
    new_df["sub"] = new_df[["y_test","y_test_pred"]].sum(axis=1)
    yy = new_df[["y_test_pred","sub"]].sub(new_df["y_test"],axis=0)

    # residual plot
    plt.figure(figsize=(15,15))
    plt.hlines(y=0, xmin=-5000, xmax=350000,color='black', lw=0.8)
    sns.scatterplot(x = "sub", y= "y_test_pred", data = yy,color = "limegreen",marker = 's', edgecolor = "white",
                   label = "Test Data")
    plt.xlabel('Predicted values')
    plt.ylabel('Residuals')
    plt.legend(loc='upper left')
    plt.savefig('TEST_Residual_Xgboost.png', bbox_inches='tight',dpi=800)


#saved_model.model_performance(h2oTest)  

y_pred = h2o_pred(df)
print("Prediction is done. test_predict.csv is saved in the current directory")

residual_plot(y_pred, df["Salary"])
print("========================================================")
print("Saved Residual plot into TEST_Residual_Xgboost.png in current directory")


print("========================================================")
print("done")














































