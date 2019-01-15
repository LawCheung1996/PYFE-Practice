# reads numbers until the user enters done
# once done is entered, print out min and maximum
# if user enters anything other than a number, detect mistake using try and except

sum = 0
count = 0
minimum = None
maximum = None

while True:
    raw_imp = input('Input a number: ')
    if raw_imp == "done":
        break
    number = float(raw_imp)
    if maximum is None and minimum is None:
        maximum = None
        minimum = None
    elif number < minimum:
        minimum = number
    elif number > maximum:
        maximum = number
    count = count + 1
    sum = sum + number

sum = str(sum)
count = str(count)
minimum = str(minimum)
maximum = str(maximum)

print ('sum ' + sum)
print ('count ' + count)
print ('minimum ' + minimum)
print ('maximum ' + maximum)
