#Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
list=["apple","banana","pear","litchi","mango"]
print("Here is the list of fruits already present:\n", list)
fruit=str(input("Enter the name of a fruit="))
list.append(fruit)
print("The new list is:\n", list)
list.pop(1)
print("The final list is: \n", list)
