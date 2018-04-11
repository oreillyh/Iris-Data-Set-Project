# Hugh O'Reilly 11/04/18
# Irisdata Set Project
# Attempt to split up data from each species

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv("data/iris.csv")

# Found the following function to try to split data evenly
# input - iris: Iris data set, chunkSize: the chunk size
# output - a list of DataFrame
# purpose - splits the DataFrame into smaller of max size chunkSize (last is smaller)
# Credit : https://stackoverflow.com/questions/17315737/split-a-large-pandas-dataframe

def split_iris(iris, chunkSize = 151): 
    listOfiris = list()
    numberChunks = len(iris) // chunkSize + 1
    for i in range(numberChunks):
       listOfiris.append(iris[i*chunkSize:(i+1)*chunkSize])
    return listOfiris

iris_split2 = split_iris(iris, chunkSize = 49)   

#print(iris_split2[0]) #print Iris Setosa data
#print(iris_split2[1]) #print Iris Versicolor data
#print(iris_split2[2]) #print Iris Virginica data


np.hsplit(iris_split2[0],(0,1)) #splits first column Iris Setosa data
#np.hsplit(iris_split2[0],(1,2)) #splits second column Iris Setosa data
#np.hsplit(iris_split2[0],(2,3)) #splits third column Iris Setosa data
#np.hsplit(iris_split2[0],(3,4)) #splits fourth column Iris Setosa data


print (np.hsplit(iris_split2[0],(0,1)))

