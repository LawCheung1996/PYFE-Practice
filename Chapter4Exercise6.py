# Pay with functions


def computepay(rate,hours):
    if hours > 40:
        extra_hours = hours-40
    else:
        extra_hours=0
    extra_pay = 0.5 * extra_hours * float(rate)
    pay = (hours * rate) + extra_pay
    print ('Pay ' + str(pay))

print ('Enter Hours')
hours = float(input())

print ('Enter Rate')
rate = float(input())

computepay(hours,rate)
