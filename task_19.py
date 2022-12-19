from random import randint

def get_random_numbers_list():
    numbers = []
    length = randint(10,100)
    for _ in range(length):
        numbers.append(randint(-100,100))
    return numbers

def sum_odd_index_numbers(number_list: list)->list:
    sum_numbers = 0
    for i in range(1, len(number_list), 2):
        sum_numbers += number_list[i]
    return sum_numbers

def sum_odd_index_numbers_2(numbers_list: list)->int:
    return sum(numbers_list[1::2])

def main():
    random_list = get_random_numbers_list()
    print(f'Рандомный список: {random_list}')
    print(sum_odd_index_numbers(random_list))

main()
