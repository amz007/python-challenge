#import modules
import os
import csv

#set path to the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#create dictionary to store votes
votes = {}

#name variables
total_votes = 0

#open the CSV file
with open(csvpath) as csvfile:

    #create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    #skip the header row
    next(csvreader)
    
    #loop through each row in the CSV file
    for row in csvreader:


        #count candidate votes
        candidate = row[2]
        votes[candidate] = votes.get(candidate, 0) + 1
        total_votes += 1


#calculate percentage of votes each candidate won
winner = None
winner_votes = 0
    
#percentage dictionary, store all votes by candidates and create percentage
percentages = {candidate: (votes[candidate] / total_votes) * 100 for candidate in votes}

#print results
print("\nElection Results")
print("\n-------------------------")
print("\nTotal Votes:", total_votes)
print("\n-------------------------")
for candidate, votes_won in votes.items():
    percentage = (votes_won / total_votes) * 100
    print(f"\n{candidate}: {percentage: .3f}% ({votes_won})")
    if votes_won > winner_votes:
        winner = candidate
        winner_votes = votes_won
print("\n-------------------------")
print(f"\nWinner: {winner}")
print("\n-------------------------")

#Export analysis to txt file
output_path = os.path.join("analysis", "analysis.txt")

#open the file using "write" mode. Specifiy the variable to hold the contents
with open(output_path, "w") as txt_file:

    #print to text file
    txt_file.write("\nElection Results\n")
    txt_file.write("\n-------------------------\n")
    txt_file.write(f"\nTotal Votes: {total_votes}\n")
    txt_file.write("\n-------------------------\n")
    for candidate, votes_won in votes.items():
        percentage = percentages[candidate]
        txt_file.write(f"\n{candidate}: {percentage: .3f}% ({votes_won} votes)\n")
    txt_file.write("\n-------------------------\n")
    txt_file.write(f"\nWinner: {winner}\n")
    txt_file.write("\n-------------------------")

