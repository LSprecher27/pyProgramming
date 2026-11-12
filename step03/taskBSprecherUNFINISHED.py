# Name: Luke Sprecher
# Date: 11/12/26
# Program: This program calculates shipping costs and delivery times for online orders

# Constants
ZONE1_RATE = 0.50
ZONE2_RATE = 0.75
ZONE3_RATE = 1.25
MINIMUM_SHIPPING = 4.00
FREE_SHIPPING_AMOUNT = 50.00
RUSH_FEE = 10.00
SHIPPING = 0.00


# Find order total, package weight(lbs), shipping zone(whole number), and rush delivery(y/n)

ORDER_TOT = input("What is your order total?")
WEIGHT = input("What does your package weigh?")
SHIPPING_ZONE = input("What is your shipping zone?")
RUSH_DELIVERY = input("Are you using rush delivery? (y/n)")


if ORDER_TOT or WEIGHT = >0
    if SHIPPING_ZONE == 1:
        SHIPPING = ZONE1_RATE 
        
else:
    print("Error: order total and weight must be more than 0")

