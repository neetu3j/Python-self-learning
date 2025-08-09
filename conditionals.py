day_of_week = input("Enter the day of the week: ").lower()
print(day_of_week)


if day_of_week == "saturday" or day_of_week == "sunday":
    print("I will learn Python on")
else:
    print("I will not learn Python on")


num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

choice = input("Enter the choice + / - / * / / %: ")

if choice == "+":
    sum = num_1 + num_2
    print("Sum of two numbers is",sum)
elif choice == "-":
    diff = num_1 - num_2
    print("Difference of two numbers is",diff)
elif choice == "*":
    product = num_1 * num_2
    print("Product of two numbers is",product)
elif choice == "/":
    quotient = num_1 / num_2
    print("Quotient of two numbers is",quotient)
elif choice == "%":
    remainder = num_1 % num_2
    print("Remainder of two numbers is",remainder)
else:
    print("Invalid choice")
