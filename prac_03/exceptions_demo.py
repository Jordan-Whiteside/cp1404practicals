"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
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

# 1. When will a ValueError occur?
# When no value is entered and when the value isn't and integer (i.e. 0.5 or "string")

# 2. When will a ZeroDivisionError occur?
# When the denominator is 0

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes. You could change the code to have an error checking with while loops which avoids the possibility of 0 being entered
# Error checking while loop found her: https://github.com/CP1404/Starter/wiki/Programming-Patterns#error-checking
