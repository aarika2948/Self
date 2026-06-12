#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
#Take input from user for two integers
x=int(input("Enter the first integer="))
y=int(input("Enter the second integer="))
if (x*y)<=1000:
    print("The results is", x*y)
else:
    print(f"The result is {x+y}")