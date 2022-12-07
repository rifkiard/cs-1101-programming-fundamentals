def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def getNumber():
    number = input("Input a negative or positive number:\n")
    formattedNumber = int(number)

    if(formattedNumber >= 0):
        countdown(formattedNumber)
    else:
        countup(formattedNumber)

getNumber()