def calc(gst_rate, amount):
    gst_amount = (gst_rate * amount)/100
    total_amount = (amount + gst_amount)
    return gst_amount, total_amount

print("Welcome to GST Calculator")
gst_rate = int(input("Please enter the GST Rate: "))
amount = int(input("Please enter your amount: ₹"))
print("your GST rate is:",gst_rate, "%")
print("your amount is: ₹", amount)
gst_amount, total_amount = calc(gst_rate, amount)
print("you will be charged: ₹", gst_amount, "gst amount." )
print("your total will be: ₹",total_amount)
