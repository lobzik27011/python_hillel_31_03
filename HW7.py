# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "John", "age": 15}, {"name": "Dimitry", "age": 15}, {"name": "Jack", "age": 45}]



# for minimum in persons:
#     age_user_list.append(list(minimum.values())[1])
#
# age_user_list = min(age_user_list)
age_list = []

for user_age in persons:
    age_list.append(user_age.get("age"))
    if len(age_list) != len(set(age_list)):
        print(user_age.get('name'))

print(age_list)


    # print(user_age)
    # print(user_age.get('age'))

    # if user_age.get('age')



    # print(user_age.get('name'))
    # if list(user_age.values())[1] == age_user_list:
    #     print(user_age.get('name'))
    #

# print(dict(persons).values())

####################################################################################################################
# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

####################################################################################################################