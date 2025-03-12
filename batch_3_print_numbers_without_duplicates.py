# Ask to user to input 10 numbers and append it to the list
numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Make another list and count each item in the list
non_duplicates = []

for num in numbers:
    if numbers.count(num) == 1:
        non_duplicate.append(num)
# Print all numbers with a count of 1
print(non_duplicates)