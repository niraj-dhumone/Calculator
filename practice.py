value_1 = float(input("Enter value 1:  "))

operation = input("use the operation in this['+', '-', '/', '*']")

value_2 = float(input("Enter value 2:  "))


if operation == "+":
    result = value_1 + value_2
    print(f"The sum of {value_1} and {value_2} is {result}")

elif operation == "-":
    result = value_1 - value_2
    print(f"The substraction of {value_1} and {value_2} is {result}")

elif operation == "*":
    result = value_1 * value_2
    print(f"The multipy of {value_1} and {value_2} is {result}") 

     
elif operation == "/":
    result = value_1 / value_2
    print(f"The divide of {value_1} and {value_2} is {result}") 

else:
    print("My name is niraj")
    
