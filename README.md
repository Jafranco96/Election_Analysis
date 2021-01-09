# Election Analysis

## Overview of Project

### Purpose

A Colorado Board of Elections employee, Tom, has been tasked with auditing the election results for a congressional precinct. His final deliverable is a vote count report which should certify the congressional race. The report should display the total votes count, the total vote amounts and percentages by county, the largest county turnout, the total vote amounts and percentages by candidate, and the overall winning candidate by the popular vote. While this analysis could be done in Excel, Tom would like to develop an automated process so the same analysis procedure can be applied to future senatorial districts and local elections. Accordingly, Python was used to develop the automated algorithm for the congressional precinct analysis and which can be refactored for future use as well.

## Election-Audit Results

With the Python algorithm completed, which takes the raw vote data as a .csv file and outputs the certification summary to a .txt file, the analysis for the congressional precinct results was able to be fully automated. The certification summary, comprised of each component described previously, was as follows:

•	Total votes cast: **369,711**

•	Breakdown of total votes count and percentage of total votes for each precinct county:

    o	Jefferson County: 38,855 votes cast (10.5% of total votes)
  
    o	Denver County: 306,055 votes cast (82.8% of total votes)
  
    o	Arapahoe County: 24,801 votes cast (6.7% of total votes)

•	Largest County Turnout: **Denver County**

•	Breakdown of total votes count and percentage of total votes by candidate:

    o	Charles Casper Stockham: 85,213 votes cast (23.0% of total votes)
    
    o	Diana DeGette: 272,892 votes cast (73.8% of total votes)
    
    o	Raymon Anthony Doane: 11,606 votes cast (3.1% of total votes)

•	Winning candidate with vote count and percentage of total votes: **Diana DeGette. 272,892 votes cast (73.8% of total votes)**

The formatted vote count report deliverable is below:


<img src = "https://github.com/Jafranco96/Election_Analysis/blob/main/analysis/election_analysis.PNG">


## Election-Audit Summary

As mentioned, one of the purposes of choosing Python for this analysis was the ability to refactor the algorithm for any future election. A key aspect of the algorithm is that the “scope” of the election does not substantially impact the structure of the code. Whether the algorithm is being performed on a national election or a local mayoral race, only small modifications need to be taken. For example, if turnout by state for a national election needs to be captured the modifications would be as follows.

First, create the tracking variables to capture and hold the state voter turnout information.

    winning_state = ""
    winning_state_count = 0
    winning_state_percentage =0
    state_options =[]
    state_votes = {}

Then, looping through the raw data, check if the state name appeared previously in the data. If it did not, add it to the list of state options and begin tracking its count. The index for the row[] function is assuming the State column is the fourth  column on the .csv file. The index can be changed accordingly based on the structure of the raw data.

    for row in reader:

        state_name = row[3]

        
        if state_name not in state_options:

            state_options.append(state_name)

            state_votes[state_name] = 0

        state_votes[state_name] += 1

Finally, retrieve the vote count and use conditional logic to determine the state with the greatest turnout.

    for state_name in state_votes:

        state_votes= state_votes.get(state_name)
            state_votes_percentage = float(state_votes)/float(total_votes) * 100
            state_results = (
                f"{state_name}: {state_votes_percentage:.1f}% ({state_votes:,})\n")
                
        if (state_votes > winning_state_count) and (state_votes_percentage > winning_state_percentage):
                winning_state_count = state_votes
                winning_state = state_name
                winning_state_percentage = state_votes_percentage

Another situation where the algorithm could be refactored are runoff elections. In elections with runoff rules, one candidate needs to get a minimum percentage of the votes to win. If no candidate reaches that designated percentage, the candidates with the top two vote percentages must face off in another election.  In these situations, to identify whether a runoff is needed, the algorithm would iterate through each candidate in the candidate dictionary and check whether their vote percentage meets that minimum threshold.  The algorithm could then print out to the terminal that a runoff is not needed or designate a runoff-needed Boolean as False. In the example below, it is assumed that the minimum vote percentage threshold is 50% and that a Boolean is needed.

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
            if vote_percentage => 50.00:
		        Runoff_Need = False
                
These are just two of the many examples that the election commission could refactor the algorithm for. The combination of the automation of the analysis and the flexibility of the algorithm to adapt to any future situations makes it clear why Python was the most suitable tool to use.
