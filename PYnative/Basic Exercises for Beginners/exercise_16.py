# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
num=int(input("Enter a number="))
numb=str(num)
numbe=numb[::-1]
if (numb==numbe):
    print(f"The number {numb} is a palyndrome.")
else:
    print(f"The number {numb} isn't a palyndrome.")