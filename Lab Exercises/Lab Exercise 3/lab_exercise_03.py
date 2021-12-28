# Lab Exercise 03
print('Lab Exercise 03 \n')

# Setup
companies = [
    "Domino's, Ann Arbor, 14400, Food",
    "Fisher Investments, Camas, 3500, financial",
    "M&T Bank, Buffalo, 16840, Financial",
    "Dimensional Insight, Burlington, 102, Tech",
    "Bloomingdale's, New York, 6500, Retail",
    "Meijer, Grand Rapids, 70000, Retail",
    "CIL Management Consultants, Chicago, 189, Consulting"
]

# Problem 01 (3 points)


locations = []
for company in companies:
    company = company.split(', ')
    if len(company) > 1:
        locations.append(company[1])
print(f"\n1. locations = {locations}")

# Problem 02 (4 points)

financial_co = []

for company in companies:
    company = company.split(', ')
    if company[3].lower() == 'financial':
        financial_co.append(company[0])
print(f"\n2. financial_co = {financial_co}")

# Problem 03 (4 points)

count = 0
for retail in companies:
    if retail.lower().endswith('retail'):
        count += 1
print(f"\n3. There are in total of {count} companies in the retail industry")

# PROBLEM 4 (4 Points)
small_companies = [] # less than 500
medium_companies = [] # all the rest
large_companies = [] # larger or equal to 5000


for company in companies:
    company = company.split(', ')
    size = int(company[2])
    if size < 500:
        small_companies.append(company[0])
    elif size >= 5000:
        large_companies.append(company[0])
    else:
        medium_companies.append(company[0])

print(small_companies)
print(medium_companies)
print(large_companies)
# PROBLEM 5 (4 Points)
largest_company = ''
num = 0
for largest in companies:
    largest = largest.split (', ')
    if int(largest[-2]) > num:
        num = int(largest[-2])
        largest_company = largest[0]
print(largest_company)
# END LAB EXERCISE
