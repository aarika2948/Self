# Print the following pattern where each row contains a number repeated a specific number of times based on its value.
rows=int(input("Enter the number of rows you want="))
for i in range(1, rows+1):#1,7
    for j in range(1, i+1):
        print(i, end=" ")
    print()