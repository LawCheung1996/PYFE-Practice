# reads numbers until the user enters done
# once done is entered, print out the total, count and average of the numbers
# if user enters anything other than a number, detect mistake using try and except

sum = 0
count = 0
average = 0

while True:
    raw_imp = input('Input a number: ')
    if raw_imp == "done":
        break
    else:
        try:
            number = int(raw_imp)
            sum = sum + number
            count = count + 1
            average = sum / count
        except:
            print ("Invalid input")
        continue

print (sum, count, average)
