# assignment 2
# 1.
def print_multiplication_table(number):
    multiplier = 1
    while multiplier <= 10:
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1

try:
    num = int(input("Enter a number to generate its multiplication table: "))

    print(f"Multiplication table for {num}:")
    print_multiplication_table(num)

except ValueError:
    print("Please enter a valid integer.")

# 2.
names_list = ["Alice", "Bob", "Charlie", "Diana", "Eva"]

user_name = input("Please enter a name to search: ")

if user_name in names_list:
    print(f"The name '{user_name}' is in the list.")
else:
    print(f"The name '{user_name}' is not in the list.")

# 3.
total_sum = 0

for number in range(1, 31):
    total_sum += number

print("The sum of all numbers from 1 to 30 is:", total_sum)

# 4.
numbers = [10, 20, 30, 40, 70, 200, 300]

total_sum = sum(numbers)

average = total_sum / len(numbers)

print("The sum of the numbers is:", total_sum)
print("The average of the numbers is:", average)
