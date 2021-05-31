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

def is_all_upper(text: str) -> bool: #Проверяет все ли символы в строке являются заглавными.

    return True

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
#Проверить все ли символы в строке являются заглавными. Если строка пустая или в ней нет букв - функция должна вернуть True.