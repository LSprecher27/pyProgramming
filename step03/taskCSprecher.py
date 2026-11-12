# Name: Luke Sprecher
# Date: 11/12/26
# Program: BPA Eligibility Checker

# Constants
MIN_GPA = 2.0
OFFICER_GPA = 3.0
HONOR_GPA = 3.5
MAX_EVENTS = 2

# Inputs
NAME = input("What is your name?")
GPA = input("what is your GPA")
GRADE = input("What is your grade?")
DUES = input("Dues paid? (y/n)")
EVENTS = input("How many events are you signed up for? (Numeric Whole Value only)")

# Other variables
STATUS = "ELIGIBLE"

# Checks

if GPA is <= 0.0 or >= 4.0:
    print("Error: GPA must be 0.0 to 4.0")
elif GRADE <= 9 or >= 12:
    print("Error: Grade must be 9 to 12")

# Test eligibiliy
if GPA is < MIN_GPA or DUES.lower() == "n":
    STATUS = "NOT ELIGIBLE"
elif GPA > MIN_GPA and DUES.lower() == "y":
    STATUS = "ELIGIBLE"

print(f"Member name: {NAME}")
print(f"Grade = {GRADE}")
print(f"GPA: {GPA}")
print(f"Dues Paid?: {DUES}")
print(f"Events signed up for: {EVENTS}")

if STATUS == "ELIGIBLE":
    print(f"/nStatus: {STATUS}")
    if events <= 2 and >= 1:
        print(f"Signed up for {EVENTS} events")
    elif EVENTS > 2:
        print(
else:
     print(f"/nStatus: {STATUS}")
     if GPA is < MIN_GPA:
         print("GPA is below 2.0")
     elif DUES.lower() == "n":
         print("Dues not paid")

         
