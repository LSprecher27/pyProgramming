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

# Input
order_total = float(input("Order total: "))
weight = float(input("Package weight (lbs): "))
zone = int(input("Shipping zone (1-3): "))
rush = input("Rush delivery? (y/n): ")

# Processing & Output
if order_total <= 0 or weight <= 0:
    print("Error: order total and weight must be more than 0.")
elif zone != 1 and zone != 2 and zone != 3:
    print("Error: zone must be 1, 2, or 3.")
else:
    is_rush = rush.lower() == "y"

    # 1. Zone rate and base delivery days
    if zone == 1:
        rate = ZONE1_RATE
        days = 2
    elif zone == 2:
        rate = ZONE2_RATE
        days = 4
    else:
        rate = ZONE3_RATE
        days = 6

    shipping = weight * rate

    # 2. Minimum shipping
    if shipping < MINIMUM_SHIPPING:
        shipping = MINIMUM_SHIPPING

    # 3. Free shipping (only if not rush)
    if order_total >= FREE_SHIPPING_AMOUNT and not is_rush:
        shipping = 0.00

    # 4. Rush delivery
    if is_rush:
        shipping = shipping + RUSH_FEE
        if zone == 1 or zone == 2:
            days = 1
        else:
            days = 2

    # 5. Heavy package
    if weight > 50:
        days = days + 2

    grand_total = order_total + shipping

    # Output summary
    print("\n--- Shipping Summary ---")
    print(f"Order total:  ${order_total:.2f}")
    if shipping == 0:
        print("Shipping:     FREE")
    else:
        print(f"Shipping:     ${shipping:.2f}")
    print(f"Grand total:  ${grand_total:.2f}")

    if days == 1:
        print("Arrives in:   1 day")
    else:
        print(f"Arrives in:   {days} days")

    if weight > 50:
        print("Note: heavy package, 2 extra days added.")
