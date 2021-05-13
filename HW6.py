# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = ['hello', 'python', 'qwerty', 'lesson', 'cola', 'fanta']
my_result = []
for i in range(len(my_list)):
    if i % 2 == 0:
        my_result.append(my_list[i])
    else:
        my_result.append(my_list[i][::-1])
print(my_result)
##################################################################################################

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['hello', 'apple', 'abc', 'lesson', 'cola', 'fanta', 'amazon']
my_result = []
for i in my_list:
    if i[0] == 'a':
        my_result.append(i)
print(my_result)
##################################################################################################

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['hello', 'apple', 'abc', 'lesson', 'cola', 'fanta', 'amazon']
my_result = []

for i in my_list:
    if i.find('a') != -1:
        my_result.append(i)
print(my_result)
##################################################################################################
# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['hello', 114, 'apple', 'abc', 'lesson', 111, 777, 23]
my_result = []
for i in my_list:
    if type(i) == str:
        my_result.append(i)
print(my_result)
##################################################################################################

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = 'Я люблю кушать бургеры =)))'
my_result = []
for i in my_str:
    if my_str.count(i) == 1:
        my_result.append(i)
print(my_result)

##################################################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = 'Я люблю кушать бургеры =)))'
my_str_2 = 'Как же я хочу в отпуск'
my_result = set(my_str).intersection(set(my_str_2))
print(list(my_result))


##################################################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = 'сихафазатрон'
my_str_2 = 'ликвидность'
my_chars = set(my_str_1).intersection(set(my_str_2))
my_result = []

for i in my_chars:
    if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
        my_result.append(i)
print(my_result)


# my_str_1 = 'сихафазатрон'
# my_str_2 = 'ликвидность'
# my_result = []
#
# for i in my_str_1:
#     if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
#         my_result.append(i)
# print(my_result)

##################################################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
person = {"Фамилия": "Курносов",
          "Имя": "Арнольд",
          "Возраст": 25,
          "Проживание": {"Страна": "Германия",
                         "Город": "Цюрих",
                         "Улица": "Васнецова"},
          "Работа": {"Наличие": "Есть",
                     "Должность": "Босс"}}

##################################################################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
recipe= {"Составляющие": {"Коржи": {"Мука": "1400 грамм",
                                    "Молоко": "",
                                    "Масло": "",
                                    "Яйцо": ""},
                          "Крем": {"Сахар": "",
                                   "Масло": "",
                                   "Ваниль": "",
                                   "Сметана": ""},
                          "Глазурь": {"Какао": "",
                                      "Сахар": "",
                                      "Масло": ""}}}

##################################################################################################