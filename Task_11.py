number = 1

while True:
    number_str = str(number)
    digit_sum = 0
    for digit_char in number_str:
        digit_sum += int(digit_char)
    if number % 7 == 0 and digit_sum % 7 == 0:
        print(number)
    number += 1
