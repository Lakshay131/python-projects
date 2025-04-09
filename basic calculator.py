print("welcomr to the calculator")
num_1 = int(input("enter your first number: "))
num_2 = int(input("enter your second number: "))
opr = input("enter which operation you would like to perform (+,-,x,/): ")
if (opr == "+"):
    print(num_1+ num_2)
elif opr == "-":
    print(num_1 - num_2)
elif(opr == "*"):
    print(num_1 * num_2)
elif(opr == "/"):
    print(num_1/num_2)
else:
    print("error!!")\


print("thanks for using our calculator.")