#Write a program to find how many times a subtring appears in a given string.
sen=input("Enter the sentence=").lower()
word=input("Enter the word whose frequency you want to find out=").lower()
count=sen.count(word)
print(f"The number of times {word} has been repeated is {count}.")

