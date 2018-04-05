import csv
import pandas
import numpy as np
import matplotlib.pyplot as plt

with open("data/iris.csv", 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    f = np.array(f)
    for line in f:# loops through each line
        #print(line.split(',')[0]) #Prints each line as a list
                    
        print (sum(f), "sum of row 1 = "  )
    #print (total)

