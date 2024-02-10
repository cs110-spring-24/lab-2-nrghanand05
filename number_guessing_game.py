import random

    print("You got it!")
high = 100
user = 0 
count = 0
boop = False 
while boop == False: 
    user = input(f"Guess a number between {low} and {high}: ")
    user = int(user)
                
    if user > num:
            print("Too high")
            high = user
            count += 1
    elif user < num:
            print("Too low")
            low = user 
            count += 1
    else:
            print(f"You win! It took you {count +1} guesses to solve it!")
            user2= input("Play again?: ")
            count = 0
            low = 1
            high = 100
            if user2 == "yes": 
                    continue
            else: 
                    print("Goodbye!")
                    break