print(ord('a'))
print(ord('z'))

for i in range(ord('a'), ord('z')+1):
    print(chr(i),end="")

alphabet = ""
for i in range(ord('a'), ord('z')+1):
    alphabet += chr(i)


print(min([1,2,3]))
print(min("abcABC"))
print(max("Ala ma kota"))

print(alphabet.index("w"))
print(list(alphabet))

print("Ala ma kota.".count("a"))
print([1,2,3,1,1].count(1))

