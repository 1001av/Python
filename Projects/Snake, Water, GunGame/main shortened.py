import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1, 0, 1])  # this will chose random no's
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

#  The below logic is written on the basis of the value of computer - you
else:   
    if((computer - you) == -1 or  (computer - you) == 2 ):
        print("You lose!")
    else:
        print("You win!") 