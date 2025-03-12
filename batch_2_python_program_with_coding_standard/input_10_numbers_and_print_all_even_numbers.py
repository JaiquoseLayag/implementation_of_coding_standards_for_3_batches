count = 0
# Use a loop and ask the user to input 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
# Use modulus (%) to check if numbers are even
    if num % 2 == 0:
        count += 1
# Print all even numbers
print(count)