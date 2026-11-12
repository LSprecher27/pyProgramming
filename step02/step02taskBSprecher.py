# Name: Luke Sprecher
# Date: 11/11/2026
# Program: Calculates costs for a road trip based off of multiple variables

# Constants
AVERAGE_SPEED = 55

# Input
destination = input("Destination: ")
distance = float(input("Trip distance (miles): "))
mpg = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
num_people = int(input("Number of people splitting the cost: "))

# Processing
gallons = distance / mpg
gas_cost = gallons * gas_price
cost_per_person = gas_cost / num_people
total_minutes = int(distance / AVERAGE_SPEED * 60)
hours = total_minutes // 60
leftover_minutes = total_minutes % 60
round_trip_gas = gas_cost * 2

# Output
print()
print(f"--- Trip to {destination} ---")
print(f"Gallons of gas:   {gallons:.1f}")
print(f"Gas cost:         ${gas_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")
print(f"Driving time:     {hours} hr {leftover_minutes} min (at {AVERAGE_SPEED} mph)")
print(f"Round trip gas:   ${round_trip_gas:.2f}")
