#import modules
import os
import csv
from datetime import datetime

#set path to the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

#name variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
changes = []
max_increase_amount = float('-inf')
max_decrease_amount = float('inf')
max_increase_date = ""
max_decrease_date = ""

#open the CSV file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    #skip the header row
    next(csvreader)
    
    #loop through each row in the CSV file
    for row in csvreader:
        #count total months
        total_months += 1
        
        #extract date/profit/loss value from the row. Adding datetime module to format date from dd-m to m-dd
        date = row[0]
        profit_loss = int(row[1])
        
        #add profit/loss to the total
        total_profit_losses += profit_loss
        
        #calcualte change in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
            #calculate max increase and max decrease with date
            if change > max_increase_amount:
                max_increase_amount = change
                max_increase_date = date
            if change < max_decrease_amount:
                max_decrease_amount = change
                max_decrease_date = date
        
        #close loop
        previous_profit_loss = profit_loss

#calculate average change
average_change = sum(changes) / len(changes)


# Print the results
print("                        ")
print("Financial Analysis")
print("                        ")
print("-------------------------")
print("                        ")
print("Total Months:", total_months)
print("Total Profit/Losses: $", total_profit_losses)
print("Average Change: $", round(average_change, 2))
print("Greatest Increase in Profits:", max_increase_date, "($", max_increase_amount,")")
print("Greatest Decrease in Profits:", max_decrease_date, "($", max_decrease_amount,")")

#Export analysis to txt file
output_path = os.path.join("analysis", "analysis.txt")

#open the file using "write" mode. Specifiy the variable to hold the contents
with open(output_path, "w") as txt_file:

    #print analysis output with spaces
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total Profit/Losses: ${total_profit_losses}\n")
    txt_file.write(f"Average Change: ${round(average_change, 2)}\n")
    txt_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount})\n")
    txt_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount})\n")
