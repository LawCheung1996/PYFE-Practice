#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error message.
#If the score is between 0.0 and 1.0, print a grade using the following table:

try:
    score = input('Enter score between 0.0 and 1.0: ')
    if score >= 0 and score <= 1.0:
        if score >= 0.9:
            result = A
            print (result)
        elif score >= 0.8:
            result = B
            print (result)
        elif score >= 0.7:
            result = C
            print (result)
        elif score >= 0.6:
            result = D
            print (result)
        else:
            result = F
            print (result)
except:
    print ('Bad score')
