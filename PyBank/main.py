# create file path acorss operating system and module for reading CSV files
import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#open and read the csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimeter=',')

    #read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
       



