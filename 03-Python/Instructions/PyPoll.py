#!/usr/bin/env python
# coding: utf-8

# # import libraries

# In[1]:


#importing needed libraries
import csv
import os
import statistics 


# # Open the file

# In[52]:


#opening the file
csvpath = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')
lines = 0
csvpath = r"PyPoll\Resources\election_data.csv"

voter_id = []
county = []
candidate = []

#reading the data file
with open(csvpath) as csvfile:    
    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader)  #Storing the header row'
    for row in csv_reader:     #putting id,county, and candidate in individual lists
        v_id = row[0]      
        co = row[1]
        ca = row[2]
        voter_id.append(v_id)
        county.append(co)
        candidate.append(ca)        


# ## Calulating all of the needed metrics

# In[56]:


#Calculating all of the needed metrics
total_votes = len(voter_id)
print(f"Total Votes = {total_votes}")
count_khan = candidate.count("Khan")
count_correy = candidate.count("Correy")
count_li = candidate.count("Li")
count_otooley = candidate.count("O'Tooley")

per_khan = count_khan/total_votes * 100
per_correy = count_correy/total_votes *100
per_li = count_li/total_votes *100
per_otooley= count_otooley/total_votes *100


# ## Projecting a winner

# In[57]:


#Projecting a winner
winner = []
winner.append(count_khan)
winner.append(count_correy)
winner.append(count_li)
winner.append(count_otooley)
winner_amount = max(winner)
winner_index = winner.index(winner_amount)

if winner_index == 0:
    winner_line = "Winner: Khan"
elif (winner_index == 1):
    winner_line = "Winner: Correy"
elif (winner_index == 2):
    winner_line = "Winner: Li"
elif (winner_index == 3):
    winner_line = "Winner: O'Tooley"
else:
    winner_line = "error in projecting winner"


# ## Printing the Report

# In[60]:


#Printing the Report
#Writing to the screen and the data file
with open('pypoll_output_file.txt', 'w') as file:  # Use file to refer to the file object

    line = "Election Results"
    print(line)
    file.write(line)
    file.write("\n")
    line = "========================="
    print(line)
    file.write(line)
    file.write("\n")
    line = f"Total Votes: {total_votes}"
    print(line)
    file.write(line)
    file.write("\n")
    line = "========================="
    print(line)
    file.write(line)
    file.write("\n")
    line = f"Khan:  {per_khan:.2f}% ({count_khan})"
    print(line)
    file.write(line)
    file.write("\n")
    line = f"Correy:  {per_correy:.2f}% ({count_correy})"
    print(line)
    file.write(line)
    file.write("\n")
    line = f"Li:  {per_li:.2f}% ({count_li})"
    print(line)
    file.write(line)
    file.write("\n")
    line = f"O'Tooley:  {per_otooley:.2f}% ({count_otooley})"
    print(line)
    file.write(line)
    file.write("\n")
    line = "========================="
    print(line)
    file.write(line)
    file.write("\n")
    print(winner_line)
    file.write(line)
    file.write("\n")
    
    

