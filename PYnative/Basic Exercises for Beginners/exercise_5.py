#Write a program to swap the values of two variables, a and b, without using a third temporary variable.
#Ask the user for the variable values
a=float(input("Enter the value of 1st variable="))
b=float(input("Enter the value of 3nd variable="))
a, b=b, a
print(f"The new value of a is {a}")
print(f"The new value of b is {b}")
