# Dependencies
import os
import csv

# The file to write to 
csvpath = os.path.join('Resources', 'election_data.csv')

# Variables
total_votes = 0
candidates = {}

# Opening the file using "write" mode and specify the variable to hold the contents
with open(csvpath, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)  

# Iterate through rows in the CSV
        for row in csvreader:
            # Count total number of votes
            total_votes += 1
            
            # Extract candidate name
            candidate_name = row['Candidate']
            
            # Update candidate's vote count
            if candidate_name in candidates:
                candidates[candidate_name] += 1
            else:
                candidates[candidate_name] = 1
    
# Calculate percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}
    
# Determine the winner based on popular vote
winner = max(candidates, key=candidates.get)
    
# Write analysis to text file
output_file_path = os.path.join('analysis', 'election_results.txt')
with open(output_file_path, 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write("----------------->\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("----------------->\n")
        for candidate, votes in candidates.items():
            output_file.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
        output_file.write("----------------->\n")
        output_file.write(f"Winner: {winner} :) \n")
        output_file.write("----------------->\n")

# # print(f"Election results have been saved to {output_file_path}")      

# # Print analysis to terminal
# print("Election Results")
# print("------------------>")
# print(f"Total Votes: {total_votes}")
# print("------------------>")
# for candidate, votes in candidates.items():
#     print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
# print("------------------>")
# print(f"Winner: {winner}")
# print("------------------>")
    