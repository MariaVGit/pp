txt = "Ala ma kota."

print(txt)
print(len(txt))
print(len(''))
print(len("\n\t\\"))

txt = """To jest tekst.
        ten tekst ma kilka linii
        Raz dwa trzy."""
print(len(txt))
print(len("a\nb\nc"))

str1 = "a"
str2 = "b"
print(str1 + str2)
print(5 * str1)
print(str1 * 5)
str1 += str2
char1 = "a"
char2 = " "
print(ord(char1))
print(ord(char2))

print(chr(97))
print(chr(945))
print("a" == chr(ord("a")))
for c in txt:
    print(c,end=" ")
for i in range(len(txt)):
    print(txt[i], end=" ")
print(txt[4:6])
print(txt[7:])
print(txt[-1:])
print(txt[2::3])