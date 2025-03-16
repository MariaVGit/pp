s = 0
for i in range(64):
    s += 2 ** i

print("Suma wszystkich ziaren na szachownicy: " + str(s))

# założenia: waga jednego ziarna to 0,4mg -> 0,0004g
#1 kg = 1000g
#1t = 1000kg
tons = int(s * 0.0004 /1000/1000)
print("ton: " ,tons)

#roczna produkcja pszenicy na świecie to 782 mln ton
years = int(tons/ 782_000_000)
print("lata: ", years)

# pociąg może przetransportować 2200t
trains = int(tons/2200)
print("pociągów: ",trains)


