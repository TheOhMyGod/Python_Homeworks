number = int(input('Введите число N: '))

sum = 0
for i in range(2, number + 1):
    if  not i % 2:
        sum += i
        if i != 2:
            print(' + ', end='')
        print(i, end='')
print(f' = {sum}')
