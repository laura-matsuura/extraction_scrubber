
import re
import csv
import sys
import codecs
import pdb;


input_file = sys.argv[1]
scrape_results = open('./'+input_file,'r',encoding="latin-1")


scrape_results_reader = csv.reader(scrape_results)



csv_out = open('clean.csv','w')
clean_data = csv.writer(csv_out)
clean_data.writerow(['URL', 'Tour_Insights','Count', 'Area_Insights','Count','Duplicate'])


for row in scrape_results_reader:
    url = row[0]
    comment = row[1]
    area_comment = row[2]
    comment = re.findall(r'note:(.*?),lastModified', comment)
    area_comment = re.findall(r'(?<=<div class=story data-reactid=...>).*?(?=<\/div>)',area_comment)
    duplicate = 'No'
    comment_count = len(comment)
    area_comment_count = len(area_comment)

    if comment == []:
        comment = None
    else:
        comment = ' | '.join(comment)
    
    if area_comment == []:
        area_comment = None
    else:
        area_comment = '|'.join(area_comment)


    clean_data.writerow([url, comment,comment_count,area_comment,area_comment_count])


scrape_results.close()
csv_out.close()
