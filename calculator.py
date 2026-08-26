# a=23
# b=35
# result = a + b
# print(result)

# a=657
# b=344
# result = a - b
# print(result)

# a=44
# b=22
# result = a / b
# print(result)

# a=6
# b=2
# result = a * b 
# print(result)

# value_1 = float(input("Enter value 1: "))
# value_2 = float(input("Enter value 2: "))

# opration = input("Pick any opration from the given['+', '-', '/', '*']")

# name = "raju"
# age = 18
# print(f"I am {name} i am {age} is year old")

# a = int(input("Enter your age: "))

# if (a>=18):
#     print("You are above the age")

# elif (a<0):
#     print("You are entering an invalid negative age")

# elif (a==0):
#      print("You are entering 0 which is not valid age")

# else:
#     print("You are below the age")

# print("End of program")    

# a = 76
# b = 24
# result =a+b
# print(f"The sum is:{a+b}")

# if(a+b>0):
#     print("The number is valid")
      
# a = 24
# b = 24
# print(a==b)      


# opration = input("Pick any opration from the given['+', '-', '/', '*']")

# a = 398
# b = 233
# print(f"If {a} is an even number then {b} is an odd number")

value_1 = float(input("Enter value 1: "))
value_2 = float(input("Enter value 2: "))

operation = input("Pick any operation from the given['+', '-', '/', '*']: ")

if operation == "+":
    result = value_1 + value_2
    print(f"The sum of {value_1} and {value_2} is {result}")
elif operation == "-":
    result = value_1 - value_2
    print(f"The subs of {value_1} and {value_2} is {result}")
elif operation == "*":
    result = value_1 * value_2
    print(f"The mul of {value_1} and {value_2} is {result}")
elif operation == "/":
    try:
       result = value_1 / value_2
       print(f"The div of {value_1} and {value_2} is {result}")
    
    except ZeroDivisionError:
       print("cannot division by zero")
    
else:
    print("Please enter valid opeaition")


# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")

# except IndexError:
#     print("Index Error")

# try:
#     value_1 = float(input("Enter value 1: "))
#     operation = input("Pick any operation from the given['+', '-', '/', '*']: ")
#     value_2 = float(input("Enter value 2: ")) 

# except ValueError:
#     print("Error: enter a valid integer")
# finally:
#     print("hello")

# value_1 = float(input("Enter value 1: "))
# operation = input("Pick any operation from the given['+', '-', '/', '*']: ")
# value_2 = float(input("Enter value 2: ")) 

# try:
#     result = value_1 / value_2
#     print(f"The div of {value_1} and {value_2} is {result}")
    
# except ValueError:
#     print("The solution is correct")