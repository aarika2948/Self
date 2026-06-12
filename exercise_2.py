#Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
previous_num=0
for i in range(10):
    x_num=(previous_num+i)
    print(f"The previous number is {previous_num} and the sum is {x_num}")
    previous_num=i