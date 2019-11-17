try:
    user_input = input('Введите  выражение в польской нотации через пробелы:')
    assert user_input[0] == '+' or user_input[0] == '-' or user_input[0] == '*' or user_input[0] == '/','Используем только +-*/'
except AssertionError:
    print('Используем только +-*/ и не забываем ставить пробел')

input_list = user_input.split(' ')
print(input_list)
sign = input_list[0]
try:
    first_number = int(input_list[1])
    second_number = int(input_list[2])
except IndexError:
    print('Не введены все условия!')
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
        print('Не забываем ставить пробел')
except ZeroDivisionError:
    print('На ноль делить нельзя!')