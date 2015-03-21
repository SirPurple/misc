__author__ = 'ejonbrk'

# Variable definitions
age = 0
yearly_salary = 0
pbb = 44500           # Prisbasbelopp
pbb_lower_limit = (pbb * 7,5)
pbb_higher_limit = (pbb * 20)


# Ask for input of age
try:
    age = int(raw_input('Enter your age: '))
except ValueError:
    print "That is not a valid number!"
#print age

# Ask for input of yearly salary
try:
    yearly_salary = int(raw_input('Enter your yearly salary: '))
except ValueError:
    print "That is not a valid number!"
#print yearly_salary

# Define what age interval/category the person belongs in
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
#print age_interval

def pension_calculator(yearly_salary, age_interval):
    # yearly_salary lower than 7.5 * pbb
    if yearly_salary <= pbb_lower_limit:
        if age_interval == 'A':
            pension = (yearly_salary * 0.05)
            return pension
        elif age_interval == 'B' or age_interval == 'C' or age_interval == 'D':
            pension = (yearly_salary * 0.06)
            return pension
    # yearly_salary higher than 7.5 * pbb but lower than 20 * pbb
    elif yearly_salary > pbb_lower_limit and yearly_salary <= pbb_higher_limit:
        if age_interval == 'A':
            pension = (pbb_lower_limit * 0.05) + ((yearly_salary - pbb_lower_limit) * 0.24)
            return pension
        elif age_interval == 'B':
            pension = (pbb_lower_limit * 0.05) + ((yearly_salary - pbb_lower_limit) * 0.30)
            return pension
        elif age_interval == 'C':
            pension = (pbb_lower_limit * 0.05) + ((yearly_salary - pbb_lower_limit) * 0.33)
            return pension
        elif age_interval == 'D':
            pension = (pbb_lower_limit * 0.05) + ((yearly_salary - pbb_lower_limit) * 0.35)
            return pension
    # yearly_salary upper than 20 * pbb             # !!!! TO BE DONE !!!!!
    elif yearly_salary > pbb_higher_limit:
        if age_interval == 'A':
            pension = (yearly_salary * 0.12)
            return pension
        elif age_interval == 'B':
            pension = (yearly_salary * 0.16)
            return pension
        elif age_interval == 'C':
            pension = (yearly_salary * 0.18)
            return pension
        elif age_interval == 'D':
            pension = (yearly_salary * 0.19)
            return pension

# Let user know how poor he/she will be, monthly pension rounded
yearly_pension = pension_calculator(yearly_salary, age_interval)
monthly_pension = (yearly_pension / 12)
monthly_salary = (yearly_salary / 12)

print ''
print "Age:", age, "(equals age category",age_interval,")"
print "Yearly salary:", yearly_salary, "SEK"
print "Montly salary:", monthly_salary, "SEK"
print 'Yearly pension', (yearly_pension), 'SEK'
print 'Monthly pension', round(monthly_pension, 2), 'SEK'


'''
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
'''