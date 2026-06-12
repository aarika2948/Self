#Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.
list_1=input("Enter integers seperated by space=")
list_2=input("Enter integers seperated by space=")
l_1=[int(num) for num in list_1.split()]
l_2=[int(numb) for numb in list_2.split()]
final=[]
for x in l_1:
    if (x%2==1):
        final.append(x)
for y in l_2:
    if (y%2==0):
        final.append(y)
print("The final list is ", final)
        
       
