def char1(char ="*",repeat=10,vertical=False):
    for i in range(repeat):
        if vertical:
            print(char)
        else:
            print(char + " ", end="")
char1("?",5,True)
char1("?",5,False)
char1("$",5,True)


