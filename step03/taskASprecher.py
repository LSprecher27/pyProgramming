# Name: Luke Sprecher
# Date: 11/12/2026
# Program: Calculates the proce of one movie ticket


# Set the prices up
TOTAL = 0.00
PRICE = 0.00
CHILD_PRICE = 7.00
ADULT_PRICE = 11.00
SENIOR_PRICE = 8.00

# Extra Factors
TICKET_TYPE = "Adult"
TUESDAY_DISCOUNT = 3.00
THREE_D_CHARGE = 2.50

NAME = input("What is your name?")
AGE = int(input("What is your age?"))
DAY = input("What day would you like to view the movie?")
THREE_D = input("Will you be viewing your movie in 3D? (y/n)")

# Price Calculating

if AGE < 0 or AGE > 120:
    print("Error: age must be 0 to 120.")
elif AGE <= 13:
    PRICE = CHILD_PRICE
    TICKET_TYPE = "Child"
    
elif AGE >= 65:
        PRICE = SENIOR_PRICE
        TICKET_TYPE = "Senior"
else:
    PRICE = ADULT_PRICE
    TICKET_TYPE = "Adult"

if DAY.lower() == "tuesday":
    TOTAL = PRICE - TUESDAY_DISCOUNT


if THREE_D.lower() == "y":
    TOTAL = PRICE + THREE_D_CHARGE

print("--- Ticket for " + NAME + " ---")
print("Ticket type: " + str(TICKET_TYPE))
print("Base price: $" + str(PRICE))

if DAY.lower() == "tuesday":
    print("Tuesday deal: -$3.00")
else:
    print("Tuesday deal: -$0.00")
    
if THREE_D.lower() == "y":
    print("3D charge: $2.50")
else:
    print("3D charge: $0.00")
print(f"Total: {TOTAL:.2f}")

