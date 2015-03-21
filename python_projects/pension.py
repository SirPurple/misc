__author__ = 'ejonbrk'

# Variable definitions
age = 0
salary = 0
pbb = 44500           # Prisbasbelopp
low_range_multiplier = 0
mid_range_multiplier = 0
top_range_multiplier = 0

# Ask for input of age
try:
    age = int(raw_input('Enter your age: '))
except ValueError:
    print "That is not a valid number!"
print age

# Ask for input of salary
try:
    salary = int(raw_input('Enter your salary: '))
except ValueError:
    print "That is not a valid number!"
print salary

# Define the age category of the person
def age_category(age):
    if (age <= 35):
        age_cat = 'A'
        return age_cat
    elif (age >= 36 and age <= 45):
        age_cat = 'B'
        return age_cat
    elif (age >= 46 and age <= 55):
        age_cat = 'C'
        return age_cat
    else:
        age_cat = 'D'
        return age_cat

age_interval = age_category(age)
print age_interval
#print "This is your age category:", age_category(age)


# Define the multipliers to use depending on the age interval
def percentage_rate(age_interval):
    if (age_interval == 'A'):
        low_range_multiplier = 0.05
        mid_range_multiplier = 0.24
        top_range_multiplier = 0.12
        return low_range_multiplier, mid_range_multiplier, top_range_multiplier
    elif (age_interval == 'B'):
        low_range_multiplier = 0.06
        mid_range_multiplier = 0.30
        top_range_multiplier = 0.16
        return low_range_multiplier, mid_range_multiplier, top_range_multiplier
    elif (age_interval == 'C'):
        low_range_multiplier = 0.06
        mid_range_multiplier = 0.33
        top_range_multiplier = 0.18
        return low_range_multiplier, mid_range_multiplier, top_range_multiplier
    elif (age_interval == 'D'):
        low_range_multiplier = 0.06
        mid_range_multiplier = 0.35
        top_range_multiplier = 0.19
        return low_range_multiplier, mid_range_multiplier, top_range_multiplier

#def pension_calculator(salary):
 #   if salary > (pbb*7.5)