#Hugh O'Reilly 11/04/18
#Iris Data Set Project
#Attempts to split up, summarise and plot data set 
#Uses less code than previous work on the data set and generates histograms with labelled axes and titles
import pandas as pd #pandas module imported
import numpy as np #numpy module imported
import matplotlib.pyplot as plt #matplotlib module imported

iris = pd.read_csv("data/iris.csv", names = ["sepal length", "sepal width", "petal length", "petal width", "species",]) #import dataset as panda
# credit to http://www.codeastar.com/beginner-data-science-tutorial/ for inspiration for lines 09-18
irisdata  = iris.values #ensures floats are used, strings eliminated

#setosa data sorted
Setosa = irisdata[:50][:,0:4] #the entire setosa data set
Setosa1 = irisdata[:50][:,0:1] #setosa petal length
Setosa2 = irisdata[:50][:,1:2] #setosa petal width
Setosa3 = irisdata[:50][:,2:3] #setosa sepal length
Setosa4 = irisdata[:50][:,3:4] #setosa sepal width

print ('Mean of Setosa petal length is', np.mean(Setosa1))
print ('Mean of Setosa petal Width is', np.mean(Setosa2))
print ('Mean of Setosa Sepal length is', np.mean(Setosa3))
print ('Mean of Setosa Sepal Width is', np.mean(Setosa4))

#versicolor data sorted
Versicolor = irisdata[50:100][:,0:4] #The entire Versicolor data set
Versicolor1 = irisdata[50:100][:,0:1] #Versicolor petal length
Versicolor2 = irisdata[50:100][:,1:2] #Versicolor petal width
Versicolor3 = irisdata[50:100][:,2:3] #Versicolor sepal length
Versicolor4 = irisdata[50:100][:,3:4] #Versicolor sepal width

print ('Mean of Versicolor petal length is', np.mean(Versicolor1))
print ('Mean of Versicolor petal Width is', np.mean(Versicolor2))
print ('Mean of Versicolor Sepal length is', np.mean(Versicolor3))
print ('Mean of Versicolor Sepal Width is', np.mean(Versicolor4))

#virginica data sorted
Virginica = irisdata[100:150][:,0:4] #The entire Virginica data set
Virginica1 = irisdata[100:150][:,0:1] #Virginica petal length
Virginica2 = irisdata[100:150][:,1:2] #Virginica petal width
Virginica3 = irisdata[100:150][:,2:3] #Virginica sepal length
Virginica4 = irisdata[100:150][:,3:4] #Virginica sepal width

print ('Mean of Virginica petal length is', np.mean(Virginica1))
print ('Mean of Virginica petal Width is', np.mean(Virginica2))
print ('Mean of Virginica Sepal length is', np.mean(Virginica3))
print ('Mean of Virginica Sepal Width is', np.mean(Virginica4))

print ('Setosa:\n', Setosa)
print ('Versicolor:\n', Versicolor)
print ('Virginica:\n', Virginica)
print (iris.describe()) #Overall summary of entire iris data: count, mean sd, min, %, max


#Some code for labelling, generating and printing histograms
fig1 = plt.figure(1)
fig2 = plt.figure(2)
fig3 = plt.figure(3)

#Initial attempts to display all plots individually as simple line graphs
ax1 = fig1.add_subplot(221)
ax1.plot(Setosa1)
ax1.set(title = 'Setosa Petal Length')

ax2 = fig1.add_subplot(222)
ax2.set(title = 'Setosa Petal Width')
ax2.plot(Setosa2)

ax3 = fig1.add_subplot(223)
ax3.set(title = 'Setosa Sepal Length')
ax3.plot(Setosa3)

ax4 = fig1.add_subplot(224)
ax4.set(title = 'Setosa Sepal Width')
ax4.plot(Setosa4)

ax5 = fig2.add_subplot(221)
ax5.set(title = 'Versicolor Petal Length')
ax5.plot(Versicolor1)

ax6 = fig2.add_subplot(222)
ax6.set(title = 'Versicolor Petal Width')
ax6.plot(Versicolor2)

ax7 = fig2.add_subplot(223)
ax7.set(title = 'Versicolor Sepal Length')
ax7.plot(Versicolor3)

ax8 = fig2.add_subplot(224)
ax8.set(title = 'Versicolor Sepal Width')
ax8.plot(Versicolor4)

ax9 = fig3.add_subplot(221)
ax9.set(title = 'Virginica Petal Length')
ax9.plot(Virginica1)

ax10 = fig3.add_subplot(222)
ax10.set(title = 'Virginica Petal Width')
ax10.plot(Virginica2)

ax11 = fig3.add_subplot(223)
ax11.set(title = 'Virginica Sepal Length')
ax11.plot(Virginica3)

ax12 = fig3.add_subplot(224)
ax12.set(title = 'Virginica Sepal Width')
ax12.plot(Virginica4)

plt.show()


#The following outputs histograms of all characteristics of all species using the pyplot function on matplotlib

#Histogram 1 Setosa Petal Length
plt.title('Setosa Petal Length')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Setosa1)
plt.show()

#Histogram 2 Setosa Petal Width
plt.title('Setosa Petal Width')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Setosa2)
plt.show()

#Histogram 3 Setosa Sepal Length
plt.title('Setosa Sepal Length')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Setosa3)
plt.show()
# Histogram 4 Setosa Sepal Width
plt.title('Setosa Sepal Width')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Setosa4)
plt.show()

#Histogram 5 Versicolor Petal Length
plt.title('Versicolor Petal Lengths')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Versicolor1)
plt.show()

#Histogram 6 Versicolor Petal Width
plt.title('Versicolor Petal Width')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Versicolor2)
plt.show()

#Histogram 7 Versicolor Sepal Length
plt.title('Versicolor Sepal Length')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Versicolor3)
plt.show()

#Histogram 8 Versicolor Sepal Width
plt.title('Versicolor Sepal Width')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Versicolor4)
plt.show()

#Histogram 9 Virginica Petal Length
plt.title('Virginica Petal Length')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Virginica1)
plt.show()

#Histogram 10 Virginica Petal Width
plt.title('Virginica Petal Width')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Virginica2)
plt.show()

#Histogram 11 Virginica Sepal Length
plt.title('Virginica Sepal Length')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Virginica3)
plt.show()

#Histogram 12 Virginica Sepal Length
plt.title('Virginica Sepal Width')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Virginica3)
plt.show()

