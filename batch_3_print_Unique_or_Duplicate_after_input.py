# Use a set and ask the user to input numbers while in a loop
entered_numbers = set()

while True:
    try:
        numbers = input("Enter a number: ")
        int(numbers)
# Store numbers in the set and print along with Unique if it's not in the set and Duplicate if it's in the set
        if numbers in entered_numbers:
            print("Duplicate")
        else:
            print("Unique")
            entered_numbers.add(numbers)
# Break the loop once the input is invalid
    except ValueError:
        print("Invalid input. Exiting")
        break