print("Wlecome to treasure island.")
print("Your mission is to find the treasure")
print("Left or right?")
UserInput = input(str("Type Right/Left: ")).lower()

print(UserInput)
if (UserInput == "right"):
    print("Sonic got the treasure before you, try again.")
elif (UserInput == "left"):
    print("Nice, you made it to the next level!")
    print("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.")
    UserInput = input(str("Type Swim/Wait: ")).lower()

    if (UserInput == "swim"):
        print("Unfortunately, you were eaten by a Great White Shark, try again.")
    elif (UserInput == "wait"):
        print("Nice, you made it to the next level, you're pretty good at this!")
        print("Now that you've made it to Treasure Island, you can dig or search the cave.")
        UserInput = input(str("Type Dig/Cave: ")).lower()
        if (UserInput == "dig"):
            print("You've found the treasure, you win!")
        elif (UserInput == "cave"):
            print("You were eaten by a bear, game over.")


