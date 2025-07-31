import math

number = float(input("Enter a number: "))

square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

print(f"Square root of {number} is: {square_root}")
print(f"Natural logarithm (ln) of {number} is: {natural_log}")
print(f"Sine of {number} radians is: {sine_value}")

#Output:
# Enter a number: 15
# Square root of 15.0 is: 3.872983346207417
# Natural logarithm (ln) of 15.0 is: 2.70805020110221
# Sine of 15.0 radians is: 0.6502878401571168
