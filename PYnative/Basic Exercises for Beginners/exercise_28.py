#Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.
import sys
l=[int(x) for x in input("Enter the values seperated by spaces=").split()]
count=0
for a in l:
    count+=1
if count!=10:
    print("Invalid Input") 
    sys.exit()   
even=[]
odd=[]
for b in l:
    if b%2==0:
        even.append(b)
    else:
        odd.append(b)
print(f"Even numbers:{even}")
print(f"Odd numbers:{odd}")
