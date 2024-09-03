# assignment 3
# 1.
def multiplication_table(number, start=1, stop=10):
    """
    Generate a multiplication table for a given number.

    :param number: The number to generate the multiplication table for.
    :param start: The starting value for the multiplication (inclusive).
    :param stop: The ending value for the multiplication (inclusive).
    """

    current = start

    # Generate the multiplication table using a while loop
    while current <= stop:
        result = number * current
        print(f"{number} x {current} = {result}")
        current += 1

multiplication_table(5)

print()  

multiplication_table(7, start=3, stop=7)

# 2.
def sum_range(lower, upper):
    """
    Sums all the numbers from the lower limit to the upper limit (inclusive).

    :param lower: The starting number of the range (inclusive).
    :param upper: The ending number of the range (inclusive).
    :return: The sum of the numbers in the range.
    """
    # Initialize the total sum to 0
    total_sum = 0

    current = lower
    while current <= upper:
        total_sum += current
        current += 1

    return total_sum

# Example usage
lower_limit = 1
upper_limit = 30
result = sum_range(lower_limit, upper_limit)
print(f"The sum of all numbers from {lower_limit} to {upper_limit} is: {result}")

# 3.
def calculate_average(numbers):
    """
    Calculates the average of numbers in a list.

    :param numbers: A list of numbers (integers or floats).
    :return: The average of the numbers, or None if the list is empty.
    """
    # Check if the list is empty
    if not numbers:
        print("The list is empty. Cannot calculate the average.")
        return None

    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    
    # Calculate the average
    average = total_sum / len(numbers)
    
    return average

# Example usage
numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)

if average is not None:
    print(f"The average of the numbers is: {average}")

# Example with an empty list
empty_list = []
average_empty = calculate_average(empty_list)

# 4.
def calculate_average(numbers):
    """
    Calculates the average of numbers in a list.

    :param numbers: A list of numbers (integers or floats).
    :return: The average of the numbers, or None if the list is empty.
    """
    # Check if the list is empty
    if not numbers:
        print("The list is empty. Cannot calculate the average.")
        return None

    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    
    # Calculate the average
    average = total_sum / len(numbers)
    
    return average

# Example usage
numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)

if average is not None:
    print(f"The average of the numbers is: {average}")

# Example with an empty list
empty_list = []
average_empty = calculate_average(empty_list)
