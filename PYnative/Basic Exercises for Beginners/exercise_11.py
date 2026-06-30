#Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
data=[int(x) for x in input("Enter a set pf data seperated by spaces=").split()]
final=list(set(data))
print("Final list", final)