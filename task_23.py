n = int(input('Введите число: \n'))

if n < 0: n = n * -1
f1 = f2 = 1
list_1 = [f1, f2]

for i in range(2, n):
    f1,f2 = f2, f1 + f2
    list_1.append(f2)

print(list_1)

f1=f2=1

for i in range(-n, 1):
    f1,f2 = f2, f1 - f2
    list_1.insert(0, f2)

print(list_1)
