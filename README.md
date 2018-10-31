# LMI-Data-Synthesis-Competitipon
[Competition Page](https://www.ncsi.com/event/dcdatacon/hackathon/)  
[Link of this project on GitHub](https://github.com/XC-Li/LMI-Data-Synthesis-Competition)  
## Group members
*All of us come from GWU Data Science Program*  

Shen Luo  
Xiaochi Li  
Xinyu Zhang  


## IDescription of files:

### 1. Code files: 
1. XGboost model:
* H2O_Xgboost.ipynb
* Pipeline--predicting_true_data.py

2. Linear Regression model:
* Prediction_Model.ipynb
* Synthesis_Evaluation.ipynb

3. Data preprocessing and EDA:
* Preprocessing.ipynb

4. AutoEncoder:
* Data_synthesis.ipynb
* 3Dvisualization.py

### 2. Data files
* X_test.pickle
* y_test.pickle
* data.xlsx
* processed_data.pickle
* test_predict.csv(if you run Xgboost Pipeline)

### 3. Presentation:
* Presentation.pptx

### 4. Saved Models:
* XGBoost
* prediction_model.pickle

### 5. others:
* 3D.gif
* LICENSE
* readme.md
* notes.md
* regression_evaluation.pdf
* .gitignore



## II. Evaluation the performance of our models : 
### 1. Linear regression:

Our model is saved in "prediction_model.pickle". Just load your test data in "Synthesis_Evaluation.ipynb" as X_test and y_test, and run that notebook.

### 2. XgBoost model:
  1. To run it, open your shell/terminal, in the currect directory, type: `python Pipeline--predicting_true_data.py -f XXX.xlsx`. `XXX.xlsx` or `XXX.csv` is the original data you want to test on our model. 
    * DON'T FORGET type your file path if the data is in differnet directory.* 
  2. The final evaluation will show on your shell/terminal
  3. The prediction of `Salary` will be saved as `test_predict.csv`. Then you can compare it with your real data. 

 
## III. For reproduction of our work:  
Put the notebooks and the original data in the same directory, and run the notebook in the following order:
  1. Preprocessing.ipynb
  2. Prediction_Model.ipynb
  3. xxx.ipynb
  4. Synthesis_Evaluation.ipynb
 
