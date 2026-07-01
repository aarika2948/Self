sum_even=0
sum_odd=0
n=int(input("Enter the number till which you want the addition="))
for i in range(1,n+1):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print("The sum of odd numbers is:", sum_odd)
print("The sum of even numbers is:", sum_even)