print("******CALULATOR PROJECT USING PYTHON******") 
print() # For Empty Line

value_1 = float(input("Enter value 1: "))
operation = input("Pick any operation from the given['+', '-', '/', '*']: ")
value_2 = float(input("Enter value 2: "))
print()

if operation == "+":
    result = value_1 + value_2
    print(f"The sum of {value_1} and {value_2} is {result}")
elif operation == "-":
    result = value_1 - value_2
    print(f"The subtraction of {value_1} and {value_2} is {result}")
elif operation == "*":
    result = value_1 * value_2
    print(f"The multiplication of {value_1} and {value_2} is {result}")
elif operation == "/":
    try:
       result = value_1 / value_2
       print(f"The division of {value_1} and {value_2} is {result}")
    except ZeroDivisionError:
       print("cannot division by zero")   
else:
    print("Please enter valid operation")

