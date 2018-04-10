import pandas as pd
import numpy as np

iris = pd.read_csv("data/iris.csv") #import dataset as panda
iris_np = np.array(iris) #convert to numpy array

np.vsplit(iris_np, 49) #split iris data set by row 49 (iris Setosa subset)

iris setosa = (np.vsplit(iris_np, 49)) #note to self: error: need to remove column with string?