def reverse_number(index: int, new_number:list)->list:
    """Эта функция возвращает число в обратном порядке с попощью рекурсии."""
    new_number += number[index]
    if len(new_number) < len(number):
        reverse_number(index - 1, new_number)
    return new_number


number = list(str(int(input('Ввод числа:'))))
index = -1
new_number = []
print('Перевёрнутое число:',''.join(map(str, reverse_number(index, new_number))))