number = 76542
reverse_num = 0
print("Given Number, number")

while number > 0:
    note = number % 10
    reverse_num = (reverse_num * 10) + note
    number = number // 10

print("Reverse Number", reverse_num)