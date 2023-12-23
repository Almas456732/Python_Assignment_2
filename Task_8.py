number = 1000
while number <= 9999:
    # Extract digits
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    units = number % 10
    if (thousands != hundreds) and (thousands != tens) and (thousands != units) and (hundreds != tens) and (hundreds != units) and (tens != units):
        print(number)
    number += 1
