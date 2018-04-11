#Hugh O'Reilly 11/04/18
#Iris Data Set Project
#attempts to split up data set 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv("data/iris.csv") #import dataset as panda
iris_np = np.array_split(iris, 3) #convert to numpy array and split into 3
#doesnt split evenly

np.hsplit(iris_np,(0,4)) #split floats from strings 
np.vsplit(iris_np,(0,49)) #split array at setosa
np.vsplit(iris_np,(49,99)) #split array at versicolor
np.vsplit(iris_np,(99,150)) #split array at virginica

np.hsplit(iris_np,(0,1)) #splits first column
np.hsplit(iris_np,(1,2)) #splits second column
np.hsplit(iris_np,(2,3)) #splits third column
np.hsplit(iris_np,(3,4)) #splits fourth column

#Some code for labelling, generating and printing histograms
#plt.xlabel('')
#plt.ylabel('count')
#plt.hist.
#plt.show()

