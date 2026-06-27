#Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.
base=int(input("Enter the no. whose power you want to know="))
exp=int(input(f"Enter the no. you want to raise {base} to="))
product=1
for i in range(1,exp+1):
    product=(product*base)
print(f"The value of {base} raise to the power {exp} is {product}")


