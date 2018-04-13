#Hugh O'Reilly 11/04/18
#Iris Data Set Project
#Attempts to split up, summarise and plot data set 

import pandas as pd #pandas module imported
import numpy as np #numpy module imported
import matplotlib.pyplot as plt #matplotlib module imported

iris = pd.read_csv("data/iris.csv", names = ["sepal length", "sepal width", "petal length", "petal width", "species",]) #import dataset as panda
# credit to http://www.codeastar.com/beginner-data-science-tutorial/ for inspiration for lines 09-16
irisdata  = iris.values #ensures floats are used, strings eliminated
Setosa = irisdata[:49][:,0:4]
Setosa1 = irisdata[:49][:,0:1]
Setosa2 = irisdata[:49][:,1:2]
Setosa3 = irisdata[:49][:,2:3]
Setosa4 = irisdata[:49][:,3:4]

print (iris.describe()) #Overall summary of entire iris data: count, mean sd, min, %, max


#Some code for labelling, generating and printing histograms
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Setosa1)
plt.hist(Setosa2)
plt.hist(Setosa3)
plt.hist(Setosa4)
plt.show()

