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

# Open the election results and read the file.
with open(file_to_load) as election_data:

   # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)