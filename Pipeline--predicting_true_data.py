
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
    df = pd.read_excel(file_name,thousands=",") #seperations in thousands
    # remove features:
    categotical_features = ["e_type", "benefit", "Time", "p_grade"]
    not_include_features = ["MOU", "MOU Title", "Title", "Department", "Record Number", "POBP"]
    selected_features = [i for i in df.columns if i not in not_include_features]
    X_selected = df.loc[:,selected_features]
    # data imputation:
    X_selected["p_dep"] = X_selected["p_dep"].fillna(X_selected["p_dep"].mean())
    X_selected["Lump Sum Pay"] = X_selected["Lump Sum Pay"].fillna(0)
    X_selected["Rate"] = X_selected["Rate"].fillna(X_selected["Rate"].mean())
    X_selected["o_pay"] = X_selected["o_pay"].fillna(X_selected["o_pay"].median())
    X_selected["p_grade"] = X_selected["p_grade"].fillna(-1)
    X_selected["benefit"] = X_selected["benefit"].fillna(-1)
    final_df = X_selected
    
    # change the format of three features into integer: p_grade, benefit, e_type:
    p_grade_map={}
    j=0
    for i in pd.unique(final_df['p_grade']):
        p_grade_map[i]=j
        j=j+1
    benefit_map={}
    j=0
    for i in pd.unique(final_df['benefit']):
        benefit_map[i]=j
        j=j+1
    e_type_map={}
    j=0
    for i in pd.unique(final_df['e_type']):
        e_type_map[i]=j
        j=j+1

    final_df['p_grade']=final_df['p_grade'].map(p_grade_map)
    final_df['benefit']=final_df['benefit'].map(benefit_map)
    final_df['e_type']=final_df['e_type'].map(e_type_map)
    return final_df



df = reading_data(input_filePath) 
print("========================================================")
print("The data after imputation (head 5)")
print(df.head(5))
print("========================================================")


def h2o_pred(test):
    h2oTest = h2o.H2OFrame(test)
    saved_model = h2o.load_model(os.getcwd()+"/XGBoost")
    preds = saved_model.predict(h2oTest)
    preds = preds.as_data_frame()
    preds.to_csv("test_predict.csv")
    

h2o_pred(df)
print("prediction is done. Saved in the current directory")
print("")
print("the csv file is test_predict.csv")
print("done")














































