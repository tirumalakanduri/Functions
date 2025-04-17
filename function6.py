def fibonacci(number):
    fib = []
    a, b = 0, 1
    for _ in range(number):
        fib.append(a)
        a, b = b, a+b
    return fib

number = int(input("how many numbers of fibonacci series you want : "))

print(f" the fist { number} fibonacci numbers is : {fibonacci(number)}")