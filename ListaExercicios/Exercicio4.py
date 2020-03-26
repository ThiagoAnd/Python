import random

rand = random.randint(2, 105)
lst = random.sample(range(1, rand + 1), rand)
print('\r', rand, lst, end=' ')

first = True
for i in range(0, rand - 1):
    for j in range(1, rand - i):
        if lst[j - 1] > lst[j]:
            aux, lst[j - 1], = lst[j - 1], lst[j]
            lst[j] = aux
            first = False if first else True

print("- Quem ganhou foi o", "Marcelo" if first else "Carlos")
''' print(lst)'''
