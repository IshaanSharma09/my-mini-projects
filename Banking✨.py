Name = ""
Key = ""
def Account():
    global Name, Key
    Name = input("Enter a Username 👤 for your account : ")
    Key = input("Enter a password 🗝️ : ")
    while len(Name)< 1 or len(Key) < 1:
        print("Please enter valid information!")
        Name = input("Enter a Username 👤 for your account : ")
        Key = input("Enter a password 🗝️ for your account : ")


def User():
    name = input("Enter your Username 👤 : ")
    if name != Name:
        print("No account found with the given name")
        print("Please create one now!!")
        print()
        Account()
    else: 
        key = input("Enter a password 🗝️ : ")
        while key != Key:
            print("Invalid Password")
            key = input("Enter a password 🗝️ : ")


def Balance():
    print(f"Your balance is ₹{balance:.2f}")
    print()

def Deposit():
    global balance
    amount = int(input("Enter amount to deposit : ₹"))
    if amount > 0:
        balance += amount
        print("Amount is succesfully added")
        print(f"Your updated balance is ₹{balance:.2f}")
        print()
    else: 
        print("Amount should be greater than 0")
        print()

def Withdraw():
    global balance
    amount = int(input("Enter amount to withdraw : ₹"))
    while amount <=0:
        print("Please enter a valid amount")
        amount = int(input("Enter amount to withdraw : ₹"))
    if balance > amount:
        balance -= amount
        print("Amount is succesfully withdrawn")
        print(f"Your updated balance is ₹{balance:.2f}")
        print()

    else: 
        print("Invalid Balance!!")
        print()


def Transfer():
    global balance
    amount = int(input("Enter amount to transfer : ₹"))
    while amount <=0:
        print("Please enter a valid amount")
        amount = int(input("Enter amount to withdraw : ₹"))
    if balance > amount:
        balance -= amount
        print("Amount is succesfully tranfered")
        print(f"Your updated balance is ₹{balance:.2f}")
        print()

    else: 
        print("Invalid Balance!!")
        print()

balance = 0
isrunning = True

while isrunning:
    print("******************************************************")
    print("                🔒  NO Bank🏦                        ")
    print("******************************************************")
    print("[1] Create Account🆔")
    print("[2] Login🔐")
    print("[3] Exit")
    user = input("What you want to do Sir/Madam 👤 (Please choose from 1-3): ")
    if user == "3":
        isrunning = False
    elif user == "2":
        User()
        while True:
            print("******************************************************")
            print("                 🔓 NO Bank🏦                        ")
            print("******************************************************")
            print(f"Greetings {Name}")
            print("[1] Check Balance💰")
            print("[2] Deposit Money 🪙")
            print("[3] Withdraw Money 💵")
            print("[4] Transfer Money 📲")
            print("[5] Exit to Home Screen")
            member = input("What you want to do Sir/Madam 👤 (Please choose from 1-5): ")
            if member == "5":
                print("Thank You for visiting📈!!")  
                break
            elif member == "1":
                Balance()
            elif member == "2":
                Deposit()
            elif member == "3":
                Withdraw()
            elif member == "4":
                Transfer()
            else: 
                print("Please choose a valid option")
                print()
                

    elif user == "1":
        Account()
        print("Now you can login 🔐")
        print()
    else: 
        print ("Please choose a valid option : ")
        print()
print("Have a great day📈!!")  