# Use a list and ask the user to input numbeers while in a loop
entered_numbers = []  

while True:
    try:
        numbers = input("Enter a number: ")  
        num = int(numbers)    
        entered_numbers.append(num)
# Break the loop if the input is invalid
# Get the sum of all inputs
    except ValueError:
        print("Invalid input. Exiting.")
        break

total = sum(entered_numbers)
# Divide by the number of inputs
# Print the average
average = total / len(entered_numbers)

print(average)