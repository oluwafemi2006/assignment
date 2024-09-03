# assignment 1
#1.
x = 78;
if 0 <= x <= 34:
    print('Fail')
elif 35 <= x <= 44:
    print('Pass')
elif 45 <= x <= 49:
    print('Fair')
elif 50 <= x <= 59:
    print('Good')
elif 60 <= x <= 69:
    print('Very Good')
elif 70 <= x <= 100:
    print('Excellence')
else:
    print("You did not write the exam")   

Student_score = int(input("Enter your score"))
if 0 <= Student_score <= 34:
    print('Fail')
elif 35 <= Student_score <= 44:
    print('Pass')
elif 45 <= Student_score <= 49:
    print('Fair')
elif 50 <= Student_score <= 59:
    print('Good')
elif 60 <= Student_score <= 69:
    print('Very Good')
elif 70 <= Student_score <= 100:
    print('Excellence')
else:
    print("You did not write the exam")   


# 2.
# Function to find the lowest number among three numbers
def find_lowest_number(num1, num2, num3):
    return min(num1, num2, num3)

print("Please enter three numbers:")

try:
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    
    lowest_number = find_lowest_number(num1, num2, num3)

    
    print(f"The lowest number is: {lowest_number}")

except ValueError:
    print("Please enter valid numbers.")