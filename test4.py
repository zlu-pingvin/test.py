# i = 2
# while i < 10:
#     print('Привет')
#     i += 3

# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     # num = int(input())

# i = 0
# while i < 101:
#     print(i)
#     i += 1

# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)

# i = 0  # Пример бесконечного цикла
# total = 0
# while i < 10:
#     total += i
#     print(total)

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)  # 21

# n = input()  # До КОНЦА 1
# while n != 'КОНЕЦ':
#     print(n)
#     n = input()

# n = input()  # До КОНЦА 2
# while 'конец' != n != 'КОНЕЦ':
#     print(n)
#     n = input()

# n = input()  # До КОНЦА 2
# while n != 'КОНЕЦ' and n != 'конец':
#     print(n)
#     n = input()

# n = input()  # Количество членов
# summ = 0
# while n != 'стоп' and n != 'хватит' and n != 'достаточно':
#     summ += 1
#     n = input()
# print(summ)

# n = int(input())  # Пока делимся
# while n % 7 == 0:
#     print(n)
#     n = int(input())

# n = int(input())  # Сумма чисел
# summ = 0
# while n > -1:
#     summ += n
#     n = int(input())
# print(summ)

# n = int(input())  # Количество пятерок
# summ = 0
# while n > 0 and n < 6:
#     if n == 5:
#         summ += 1
#     n = int(input())
# print(summ)

# n = int(input())  # Ведьмаку заплатите чеканной монетой
# n1 = n
# q = 25
# w = 10
# e = 5
# r = 1
# summ = 0
# while n1 > 0:
#     while n1 >= q:
#         summ += 1
#         n1 = n1 - q
#     while n1 >= w:
#         summ += 1
#         n1 = n1 - w
#     while n1 >= e:
#         summ += 1
#         n1 = n1 - e
#     while n1 >= r:
#         summ += 1
#         n1 = n1 - r
# print(summ)

# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n // 10  # удалить последнюю цифру из числа
# print(last_digit)
# print(n)
# num = int(input())
# has_seven = False  # сигнальная метка

# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# n = int(input())  # Обратный порядок 1
# while n != 0:
#     m = n % 10
#     print(m)
#     n = n // 10

# n = int(input())  # Обратный порядок 2
# while n != 0:
#     m = n % 10
#     print(m, end='')
#     n = n // 10

# n = int(input())  # max и min
# m = str(n)
# print('Максимальная цифра равна', max(m))
# print('Минимальная цифра равна', min(m))

# n = int(input())  # Все вместе
# summ = 0
# count = 0
# mult = 1
# o = n % 10
# while n != 0:
#     z = n * 10 // 10
#     m = n % 10
#     c = z + m
#     summ += m
#     count += 1
#     n = n // 10
#     i = summ / count
#     mult *= m
# c = z + o
# print(summ, count, mult, i, z, c, sep='\n')

# n = int(input())  # Вторая цифра
# while n > 9:
#     z = n % 10
#     n = n // 10
# print(z)

# n = int(input())  # Одинаковые цифры
# count = 0
# z = n % 10
# while n != 0:
#     m = n % 10
#     if m != z:
#         count += 1
#     n = n // 10
# if count == 0:
#     print('YES')
# else:
#     print('NO')

# n = int(input())  # Упорядоченные цифры 🌶️
# flag = True
# q = n % 10
# while n != 0:
#     m = n % 10
#     n = n // 10
#     if q > m:
#         flag = False
#     q = m
# if flag == True:
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         break               # останавливаем цикл если встретили делитель числа
# if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10
# if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')

# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# n = int(input())  # Наименьший делитель не правильно
# while n != 0:
#     if n % 2 == 0:
#         print(2)
#         break
#     elif n % 3 == 0:
#         print(3)
#         break
#     elif n % 5 == 0:
#         print(5)
#         break
#     else:
#         print(n)
#         break

# n = int(input())  # Наименьший делитель
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break

# n = int(input())  # Следуй правилам
# for i in range (1, n + 1):
#     if i > 4 and i < 10:
#         continue
#     if i > 16 and i < 38:
#         continue
#     if i > 77 and i < 88:
#         continue
#     print(i)

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Цикл завершен.')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
#     if n == 2:
#         break
# else:
#     print('Цикл завершен.')

# n = int(input())
# while n != 0:
#     last = n % 10
#     if last == 7:
#         print('Число', n, 'содержит цифру 7')
#         break
#     n //= 10
# else:
#     print('Число', n, 'не содержит цифру 7')

# count = 0  # Ревью кода-1 🌶️🌶️
# p = 1  # 0 --> 1
# for i in range(1, 11):  # 10 --> 11
#     x = int(input())
#     if x >= 0:  # > --> >=
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)  # x --> count
#     print(p)
# else:
#     print('NO')

