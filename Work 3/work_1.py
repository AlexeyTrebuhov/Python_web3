# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint
print()
list_01 = []
list_02 = []
list_03 = []

y = 1
m = 30
while y <= m:
    list_01.append(randint(1,20))
    y += 1
print("Список повторяющихся элементов", list_01)

sort_list = sorted (list_01)
print ("Сортированный список повторяющихся элементов", sort_list)
print()

i = 0
while ( i < 30):
    spam = sort_list.count(sort_list[i])

    if spam == 1:
        list_02.append(sort_list[i])
    else:
        list_03.append(sort_list[i])
    i += 1


print ("Список без дублирующихся элементов", list_02)
print ("Список только дублирующихся элементов", list_03)


