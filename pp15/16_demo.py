import math
import sys

print(math.sin(math.pi /2))
print(math.factorial(5))
print(math.floor(4.9999999))

from math import pi, sin
print(sin(pi))

import math as m
print(m.pi)

from math import pi as PI
print(PI)

print(dir(math))

import random
print(random.random())

from random import random, seed
seed(1)

for i in range(5):
    print(random())

from random import choice, sample
lst = [i for i in range(1,11)]

print(choice(lst)) #wybiera jedną liczbę ze zbioru
print(sample(lst, 5))




