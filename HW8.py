# Для задания 1-7 за основу можете взять код из ДЗ № 7.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ['hello', 'python', 'qwerty', 'lesson', 'cola', 'fanta']


def my_sort(in_list):
    my_result = []
    for i in range(len(in_list)):
        if i % 2 == 0:
            my_result.append(in_list[i])
        else:
            my_result.append(in_list[i][::-1])
    return my_result

print(my_sort(my_list))
##################################################################################################

# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

my_list = ['hello', 'apple', 'abc', 'lesson', 'cola', 'fanta', 'amazon']

def my_sort(in_list):
    my_result = []
    for i in in_list:
        if i[0] == 'a':
            my_result.append(i)
    return my_result

print(my_sort(my_list))
##################################################################################################

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['hello', 'apple', 'abc', 'lesson', 'cola', 'fanta', 'amazon']


def my_sort(in_list):
    my_result = []
    for i in in_list:
        if i.find('a') != -1:
            my_result.append(i)
    return my_result
print(my_sort(my_list))
##################################################################################################

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

my_list = ['hello', 114, 'apple', 'abc', 'lesson', 111, 777, 23]


def my_sort(in_list):
    my_result = []
    for i in in_list:
        if type(i) == str:
            my_result.append(i)
    return my_result


print(my_sort(my_list))
##################################################################################################

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

my_str = 'Я люблю кушать бургеры =)))'


def my_sort(in_str):
    my_result = []
    for i in in_str:
        if in_str.count(i) == 1:
            my_result.append(i)
    return my_result

print(my_sort(my_str))
##################################################################################################


# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = 'Я люблю кушать бургеры =)))'
my_str_2 = 'Как же я хочу в отпуск'


def my_sort(in_str_1, in_str_2):
    my_result = list(set(in_str_1).intersection(set(in_str_2)))
    return my_result


print(my_sort(my_str, my_str_2))
##################################################################################################

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = 'сихафазатрон'
my_str_2 = 'ликвидность'


def my_sort(in_str_1, in_str_2):
    my_result = []
    my_chars = set(in_str_1).intersection(set(in_str_2))

    for i in my_chars:
        if in_str_1.count(i) == 1 and in_str_2.count(i) == 1:
            my_result.append(i)
    return my_result


print(my_sort(my_str_1, my_str_2))
##################################################################################################


# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
import random
import string


names = ["john", "dimitry", "jack"]
domains = ["ru", "pl", "tx"]

def create_email(u_name, u_domains):
    random_str = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(5, 7)))
    my_result = random.choice(u_name) + '.' + str(random.randint(100, 500)) + '@' + random_str.lower() + '.' + random.choice(u_domains)
    return my_result

print(create_email(names, domains))
