"""Caden Khuu
CA
SoftDev
K06: Divine your Destiny (dictionary from csv file)
2024-09-19
time spent: 1 hour"""

import csv #used for reading csv
import random
d = {} #create dictionary


def createList():
 with open('occupations.csv', newline='') as csvfile: # reads csv file
    l = csv.reader(csvfile)
    for row in l:
        if (row[0] != 'Job Class') and (row[0] != 'Total'):
            #print(row[0])
            #print(row[1])
            d.update({row[0]:float(row[1])})
       
def rand():
    x = random.uniform(0.0,99.8)
    #print(x)
    for key, value in d.items():
        x = x - value 
        if x <= 0: #move on to next occupation if necessary
            print(key)
            break
createList()
rand()
