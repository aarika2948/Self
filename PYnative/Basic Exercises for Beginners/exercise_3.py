#Display only those characters which are present at an even index number in given string.
#Take input from the user for the string
x=str(input("Enter your desired sentence or word="))
even=(x[0::2])
for eve in even:
    print(eve)