def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def T(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

def root(n, type=2):
    return n**(1/type)

def average(numbers):
    return sum(numbers)/len(numbers)