#Hugh O'Reilly 11/04/18
#Iris Data Set Project
#Attempts to split up, summarise and plot data set 

import pandas as pd #pandas module imported
import numpy as np #numpy module imported
import matplotlib.pyplot as plt #matplotlib module imported

iris = pd.read_csv("data/iris.csv", names = ["sepal length", "sepal width", "petal length", "petal width", "species",]) #import dataset as panda
# credit to http://www.codeastar.com/beginner-data-science-tutorial/ for inspiration for lines 09-16
irisdata  = iris.values #ensures floats are used, strings eliminated

#setosa data sorted
Setosa = irisdata[:50][:,0:4]
Setosa1 = irisdata[:50][:,0:1]
Setosa2 = irisdata[:50][:,1:2]
Setosa3 = irisdata[:50][:,2:3]
Setosa4 = irisdata[:50][:,3:4]

print ('Mean of Setosa petal length is', np.mean(Setosa1))
print ('Mean of Setosa petal Width is', np.mean(Setosa2))
print ('Mean of Setosa Sepal length is', np.mean(Setosa3))
print ('Mean of Setosa Sepal Width is', np.mean(Setosa4))

#versicolor data sorted
Versicolor = irisdata[50:100][:,0:4]
Versicolor1 = irisdata[50:100][:,0:1]
Versicolor2 = irisdata[50:100][:,1:2]
Versicolor3 = irisdata[50:100][:,2:3]
Versicolor4 = irisdata[50:100][:,3:4]

print ('Mean of Versicolor petal length is', np.mean(Versicolor1))
print ('Mean of Versicolor petal Width is', np.mean(Versicolor2))
print ('Mean of Versicolor Sepal length is', np.mean(Versicolor3))
print ('Mean of Versicolor Sepal Width is', np.mean(Versicolor4))

#virginica data sorted
Virginica = irisdata[100:150][:,0:4]
Virginica1 = irisdata[100:150][:,0:1]
Virginica2 = irisdata[100:150][:,1:2]
Virginica3 = irisdata[100:150][:,2:3]
Virginica4 = irisdata[100:150][:,3:4]

print ('Mean of Virginica petal length is', np.mean(Virginica1))
print ('Mean of Virginica petal Width is', np.mean(Virginica2))
print ('Mean of Virginica Sepal length is', np.mean(Virginica3))
print ('Mean of Virginica Sepal Width is', np.mean(Virginica4))

print ('Setosa ', Setosa)
print ('Versicolor', Versicolor)
print ('Virginica', Virginica)
print (iris.describe()) #Overall summary of entire iris data: count, mean sd, min, %, max


#Some code for labelling, generating and printing histograms
fig1 = plt.figure(1)
fig2 = plt.figure(2)
fig3 = plt.figure(3)

#Initial attempts to display all plots individually
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
#Hist1 = (plt.hist(Setosa1))
plt.title('Setosa Petal Lengths')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Setosa1)
plt.show()
#Hist2 = (plt.hist(Setosa2))
plt.title('Setosa Petal Width')
plt.xlabel('size (cm)')
plt.ylabel('count')
plt.hist(Setosa2)
plt.show()
#plt.hist(Setosa2)
#plt.hist(Setosa2)
#plt.title('Setosa Sepal Length')
#plt.xlabel('size (cm)')
#plt.ylabel('count')
#plt.hist(Setosa4)
#plt.hist(Setosa4)
#plt.title('Setosa Sepal Width')
#plt.xlabel('size (cm)')
#plt.ylabel('count')
#plt.hist(Versicolor1)
#plt.hist(Versicolor2)
#plt.hist(Versicolor3)
#plt.hist(Versicolor4)
#plt.hist(Virginica1)
#plt.hist(Virginica2)
#plt.hist(Virginica3)
#plt.hist(Virginica4)
#plt.show(setosa1)
#plt.show(setosa2)
