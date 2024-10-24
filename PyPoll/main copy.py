# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
current_cand = ""

# Define lists and dictionaries to track candidate names and vote counts
cand_dict = {
   "total": total_votes,
   "candidates": {
      
   }
}
# {"candidate":"","votes":0}

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
      #total_votes = total_votes + 1
      cand_dict["total"] = cand_dict["total"] + 1

        # Get the candidate's name from the row
      current_cand = row[2]

        # If the candidate is not already in the candidate list, add them
      if current_cand not in cand_dict["candidates"].keys():
         #cand_dict["Name"] = current_cand
         #cand_dict["Votes"] = 1
         cand_dict["candidates"][current_cand] = 0
         #cand_list.append(cand_dict)
         #print(cand_list[cand_dict[0]["Name"]])

        # Add a vote to the candidate's count
      cand_dict["candidates"][current_cand] = cand_dict["candidates"][current_cand] + 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
  print(
f"\n\
Election Results\n\
-------------------------\n\
Total Votes: {cand_dict["total"]}"
  )

  print(f"Dictionary: {cand_dict}")
  #print(f"List: {cand_list}")
    # Write the total vote count to the text file

    # Loop through the candidates to determine vote percentages and identify the winner
  for i in cand_dict["candidates"].keys():
     # print(f"Look here: {cand_dict}")
     #print(f"Candidates: {cand_dict["candidates"][i]}")
     print(i)
     # cand_dict["percent"] = f"{'{:.3%}'.format(cand_dict["candidates"][i] / cand_dict["total"])}"
     cand_dict["percent"] = {i:f"{'{:.3%}'.format(cand_dict["candidates"][i] / cand_dict["total"])}"}
     #percent_votes = cand_dict[i] / total_votes
     #cand_dict[f"Percent{percent_votes}"] = percent_votes
     #perc_dict = {"Total": cand_dict[i], "Percent": percent_votes}
  print(f"Final Dictionary: {cand_dict}")
        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
