import csv
import numpy as numpy
import matplotlib.pyplot as plt

with open("data/iris.csv", 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    
    for line in f:# loops through each line
        line = line.replace(',', '   ') #replaces comma with space, code from Mohamed Noor
        line = line.rstrip() #Removes nextline code on end, code from Mohamed Noor
        print(line.split(',')) #Splits and Prints 
        #each line as a list, colon separates each item in
        # columns
    
    print (f.read())

