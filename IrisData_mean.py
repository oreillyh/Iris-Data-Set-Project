#Hugh O'Reilly 11/04/18
#Iris Data Set Project
#attempts to calculate means and standard deviations for each species
# Updated on 23/04/18 to include calculations for standard deviations
import pandas as pd
import numpy as np

iris = pd.read_csv("data/iris.csv") #import dataset as panda
iris_np = np.array(iris) #convert to numpy array

#printing of means of each characteristic for each species, to 3 decimal places
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


#Function to calculate standard deviations
stddev_sl_set = (np.std(iris_np[51:, 0]))
stddev_sw_set = (np.std(iris_np[51:, 1]))
stddev_pl_set = (np.std(iris_np[51:, 2]))
stddev_pw_set = (np.std(iris_np[51:, 3]))

stddev_sl_Vers = (np.std(iris_np[51:101, 0]))
stddev_sw_Vers = (np.std(iris_np[51:101, 1]))
stddev_pl_Vers = (np.std(iris_np[51:101, 2]))
stddev_pw_Vers = (np.std(iris_np[51:101, 3]))

stddev_sl_Vir = (np.std(iris_np[101:, 0]))
stddev_sw_Vir = (np.std(iris_np[101:, 1]))
stddev_pl_Vir = (np.std(iris_np[101:, 2]))
stddev_pw_Vir = (np.std(iris_np[101:, 3]))

#printing of Standard Deviations of each characteristic for each species, to 3 decimal places
print ("Standard deviation of Sepal Length for Iris Setosa:\n",float("{0:.3f}".format(stddev_sl_set)))
print ("Standard deviation of Sepal Width for Iris Setosa:\n",float("{0:.3f}".format(stddev_sw_set)))
print ("Standard deviation of Petal Length for Iris Setosa:\n",float("{0:.3f}".format(stddev_pl_set)))
print ("Standard deviation of Petal Width for Iris Setosa:\n",float("{0:.3f}".format(stddev_pw_set)))

print ("Standard deviation of Sepal Length for Iris Versicolor:\n",float("{0:.3f}".format(stddev_sl_Vers)))
print ("Standard deviation of Sepal Width for Iris Versicolor:\n",float("{0:.3f}".format(stddev_sw_Vers)))
print ("Standard deviation of Petal Length for Iris Versicolor:\n",float("{0:.3f}".format(stddev_pl_Vers)))
print ("Standard deviation of Petal Width for Iris Versicolor:\n",float("{0:.3f}".format(stddev_pw_Vers)))

print ("Standard deviation of Sepal Length for Iris Virginica:\n",float("{0:.3f}".format(stddev_sl_Vir)))
print ("Standard deviation of Sepal Width for Iris Virginica:\n",float("{0:.3f}".format(stddev_sw_Vir)))
print ("Standard deviation of Petal Length for Iris Virginica:\n",float("{0:.3f}".format(stddev_pl_Vir)))
print ("Standard deviation of Petal Width for Iris Virginica:\n",float("{0:.3f}".format(stddev_pw_Vir)))