__author__ = 'ejonbrk'

# Variable definitions
age = 0
monthly_salary = 0
pbb = 44500                     # Prisbasbelopp value set for 2015
pbb_low_limit = (pbb * 7.5)
pbb_hi_limit = (pbb * 20)


# Ask for input of age, verify that the input is an integer
while True:
    try:
        age = int(raw_input('Enter your age: '))
        age = int(age)
        break
    except ValueError:
        print "That is not a valid number!"
    #print age

# Ask for input of yearly salary, verify that the input is an integer
while True:
    try:
        monthly_salary = int(raw_input('Enter your monthly salary: '))
        monthly_salary = int(monthly_salary)
        break
    except ValueError:
        print "That is not a valid number!"
    #print monthly_salary

yearly_salary = (monthly_salary * 12)

# Define what age interval/category the person belongs in
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

age_interval = age_category(age)
#print age_interval

# Calculate pension based on yearly salary and age
def pension_calculator(yearly_salary, age_interval):
    # yearly_salary lower than 7.5 * pbb
    if yearly_salary <= pbb_low_limit:
        if age_interval == 'A':
            pension = (yearly_salary * 0.05)
            return pension
        elif age_interval == 'B' or age_interval == 'C' or age_interval == 'D':
            pension = (yearly_salary * 0.06)
            return pension
    # yearly_salary higher than 7.5 * pbb but lower than 20 * pbb
    elif yearly_salary > pbb_low_limit and yearly_salary <= pbb_hi_limit:
        if age_interval == 'A':
            pension = (pbb_low_limit * 0.05) + ((yearly_salary - pbb_low_limit) * 0.24)
            return pension
        elif age_interval == 'B':
            pension = (pbb_low_limit * 0.06) + ((yearly_salary - pbb_low_limit) * 0.30)
            return pension
        elif age_interval == 'C':
            pension = (pbb_low_limit * 0.06) + ((yearly_salary - pbb_low_limit) * 0.33)
            return pension
        elif age_interval == 'D':
            pension = (pbb_low_limit * 0.06) + ((yearly_salary - pbb_low_limit) * 0.35)
            return pension
    # yearly_salary upper than 20 * pbb
    elif yearly_salary > pbb_hi_limit:
        if age_interval == 'A':
            pension = (pbb_low_limit * 0.05) + ((pbb_hi_limit - pbb_low_limit) * 0.24) + \
                      ((yearly_salary - pbb_hi_limit) * 0.12)
            return pension
        elif age_interval == 'B':
            pension = (pbb_low_limit * 0.05) + ((pbb_hi_limit - pbb_low_limit) * 0.24) + \
                      ((yearly_salary - pbb_hi_limit) * 0.16)
            return pension
        elif age_interval == 'C':
            pension = (pbb_low_limit * 0.05) + ((pbb_hi_limit - pbb_low_limit) * 0.24) + \
                      ((yearly_salary - pbb_hi_limit) * 0.18)
            return pension
        elif age_interval == 'D':
            pension = (pbb_low_limit * 0.05) + ((pbb_hi_limit - pbb_low_limit) * 0.24) + \
                      ((yearly_salary - pbb_hi_limit) * 0.19)
            return pension

# Let the user know how poor he/she will be, pension rounded to integer
yearly_pension = pension_calculator(yearly_salary, age_interval)
monthly_pension = (yearly_pension / 12)

print ''
print "Age:", age, "years"
print "Montly salary:", monthly_salary, "SEK", "- which equals", yearly_salary, "SEK per year."
print 'Monthly pension', round(monthly_pension, 0), 'SEK', "- which equals", round(yearly_pension, 0), 'SEK per year.'