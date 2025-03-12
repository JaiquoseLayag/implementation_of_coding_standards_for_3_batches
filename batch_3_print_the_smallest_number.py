# Use a set and ask the user to input numbers while in a loop
entered_numbers = set()

while True:
    try:
        numbers = input("Enter a number: ")
        num = int(numbers)
        entered_numbeers.add(num)                
# Store the numbers in a set and check which is the smallest
# Break the loop once the input is invalid and print the smallest number