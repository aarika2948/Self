#Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.
import sys
l_1=input("Enter a list of 5 words=")
l_2=l_1.split()
count=0
for y in l_2:
    count+=1
if count!=5:
    print("Invalid Input")
    sys.exit()
for x in l_2:
    letter=0
    for i in x:
        letter+=1
    print(f"{x}-{letter}")
