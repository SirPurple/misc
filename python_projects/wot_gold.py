__author__ = 'Johan Bradvik'
# A small program for calculating gold and subscription prices

# Variable definitions

# Ask for input of gold and subscription days, verify that the inputs are in the correct format.
while True:
    try:
        gold = int(input('Amount of gold purchased: '))
        gold = int(gold)
    except ValueError:
        print ("That is not a valid number!")

    try:
        days = int(input('Number of days purchased: '))
        days = int(days)
    except ValueError:
        print ("That is not a valid number!")

    try:
        cost = float(input('Cost of purchase: '))
        cost = float(cost)
    except ValueError:
        print ("That is not a valid number!")

    break

print ("You purchased", (gold), "gold and", (days), "days for", (cost), "kr.");


# Calculate cost
price = (gold/cost);
print ("The rate is", round(price, 1), "gold per krona");

'''
# Calculate cost
def gold_per_cash(gold, cost):



def age_category(age):
    if age <= 35:
        interval = 'A'
        return interval
    elif age >= 36 and age <= 45:
        interval = 'B'
        return interval
    elif age >= 46 and age <= 55:
        interval = 'C'
        return interval
    else:
        interval = 'D'
        return interval
'''