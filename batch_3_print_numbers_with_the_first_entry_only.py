# Make a list and loop to ask the user to input 10 numbers and append to the list
numbers = []  
first_entry = set()  


for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Use a loop and use a set to ensure the first entry is printed
for num in numbers:
    if num not in first_entry:
# Print the numbers
        print(num)
        first_entry.add(num)