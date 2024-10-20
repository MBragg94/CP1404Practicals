"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When you try to divide by a smaller number then yourself
2. When will a ZeroDivisionError occur? When you divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError? im honestly not sure
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")