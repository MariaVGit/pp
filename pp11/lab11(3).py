import random
blank_square = "__"
pieces = ["wp","bp","bt","wt","wq"]
chessboard = [[blank_square for _ in range(8)] for _ in range(8)]
counter = 0
while counter < 5:
    row = random.randint(0,7)
    col = random.randint(0,7)
    if chessboard[row][col] == blank_square:
        chessboard[row][col] = pieces[counter]
        counter += 1
for row in range(len(chessboard)):
    for col in range(len(chessboard[row])):
        print(chessboard[row][col],end=" ")

