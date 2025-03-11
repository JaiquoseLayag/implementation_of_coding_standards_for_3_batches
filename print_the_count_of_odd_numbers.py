# Initialize count to 0
count = 0

# Use a loop to ask user to input 10 numbers
for i in range(10):
    i = int(input("Enter a number: "))
    
# Check each number if they are odd
# Add 1 to the count for each odd number found
    if i % 2 != 0:
        count += 1
        
# Print the total count