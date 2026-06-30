import random
name=(input("Enter your name="))
print(f"Hi {name}! This is a Rock, Paper, Scissor Game. \n You can type in rock, paper or scissor. \n Your score will be displayed after each round. \n You will be playing against a robot. \n This game is the best of five")
print("Let's begin!")
list=["rock","paper","scissor"]
scorer=0
scoreh=0
round=1
for i in range(5):
    human=input(str("Enter your move=")).lower()
    robot=random.choice(list)
    if (robot=="rock")&(human=="scissor"):
        print("You lost!")
        scorer+=1
        print(f"The robot's score is {scorer}")
        print(f"Your score is {scoreh}")
    elif (robot=="rock")&(human=="paper"):
        print("You won!")
        scoreh+=1
        print(f"The robot's score is {scorer}")
        print(f"Your score is {scoreh}")
    elif (robot=="paper")&(human=="rock"):
        print("You lost!")
        scorer+=1
        print(f"The robot's score is {scorer}")
        print(f"Your score is {scoreh}")
    elif (robot=="paper")&(human=="scissor"):
        print("You won!")
        scoreh+=1
        print(f"The robot's score is {scorer}")
        print(f"Your score is {scoreh}")
    elif (robot=="scissor")&(human=="rock"):
        print("You won!")
        scoreh+=1
        print(f"The robot's score is {scorer}")
        print(f"Your score is {scoreh}")
    elif (robot=="scissor")&(human=="paper"):
        print("You lost!")
        scorer+=1
        print(f"The robot's score is {scorer}")
        print(f"Your score is {scoreh}")
    elif (robot==human):
        print("It's a tie!")
        print(f"The robot's score is {scorer}")
        print(f"Your score is {scoreh}")
    else:
        print("Invalid Input")
    round+=1
    print(f"Round {round}")

print(f"Your final score is {scoreh}")
print(f"The robot's final score is {scorer}")
if(scoreh>scorer):
    diff=(scoreh-scorer)
    print(f"Hurray {name}! You won by {diff} points.")
elif(scorer==scoreh):
    print(f"Ohkkk {name}! Its a tie.")
else:
    diff=(scorer-scoreh)
    print(f"Oh no {name}! You lost by {diff} points.")




