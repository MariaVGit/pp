own_funds = 46_567
deposit = own_funds
factor = 1.075

deposit *= factor
deposit *= factor
deposit *= factor

(print("Zysk z inwestycji wynosi", round(deposit - own_funds, 2), "zł"))

