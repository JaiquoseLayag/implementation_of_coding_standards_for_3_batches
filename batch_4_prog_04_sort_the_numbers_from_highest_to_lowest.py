# Use a list and ask user to input numbers while in a loop
entered_numbers = []  

while True:
    try:
        numbers = input("Enter a number: ")  
        num = int(numbers)    
        entered_numbers.append(num)   
# Break the loop once input is invalid
# Sort the list from highest to lowest and print the list
    except ValueError:
        print("Invalid input. Exiting.")
        break

entered_numbers.sort(reverse=True)
print(entered_numbers)
