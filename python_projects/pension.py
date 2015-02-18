__author__ = 'ejonbrk'

try:
    age = int(raw_input('Enter your age: '))
except ValueError:
    print "That is not a valid number!"
print age

try:
    salary = int(raw_input('Enter your salary: '))
except ValueError:
    print "That is not a valid number!"
print salary

pbb = 44500           # Prisbasbelopp
low_range_multiplier = 0
mid_range_multiplier = 0
top_range_multiplier = 0

age_interval = ''

# Define the age category of the person
def age_category(age):
    if (age <= 35):
        age_interval = 'A'
        return age_interval
    elif (age >= 36 and age <= 45):
        age_interval = 'B'
        return age_interval
    elif (age >= 46 and age <= 55):
        age_interval = 'C'
        return age_interval
    else:
        age_interval = 'D'
        return age_interval

print "This is your age category:", age_category(age)


# Define the multipliers to use depending on the age interval
def procentsats(age_interval):
    if age_interval (A):
        low_range_multiplier = 0.05
        return low_range_multiplier
        mid_range_multiplier = 0.24
        return mid_range_multiplier
        top_range_multiplier = 0.12
        return top_range_multiplier

    if age_interval (B):
        low_range_multiplier = 0.06
        return low_range_multiplier
        mid_range_multiplier = 0.30
        return mid_range_multiplier
        top_range_multiplier = 0.16
        return top_range_multiplier

    if age_interval (C):
        low_range_multiplier = 0.06
        return low_range_multiplier
        mid_range_multiplier = 0.33
        return mid_range_multiplier
        top_range_multiplier = 0.18
        return top_range_multiplier

    if age_interval (D):
        low_range_multiplier = 0.06
        return low_range_multiplier
        mid_range_multiplier = 0.35
        return mid_range_multiplier
        top_range_multiplier = 0.19
        return top_range_multiplier



#def pension_calculator(salary):
 #   if salary > (pbb*7.5)