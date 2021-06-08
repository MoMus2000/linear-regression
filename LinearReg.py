import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class LinearRegression:

	def __init__(self):
		self.m = None
		self.b = None


	def train(self, X_train,y_train):
		num = 0
		denom = 0

		for i in range(0,X_train.shape[0]):
			num = num + ((X_train[i] - X_train.mean())*(y_train[i]-y_train.mean()))	
			denom = denom + ((X_train[i] - X_train.mean())*((X_train[i] - X_train.mean())))


		self.m = num/denom
		self.b = y_train.mean()- self.m*X_train.mean() 

		print(self.m)
		print(self.b)


	def predict(self,X_train):
		return self.m*X_train+self.b



if __name__ == '__main__':
	lg = LinearRegression()
	df = pd.read_csv("data.csv")
	X = df['cgpa'].values
	y = df['package'].values
	X_train,X_test,y_train,y_test = train_test_split(X,y)
	lg.train(X_train,y_train)
	print(lg.predict(8.5))

