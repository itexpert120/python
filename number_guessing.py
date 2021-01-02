import random

lower = int(input("Enter Lower Bound:- "))
upper = int(input("Enter Upper Bound:- "))

x = random.randint(lower, upper)
count = 0
while True:
    count += 1

    guess = int(input("\nEnter Your Guess:- "))
    if x == guess:
        print(f"\nCongratulations! You Did it in {count} tries")
        break
    elif x < guess:
        print("Your Guess is too High")
    elif x > guess:
        print("Your Guess is too Low")