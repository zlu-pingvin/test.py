# n1, n2 = float(input()), float('32')
# print(n1 + n2)

# n1, n2 = float(input()), float(input())  # Площадь треугольника
# s = (1 / 2) * n1 * n2
# print(s)

# s, n1, n2 = float(input()), float(input()), float(input())  # Две старушки
# a = s / (n1 + n2)
# print(a)

# n1 = float(input())  # Обратное число
# if n1 == 0:
#     print('Обратного числа не существует')
# else:
#     print (n1 ** -1)

# f = float(input())  # 451 градус по Фаренгейту
# c = (5 / 9) * (f - 32)
# print(c)

# n1 = int(input())  # Dog age
# if n1 == 1:
#     print(10.5)
# elif n1 == 2:
#     print(21)
# elif n1 > 2:
#     print(21 + ((n1 - 2) * 4))

# n = float(input())  # Первая цифра после точки
# n1 = n * 10
# n2 = int(n1)
# n3 = n2 % 10
# print(n3)

# n = float(input())
# n2 = n % 1
# print(n2 % 10)

# n = float(input())
# n1 = int(n)
# print(n, n1, n - n1)

# a = max(3, 8, -3, 12, 9)
# b = min(3, 8, -3, 12, 9)
# c = max(3.14, 2.17, 9.8)
# print(a)
# print(b)
# print(c)

# n1, n2, n3, n4, n5 = int(input()), int(input()), int(input()), int (input()), int(input())
# print('Наименьшее число =', min(n1, n2, n3, n4, n5))
# print('Наибольшее число =', max(n1, n2, n3, n4, n5))


# a1 = int(input())  # Интересное число
# n1 = a1 // 100
# n2 = a1 // 10 % 10
# n3 = a1 % 10
# if max(n1, n2, n3) - min(n1, n2, n3) == (n1 + n2 + n3) - max(n1, n2, n3) - min(n1, n2, n3):
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# n1, n2, n3, n4, n5 = float(input()), float(input()), float(input()), float(input()), float(input())
# print(abs(n1) + abs(n2) + abs(n3) + abs(n4) + abs(n5))  #Абсолютная сумма

# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# n = (abs(p1 - q1)) + (abs(p2 - q2))  # Манхэттенское расстояние
# print(n)

# import math
#
# num1 = math.sqrt(2)     # вычисление корня квадратного из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)

# from math import *
#
# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)

# from math import sqrt, ceil
#
# print(sqrt(25))
# print(ceil(34.7))

#print(floor(12.8))  # приведет к ошибке, так как функция floor не подключена

# from math import *  # Евклидово расстояние
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# print(p)

# from math import pi  # Площадь и длина
# r = float(input())
# s = pi * (r ** 2)
# c = 2 * pi * r
# print(s, c, sep='\n')

# from math import sqrt  # Средние значения
# a, b = float(input()), float(input())
# q = (a + b) / 2
# w = sqrt(a * b)
# e = (2 * a * b) / (a + b)
# r = sqrt((a ** 2 + b ** 2) / 2)
# print(q, w, e, r, sep='\n')

# from math import radians, pi, sin, cos, tan  # Тригонометрическое выражение
# x = float(input())
# n = (sin(radians(x)) + cos(radians(x)) + tan(radians(x)) ** 2)
# # r = radians(n)
# print(n)

# from math import ceil, floor  # Пол и потолок
# n = float(input())
# print(ceil(n) + floor(n))

# from math import sqrt  # Квадратное уравнение
# a, b, c = float(input()), float(input()), float(input())
# d = b ** 2 - 4 * (a * c)
# if d > 0:
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     print(min(x2, x1), max(x2, x1), sep='\n')
# elif d < 0:
#     print('Нет корней')
# else:
#     print(-b / (2 * a))

# from math import pi, tan  # Правильный многоугольник
# n = int(input())
# a = float(input())
# print((n * a ** 2) / (4 * tan(pi / n)))

# n = 'sd,fsdlfnsdlkfnsdflsdfsdkf;lsdkfsdfsdf'
# q = len(n)
# w = len('sdfsdfds sdfgg zdsd ывпвчваврчячм ')
# print(q)
# print(w)

