﻿""" 1. Ожидаются два целых числа """
a = int(input("Введите первое слагаемое: "))
b = int(input("Введите второе слагаемое: "))
s = a + b
print("Результат: ", s)
print("Рез" , s, sep=': ')  # вывод с разделителем 

""" 2. Ожидаются два вещественных числа """
n1 = input("Enter the first number:  ")
n2 = input("Enter the second number: ")
n3 = int(n1) + float(n2)
n4 = int(n3)
print("S = ", n3, " или ", n4)

"""
Подумайте, есть ли разница когда проводить преобразование вводимого типа -
сразу при вводе, как в первом случае,
или непосредственно при выполнении операции, как во втором случае?
"""

"""
Проверьте, что будет,
если в первом случае ввести вместо целого числа - вещественное?
и если во втором случае вместо вещественного ввести целое?
"""
