def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

sample_number = int(input("Enter integer number only: "))
print(f"The factorial of {sample_number} is {factorial(sample_number)}")

#Output:
# Enter integer number only: 6
# The factorial of 6 is 720