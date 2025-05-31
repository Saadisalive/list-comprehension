# Take a number from the user
n = int(input("Enter a number: "))

# List of all odd numbers under the input
odd_numbers = [i for i in range(n) if i % 2 != 0]

# List of all even numbers under the input
even_numbers = [i for i in range(n) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

#now fruits
fruits = ["apple", "banana", "cherry", "date"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)