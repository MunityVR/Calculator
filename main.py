import math

# Setting up storage for numbers.

a = float(input("Enter a number : "))
o = str(input("Enter an operator : "))
b = float(input("Enter a number : "))

# Calculating exponent: if needed or not.

aa = str(input("Do you want an exponent? Y/N : "))
if aa == 'y' or aa == 'Y':
    ab = float(input("What is your exponent for the first number? : "))
elif aa == 'n' or aa == 'N':
    ab = 1
else:
    print("Invalid Variable!")

# Calculating exponent: if needed or not.

ba = str(input("Do you want an exponent? Y/N : "))
if ba == 'y' or ba == 'Y':
    bb = float(input("What is your exponent for the second number? : "))
elif ba == 'n' or aa == 'N':
    bb = 1
else:
    print("Invalid Variable!")

# Fixing errors with if statement
if aa == not 'y' or aa == not 'Y' and aa == not 'n' or aa == not 'N':
    print("Please make sure you use the following variables: y, n or Y, N | Invalid Variable(s)")
    ab = 1
    
if ba == not 'y' or ba == not 'Y' and ba == not 'n' or ba == not 'N':
    print("Please make sure you use the following variables: y, n or Y, N | Invalid Variable(s)")
    bb = 1
    
ac = math.pow(a, ab)
bc = math.pow(b, bb)

# Actual calculation and printing out the answer.

if aa == 'y' or aa == 'Y' and ba == 'y' or ba == 'Y':
    if o == '+':
        print(ac + bc)
    elif o == '-':
        print(ac - bc)
    elif o == '*' or o == 'x':
        print(ac * bc)
    elif o == '/' or o == '÷':
        print(ac / bc)
    else:
        print("Invalid Operator!")
elif aa == 'y' or aa == 'Y' and ba == 'n' or ba == 'N':
    if o == '+':
        print(ac + b)
    elif o == '-':
        print(ac - b)
    elif o == '*' or o == 'x':
        print(ac * b)
    elif o == '/' or o == '÷':
        print(ac / b)
    else:
        print("Invalid Operator!")
elif aa == 'n' or aa == 'N' and ba == 'y' or ba == 'Y':
    if o == '+':
        print(a + bc)
    elif o == '-':
        print(a - bc)
    elif o == '*' or o == 'x':
        print(a * bc)
    elif o == '/' or o == '÷':
        print(a / bc)
    else:
        print("Invalid Operator!")
elif aa == 'n' or aa == 'N' and ba == 'n' or ba == 'N':
    if o == '+':
        print(a + b)
    elif o == '-':
        print(a - b)
    elif o == '*' or o == 'x':
        print(a * b)

    elif o == '/' or o == '÷':
        print(a / b)
    else:
        print("Invalid Operator!")
else:
    print("Please make sure you use the following variables: y, n or Y, N | Invalid Variable(s)")


