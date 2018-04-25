#Hugh O'Reilly 25/04/18
#Iris Data Set Project
#Investigation of the seaborn package
# Seaborn is reliant on prequisite packages imported including numpy, pandas, matplotlib and scipy
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns; sns.set() #imports the seaborn python package
import scipy as sc
iris = pd.read_csv("data/iris.csv", names = ["sepal length", "sepal width", "petal length", "petal width", "species",]) #import dataset as panda
iris1 = sns.load_dataset("iris") #loads the iris dataset in 'seaborn' format
iris1.head() #displays first 8 rows of dataset

g = sns.PairGrid(iris1)
g = sns.pairplot(iris1, hue="species") #creates a plot of pairs of attributes
g = g.map(plt.scatter) 
plt.show()
