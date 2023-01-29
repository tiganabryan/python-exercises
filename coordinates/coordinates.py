# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇


def coordinates(double_digit_int):
    digit_list = []
    for digit in double_digit_int:
        digit_list.append(int(digit))

    x = digit_list[0]
    y = digit_list[1]
    row = map[y - 1]
    row[x - 1] = "X"


coordinates(position)


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
