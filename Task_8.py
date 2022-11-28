x_coordinate = int(input('Введите координату X: '))
y_coordinate = int(input('Введите координату Y: '))

if x_coordinate > 0 and y_coordinate > 0:
    print(f'Точка с координатами ({x_coordinate},{y_coordinate}) находится в Первой координатной четверти')
elif x_coordinate < 0 and y_coordinate > 0:
    print(f'Точка с координатами ({x_coordinate},{y_coordinate}) находится во Второй координатной четверти')
elif x_coordinate < 0 and y_coordinate < 0:
    print(f'Точка с координатами ({x_coordinate},{y_coordinate}) находится в Третьей координатной четверти')
elif x_coordinate > 0 and y_coordinate < 0:
    print(f'Точка с координатами ({x_coordinate},{y_coordinate}) находится в Четвертой координатной четверти')
else:
    print(f'Точка с координатами ({x_coordinate},{y_coordinate}) - центр координатной плоскости')
