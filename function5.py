def sum_of_digits(number):
    total = 0
    while number >0:
        digit = number % 10
        total +=digit
        number = number // 10
    return total 
number = int(input("enter the number : "))
print(f"sum of digits of {number} is {sum_of_digits(number)}")


