import os
import csv


budget_data = os.path.join("Resources", "budget_data.csv")

# The total number of months included in the dataset

# The net total amount of Profit/Losses over the entire period

# Calculate the changes in Profit/Losses over the enire period,
# then thin dthe average of those changes.

# The greatestincrease in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#with open(budget_data, 'r') as text:
    #print(text)
    #lines = text.read()
    #print(lines)

#with open(budget_data)as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #for row in csvreader:
    #print(row)
csv_file = csv.reader(open(budget_data))
months = 0
for row in csv_file:    
    months = row[0]
    months = str(months)
    print(months)


