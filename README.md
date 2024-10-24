# Module 3: python-challenge

## The Task
Write a pair of Python scripts to evaluate data from two real-world situations: business finance and election tabulation.
### PyBank
The banking script should determine the duration (in months) of the dataset, the net total of Profits/Losses, the average change in Profits/Losses between months, the period of greatest increase in profits, and the period of greatest decrease in profits. This analysis should then be exported to a text file.
### PyPoll
The election script should count the total number of votes, list the candidates and the total votes they received. Then, the script should calculate the percentage of total votes each candidate received, and determine the winner. This analysis should then be exported to a separate text file.

## User Story
```md
AS A business analyst
I WANT to be able to summarize profits and losses over time
SO THAT I can easily convey to others the company's financial trends.
```
```md
AS A polling analyst
I WANT to be able to quickly tabulate the votes for each candidate and determine the winner
SO THAT I can help modernize a small, rural town's vote-counting process.
```

## Acceptance Criteria
```md
CORRECTLY READS IN THE CSV
  * Reads in the CSVs for both PyBank and PyPoll using Python
  * Successfully stores the header row

RESULTS PRINTED OUT TO TERMINAL CORRECTLY
  * Results correctly display for PyBank:
    * Total Months
    * Total
    * Average Change
    * Greatest Increase
    * Greatest Decrease
  * Results correctly display for PyPoll:
    * Total Votes
    * Each candidate’s total votes and percent of votes
    * Winner

CODE RUNS ERROR FREE
  * Error free
  * Producing consistent results

EXPORTS RESULTS TO TEXT FILE
  * The text file contains for PyBank:
    * Total Months
    * Total
    * Average Change
    * Greatest Increase
    * Greatest Decrease
  * The text file contains for Pypoll:
    * Total Votes
    * Each candidate’s total votes and percent of votes
    * Winner

CODE IS CLEANED AND COMMENTED
  * Has additional tests and debugging removed
  * Commented
```

## Examples of Use
### PyBank
The financial records dataset we are given has only dates and profits/losses in a CSV file. Information is a bit difficult to parse in this format:
![An image of a CSV file containing unedited financial records.](./Resources\PyBank-dataset.png)

Our script analyzes this data and exports it as a text file. This format is significantly easier for everyone at the company to understand:
![The output file of summarized profits and losses.](./Resources\PyBank-summary.png)
### PyPoll
The polling data contains hundred of thousands of votes. Tabulating votes manually would take significant amount of human work hours:
![An image of a CSV file containing all the votes of a small town election.](./Resources\PyPoll-dataset.png)

Our script quickly counts the votes for each candidate, displays the total number of votes, the percentage earned by each candidate, and the winner. It does all of this in a matter of seconds:
![The output file of summarized election data.](./Resources\PyPoll-summary.png)

## License
This project is licensed under the GNU General Public License v3.0.  
License Link:
https://www.gnu.org/licenses/gpl-3.0.en.html   
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)