#Iterate through a given list of numbers and print only those numbers which are divisible by 5.
list_1=input("Enter integers=")
num_list=[int(num) for num in list_1.split()]
int_list=[]
for numb in num_list:
    if (numb%5==0):
        int_list.append(numb)
print(f"The divisible numbers are:{int_list}")

