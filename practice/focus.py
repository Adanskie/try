import time
import sys

storage_acc = []
storage_pass = []
while True:
    create_acc = input("Create Account : ")
    create_pass = input("Create Password : ")

    time.sleep(1)
    print("Loading",end="")
    time.sleep(1)
    print(end=".")
    time.sleep(1)
    print(end=".")
    time.sleep(1)
    print(end=".")
    time.sleep(1)
    print()
    print("----------------------")
    print("Success Create Account")
    print("----------------------")

    user = input("Do you wanna create more Account Choice (Yes or No) : ")

    if user.upper() == "YES":
        print("==(CREATE MORE ACCOUNT)==")
        continue
    elif user.upper() == "NO":
        print("-----------------")
        print("Stop Creating Acc")
        print("-----------------")
        break
    else:
        print()
        sys.exit("Invalid Choices")

storage_acc.append(create_acc)
storage_pass.append(create_pass)

account = input("Enter Account : ")
password = input("Enter Password : ")

for i in range(len(storage_acc)):
    if account == storage_acc[i] and password == storage_pass[i]:
        time.sleep(1)
        print("Loading", end="")
        time.sleep(1)
        print(end=".")
        time.sleep(1)
        print(end=".")
        time.sleep(1)
        print(end=".")
        break
else:
    print("Loading", end="")
    time.sleep(1)
    print(end=".")
    time.sleep(1)
    print(end=".")
    time.sleep(1)
    print(end=".")
    sys.exit("Invalid Password or Account")
print()
print("Success You are Log-in now")
print("--------------------")
print(f"WELCOME, {account}")
print("--------------------")

balance = 10000
deposit = 0
withdraw = 0

while True:
    print("----------------")
    print("==ATM MACHINE==")
    print("----------------")
    print("[1] Check Balance")
    print("[2] Deposit")
    print("[3] Withdraw")
    print("[4] EXIT")
    choice = input("Choice Operator : ")

    if choice == "1" :
        print(f"Your Balance is ${balance}")
    elif choice == "2" :
        deposit = int(input("Enter Your Deposit Amount : "))

        if deposit >= 1000 :
            balance += deposit
            print("Loading", end="")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            print(f"Success Deposit ${deposit}")
        else :
            print("Loading", end="")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            print("Invalid Money Please Try Again")
    elif choice == "3" :
        withdraw = int(input("Enter Your Withdrawal Amount : "))

        if withdraw >= 1000 :
            balance -= withdraw
            print("Loading", end="")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            print(f"Success Withdrawal ${withdraw}")
        else :
            print("Loading", end="")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            time.sleep(1)
            print(end=".")
            print("Invalid Money Please Try Again")
    elif choice == "4" :
        sys.exit("THANK YOU FOR COMING")
    else :
        print("Invalid Choices Please Try Again")
