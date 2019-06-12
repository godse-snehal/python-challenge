import os
import csv
import statistics 

# get file path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
text_file_path = os.path.join('..', 'Resources', 'budget_data_summary.txt')

with open(csvpath) as csvfile:

    # read csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    number_of_months = 0
    total_amount = 0
    amount_list = []
    date_list = []
    
    # iterate through the file
    for row in csvreader:
        number_of_months += 1
        date_list.append(row[0])
        amount_list.append(row[1])
        amount_list_to_int = list(map(int, amount_list))
        
        
    total_amount = sum(amount_list_to_int)
    
    amount_diff_list = [j-i for i, j in zip(amount_list_to_int[:-1], amount_list_to_int[1:])]
    average = '%.2f' % statistics.mean(amount_diff_list)
    
    greatest_increase = max(amount_list_to_int)
    greatest_increase_index = amount_list_to_int.index(greatest_increase)
    greatest_increase_date = date_list[greatest_increase_index]

    greatest_decrease = min(amount_list_to_int)
    greatest_decrease_index = amount_list_to_int.index(greatest_decrease)
    greatest_decrease_date = date_list[greatest_decrease_index]


with open(text_file_path, 'w') as textfile:
    print("Financial Analysis", 
        "-------------------------------",
        "Total Months: {}".format(number_of_months),
        "Total: ${}".format(total_amount),
        "Average  Change: ${}".format(average),
        "Greatest Increase in Profits: {} ({})".format(greatest_increase_date, greatest_increase),
        "Greatest Decrease in Profits: {} ({})".format(greatest_decrease_date, greatest_decrease), sep='\n', file = textfile)

print("Financial Analysis", 
        "-------------------------------",
        "Total Months: {}".format(number_of_months),
        "Total: ${}".format(total_amount),
        "Average  Change: ${}".format(average),
        "Greatest Increase in Profits: {} ({})".format(greatest_increase_date, greatest_increase),
        "Greatest Decrease in Profits: {} ({})".format(greatest_decrease_date, greatest_decrease), sep='\n')

