number = int(input("Enter a number (0 to stop): "))
total = 0


if number == 0:
    print(f"The total is: {total}")

else:
    while number != 0:
        total = number + total
        number = int(input("Enter a number (0 to stop): "))
        if number == 0:
              print(f"The total is: {total}")
