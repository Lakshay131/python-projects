def entry():
    print("*****WELCOME TO THE ATM*****")
    print("1. New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. SHOW BALANCE")

def new_account():
    global name, age, pin
    name = input("ENTER YOUR NAME: ")
    age = int(input("ENTER YOUR AGE: "))
    if age >= 18:
        pin = int(input("ENTER YOUR PIN OF 4 DIGIT: "))
        print("YOUR ACCOUNT HAS BEEN CREATED.")
    else:
        print("YOUR AGE IS BELOW 18, SO YOU CANT CREATE A ACCOUNT.")

def deposit_():
    global check_name, check_pin, deposit, balance
    check_name = input("ENTER YOUR USERNAME: ")
    check_pin = int(input("ENTER YOUR PIN: "))
    if check_name == name:
        if check_pin == pin:
            deposit = int(input("ENTER HOW MUCH AMOUNT YOU WANT TO DEPOSIT: "))
            balance = balance + deposit
            print("MONEY DEPOSITED SUCCECFULLY")
        else:
            print("!!INCORRECT PIN!!")
    else:
        print("!!INCORRECT USERNAME!!")

def withdraw():
    global check_name, check_pin, withdraw, balance
    check_name = input("ENTER YOUR USERNAME: ")
    check_pin = int(input("ENTER YOUR PIN: "))
    if check_name == name:
        if check_pin == pin:
            withdraw = int(input("ENTER HOW MUCH AMOUNT YOU WANT TO WITHDRAW: "))
            balance = balance - withdraw
            print("MONEY WITHDRAW SUCCECFULLY")
        else:
            print("!!INCORRECT PIN!!")
    else:
        print("!!INCORRECT USERNAME!!")

def show_balance():
     global check_name, check_pin, withdraw, balance
     check_name = input("ENTER YOUR USERNAME: ")
     check_pin = int(input("ENTER YOUR PIN: "))
     if check_name == name:
         if check_pin == pin:
           print(balance)
         else:
            print("!!INCORRECT PIN!!")
     else:
        print("!!INCORRECT USERNAME!!")


choice = 0

deposit = 0

balance = 0

name = ""

age = 0



def main():
    entry()
    while True:
     
      choice = int(input("WHAT WOULD YOU LIKE TO DO: "))

      if choice == 1:
         new_account()
         ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
         if ask == "yes":
               continue
         else:
             quit()
      elif choice == 2:
         deposit_()
         ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
         if ask == "yes":
               continue
         else:
             quit()
      elif choice == 3:
         withdraw()
         ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
         if ask == "yes":
               continue
         else:
             quit()
      elif choice == 4:
         show_balance()
         ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
         if ask == "yes":
               continue
         else:
             quit()
      else:
         print("!!ERROR!!")

main()