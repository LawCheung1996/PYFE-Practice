# Exercise 2: Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:

try:
    print ('Enter hours')
    hours = float(input())
except:
    print ('Error, please enter a numeric input')
    hours = float(input())

try:
    print ('Enter rate')
    rate = float(input())
except:
    print ('Error, please enter a numeric input')
    rate = float(input())

if hours > 40:
    extra_hours = hours-40

else:
    extra_hours=0

extra_pay = 0.5 * extra_hours * float(rate)

pay = (hours * rate) + extra_pay

print ('Pay: ' + str(pay))
