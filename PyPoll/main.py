# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
current_cand = "" # Selecting candidate for vote counting
win_calc = "" # Comparison for winning percentage
summary = "" # Text to write summary

# Define lists and dictionaries to track candidate names and vote counts
cand_dict = {
  "total": 0, # Tracks total votes
  "votes": {}, # Tracks votes for each candidate
  "percent": {} # Tracks percentage of votes
}

# Winning Candidate and Winning Count Tracker
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
      print(". ", end="")

        # Increment the total vote count for each row
      cand_dict["total"] = cand_dict["total"] + 1

        # Get the candidate's name from the row
      current_cand = row[2]

        # If the candidate is not already in the candidate list, add them
      if current_cand not in cand_dict["votes"].keys():
         cand_dict["votes"][current_cand] = 0

        # Add a vote to the candidate's count
      cand_dict["votes"][current_cand] = cand_dict["votes"][current_cand] + 1

# Prepare winning candidate summary for export to the text file
# Write the total vote count to the summary
summary = f"""Election Results\n\
-------------------------\n\
Total Votes: {cand_dict["total"]}\n\
-------------------------\n"""

# Loop through the candidates to determine vote percentages and identify the winner
for i in cand_dict["votes"].keys():
  cand_dict["percent"][i] = f"{'{:.3%}'.format(cand_dict['votes'][i] / cand_dict['total'])}"

  # Update the winning candidate if this one has more votes
  if cand_dict["percent"][i] > win_calc:
    win_calc = cand_dict["percent"][i]
    winner = i

  # Save each candidate's vote count and percentage
  summary = summary + (f"{i}: {cand_dict["percent"][i]} ({cand_dict['votes'][i]})\n")

# Save the winning candidate to the summary
summary = summary + (f"-------------------------\nWinner: {winner}\n-------------------------")

# Print the summary (to terminal)
print(summary)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
  txt_file.write(summary)