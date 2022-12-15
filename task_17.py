n = int(input('Введите число N: '))
numbers = list(range(-n, n+1))
print(f'Список: \n {numbers}')
indexes = [0, 1, 2, 3, 5]
print(f'Индексы: \n {indexes}')
multipication = numbers[indexes[0]] + numbers[indexes[1]] + numbers[indexes[2]] + numbers[indexes[3]]\
                + numbers[indexes[4]]
print(f'Произведение: \n {multipication}')
