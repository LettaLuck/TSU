# Задание 1
# Имеются два списка элементов [1, 1, 2, 3, 1] и [1, 1, 1, 2]. Необходимо:
# 1) создать два множества с помощью метода set()
lst_one = [1, 1, 2, 3, 1]
lst_two = [1, 1, 1, 2]
set_1 = set(lst_one)
set_2 = set(lst_two)

# 2)с полученными множествами реализовать операции объединения, пересечения, разности
# ПЕРЕСЕЧЕНИЕ
print(set_1 & set_2)
# или
print(set_1.intersection(set_2))

# ОБЪЕДИНЕНИЕ
print(set_1 | set_2)
# или
print(set_1.union(set_2))

# РАЗНОСТЬ
print(set_1 - set_2)

# Задание 2
# Имеется строка 'некоторый текст'. Переведите ее в множество
str_some = 'некоторый текст'
mn = set(str_some)
print(mn)
