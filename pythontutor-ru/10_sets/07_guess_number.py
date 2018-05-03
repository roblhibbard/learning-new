"""
http://pythontutor.ru/lessons/sets/problems/guess_number/
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае.
После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и
просит вас помочь ей определить, какие числа мог задумать Август.

В первой строке задано n - максимальное число, которое мог загадать Август.
Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.

Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
"""

n = int(input())
question = input()
possible = set(range(1, n + 1))

while question != 'HELP':
    question = set([int(el) for el in question.split()])
    answer = input()

    if answer == 'YES':
        possible.intersection_update(question)
    else:
        possible.difference_update(question)

    question = input()

print(' '.join([str(el) for el in sorted(possible)]))