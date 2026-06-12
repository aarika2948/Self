#WAP to slice the word into half and only write the 2nd part
x=str(input("Enter a sentence or word="))
y=int(len(x))
z=int(y//2)
print(x[z:y])