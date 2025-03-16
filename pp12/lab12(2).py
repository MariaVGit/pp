def perimeter(a,b):
    return 2 * a + 2 * b
def area(a,b):
    return a*b
def length(a,b):
    return (a**2 + b**2)**0.5

def show_result(a,b):
    print("prostokąt o bokach {} i {}:".format(a,b))
    print("obwód:", perimeter(a,b))
    print("pole powierzchni:",area(a,b))
    print("długość przekątnej:",length(a,b))
    print()
show_result(4,5)
show_result(2677,5678)
show_result(344555,788998)