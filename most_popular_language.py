import csv
from collections import defaultdict, Counter

with open(
    "C:\\Users\\patel\\OneDrive\\Desktop\\data\\survey_results_public.csv",
    encoding="utf-8",
) as f:
    total = 0
    csv_reader = csv.DictReader(f)
    language_counter = Counter()
    for line in csv_reader:
        languages = line["LanguageWorkedWith"].split(";")
        language_counter.update(languages)
        total += 1
print("-----Most Popular Technologies-----")
for language, value in language_counter.most_common(5):
    language_pct = (value / total) * 100
    language_pct = round(language_pct, 2)
    print(f"{language}:{language_pct}%")
