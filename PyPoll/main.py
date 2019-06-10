import os
import csv
import statistics
import operator
from collections import Counter

# get file path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
text_file_path = os.path.join('..', 'Resources', 'election_data_summary.txt')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csv_header)

    total_votes = 0
    candidates_list = []

    for row in csvreader:
        total_votes += 1
        candidates_list.append(row[2])
        

candidates_list_set = set(candidates_list)
candidates_count = Counter(candidates_list)

percent_votes_dict = {}
for i in candidates_count.elements():
    percent_votes = '{:.3%}'.format(candidates_count[i] / total_votes)
    percent_votes_dict[i] = percent_votes

winner_candidate = max(percent_votes_dict.items(), key=operator.itemgetter(1))[0]

print("Election Results", 
        "-------------------------------",
        "Total Votes: {}".format(total_votes), 
         "-------------------------------", sep='\n')

for key, value in percent_votes_dict.items() :
    print("{} : {} ({})".format(key, value, candidates_count[key]), sep='\n')

print( "-------------------------------",
        "Winner : {}".format(winner_candidate), sep='\n')


with open(text_file_path, 'w') as textfile:
    print("Election Results", 
        "-------------------------------",
        "Total Votes: {}".format(total_votes), 
         "-------------------------------", sep='\n', file = textfile)

    for key, value in percent_votes_dict.items() :
        print("{} : {} ({})".format(key, value, candidates_count[key]), sep='\n', file = textfile)

    print( "-------------------------------",
            "Winner : {}".format(winner_candidate), sep='\n', file = textfile)
