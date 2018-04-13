# Iris-Data-Set-Project

The Search For The Holy Grail
> ARTHUR: What manner of man are you that can summon up fire without flint or tinder?
TIM:
> I... am an enchanter.
ARTHUR: 
> By what name are you known?
TIM:  
>There are some who call me... 'Tim'? 
## Hugh O'Reilly 01/04/2018
## Exploration of the Iris Data set using Python
## python files in this repository
### Irisdata.py = a basic few lines of code to import csv file and sort into rows and column
### IrisData_np.py attempt to import pandas, numpy and matplotlib packages and work on data set
### Irisdata_mean.py is an initial attempt to write simple functions on irisdata set as csv file
## PROJECT PLANNING:
  ### 1.0 INTRODUCTION
  #### 1.1 The Iris Data Set
   The iris data set was first described in a paper written by R.A. Fisher in the *Annals of Human Genetics* in 1936. It is a data set of 50 samples which the author gathered on each of three species of Irises: *setosa*, *versicolor* and *virginica*. Measurements of 4 properties of 50 flowers of each of the plants were taken, namely Sepal length, Sepal width, Petal Length, and Petal width. The author suggests that these characteristics can be used to identify which species they belong to based on a linear discriminant model. Fischer himself developed the linear discriminant model,a statistical, machine learning and pattern recognition technique used to distinguish between two or more objects, classes or events. Ref [Linear discriminant analysis] [https://en.wikipedia.org/wiki/Linear_discriminant_analysis]Ref [Iris Data set wikipedia] [https://en.wikipedia.org/wiki/Iris_flower_data_set]  Fischer presented the data for the 3 species in a table  with each of the four measurements and subsequently, tables of observed means, sums of squares etc in order to demonstrate how each species can be discriminated from one another. Ref [The use of multiple measurements in taxonomic problems][http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf]
    
   #### 1.2 Background to Fishers Iris Data Set Analysis
  
   #### 1.3 Simple Python functions
   #### 1.4 Python Packages
   ##### Numpy

   The NumPy package is a basic package for scientific computation in python. It is also particularly useful as a container for multidimensional data which makes NumPy arrays easy to work with,manipulate and analyse. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases. Ref [NumPy][https://docs.scipy.org/doc/numpy/index.html]

   #### Matplotlib

   The Matplotlib python library is used to make charts such as histograms, plots and bar charts. The pyplot module is used in this project to generate simple histograms of the python data set for example in file 'Iris_data_np_v2.py'. Addition of add-on toolkits such as 3d plotting with mplot3d enhance the functionality of the matplotlib library. Ref [matplotlib] [https://matplotlib.org/]

   #### 1.5 Literature Review
    
   ### 2.0 EXPERIMENTAL

   Work done on the data set

   #### 2.1 Downloading and importing the Data Set

   note to self: look up *csv* module in Python's standard library :+1:

   #### 2.2 Simple Python scripts
   #### 2.3 Simple Statistical Analysis
  Some simple calculations on the data set might involve getting the mean of each column i.e. looping through column 1 to 4, getting the sum of each column and dividing by the number of rows to get the mean. This loop would have to terminate at the strings in the data set.

  The IrisData_mean.py file in this repository has been written using the NumPy package to carry out simple statistical analysis of the data set.

  The next step might be to calculate the mean of each property: Sepal length, Sepal width, Petal Length, and Petal width for each species.

  Further work would be to calculate the standard deviation from the mean for each property
   ### 3.0  DISCUSSION AND CONCLUSION

   ### REFERENCES
