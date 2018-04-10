import pandas as pd
import numpy as np

iris = pd.read_csv("data/iris.csv") #import dataset as panda
iris_np = np.array(iris) #convert to numpy array

print ("Average of column 1 (Sepal Length) for all species is:", float("{0:.3f}".format(np.mean(iris_np[:, 0]))))
print ("Average of column 2 (Sepal Width) for all species is:\n", float("{0:.3f}".format(np.mean(iris_np[:, 1]))))
print ("Average of column 3 (Petal Length) for all species is:\n", float("{0:.3f}".format(np.mean(iris_np[:, 2]))))
print ("Average of column 4 (Petal Width) for all species is:\n", float("{0:.3f}".format(np.mean(iris_np[:, 3]))))

print ("Average of column 1 (Sepal Length) for Iris Setosa:\n",float("{0:.3f}".format(np.mean(iris_np[51:, 0])))) 
print ("Average of column 2 (Sepal Width) for Iris Setosa:\n", float("{0:.3f}".format(np.mean(iris_np[51:, 1]))))
print ("Average of column 3 (Petal Length) for Iris Setosa:\n", float("{0:.3f}".format(np.mean(iris_np[51:, 2]))))
print ("Average of column 4 (Petal Width) for Iris Setosa:\n", float("{0:.3f}".format(np.mean(iris_np[51:, 3]))))

print ("Average of column 1 (Sepal Length) for Iris Versicolor:\n",float("{0:.3f}".format(np.mean(iris_np[51:101, 0])))) 
print ("Average of column 2 (Sepal Width) for Iris Versicolor:\n", float("{0:.3f}".format(np.mean(iris_np[51:101, 1]))))
print ("Average of column 3 (Petal Length) for Iris Versicolor:\n",float("{0:.3f}".format(np.mean(iris_np[51:101, 2])))) 
print ("Average of column 4 (Petal Width) for Iris Versicolor:\n", float("{0:.3f}".format(np.mean(iris_np[51:101, 3]))))

print ("Average of column 1 (Sepal Length) for Iris Virginica:\n", (float("{0:.3f}".format(np.mean(iris_np[101:, 0]))))) 
print ("Average of column 2 (Sepal Width) for Iris Virginica:\n", float("{0:.3f}".format(np.mean(iris_np[101:, 1]))))
print ("Average of column 3 (Petal Length) for Iris Virginica:\n", float("{0:.3f}".format(np.mean(iris_np[101:, 2]))))
print ("Average of column 4 (Petal Width) for Iris Virginica:\n",float("{0:.3f}".format(np.mean(iris_np[101:, 3])))) 
import matplotlib.pyplot as pl

pl.hist(iris_np[51:, 0])
pl.show()

