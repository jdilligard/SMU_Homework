#!/usr/bin/env python
# coding: utf-8

# # import libraries

# In[4]:


#importing needed libraries
import csv
import os
import statistics 


# # Open the file

# In[15]:


#opening the file
csvpath = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')
lines = 0
csvpath = r"PyBank\Resources\budget_data.csv"

dates = []
profloss = []
profincr = [0]

#reading the data file
with open(csvpath) as csvfile:    
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader)  #Storing the header row'
    i = 1  

    for row in csv_reader:     #putting the dates and profits in individual lists
        day = row[0]       
        money = int(row[1])     
        dates.append(day)
        profloss.append(money)
        
         

while i < len(profloss):       #Calculating the profit/loss 
    thisprof = i-1
    nextprof = i
    profincr.append(profloss[nextprof] - profloss[thisprof])
    i=i+1

total_months = len(profloss)  #Getting the requested data
max_pf= max(profincr)
min_pf = min(profincr)
sum_pf = sum(profloss)

max_index = profincr.index(max_pf)
min_index = profincr.index(min_pf)
max_date = dates[max_index]
min_date = dates[min_index]
profincr.remove(0)                #I calculated this offset
avg_ch = statistics.mean(profincr)


#Writing to the screen and the data file
with open('pybank_output_file.txt', 'w') as file:  # Use file to refer to the file object

    title1 = "Financial Analysis"
    print(title1)
    file.write(title1)
    file.write("\n")
    title2 = "---------------------"
    file.write("\n")
    print(title2)
    file.write(title2)
    file.write("\n")
    title3 = f"Total Months:{total_months}\n "    #Using f'strings to format  
    print(title3)
    file.write(title3)
    title3 = f"Total: ${sum_pf}\n "  
    print(title3)
    file.write(title3)
    title3 = f"Average Change: ${avg_ch:.2f}\n "    #setting the change part of this dollar amount
    print(title3)
    file.write(title3)
    title3 = f"Greatest Increase in Profits: {max_date}  (${max_pf})\n "
    print(title3)
    file.write(title3)
    title3 = f"Decrease Increase in Profits: {min_date}  (${min_pf})\n "
    print(title3)
    file.write(title3)

        

