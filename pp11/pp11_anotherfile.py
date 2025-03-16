#całe nie działa

#tworzymy planszę do gry w szachy
#chess_row = ["--" for _ in range(8)]
#chessboard =[chess_row[:]for _ in range(8)]

chessboard = [["--" for _ in range(8)] for _ in range(8)]
white_pawn = "BP"
black_pawn = "CP"
chessboard[3],[4] = white_pawn
chessboard[2],[7] = black_pawn
for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square,end=" ")

print(chessboard)
