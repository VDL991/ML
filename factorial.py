def factorial_recursion(n):
    if(n < 0): 
        raise ValueError ("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * factorial_recursion(n - 1)
   

user_input = int(input("Enter number: "))
result = factorial_recursion(user_input)
print("Factorial of given number is:", result)