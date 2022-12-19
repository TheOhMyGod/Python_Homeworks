num_a = int(input('Введите число: \n'))
num_b = ''
while num_a > 0:
    num_b = str(num_a%2) + num_b
    num_a = num_a // 2
print(num_b)
