"""
1.	 Основы циклов.
a.	 Напишите цикл for, который выводит ASCII-коды всех символов в стро-
ке с  именем S. Для преобразования символов в  целочисленные ASCII-
коды используйте встроенную функцию ord(character). (Поэксперимен-
тируйте с  ней в  интерактивной оболочке, чтобы понять, как она рабо-
тает.)
b.	 Затем измените цикл так, чтобы он вычислял сумму кодов ASCII всех
символов в строке.
c.	 Наконец, измените свой программный код так, чтобы он возвращал но-
вый список, содержащий ASCII-коды всех символов в  строке. Дает ли
выражение map(ord, S) похожий результат?
"""

S = input('Введите строку для преобразования: ')
count = 0
codes = []
for ch in S:
    print('{} -> {}'.format(ch, ord(ch)))  # task a.
    count += ord(ch)                       # task b.
    codes.append(ord(ch))                  # task c.
print('Сумма кодов ASCII всех символов в строке -> {}'.format(count))
print(codes)

for ch in map(ord, S):
    print(ch)
