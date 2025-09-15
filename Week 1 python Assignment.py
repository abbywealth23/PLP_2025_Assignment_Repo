# A simple Calculator that ask users for input of two figures and an operator.
# # ask user to enter the figures and the operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = (input("Enter the operator (-, +, x, /): "))

#calculations 
if operator == "+":
        add = num1 + num2   #if the user enters the + operation, this line performs the addition arithmetic
        print(f"{num1} + {num2} = {add}")
        print("Done!")
elif operator == "-":
        subtract = num1 - num2  #if the user enters the - operation, this line performs the subtraction arithmetic
        print(f"{num1} - {num2} = {subtract}")
        print("Done")
elif operator == "/":
        if num2 != 0:
            division = num1 / num2  #if the user enters the / operation, this line performs the Division arithmetic
            print(f"{num1} / {num2} = {division}")   
            print("Done")
        else:
            print("sorry, you can't divide by 0")
elif operator == "*":
        multiply = num1 * num2  #if the user enters the * operation, this line performs the multiplication arithmetic
        print(f"{num1} * {num2} = {multiply}")
        print("Done")
else: print("Oops! Wrong Operator")