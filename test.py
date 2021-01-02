def main():
    pass_gen()
    while True:
        imput = input("Wanna try again? (y/N) => ") or "n"
        if "y" in imput.lower():
            pass_gen()
        else:
            break

def pass_gen():
    import random
    import string
    length = int(input("How long do you want the password to be? => ") or 0)
    punctuation = "!@#$%^&*()"
    symbols = string.ascii_letters + string.digits + punctuation
    random = random.choices(symbols, k=length)
    if length == 0:
        print("Wrong Input. Program Terminated")
        exit()
    else:
        print("Your New Password is:", ''.join(random))
        print("")

main()
print("Thanks for using this Script")
