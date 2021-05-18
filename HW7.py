# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "John", "age": 15}, {"name": "Dimitry", "age": 177}, {"name": "John", "age": 45}]

# найти имя самого молодого человека
age_min = persons[0]["age"]

for user_age_min in persons:
    if user_age_min["age"] < age_min:
        age_min = user_age_min["age"]

names_user = []

for name_user_min in persons:
    if name_user_min["age"] == age_min:
        names_user.append(name_user_min["name"])

print(names_user)

# найти самое длинное имя
max_name = persons[0]["name"]

for user_name_max in persons:
    if len(user_name_max["name"]) > len(max_name):
        max_name = user_name_max['name']

max_name_user = []

for name_user_max in persons:
    if len(name_user_max["name"]) == len(max_name):
        max_name_user.append(name_user_max["name"])

print(max_name_user)

# найти средний возвраст
middle_age = []

for i in persons:
    middle_age.append(i.get("age"))


print(sum(middle_age) / len(middle_age))

####################################################################################################################
print() # добавил чисто для терминала, чтобы удобней было смотреть!!!!!!!!!!
####################################################################################################################
# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {1: 1255, 2: 111, 77: 1188, 3: 777, 10: 707}
my_dict_2 = {1: 56734, 2: 56664, 3: 111, 7: 323}

# а) Создать список из ключей, которые есть в обоих словарях.
my_result_key = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
print(my_result_key)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
my_result = list(set(my_dict_2).symmetric_difference(set(my_dict_1)) - set(my_dict_2))
print(my_result)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
my_dict = dict()
for i in my_result:
    my_dict[i] = my_dict_1.setdefault(i)
print(my_dict)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_result_2 = list(set(my_dict_1).symmetric_difference(set(my_dict_2)) - set(my_dict_1))

my_dict_result = dict()
my_dict_result.update(my_dict)
for i in my_result_2:
    my_dict_result[i] = my_dict_2.setdefault(i)

for i in my_result_key:
    my_dict_result[i] = [my_dict_1.setdefault(i), my_dict_2.setdefault(i)]

print(my_dict_result)
# ####################################################################################################################

