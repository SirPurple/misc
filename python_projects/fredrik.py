__author__ = 'egiafre'

#prisbasbelopp 2015 = 44500 SEK
#dvs. p� allt du tj�nar under 7,5 * 44500 (= 333750) f�r du �rsl�n * 0,05 i pension om du �r 25-35 �r och �rsl�n * 0,06 i #pension om du �r 36 �r eller �ldre

pbb = 44500 
#7,5* pbb = 333750
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

 
if yearly_salary < 7,5 * pbb:
    if age <= 35:
        pension = yearly_salary * 0,05
    else:
        pension = yearly_salary * 0,06
 
elif yearly_salary > 7,5 * pbb < 20 * pbb:
    if age <= 35:
        pension = yearly_salary * 0,05
 
    elif age > 35 and age < 46:
        pension = yearly_salary * 0,30
    elif age > 45 and age < 56:
        pension = yearly_salary * 0,33
    else:
        pension = yearly_salary * 0,35
else:
     
    if age <= 35:
        pension = yearly_salary * 0,05
 
    elif age > blabla:
        pension = yearly_salary * 0,06