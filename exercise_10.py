#Take the input of a list of integers, find and print both the largest and the smallest numbers.
list=input("Enter the items of the list=")
nums=[int(x) for x in list.split()]
highest=max(nums)
lowest=min(nums)
print(f"The lowest value is {lowest}")
print(f"The highest value is {highest}")
