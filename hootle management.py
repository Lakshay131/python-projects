def entry():
    print("------WELCOME TO OUR HOTEL------")
    print("1.Enter Customer Data")
    print("2.Calculate rommrent")
    print("3.Calculate restaurant bill")
    print("4.Calculate laundry bill")
    print("5.Calculate gamebill")
    print("6.Show total cost")
    print("7.EXIT")
    

def customer_data():
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
     print("-----WELCOME TO OUR CAFE-----")
     menu = [
    ("1. Coffee : 30"),
    ("2. Maggie : 50"),
    ("3. Burger : 60"),
    ("4. Tea : 20"),
    ("5. Bun Maska : 10"),
    ]
     print(menu)
     items = int(input("WHAT DO YOU WANT TO ORDER? :"))
     menu_total = 
     

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

name = ""

roomrent = 0

stay = 0

laundry_bill = 0

rchoice = 0

choice = 0

days = 0

def main():
     entry()
     choice = int(input("Enter your choice: "))

     if choice == 1:
          customer_data()
     elif choice == 2:
          rrent()
     elif choice == 3:
          cafe()
     elif choice == 4:
          laundry()
     elif choice == 7:
          quit()

main()