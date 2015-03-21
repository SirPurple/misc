__author__ = 'egiafre'

pbb = 44500
#7.5* pbb = 333750
#20 * pbb = 890000
#30 * pbb = 1335000


# Ask for input of age
try:
    age = int(raw_input('Enter your age: '))
except ValueError:
    print "That is not a valid number!"
#print age

# Ask for input of yearly salary
try:
    yearly_salary = int(raw_input('Enter your yearly yearly_salary: '))
except ValueError:
    print "That is not a valid number!"
#print yearly_salary

 
if yearly_salary < 7.5 * pbb:
    if age <= 35:
        pension = yearly_salary * 0.05
    else:
        pension = yearly_salary * 0.06
 
elif yearly_salary > 7.5 * pbb < 20 * pbb:
    if age <= 35:
        pension = yearly_salary * 0.05
 
    elif age > 35 and age < 46:
        pension = yearly_salary * 0.30
    elif age > 45 and age < 56:
        pension = yearly_salary * 0.33
    else:
        pension = yearly_salary * 0.35
else:
     
    if age <= 35:
        pension = yearly_salary * 0.05
 
    elif age > blabla:
        pension = yearly_salary * 0.06

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