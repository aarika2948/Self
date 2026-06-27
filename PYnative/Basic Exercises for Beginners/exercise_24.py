 #Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
terms=int(input("Enter the number of terms="))
l=[0,1]
sum=1
for i in range(terms+1):
    digit=l[i]
    sum=sum+digit
    l.append(sum)
print(*l)

