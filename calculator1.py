def add_numbers(a,b):
    return a+b
def subtract_numbers(a,b):
    if(a>b):
        return a-b
    else:
        return b-a
def multiply_numbers(a,b):
    return a*b
def divide_numbers(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Division by zero is not allowed as the result will be infinity")
def modulus_numbers(a,b):
    try:
        return a%b
    except ZeroDivisionError:
        print("Modulus by zero is not possible")
def square_numbers(a,b):
    try:
        return a**b
    except ZeroDivisionError:
        print("Squaring the number by zero gives you 1 ")
        print(1)

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

result1=add_numbers(num1,num2)
result2=subtract_numbers(num1,num2)
result3=multiply_numbers(num1,num2)
result4=divide_numbers(num1,num2)
result5=modulus_numbers(num1,num2)
result6=square_numbers(num1,num2)

print(f"The sum of two numbers is: {result1}")
print(f"The difference between the two numbers is: {result2}")
print(f"The multiplication of the two numbers is: {result3}")
print(f"The Quotient of a and b is: {result4}")
print(f"The mod between a and b is: {result5}")
print(f"The square of a to the power of b is: {result6}")