# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def qu(a, b):
    k = 0
    for j in a:
        if int(j) == b:
            k += 1
    return k


n = int(input("сколько чисел вы хотите ввести "))
t = int(input("какую цифру буде искать "))
v = 0
for i in range(0, n):
    d = input()
    v += qu(d, t)
print("число ", t, "встретилось ", v, "раз")



