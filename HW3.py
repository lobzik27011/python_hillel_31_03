# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
value = int(99)
new_value = value / 2 if value < 100 else - value
print(new_value)
####################################################################################################################

# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0
value = int(99)
new_value = 1 if value < 100 else 0
print(new_value)
####################################################################################################################

# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False
value = int(111)
new_value = True if value < 100 else False
print(new_value)
####################################################################################################################

# 4) У вас есть переменная my_str, тип - str. Напечатать все символы, стоящие на четных местах (начиная с нуля).
my_str = 'Привет. Меня зовут Дмитрий'
print(my_str[::2])
####################################################################################################################

# 5) У вас есть переменная my_str, тип - str. Напечатать все символы, стоящие не четных местах (начиная с нуля).
my_str = 'Привет. Меня зовут Дмитрий'
print(my_str[1::2])
####################################################################################################################

# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
my_str = 'qwer'
my_str = my_str * 2 if len(my_str) < 5 else my_str
print(my_str)
####################################################################################################################

# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
my_str = 'qwer'
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)
####################################################################################################################