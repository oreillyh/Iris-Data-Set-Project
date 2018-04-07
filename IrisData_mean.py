import math
import pandas
import numpy as np
import matplotlib.pyplot as plt
dataset = pandas.read_csv("data/iris.csv") #import dataset as panda
dataset_np = np.array(dataset) #convert to numpy array
x = dataset_np [:3] #select first 4 columns
def mean(x):
    return sum (x)/len(x) #write function to define mean
print ("Average of column 1 (Sepal Length) for all species is:", mean(dataset_np[:, 0]))
print ("Average of column 2 (Sepal Width) for all species is:\n", mean(dataset_np[:, 1]))
print ("Average of column 3 (Petal Length) for all species is:\n", mean(dataset_np[:, 2]))
print ("Average of column 4 (Petal Width) for all species is:\n", mean(dataset_np[:, 3]))