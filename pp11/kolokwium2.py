# napisz skrypt który wyświetli 5 losowych liczb całkowitych z zakresu liczb podanego przez użytkownika
import random
list = []
num1 = int(input("podaj zakres od: "))
num2 = int(input("podaj zakres do: "))
for i in range(5):
   number = random.randint(num1,num2+1)
   list.append(number)
print(list)



