import random
import sys
import time

n=int(input("Enter the no. of players="))
i=1
while i>0:
    for j in range(1, n+1):
        print(f"Player {j}:")
        print(random.randint(1,7))
        time.sleep(4)
    e=input("Type exit if you want to leave=")
    if e==exit:
        sys.exit()
