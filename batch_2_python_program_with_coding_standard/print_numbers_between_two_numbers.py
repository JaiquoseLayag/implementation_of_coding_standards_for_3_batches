# Ask the user to input the first number
first_num = int(input("Enter a number: "))
# Ask the user to input the second number
second_num = int(input("Enter a number: "))

# Apply a condition to let the smaller number be the first number
if a > b:
    a, b = b, a
# Use a loop and increment by 1 until it reaches the bigger number
# Print the number
for i in range(a + 1, b):
    print(i)