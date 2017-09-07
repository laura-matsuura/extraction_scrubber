import csv
import sys
import pdb

input_file = sys.argv[1]
scrape_results = open('./'+input_file, 'r', encoding="latin-1")
unique_comments = []


scrape_results_reader = csv.reader(scrape_results)

for row in scrape_results_reader:
    area_insights = row[3].split("|")
    for comment in area_insights:
        if comment not in unique_comments and comment != "": 
            unique_comments.append(comment)

for comment in unique_comments:
    print(comment)    
    # print('\n')
    # print('-------------------------------')



print('*************************************************')
print('Number of Unique Comments:')
print(len(unique_comments))


