import os
import csv


budget_data = os.path.join("Resources", "budget_data.csv")

totmon = []
pltot = []
plchg = 0.0



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

with open(budget_data)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader, None)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)