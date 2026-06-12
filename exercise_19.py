#Calculate income tax for a given income based on these rules:
money=int(input("Enter the value of money="))
if (money <= 10000):
    print(f"Your final tax is 0")
elif money in range(10000, 20000):
    money_1=(money-10000)
    money_2=(money_1+((money_1*10)/100))
    final_1=(money_2+10000)
    print(f"The final tax is {final_1 - money}")
else:
    money_3=(money-20001)
    money_4=(money_3+((money_3*20)/100))
    money_5=(10000+((10000*10)/100))
    final_2=(money_4 + money_5 + 10000)
    print(f"The final tax is {final_2 - money}")



