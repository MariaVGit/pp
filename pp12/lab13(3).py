import random

first_symbol = "A"
last_symbol = "H"
number_of_letters = 3
#kod znaku A to 65 ord("A")
def draw_letter():
    return chr(random.randint(ord(first_symbol),ord(last_symbol)))
def draw_row():
    return [draw_letter() for _ in range(number_of_letters)]
def check(row):
    if row[0] == row[1] == row[2]:
        return True
    else:
        return False

counter = 1
while True:
    row = draw_row()
    print(row,counter)
    if check(row):
        break
    counter += 1

print(draw_letter())
print(draw_row())
print(check(draw_row()))

