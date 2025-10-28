def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Undefined (division by zero)"


def modulus_numbers(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Undefined (modulus by zero)"


def power_numbers(a, b):
    return a ** b


def calculator():
    print("===== Simple Python Calculator =====")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")

    choice = input("\nEnter choice (1/2/3/4/5/6): ")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if choice == "1":
        result = add_numbers(a, b)
        print(f"Result: {a} + {b} = {result}")

    elif choice == "2":
        result = subtract_numbers(a, b)
        print(f"Result: {a} - {b} = {result}")

    elif choice == "3":
        result = multiply_numbers(a, b)
        print(f"Result: {a} × {b} = {result}")

    elif choice == "4":
        result = divide_numbers(a, b)
        print(f"Result: {a} ÷ {b} = {result}")

    elif choice == "5":
        result = modulus_numbers(a, b)
        print(f"Result: {a} % {b} = {result}")

    elif choice == "6":
        result = power_numbers(a, b)
        print(f"Result: {a}^{b} = {result}")

    else:
        print("Invalid choice! Please select a valid operation.")

    print("=====================================")


if __name__ == "__main__":
    calculator()
