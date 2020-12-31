answer = input("Do you wanna hear a joke? ")
if "y" in answer.lower():
    print("")
    affirmation = input("Really?")
    if "y" in affirmation.lower():
        print("very funny lol")

    else:
        print("sad")
else:
    print("f off")