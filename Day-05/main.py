import random

Password = []

print("Welcome to password generator!")
LettersUserInput = int(input("How many letters would you like in your password?"))
SymbolsUserInput = int(input("How many symbols would you like in your password?"))
NumbersUserInput = int(input("How many numbers would you like in your password?"))

def Random_Letters():
    RandomN = chr(random.randint(65,122))
    Password.append(RandomN)

def Random_Symbols():
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    RandomN = random.randint(0,8)
    Password.append(symbols[RandomN])

def Random_Numbers():
    RandomN = random.randint(0,9)
    Password.append(str(RandomN))


LettersCount = LettersUserInput
SymbolsCount = SymbolsUserInput
NumbersCount = NumbersUserInput

def Random_Charcters():
    
    
    global LettersCount
    global SymbolsCount
    global NumbersCount
    
    
    while LettersCount > 0 or SymbolsCount > 0 or NumbersCount > 0:
        Rand_Num = random.randint(1,3)
        if Rand_Num == 1 and LettersCount > 0:
            Random_Letters()
            LettersCount -=1
            break
        if Rand_Num == 2 and SymbolsCount > 0:
            Random_Symbols()
            SymbolsCount -=1
            break
        if Rand_Num == 3 and NumbersCount > 0:
            Random_Numbers()
            NumbersCount -=1
            break



for i in range(LettersUserInput+SymbolsUserInput+NumbersUserInput):
    Random_Charcters()
    
print("".join(Password))

if len(Password) <= 6:
    print("Your password is weak, try to include at least 8 characters for a stronger password.")
elif len(Password) == 7:
    print("Your password is medium, try to include at least 8 characters for a stronger password.")
else:
    print("Your password is strong.")