# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
from operator import itemgetter

Tourist_set = dict([("Ложка", 100), ("Вилка", 100), ("Кружка", 200) ,("Спальник", 3000), ("Палатка", 5000), ("Гиря", 16000),
                    ("Котелок", 500), ("Керосин", 1500), ("Бинокль", 700)])

sorted_Tourist_set = dict(sorted(Tourist_set.items(),reverse=True, key=itemgetter(1)))

load_capacity = int(input('Введите грузоподъемность хозяина рюкзака:   '))

for key,value in sorted_Tourist_set.items():

    if ((load_capacity - value) <0):
        break

    print (f'{key = } остаток грузоподъемности = {load_capacity - value}')
    load_capacity = load_capacity - value




