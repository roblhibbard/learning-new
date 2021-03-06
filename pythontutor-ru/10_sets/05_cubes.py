"""
http://pythontutor.ru/lessons/sets/problems/cubes/
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету.
Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
Для этого они занумеровали все цвета случайными числами от 0 до 108. Н
а этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.

В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори.
В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.

Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков,
которые есть только у Ани и номера цветов кубиков, которые есть только у Бори.
Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.
"""

n, m = [int(i) for i in input().split()]

_anna = set()
for i in range(n):
    _anna.add(int(input()))

_boris = set()
for i in range(m):
    _boris.add(int(input()))

both = _anna.intersection(_boris)
anna = _anna.difference(_boris)
boris = _boris.difference(_anna)

print(len(both))
print(' '.join([str(i) for i in sorted(both)]))
print(len(anna))
print(' '.join([str(i) for i in sorted(anna)]))
print(len(boris))
print(' '.join([str(i) for i in sorted(boris)]))
