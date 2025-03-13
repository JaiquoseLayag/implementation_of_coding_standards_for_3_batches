# Use a list and ask the user to input numbers while in a loop
numbers = []

while True:
    user_input = input("Enter a number (or any non-numeric value to stop): ")
    try:
        number = int(user_input)  
        numbers.append(number)
# Break the loop if the input is invalid
# Count each number in the list
    except ValueError:
        break  

if numbers:
    unique_numbers = list(set(numbers))  
    max_count = 0
    most_frequent = numbers[0]  

    for num in unique_numbers:
        count = numbers.count(num)
# Store the most frequent number in the list and print
        if count > max_count:
            max_count = count
            most_frequent = num

    print(most_frequent)