# mx = -10 ** 6  # 0 --> -10 **  # Ревью кода-2 🌶️🌶️
# s = 0
# for i in range(1, 11):  # 11 --> 1, 11
#     x = int(input())
#     if x < 0:
#         s += x  # = --> +=
#         if x > mx:  # --> відступи
#             mx = x
# if s == 0:
#     print('NO')
# else:
#     print(s)
#     print(mx)

# s = 0  # 1 --> 0  # Ревью кода-3
# for i in range(1, 8):  # 7 --> 8
#     n = int(input())  # int
#     if n % 2 == 0:  # i --> n
#         s += n
# if s == 0:  # --> if...
#     print(0)
# else:
#     print(s)

# n = int(input())  # Ревью кода-4 🌶️🌶️
# max_digit = -1  # n % 10 --> -1
# count = 0 # count
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:  # < --> >
#             max_digit = digit   # digit = max_digit --> max_digit = digit
#         count += 1
#     n = n // 10  # --> //
# if count < 1:  # count < 1
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())  # Ревью кода-5 🌶️
# while n != 0:
#     m = n % 10
#     n = n // 10
# print(m)

# n = int(input())  # --> int # Ревью кода-6
# product = 1  # n % 10 --> 1
# while n > 0:  # >= 10 --> 0
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# for mu in range(11):
#     for lazio in range(6):
#         for barca in range(23):
#             print(mu, lazio, barca)

# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()

# for i in range(8):  # !!!!!!!!!!!!!!!
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# from time import *
# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds, end='')
#         sleep(1)
#         print(end='\r')

# from time import *
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds, end='')
#             sleep(1)
#             print(end='\r')

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())  # Таблица-1
# for i in range(n):
#     for i in range(3):
#         continue
#     print(n, n, n, sep=' ')

# n = int(input())  # Ще варіант
# for i in range(n):
#     for j in range(3):
#         print(n, end=" ")
#     print()

# n = int(input())  # Таблица-2
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())  # Таблица-3
# for i in range(1, n +1):
#     for j in range(1, 10):
#         print(i,'+', j, '=', (i + j))
#     print()

# n = int(input())  # Звездный треугольник 🌶️🌶️
# for i in range(1, n // 2 + 2):
#     print('*' * i)
# for i in range(n // 2, 0, - 1):
#     print('*' * i)

# n = int(input())
# for i in range(1):
#     for j in range(n // 2 + 1):
#         print("*" * (j + 1))
#     for k in range(n // 2):
#         print("*" * (n // 2 - k))

# n = int(input())  # Численный треугольник 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end='')
#     print()

# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)

# total = 0
# for x in range(1, 100):
#     for y in range(1, 100):
#         for z in range(1, 100):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)


# for n in range(1, 32):
#     for k in range(1, 32):
#         for m in range(1, 32):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print(n, k, m)

# for b in range(101):
#     for k in range(101):
#         for t in range(101):
#             if b * 10 + k * 5 + t * 0.5 == 100 and b + k + t == 100:
#                 print(b, k, t)

# for a in range(1, 151):
#     for b in range(a + 1, 151):
#         for c in range(b + 1, 151):
#             for d in range(c + 1, 151):
#                 # for e in range(1, 151):
#                 e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5) ** 0.2)
#                 if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
#                     print(a + b + c + d + e)
#                     break
# print(a + b + c + d + e)
# print(e)

# for a in range(1, 151):  # Не сам
#     for b in range(a + 1, 151):
#         for c in range(b + 1, 151):
#             for d in range(c + 1, 151):
#                 e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
#                 if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
#                     print(a + b + c + d + e)

# n = int(input())  # Численный треугольник 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end='')
#     print()

# n = int(input())  # Численный треугольник 1
# total = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         total += 1
#         print(total)


# n = int(input())  # Численный треугольник 3
# total = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         total += 1
#         print(total, end = ' ')
#     print()

# n = int(input())  # Чисельній треугольник 4
# for i in range(1, n // 2 + 2):
#     print('*' * i)
# for i in range(n // 2, 0, - 1):
#     print('*' * i)

# n = int(input())  # Чисельній треугольник 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for k in range(i - 1, 0, -1):
#             print(k, end='')
#     print()

# a, b = int(input()), int(input())  # Делители-1 🌶️
# n = 0  # сума
# m = 0  # число з найбільшою сумою ділителів
# z = 0  # найбільша сума?
# for i in range(a, b + 1):
#     n = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             n += j
#         if n >= z:
#             m = i
#         if n > z:
#             z = n
# print(m, z)

# a, b = int(input()), int(input())  # Делители-1 🌶️
# n = 0  # сума
# m = 0  # число з найбільшою сумою ділителів
# z = 0  # найбільша сума?
# for i in range(a, b + 1):
#     n = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             n += j
#         if n >= z:
#             m = i
#             z = n
# print(m, z)