# print('"Python is a great language!", said Fred. ' + '"I don' + "'t ever remember " + 'having this much fun before."')
# print('don\'t')  # экранирование

# n1, n2 = input(), input()  # What's Your Name?
# print('Hello ' + n1 + ' '+ n2 + '! You just delved into Python')

# n = str(input())  # Футбольная команда
# print('Футбольная команда ' + n + ' имеет длину ' + str(len(n)) + ' символов')

# n1 = input()
# n2 = len(n1)
# print('Футбольная команда ' + n1 + ' имеет длину ' + str(n2) + ' символов')


# n1, n2, n3 = input(), input(), input()  # Три города
# if len(n1) < len(n2) < len(n3):
#     print(n1, n3, sep='\n')
# elif len(n1) < len(n3) < len(n2):
#     print(n1, n2, sep='\n')
# elif len(n2) < len(n1) < len(n3):
#     print(n2, n3, sep='\n')
# elif len(n2) < len(n3) < len(n1):
#     print(n2, n1, sep='\n')
# elif len(n3) < len(n2) < len(n1):
#     print(n3, n1, sep='\n')
# elif len(n3) < len(n1) < len(n2):
#     print(n3, n2, sep='\n')

# n1, n2, n3 = len(input()), len(input()), len(input())  # Арифметические строки
# q3 = max(n1, n2, n3)
# q1 = min(n1, n2, n3)
# q2 = (n1 + n2 + n3) - (q1 + q3)
# if q2 - q1 == q3 - q2:
#     print('YES')
# else:
#     print('NO')

# s = input()
# if 'a' in s:
#     print('Введенная строка содержит символ а')
# else:
#     print('Введенная строка не содержит символ а')

# n = input()  # Цвет настроения синий
# if 'синий' in n:
#     print('YES')
# else:
#     print('NO')

# n = input()  # Отдыхаем ли?
# if 'суббота' in n or 'воскресенье' in n:
#     print('YES')
# else:
#     print('NO')

# n = input()  # Корректный email
# if '@' in n and '.' in n:
#     print('YES')
# else:
#     print('NO')

# for i in range(10):  # Привет 10 hfp
#     print('Привет')

# for ne in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# print('A')
# print('B')
# for i in range(5):
#     print('C')
# for i in range(5):
#     print('D')
# print('E')

# for i in range(10):
#     print('Python is awesome!')

# n1, n2 = input(), int(input())  # Повторяй за мной 1
# for i in range(n2):
#     print(n1)

# for i in range(6):  # Последовательность символов
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# n = int(input())  # Звездный прямоугольник
# for i in range(n):
#     print('*' * 19)

# for qwerty in range(5):
#     print(qwerty +12, ' O_o')

# for number in range(5):
#     print(number + 1)

# for _ in range(5):
#     print('Python - awesome!')

# n = input()  # Повторяй за мной 2
# for _ in range(10):
#     print(_, n)

# n = int(input())  # Квадрат числа
# for i in range(n + 1):
#     print('Квадрат числа', i, 'равен', (i ** 2))

# n = int(input())  # Звездный треугольник
# for i in range(n):
#     print((n - i) * '*')

# m, p, n = float(input()), float(input()), int(input())  # Популяция
# for i in range(n):
#     print(i + 1, m)
#     add_per_day = m * p / 100
#     m = m + add_per_day

# for i in range(10, 1000):  # перебираем числа от 100 до 999
#     if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
#         print(i)

# for i in range(56, 171, 2):
#     print(i)

# for i in range(15, -20, -3):
#     print(i, end=' ')
# print('Взлетаем!!!')

# n, m = int(input()), int(input())  # Последовательность чисел 1
# for i in range(n, m + 1):
#     print(i)

# n, m = int(input()), int(input())  # Последовательность чисел 2 🌶️
# if n < m:
#     for i in range(n, m + 1):
#         print(i)
# elif n > m:
#     for i in range(n, m -1, -1):
#         print(i)
# else:
#     print(n)

