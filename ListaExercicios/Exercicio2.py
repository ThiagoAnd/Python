import random

rand = random.randint(2, 5)
lista = random.sample(range(1, rand+1), rand)
print(rand, " ", lista)

for i in range(1,rand+1):
    for j in range(1, rand -2):
        print(j, "voltadd")
    print(i, "volta")
