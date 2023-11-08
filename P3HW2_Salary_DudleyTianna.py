# CTI-110
   # P3HW2 - Salary
   # Tianna Dudley
   # 11/07/2023
   #

# Pseudocode :

'''
name = input ask Enter employee's name
hours = input ask Enter worked hours
payrate = input ask Enter pay rate

set overtime pay = 0.0
set over_time = 0.0

if hours greater than 40
do the evaluation of the overtime pay and regular pay
over_time = hours_worked - 40
ot_payRate = pay_rate + (pay_rate * 0.5)
overTime_pay = over_time * ot_payRate
reg_pay = 40 * pay_rate

else
do the evaluation of the regular pay
reg_pay = hours_worked * pay_rate

And then calculate the gross pay = regular pay + overtime pay

print output
'''

ename = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

ename = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

overTime_pay = 0.0
over_time = 0.0
if hours_worked > 40:
overt_time = hours_worked - 40
ot_payRate = pay_rate + (pay_rate * 0.5)
overTime_pay = over_time * ot_payRate
reg_pay = 40 * pay_rate
else:
reg_pay = hours_worked * pay_rate

gross_pay = reg_pay + overTime_pay

print("-"*36)
print("Employee name: ",ename)
print()
print("Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay")
print("-"*90)
print(hours_worked," \t\t ",pay_rate," \t",over_time," \t\t ",overTime_pay," \t",reg_pay," \t ",gross_pay)


