number = str(input('Введите положительное целое число:'))
list_number = list(number)
list_number = map(int, list_number)
print('Сумма чисел равна:', sum(list_number))
