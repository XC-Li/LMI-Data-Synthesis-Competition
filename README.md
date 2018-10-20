# LMI-Data-Synthesis-Competitipon
**注意： 请开一个自己的NoteBook或者新的branch 而不要直接在别人的文件上修改以避免冲突**

1.	Eda，Preprocessing (George) --Done
2.	Simple imputation(Mandy) -- Done
3.	Splitting training and validation -- Done
4.	Synthesis data (Mandy)
5.	Feature engineering --Working
6.	Feature selection --Working
7.	Build model (George)  --Working
8.	Output report/video

大家把自己做的工作简单地写在这里，便于交流

10/17（George）: 

1. 完成: imputation， model evaluation(Residual plot, R^2 and MSE)，将预处理后的数据存为可以直接使用的pickle文件
2. EDA 发现情况并不乐观，Scatterplot见大多数变量与Salary无线性关系， 代入全部变量后Linear model under fitting

我觉得需要进一步预处理数据（挑出重要变量），并且试用其他regression model

10/19 (George):

尝试了其他种类的regression，以MSE为评价标准，效果都不如Linear Regression好。

尝试的方法有与效果：(O)verfitting, (U)nderfitting, MSE of test 1eN

|尝试的方法|O/U|MSE of test set|
|----|----|----|
|Linear Regression|U|466|
|只采用与target相关性最大的变量|O|1e8|
|RANSAC|U|756|
|对10万以下回归|U|525|
|对10万以上回归|U|56|
|Regression on Standardized data|U|566|
|Ridge|U|466|
|Lasso|U|2125|
|ElasticNet|O|8395|
|Decision Tree Regression|O|9e7|
|Random Forest Regression|O|8e6|

看起来用更复杂的模型（类似于Random Forest Regression）虽然能解决Underfitting问题，但并不符合数据本身的规律，因此MSE极大。 取得最好表现的仍旧是最基本的线性回归。
