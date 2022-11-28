point_a_x = float(input('Введите координату X точки A: '))
point_a_y = float(input('Введите координату Y точки B: '))
point_b_x = float(input('Введите координату X точки A: '))
point_b_y = float(input('Введите координату Y точки B: '))

import math

a_to_b_length = round(math.sqrt(math.pow(abs(point_a_x - point_b_x),2) + math.pow(abs(point_a_y - point_b_y),2)),2)

print(f'Расстояние между точкой A({point_a_x},{point_a_y}) и точкой B({point_b_x},{point_b_y}) равняется {a_to_b_length}!')
