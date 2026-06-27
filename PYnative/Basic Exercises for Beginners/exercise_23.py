#Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).
n=int(input("Enter the number="))
string=str(n)
if len(string)!=3:
    print("Invalid Input")
temp=n
digit_1=temp%10
temp=temp//10
digit_2=temp//10
if (digit_1==digit_2):
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is a not palindrome number.")
#or
n=int(input("Enter the number="))
string=str(n)
rev=string[::-1]
if (string==rev):
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is a not palindrome number.")

  

