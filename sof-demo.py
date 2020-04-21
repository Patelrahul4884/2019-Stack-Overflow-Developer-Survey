import csv
from collections import defaultdict,Counter
with open('data/survey_results_public.csv',encoding='utf-8')as f:
    total=0
    csv_reader=csv.DictReader(f)
    counts={
        'Yes':0,
        'No':0
    }
    #--multiple ways to implement using Dictionary--#
    #counts=defaultdict(int)
    language_counter=Counter()
    for line in csv_reader:
        languages=line['LanguageWorkedWith'].split(';')
        language_counter.update(languages)
        total+=1
        counts[line['Hobbyist']]+=1    
print('-----Most Popular Technologies-----')
for language,value in language_counter.most_common(5):
    language_pct=(value/total)*100
    language_pct=round(language_pct,2)
    print(f"{language}:{language_pct}%")
                
print('-----Coding as a Hobby-----')
yes_pct=(counts['Yes']/total)*100
yes_pct=round(yes_pct,2)
no_pct=(counts['No']/total)*100
no_pct=round(no_pct,2)
print(f"Yes:{yes_pct}%")
print(f"No:{no_pct}%")
