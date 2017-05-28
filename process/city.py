#-!- coding:utf-8- -*-
import csv
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import time
import matplotlib.pyplot as plt

def processing(nowCityName, myX, Y):
    Y = np.array(Y)
    myX = np.array(myX)
    nowTime = time.localtime().tm_sec
    trainX, testX, trainY, testY = train_test_split(myX,Y, test_size=0.1, random_state=nowTime)

    # xgb DMatrix
    data_training = xgb.DMatrix(trainX, label=trainY)
    data_testing = xgb.DMatrix(testX, label=testY)

    # xgb parameter
    param = {'silent':1, 'max_depth':3, 'eta':1,}

    # training
    model = xgb.train(param, data_training)

    # prediction
    data_predict = model.predict(data_testing)

    # accuracy evaluate
    avg = 0.0
    for i in range(len(testY)):
        avg += (abs(data_predict[i]-testY[i]))/testY[i]
    avg /= len(testY)
    print("%s: %f percent" % (nowCityName, avg*100))




dataset = np.genfromtxt('./myProcessedData.csv', delimiter=",")
Y = dataset[1:,1:2]
cities = []
f = open('./myProcessedData.csv', 'r')
csvReader = csv.reader(f)
for row in csvReader:
	cities.append(row[3])
f.close()
cities = cities[1:]

myX = []
for i in range(1, len(dataset)):
	row = dataset[i][4:6]
	myX.append(row)

nowCity = cities[0]
cityNum = 0
nowRow = []
nowY = []
for i in range(len(cities)):
	if nowCity == cities[i]:
		nowRow.append(myX[i])
		nowY.append(Y[i])		
	else:
		processing(nowCity, nowRow, nowY)
		nowCity = cities[i]
		i-=1
		nowRow=[]
		nowY=[]

