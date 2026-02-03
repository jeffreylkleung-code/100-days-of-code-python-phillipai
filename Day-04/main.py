import random

UserInput = 3
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors")

RandomChoice = random.randint(0,2)

while(UserInput < 0 or UserInput > 2):
    UserInput = int(input("0/1/2:"))
    if (UserInput < 0 or UserInput > 2):
        print("Please enter a number between 0 and 2")
    
if (UserInput == 0):
    UserChoice = "Rock"
elif (UserInput == 1):
    UserChoice = "Paper"
elif (UserInput == 2):
    UserChoice = "Scissors"
    
if (RandomChoice == 0):
    ComputerChoice = "Rock"
elif (RandomChoice == 1):
    ComputerChoice = "Paper"
elif (RandomChoice == 2):
    ComputerChoice = "Scissors"

print("You chose:", UserChoice)
print("The computer chose:", ComputerChoice)

if (UserInput == RandomChoice):
    print("Its a draw!")
    quit()
    
if (UserInput == 0):
    if (RandomChoice == 1):
        print("You lose!")
    elif (RandomChoice == 2):
        print("You Win!")
    
if (UserInput == 1):
    if (RandomChoice == 2):
        print("You lose!")
    elif (RandomChoice == 0):
        print("You Win!")
        
if (UserInput == 2):
    if (RandomChoice == 0):
        print("You lose!")
    elif (RandomChoice == 1):
        print("You Win!")
        
        

