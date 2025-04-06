def entry():
    print("------WELCOME TO OUR HOTEL------")
    print("1.Enter Customer Data")
    print("2.Calculate rommrent")
    print("3.Calculate restaurant bill")
    print("4.Calculate laundry bill")
    print("5.Show total cost")
    print("6.EXIT")
    

def customer_data():
     global name, stay
     name = input("ENTER CUSTOMER NAME: ")
     stay = int(input("ENTER HOW MANY DAYS CUSTOMER WANT: "))
     rooms()
     rrent()

def rooms():
    global rchoice, days
    print("We have the following rooms for you:- ")
    print("1.  type A---->rs 6000 PN- ")
    print("2.  type B---->rs 5000 PN-")
    print("3.  type C---->rs 4000 PN-")
    print("4.  type D---->rs 3000 PN-")
    rchoice = int(input('WHICH ROOM YOU WANT --- '))
    days = int(input('HOW MANY DAYS DO YOU WANT: '))

def cafe():
     global restaurant_bill
     print("-----WELCOME TO OUR CAFE-----")
     print("1. TEA : ₹20")
     print("2. COFFEE : ₹30")
     print("3. SANDWICH : ₹50")
     print("4. BREAKFAST : ₹90")
     print("5. LUNCH : ₹110")
     print("6. DINNER : ₹150")
     tea = coffee = bf = lunch = dinner = 0

     order = input("Do you want Tea? (yes/no): ").lower()
     if order == "yes":
            tea = int(input("HOW MANY TEA? "))
     else:
             tea = 0

     order = input("Do you want Coffee? (yes/no): ").lower()
     if order == "yes":
                   coffee = int(input("HOW MANY COFFEE? "))
     else:
            coffee = 0

     order =  input("Do you want Breakfast? (yes/no): ").lower()
     if order == "yes":
           bf = int(input("HOW MANY BREAKFASTS? "))
     else:
           bf = 0

     order = input("Do you want Lunch? (yes/no): ").lower()
     if order == "yes":
           lunch = int(input("HOW MANY LUNCHES? "))
     else:
           lunch = 0

     order = input("Do you want Dinner? (yes/no): ").lower()
     if order == "yes":
             dinner = int(input("HOW MANY DINNERS? "))
     else:
          dinner = 0

     restaurant_bill = tea * 10 + coffee * 20 + bf * 90 + lunch * 110 + dinner * 150
     print("YOUR TOTAL RESTAURANT BILL IS: ₹", restaurant_bill)


  
def rrent():
        rooms()
        global roomrent
        if rchoice == 1:
             roomrent = 6000*days
        elif rchoice == 2:
             roomrent = 5000 * days
        elif rchoice == 3:
             roomrent = 4000*days
        elif rchoice == 4:
             roomrent = 3000*days
        else:
             print("ERROR!!")
        return print("YOUR TOTAL WOULD BE : ₹", roomrent)

def laundry():
      global laundry_bill
      print("-----LAUNDRY MENU-----")
      print("1. Shorts = ₹3")
      print("2. Trousers = ₹4")
      print("3. Shirt = ₹5")
      print("4. Jeans = ₹6")
      print("5. Girl Suit = ₹8")
      s = int(input("ENTER HOW MANY SHORTS? :"))
      t = int(input("ENTER HOW MANY TROUSERS? :"))
      s = int(input("ENTER HOW MANY SHIRTS? :"))
      j = int(input("ENTER HOW MANY JEANS? :"))
      gs = int(input('ENTER HOW MANY GIRL SUITS? :'))
      laundry_bill = s*3 + t*4 + s*5 + j*6 + gs*8
      print("YOUR TOTAL WOULD BE : ₹", laundry_bill)

def total_cost():
        total = roomrent + laundry_bill + restaurant_bill
        print("------HOTEL BILL------")
        print("Customer name:", name)
        print("Room rent: ₹", roomrent)
        print("Restaurant bill: ₹", restaurant_bill)
        print("Laundry bill: ₹", laundry_bill)
        print("Total amount: ₹", total)
        print("----------------------")


name = ""

roomrent = 0

restaurant_bill = 0

stay = 0

laundry_bill = 0

rchoice = 0

choice = 0

days = 0

def main():
     while True:
      entry()
      choice = int(input("Enter your choice: "))

      if choice == 1:
            customer_data()
            ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
            if ask == "yes":
               continue
            else:
               quit()
      elif choice == 2:
          rrent()
          ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
          if ask == "yes":
               continue
          else:
               quit()
      elif choice == 3:
          cafe()
          ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
          if ask == "yes":
               continue
          else:
               quit()
      elif choice == 4:
          laundry()
          ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
          if ask == "yes":
               continue
          else:
               quit()
      elif choice ==5 :
          total_cost()
          ask = input("DO YOU WANT TO CONTINUE (yes/no): ")
          if ask == "yes":
               continue
          else:
               quit()
      elif choice == 6:
          quit()



main()