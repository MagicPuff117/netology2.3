try:
    user_input = input('Введите  выражение в польской нотации через пробелы:')
    assert user_input[0] in ('+', '-', '*', '/'), 'Используем только +-*/'
except AssertionError:
    print('Используем только +-*/ и не забываем ставить пробел')

input_list = user_input.split(' ')
# print(input_list)
sign = input_list[0]
try:
    first_number = int(input_list[1])
    second_number = int(input_list[2])
except IndexError:
    print('Не введены все условия!')
except ValueError:
    print('Условия должны быть в ввиде числа.')

try:
    if sign == '+':
        print(first_number + second_number)
    elif sign == '-':
        print(first_number - second_number)
    elif sign == '*':
         print(first_number * second_number)
    elif sign == '/':
         print(first_number // second_number)
    else:
        class MyException(Exception):
            print('Не забываем ставить пробелы!')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except NameError:
    print('Условия должны быть в ввиде числа.')