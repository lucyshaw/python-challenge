#import libraries
import os
import csv

profitsLoss = []
date = []

#pull csv file
csvpath = os.path.join("budget_data.csv")
#close the file after completing the tasks
with open (csvpath) as csvfile:
   #read the csv file 
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header in count
    next(csvreader)
   
    #loop throgh csv file 
    for row in csvreader:  
    #add dates into date list
        date.append(row[0])
        #add profits/losses into pL list
        profitsLoss.append(int(row[1]))
    totalPL = sum(profitsLoss)

    increase = profitsLoss[0]
    decrease = profitsLoss[0]

    for r in range(len(profitsLoss)):
        if profitsLoss[r] >= increase:
            increase = profitsLoss[r]
            increase_month = date[r]
        elif profitsLoss[r] <= decrease:
            decrease = profitsLoss[r]
            decrease_month = date[r]
   #set initial total change to 0
    totalChange = 0
    for r in range(len(profitsLoss)-1):
       change = (profitsLoss[r+1] - profitsLoss[r])
       totalChange = totalChange + change

    average_change = totalChange / (len(date)-1)
     
print(f"The total number of months is {len(date)}.")
print(f"The total profit and loss value is ${totalPL}.")
print(f"The average change in profits and loss between months is ${round(average_change, 2)}.")
print(f"The greatest increase was ${increase} and occured in {increase_month}.")
print(f"The greatest decrease was ${decrease} and occured in {decrease_month}.")

#write to txt file
write_file = f'pybank_analysis.txt'
filewriter = open(write_file, mode='w')

filewriter.write(f"The total number of months is {len(date)}.")
filewriter.write(f"The total profit and loss value is ${totalPL}.")
filewriter.write(f"The average change in profits and loss between months is ${round(average_change, 2)}.")
filewriter.write(f"The greatest increase was ${increase} and occured in {increase_month}.")
filewriter.write(f"The greatest decrease was ${decrease} and occured in {decrease_month}.")

filewriter.close()
  
