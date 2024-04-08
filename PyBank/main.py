# Dependencies
import os
import csv

# The file to write to 
csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Opening the file using "write" mode and specify the variable to hold the contents
with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.DictReader(csvfile)  
            # Unlike csv.reader, in csv.Dictreader the first row is represented as the header 
            # but when using csv.reader, one can use--csv_header = next(csvreader)-- to read the header row
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Count total number of months
        total_months += 1

        # Calculate net total amount of Profit/Losses
        net_total += int(row['Profit/Losses'])

        # Calculate change in Profit/Losses
        change = int(row['Profit/Losses']) - previous_profit_loss
        previous_profit_loss = int(row['Profit/Losses'])
        changes.append(change)

        # Check for greatest increase and decrease
        if change > greatest_increase[1]:
            greatest_increase = [row['Date'], change]
        if change < greatest_decrease[1]:
            greatest_decrease = [row['Date'], change]

# The average change
average_change = sum(changes[1:]) / len(changes[1:])

# Writing the analysis to text file
output_file_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------>\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# # print(f"Financial analysis results have been saved to {output_file_path}")

# # Print analysis to terminal
# print("Financial Analysis")
# print("------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${net_total}")
# print(f"Average Change: ${average_change:.2f}")
# print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
# print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")