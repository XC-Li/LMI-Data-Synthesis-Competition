# LMI-Data-Synthesis-Competitipon
[Competition Page](https://www.ncsi.com/event/dcdatacon/hackathon/)  
[Link of this project on GitHub](https://github.com/XC-Li/LMI-Data-Synthesis-Competition)  
## Group members
*All of us come from GWU Data Science Program*  

Shen Luo  
Xiaochi Li  
Xinyu Zhang  


## Usage of the code:

### 1. For evaluation the performance of our model : 
Our model is saved in "prediction_model.pickle". Just load your test data in "Synthesis_Evaluation.ipynb" as X_test and y_test, and run that notebook.
 
### 2. For reproduction of our work:  
Put the notebooks and the original data in the same directory, and run the notebook in the following order:
 
  1. Preprocessing.ipynb
  2. Prediction_Model.ipynb
  3. xxx.ipynb
  4. Synthesis_Evaluation.ipynb
 
### 3. For grader using your own data:
  1. You may use XgBoost model.
  2. To run it, open your shell/terminal, in the currect directory, type: `python Pipeline--predicting_true_data.py -f XXX.xlsx`. `XXX.xlsx` or `XXX.csv` is the original data you want to test on our model. 
    * DON'T FORGET type your file path if you are in differnet directory. 
  3. The final evaluation will show on your shell/terminal
  4. The prediction of `Salary` will be saved as `test_predict.csv`. Then you can compare it with your real data. 
