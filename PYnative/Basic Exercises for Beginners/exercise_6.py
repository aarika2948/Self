#Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
fact=1
num=int(input("Enter a value whose factorial you want to find out="))
for i in range(1,num+1):
    fact*=i
print(fact)