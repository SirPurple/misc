__author__ = 'ejonbrk'

# Variable definitions
age = 0
salary = 0
pbb = 44500           # Prisbasbelopp
#lower_limit = (pbb * 7,5)
#higher_limit = (pbb * 20)

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


# Define the multipliers to be used for the different age intervals
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

multipliers = percentage_rate(age_interval)
print 'These are the multipliers that will be used when doing the calculations:', multipliers


def pension_calculator(salary):
    # Lönen lägre än 7,5 pbb
    if salary <= (pbb*7.5):
        if age_interval == 'A':
            pension = (salary * 0.05)
            return pension
        elif age_interval == 'B' or age_interval == 'C' or age_interval == 'D':
            pension = (salary * 0.06)
            return pension
    # Lönen högre än 7,5 pbb men lägre än 20 pbb
    elif (salary > (pbb * 7.5)) and (salary <= (pbb * 20)):
        if age_interval == 'A':
            sub_pbb_part = (salary - (pbb * 7.5))
            pension = sub_pbb_part + 
            pension = (salary - ) (salary * 0.24)
            return pension
        if age_interval == 'B':
            pension = (salary * 0.30)
            return pension
        if age_interval == 'C':
            pension = (salary * 0.33)
            return pension
        if age_interval == 'D':
            pension = (salary * 0.35)
            return pension
    # Lönen högre än 20 pp
    elif salary > (pbb*20):
        if age_interval == 'A':
            pension = (salary * 0.12)
            return pension
        if age_interval == 'B':
            pension = (salary * 0.16)
            return pension
        if age_interval == 'C':
            pension = (salary * 0.18)
            return pension
        if age_interval == 'D':
            pension = (salary * 0.19)
            return pension

# Let user know how poor he/she will be, rounded to two digits
yearly_pension = pension_calculator(salary)
monthly_pension = (yearly_pension / 12)
print ''
print 'Yearly pension will be', round(yearly_pension,2), 'SEK'
print 'Monthly pension will be', round(monthly_pension,2), 'SEK'