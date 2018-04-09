import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("data/iris.csv") #import dataset as panda
dataset_np = np.array(dataset) #convert to numpy array
x = dataset_np [:3] #select first 4 columns
def mean(x):
    return sum ((x)/len(x)) #write function to define mean


 
print ("Average of column 1 (Sepal Length) for all species is:", float("{0:.3f}".format(mean(dataset_np[:, 0]))))
print ("Average of column 2 (Sepal Width) for all species is:\n", float("{0:.3f}".format(mean(dataset_np[:, 1]))))
print ("Average of column 3 (Petal Length) for all species is:\n", float("{0:.3f}".format(mean(dataset_np[:, 2]))))
print ("Average of column 4 (Petal Width) for all species is:\n", float("{0:.3f}".format(mean(dataset_np[:, 3]))))

print ("Average of column 1 (Sepal Length) for Iris Setosa:\n",float("{0:.3f}".format(mean(dataset_np[51:, 0])))) 
print ("Average of column 2 (Sepal Width) for Iris Setosa:\n", float("{0:.3f}".format(mean(dataset_np[51:, 1]))))
print ("Average of column 3 (Petal Length) for Iris Setosa:\n", float("{0:.3f}".format(mean(dataset_np[51:, 2]))))
print ("Average of column 4 (Petal Width) for Iris Setosa:\n", float("{0:.3f}".format(mean(dataset_np[51:, 3]))))

print ("Average of column 1 (Sepal Length) for Iris Versicolor:\n",float("{0:.3f}".format(mean(dataset_np[51:101, 0])))) 
print ("Average of column 2 (Sepal Width) for Iris Versicolor:\n", float("{0:.3f}".format(mean(dataset_np[51:101, 1]))))
print ("Average of column 3 (Petal Length) for Iris Versicolor:\n",float("{0:.3f}".format(mean(dataset_np[51:101, 2])))) 
print ("Average of column 4 (Petal Width) for Iris Versicolor:\n", float("{0:.3f}".format(mean(dataset_np[51:101, 3]))))

print ("Average of column 1 (Sepal Length) for Iris Virginica:\n", (float("{0:.3f}".format(mean(dataset_np[101:, 0]))))) 
print ("Average of column 2 (Sepal Width) for Iris Virginica:\n", float("{0:.3f}".format(mean(dataset_np[101:, 1]))))
print ("Average of column 3 (Petal Length) for Iris Virginica:\n", float("{0:.3f}".format(mean(dataset_np[101:, 2]))))
print ("Average of column 4 (Petal Width) for Iris Virginica:\n",float("{0:.3f}".format(mean(dataset_np[101:, 3])))) 
