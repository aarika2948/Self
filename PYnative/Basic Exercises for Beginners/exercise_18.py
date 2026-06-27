#Write a program to extract each digit from an integer in the reverse order.
num=int(input("Enter an integer="))
final=[]
while num > 0:
    d=num%10
    final.append(d)
    num=num//10
print(*final)
