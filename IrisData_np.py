import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("data/iris.csv") #import dataset as panda
dataset_np = np.array(dataset) #convert to numpy array
x = dataset_np [:3] #select first 4 columns
def mean(x):
    return sum (x)/len(x) #write function to define mean
print ("Average of column 1 (Sepal Length) for all species is:", mean(dataset_np[:, 1]))
    




