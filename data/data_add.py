import random

data = open('data\lesmis.txt', 'r')
data2 = open('data\lesmis_test.txt', 'a')
qtd = 50

for i in range(qtd):
    s = random.randint(77,91)
    t = random.randint(0, 91)
    v = random.randint(1,13)

    data2.write(f"edge\nsource {s}\ntarget {t}\nvalue {v}\n")
