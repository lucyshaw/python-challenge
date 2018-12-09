#import dependencies
import os
import csv

candidates = []
votes = []
vote_count_total = 0

#path to the data file
electionData_path = os.path.join('election_data.csv')

with open (electionData_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header row
    next(csvreader)
#loop through the data
    for row in csvreader:
        #count the total number of votes
        vote_count_total = vote_count_total + 1
        #candidates
        candidate = row[2]
        #add 1 to each candidates vote count for every time the name appears
        if candidate in candidates:
            candidate_list = candidates.index(candidate)
            votes[candidate_list] = votes[candidate_list] + 1
        else: #if new name, add them to the list of candidates and add 1 vote
            candidates.append(candidate)
            votes.append(1)

percentages = []
max_votes = votes[0]
max_index = 0

for count in range(len(candidates)):
    vote_percent = votes[count] / vote_count_total * 100
    percentages.append(vote_percent)
    if votes[count] > max_votes:
        max_votes = votes[count]
        print(max_votes)
        max_index = count
    winner = candidates[max_index]

print('Election Results')        
print(f'Total Votes: {vote_count_total}')
for count in range(len(candidates)):
    print(f'{candidates[count]}: {round(percentages[count], 2)}% ({votes[count]})')
print('-----------------------------------')
print(f'Winner: {winner}')

#write analysis to .txt file
#open text writer and name file
write_file = f'pypoll_summary.txt'
filewriter = open(write_file, mode='w')
#write the results
filewriter.write('Election Results\n')
filewriter.write(f'Total Votes: {vote_count_total}')
for count in range(len(candidates)):
    filewriter.write(f'{candidates[count]}: {round(percentages[count], 2)}% ({votes[count]})')
filewriter.write('-----------------------------------')
filewriter.write(f'Winner: {winner}')

#close file writer
filewriter.close()










