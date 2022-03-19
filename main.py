def calculator():
    n1 = int(input('Введите первое число: '))
    operator = input('Введите оператора: ')
    n2 = int(input('Введите второе число: '))

    if operator == '+':
        print(n1 + n2)
    elif operator == '-':
        print(n1 - n2)
    elif operator == '*':
        print(n1 * n2)
    elif operator == '/':
        print(n1 / n2)
    else:
        print('Вы ввели недопустимое значение!')