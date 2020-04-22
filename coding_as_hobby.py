import csv
from collections import defaultdict,Counter
with open('C:\\Users\\patel\\OneDrive\\Desktop\\data\\survey_results_public.csv',encoding='utf-8')as f:
    total=0
    csv_reader=csv.DictReader(f)
    counts={
        'Yes':0,
        'No':0
    }
    #--multiple ways to implement using Dictionary--#
    #counts=defaultdict(int)
    for line in csv_reader:
        counts[line['Hobbyist']]+=1
        total+=1 
                
print('-----Coding as a Hobby-----')
yes_pct=(counts['Yes']/total)*100
yes_pct=round(yes_pct,2)
no_pct=(counts['No']/total)*100
no_pct=round(no_pct,2)
print(f"Yes:{yes_pct}%")
print(f"No:{no_pct}%")