# n = int(input())  # Делители-2
# z = 0
# for i in range(1, n + 1):
#     z = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             z += 1
#     print(i, '+' * z, sep='')

# n = int(input())  # Цифровой корень
# summ = 0
# z = 0
# m = 0
# for i in range(1, n + 1):
#     while n > 0:
#         m = n % 10
#         summ += m
#         n = n // 10
#     for j in range(1, summ + 1):
#         while summ > 0:
#             m = summ % 10
#             z += m
#             summ = summ // 10
# print(z)

# n = int(input())  # Цифровой корень
# summ = 0
# z = 0
# m = 0
# c = 0
# while n != 0:
#     m = n % 10
#     summ += m
#     n = n // 10
#     while summ != 0:
#         m = summ % 10
#         z += m
#         summ = summ // 10
# print(z)

# n = int(input())  # Цифровой корень
# summ = 0
# z = 0
# m = 0
# c = 0
# x = 0
# while n != 0:
#     m = n % 10
#     summ += m
#     n = n // 10
# while summ != 0:
#     c = summ % 10
#     z += c
#     summ = summ // 10
# print(z)

# n = int(input())  # Цифровой корень
# while n > 9:
#     z = 0
#     while n != 0:
#         c = n % 10
#         z += c
#         n = n // 10
#     n = z
# print(n)

# n = int(input())  # Сумма факториалов
# f = 1
# summ = 0
# for i in range(1, n + 1):
#     f *= i
#     summ += f
# print(summ)

# n = int(input())  # Сумма факториалов модуль
# c = 0
# x = 0
# from math import factorial
# for i in range(n, 0, -1):
#     c = factorial(i)
#     x += c
#     # print(i)
#     print(c)
#         # for j in range(1, n + 1):
#         #     x += c
# z = factorial(n)
# print(z)
# print(x)
# print(c)

# n = int(input())  # Сумма факториалов дубль 2
# f = 1
# summ = 0
# c = 0
# for i in range(1, n + 1):
#     f *= i
#     for j in range(1, n + 1):
#         summ = f
#     c += f
# print(c)

# from math import factorial
# n, total = int(input()), 0
# for i in range(1, n + 1):
#     total += factorial(i)
# print(total)

# a, b = int(input()), int(input())  # Простые числа
# for i in range(a, b + 1):
#     # print(i)
#     for j in range(a, i + 1):
#         if i % j == 0:
#             print(j)
#             # print(i)

# a, b = int(input()), int(input())  # Простые числа
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)

# n = int(input())
# for i in range(1, 9):
#     q = (4 / (n + 2))
# print(q)


# s = 0.0  # 8 членов ряда Лейбница
# for i in range(1, 17, 2):
#     s = 4.0 / i - s
# print(abs(s))

# n = int(input())  # Ревью кода — 7 🌶️
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)

# n = 8  # Ревью кода - 8 🌶️
# count = 0
# maximum = -10 ** 6
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = 4  # Ревью кода - 9
# count = 0
# maximum = 0
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())  # Звездная рамка
# print('*' * 19)
# for i in range(1, n - 1):
#     print('*                 *')
# print('*' * 19)

# n = int(input()) # Третья цифра
# while n > 1000:
#     n //= 10
# print(n % 10)

# n = int(input()) # Все вместе 2
# count3 = 0
# last_number = n % 10
# last_digit = 0
# count_chet = 0
# summ5 = 0
# eight = 1
# count_zerofive = 0
# while n > 0:
#     x = n % 10
#     if x == 3:
#         count3 += 1
#     if x % 2 == 0:
#         count_chet += 1
#     if x > 5:
#         summ5 += x
#     if x > 7:
#         eight *= x
#     if x == 0 or x == 5:
#         count_zerofive += 1
#     if x == last_number:
#         last_digit += 1
#     n //= 10
# print(count3)
# print(last_digit)
# print(count_chet)
# print(summ5)
# print(eight)
# print(count_zerofive)

# for a in range(1, 34):  # Числа Рамануджана 🌶️
#     for b in range(1, 34):
#         for c in range(1, 34):
#             for d in range(1, 34):
#                 if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and a != c and a != d and b != c and b != d and c != d:
#                     (print(a ** 3 + b ** 3))


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
# print(d)

# x = int(input())
# y = (7 * x ** 2) - (3 * x) + 6
# print(y)

# n = int(input())
# print(n * 4)

# a, b, c = int(input()), int(input()), int(input())
# x = (b + (1 / a)) / (2 / c)
# print(x)


# a, b, c = int(input()), int(input()), int(input())
# d = b ** 2 - (4 * a * c)
# print(d)
















