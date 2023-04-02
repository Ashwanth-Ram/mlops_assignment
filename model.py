import pandas as pd

data=pd.read_csv(r"C:\Users\Ashwanth Ram A S\Desktop\mlops\placement.csv")

x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.linear_model import LinearRegression
regression = LinearRegression()

regression.fit(x,y)


import pickle

pickle.dump(regression,open(r"C:\Users\Ashwanth Ram A S\Desktop\mlops\model.pkl",'wb'))
