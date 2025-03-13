# Ask the user to input 10 numbers
numbers = []
duplicates = set()

for i in range(10):
    num = int(input("Enter a number: "))
# Store the inputs into a list and count every item
    numbers.append(num)
    numbers.count(num)
# Store the numbers with duplicates into a set
for num in numbers:
    if numbers.count(num) > 1:
        duplicates.add(num)
# Print the numbers
print(duplicates)