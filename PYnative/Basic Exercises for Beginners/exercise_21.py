#Print a downward half-pyramid pattern using stars (*)
rows=int(input("Enter the number of rown you want=")) #5
number=rows
for i in range(1,rows+1): #(1,6)
    for j in range(number,1,-1):
        print("*", end=" ")
    number-=1
    print()
