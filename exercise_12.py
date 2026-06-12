#Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
input_1=input("Enter the items of the list seperated by space:")
list_1= input_1.split()
a=list_1[0]
b=list_1[-1]
if (a==b):
    print("True")
else:
    print("False")