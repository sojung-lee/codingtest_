#반복적으로 구현한 n!
def factorial_it(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

#재귀적으로 구현한 n!
def factorial_re(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)