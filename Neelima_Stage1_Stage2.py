num1= float(input ("Please enter your first number:"))
num2= float(input (" please enter your second number:"))
operator= input (" Which operator you wnat to use on these number:")

if operator == '+':
    result= num1 + num2
elif operator == '-':
    result= num1 - num2
elif operator == '*':
    result= num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result= num1 / num2
else:
    print ("Invalid operator")

print("The result is:", result)

if result > 0:
    print("The result is positive.")    
elif result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is zero.")