# n, m = int(input()), int(input())  # Последовательность чисел 3 🌶️
# for i in range (n, m - 1, -1):
#     if i % 2 != 0:
#         print(i)

# n, m = int(input()), int(input())  # Последовательность чисел 4
# if n == m:
#     print(n)
# else:
#     for i in range(n, m + 1):
#         if i % 17 == 0 or i % 10 == 9 or (i % 5 == 0 and i % 3 == 0):
#             print(i)

# n = int(input())  # Таблица умножения
# for i in range(1, 11):
#     m = n * i
#     print(n, 'x', i, '=', m)

# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# counter1 = 0
# counter2 = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(counter)

# total = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
# print('Сумма чисел больших 10 равна',  total)

# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)

# total = 0
# for i in range(10):
#     num = int(input())
#     total = total + num
# average = total / 10
# print('Среднее значение равно', average)

# temp = x  # Обмен значений переменных
# x = y
# y = temp
#
# x, y = y, x

# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
# if num != 1 and flag == True:  # Сигнальные метки
#     print('Число простое')
# else:
#     print('Число составное')

# largest = -1  # Максимум и минимум
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)

# total = 0  # друкує кожну ітерацію
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# a, b = int(input()), int(input())
# total = 0
# for i in range(a, b + 1):
#     if ((i ** 3) % 10) == 4 or ((i ** 3) % 10) == 9:
#         total += 1
# print(total)

# n = int(input())  # Сумма чисел
# summ = 0
# for i in range(n):
#     m = int(input())
#     summ += m
# print(summ)

# from math import log  # Асимптотическое приближение
# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     m = 1 / i
#     counter += m
# z = counter - log(n)
# print(z)

# n = int(input())  # ДЕБАГ Сумма чисел https://stepik.org/lesson/294243/step/6?unit=275922
# total = 0
# for i in range(n):
#     m = int(input())
#     total += i
# print(total - n)

# n = int(input())  № правильно
# summ = 0
# for i in range(n):
#     m = int(input())
#     summ += m
# print(summ)

# n = int(input())  # Сумма чисел не зовсім правильно, можна було or і треба було range(1, n + 1)
# summ = 0
# for i in range(n + 1):
#     if i ** 2 % 10 == 2:
#         summ += i
#     if i ** 2 % 10 == 5:
#         summ += i
#     if i ** 2 % 10 == 8:
#         summ += i
# print(summ)

# n = int(input())  # Факториал
# summ = 1
# for i in range(1, n +1):
#     summ *= i
# print(summ)

# total = 1  # Без нулей
# for i in range(1, 11):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)

# n = int(input())  # Сумма делителей
# summ = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         summ += n / i
# print(int(summ))

# n = int(input())  # Сумма делителей
# summ = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         summ += i
# print(int(summ))

# n = int(input())  # Знакочередующаяся сумма
# summ = 1
# for i in range(2, n + 1):
#     if i % 2 == 0:
#         summ -= i
#     else:
#         summ += i
# print(summ)

# n = int(input())  # Наибольшие числа 🌶️🌶️ з підказками(
# premaxi = 0
# maxi = 1
# for i in range(1, n + 1):
#     m = int(input())
#     if m > premaxi and m < maxi:
#         premaxi = m
#         # maxi = m
#     elif m > maxi:
#         premaxi = maxi
#         maxi = m
# print(maxi, premaxi, sep='\n')

# summ = 0
# for i in range(10):  # Only even numbers 🌶️
#     n = int(input())
#     if n % 2 == 0:
#         summ += 1
# if summ == 10:
#     print('YES')
# else:
#     print('NO')

# flag = 'YES'  # Only even numbers 🌶️ №2
# for i in range(10):
#     n = int(input())
#     if n % 2 != 0:
#         flag = 'NO'
# print(flag)

# n = int(input())  # Последовательность Фибоначчи 🌶️
# f1 = 0
# f2 = 1
# if n == 1:
#     print(1)
# for i in range(1, n):
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
#     if i < 2:
#         print(1, end=' ')
#     print(f3, end=' ')
