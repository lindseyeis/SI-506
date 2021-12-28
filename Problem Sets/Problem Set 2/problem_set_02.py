# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1 (10 points)
print('\nProblem 1')

gme_prices = [15.84, 35.50, 65.01, 325.00, 63.77]

price_max = max(gme_prices) #TODO: Replace
print(price_max)

price_max_index = gme_prices.index(price_max) #TODO: Replace
print(price_max_index)

#TODO: Problem 1.3

gme_prices.append(52.40)
print(gme_prices)

#TODO: Problem 1.4

gme_prices[0] = 17.69
print(gme_prices)

# PROBLEM 2 (10 points)
print('\nProblem 2')

amc_prices = [33.47, 34.41, 40.84, 44.02, 50.16] #TODO: Replace
print(amc_prices)

amc_prices_latest = amc_prices[4] #TODO: Replace
print(amc_prices_latest)

amc_prices_last_three = amc_prices[2:] #TODO: Replace
print(amc_prices_last_three)

# PROBLEM 3 (10 points)
print('\nProblem 3')

pltr_prices = ' 21.82-24.90-24.01-25.71-26.64-26.28 '

pltr_prices_list = pltr_prices.strip().split("-") #TODO: Replace
print(pltr_prices_list)

# PROBLEM 4 (20 points)
print('\nProblem 4')

dates = ['September 10th', 'September 3rd', 'August 27th', 'August 20th', 'August 13th', 'August 6th']
dates.reverse()
print(dates)

dates_str = '|'.join(dates)
print(dates_str)

# PROBLEM 5 (20 points)
print('\nProblem 5')

max_price = max(pltr_prices_list)
max_price_index = pltr_prices_list.index(max_price)
amc_max_price = max(amc_prices)
amc_max_price_index = amc_prices.index(amc_max_price)
pltr_highest = f'In the week ending on {dates[max_price_index]}, Palantir closed with a price of ${pltr_prices_list[max_price_index]} and AMC closed with a price of ${amc_prices[max_price_index-1]}.'
amc_highest = f'In the week ending on {dates[amc_max_price_index+1]}, Palantir closed with a price of ${pltr_prices_list[amc_max_price_index+1]} and AMC closed with a price of ${amc_prices[amc_max_price_index]}.'

#Uncomment once you've defined pltr_highest
print(pltr_highest)

#Uncomment once you've defined amc_highest
print(amc_highest)

# PROBLEM 6 (20 points)
print('\nProblem 6')
dates_reversed = dates[::-1]
print(dates_reversed)

# PROBLEM 7 (10 points)
print('\nProblem 7')
every_other_date = dates_reversed[::2]
print(every_other_date)