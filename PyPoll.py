# the data we need to retrieve:
#total number of votes cast
# a complete list of candidates that received votes
# percentage of votes each candidate won
#total number of votes each candidate won
#populat vote winner


# import csv
# import os

# file_to_load = os.path.join("Resources", "election_results.csv")

# with open(file_to_load) as election_data:

     # To do: perform analysis.
    # print(election_data)

# file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()
# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson")



# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidates_options =[]
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidates_options:
            # Add it to the list of candidates.
            candidates_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
# Print the candidate list.
print(candidates_options)
print(candidate_votes)


# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
     # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
     # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
     # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

         
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)