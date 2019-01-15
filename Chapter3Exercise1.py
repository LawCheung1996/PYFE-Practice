# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

print ('Enter Hours')
hours = float(input())

print ('Enter Rate')
rate = float(input())

if hours > 40:
    extra_hours = hours-40

else:
    extra_hours=0

extra_pay = 0.5 * extra_hours * float(rate)

pay = (hours * rate) + extra_pay

print ('Pay: ' + str(pay))
