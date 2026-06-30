# Take two lists and find the elements that appear in both. Use Sets to perform the operation.
l_1=[int(x) for x in input("Enter the values seperated by spaces=").split()]
l_2=[int(y) for y in input("Enter the values seperated by spaces=").split()]
final=[]
s_1=set(l_1)
s_2=set(l_2)
for i in s_1:
    if i in s_2 and i not in final:
        final.append(i)
print("Common:"*final)
#or
l_1=[int(x) for x in input("Enter the values seperated by spaces=").split()]
l_2=[int(y) for y in input("Enter the values seperated by spaces=").split()]
s_1=set(l_1)
s_2=set(l_2)
common = s_1 & s_2
print(f"Common Elements: {common}")


    
