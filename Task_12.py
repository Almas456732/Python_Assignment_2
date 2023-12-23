num = int(input())
count_0 = count_1 = count_2 = count_3 = count_4 = count_5 = count_6 = count_7 = count_8 = count_9 = 0
num_str = str(num)
for char in num_str:
    if char == '0':
        count_0 += 1
    elif char == '1':
        count_1 += 1
    elif char == '2':
        count_2 += 1
    elif char == '3':
        count_3 += 1
    elif char == '4':
        count_4 += 1
    elif char == '5':
        count_5 += 1
    elif char == '6':
        count_6 += 1
    elif char == '7':
        count_7 += 1
    elif char == '8':
        count_8 += 1
    elif char == '9':
        count_9 += 1
print("Digit counts:")
if count_0 > 0:
    print(f"Digit 0: {count_0} ")
if count_1 > 0:
    print(f"Digit 1: {count_1} ")
if count_2 > 0:
    print(f"Digit 2: {count_2} ")
if count_3 > 0:
    print(f"Digit 3: {count_3} ")
if count_4 > 0:
    print(f"Digit 4: {count_4} ")
if count_5 > 0:
    print(f"Digit 5: {count_5} ")
if count_6 > 0:
    print(f"Digit 6: {count_6} ")
if count_7 > 0:
    print(f"Digit 7: {count_7} ")
if count_8 > 0:
    print(f"Digit 8: {count_8} ")
if count_9 > 0:
    print(f"Digit 9: {count_9} ")

