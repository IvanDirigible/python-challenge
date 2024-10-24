# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list =[]
list_item = None
great_inc = 0
great_dec = 0
def average(n):
   return sum((n)) / len(n)

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Track the total and net change
    # Process each row of data
    for row in reader:

        # Track the total
      total_months = total_months + 1

        # Track the net change, running comparisons on all but the first row
      if list_item != None:  
        list_item = int(row[1]) - list_item
        net_change_list.append(list_item)

          # Calculate the greatest increase in profits (month and amount)
        if list_item > great_inc:
          great_inc = list_item
          month_inc = row[0]

          # Calculate the greatest decrease in losses (month and amount)
        if list_item < great_dec:
          great_dec = list_item
          month_dec = row[0]

       # If first item in loop, set as list item
      list_item = int(row[1])
       # Add value to total
      total_net = total_net + int(row[1])

# Calculate the average net change across the months
net_change = round(average(net_change_list), 2)

# Generate the output summary
output = (
f"Financial Analysis\n\
----------------------------\n\
Total Months: {total_months}\n\
Total: ${total_net}\n\
Average Change: ${net_change}\n\
Greatest Increase in Profits: {month_inc} (${great_inc})\n\
Greatest Decrease in Profits: {month_dec} (${great_dec})"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
