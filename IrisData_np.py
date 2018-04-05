import csv
import pandas
import numpy as np
import matplotlib.pyplot as plt
dataset = pandas.read_csv("data/iris.csv") #import dataset as panda
dataset_np = np.array(dataset) #convert to numpy array
print (dataset_np[:])



