# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

# my_str_1 = 'сихафазатрон'
# my_str_2 = 'ликвидность'
# my_result_1 = []
# my_result_2 = []
# for i in my_str_1:
#     if my_str_1.count(i) == 1:
#         my_result_1.append(i)
# for i in my_str_2:
#     if my_str_2.count(i) == 1:
#         my_result_2.append(i)
# my_result = set(my_result_1).intersection(set(my_result_2))
# print(my_result)

# my_str_1 = 'сихафазатрон'
# my_str_2 = 'ликвидность'
# my_result = []
#
# for i in my_str_1:
#     if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
#         my_result.append(i)
# print(my_result)

##################################################################################################


# def split_pairs(a):
#     my_str = a
#     if len(a) % 2:
#         my_str += '_'
#     my_result = []
#     for two_sumbol in range(len(my_str) // 2):
#         two_sumbol = two_sumbol * 2
#         my_result.append(my_str[two_sumbol: two_sumbol + 2])
#     return my_result
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(split_pairs('abcd')))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(split_pairs('abcd')) == ['ab', 'cd']
#     assert list(split_pairs('abc')) == ['ab', 'c_']
#     assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
#     assert list(split_pairs('a')) == ['a_']
#     assert list(split_pairs('')) == []
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
########################################################################################################################

# def correct_sentence(text: str) -> str: #делает первую букву заглавное и в конце добавляет точку если необходимо
#     text = text[0].upper() + text[1:]
#     if text[-1] != '.':
#         text = text + '.'
#     return text
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(correct_sentence("greetings, friends"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert correct_sentence("greetings, friends") == "Greetings, friends."
#     assert correct_sentence("Greetings, friends") == "Greetings, friends."
#     assert correct_sentence("Greetings, friends.") == "Greetings, friends."
#     assert correct_sentence("hi") == "Hi."
#     assert correct_sentence("welcome to New York") == "Welcome to New York."
#
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
# Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой
########################################################################################################################

# def is_even(num: int) -> bool: #Проверить является ли число четным или нет.
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_even(2))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_even(2) == True
#     assert is_even(5) == False
#     assert is_even(0) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#Проверить является ли число четным или нет. Ваша функция должна возвращать True если число четное, и False если число не четное.
########################################################################################################################

# def is_all_upper(text: str) -> bool: #Проверяет все ли символы в строке являются заглавными.
#     my_str = text.upper()
#     if my_str == text:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_all_upper('ALL UPPER'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_all_upper('ALL UPPER') == True
#     assert is_all_upper('all lower') == False
#     assert is_all_upper('mixed UPPER and lower') == False
#     assert is_all_upper('') == True
#     assert is_all_upper('     ') == True
#     assert is_all_upper('444') == True
#     assert is_all_upper('55 55 5') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#Проверить все ли символы в строке являются заглавными. Если строка пустая или в ней нет букв - функция должна вернуть True.
########################################################################################################################

# def beginning_zeros(number: str):
#     len_str = len(number)
#     len_str_strip = len(number.lstrip('0'))
#     return len_str - len_str_strip
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(beginning_zeros('100'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert beginning_zeros('100') == 0
#     assert beginning_zeros('001') == 2
#     assert beginning_zeros('100100') == 0
#     assert beginning_zeros('001001') == 2
#     assert beginning_zeros('012345679') == 1
#     assert beginning_zeros('0000') == 4
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.
########################################################################################################################
#
# def nearest_value(values: set, one: int) -> int:
#     return min(values, key=lambda n: (abs(one - n), n))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
#
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
#     assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
#     assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
#     assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
#     assert nearest_value({-1, 2, 3}, 0) == -1
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#Найдите ближайшее значение к переданному.
#Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
#Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9.
#Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.
#Несколько уточнений:
#Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
#Ряд чисел всегда не пустой, т.е. размер >= 1;
#Переданное значение может быть в этом ряде, а значит оно и является ответом;
#В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
#Ряд не отсортирован и состоит из уникальных чисел.