weekday = int(input('Введите номер дня недели: \n'))

if 0 < weekday <=7:
    if weekday == 6 or weekday == 7:
        print('Это выходной день!')
    else:
        print('Это будний день!')
else:
    print('В неделе СЕМЬ дней!')
