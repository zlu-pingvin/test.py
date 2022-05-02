# answer = input('Какой язык программирования мы изучаем?')
# if answer == 'Python':
#     print('Верно! Мы ботаем Python =)')
#     print('Python - отличный язык!')

# answer = input('Какой язык программирования мы изучаем?')
# if answer == 'Python':
#     print('Верно! Мы ботаем Python =)')
#     print('Python - отличный язык!')
# else:
#     print('Не совсем так!')

# num1 = int(input())
# num2 = int(input())
# if num1 < num2:
#     print(num1, 'меньше чем', num2)
# if num1 > num2:
#     print(num1, 'больше чем', num2)
# if num1 == num2:                      # используем двойное равенство
#     print(num1, 'равно', num2)
# if num1 != num2:
#     print(num1, 'не равно', num2)


# word = input()
# if word == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# n1, n2 = int(input()), int(input())
# if n1 == n2:
#     print('DA')
# if n1 != n2:
#     print('NET')

# n0 = int(input())
# n1 = n0 % 10
# n2 = n0 //10
# print(n1, n2)
# if n1 == n2:
#     print('DA')
# if n1 != n2:
#     print('NET')

# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# i = int(input())
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')

# n1, n2 = str(input()), str(input())  # Можна просто input() без str
# if n1 == n2:
#     print('Пароль принят')
# if n1 != n2:
#     print('Пароль не принят')

# n1, n2 = input(), input()
# if n1 == n2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# print('Пароль принят' if input() == input() else 'Пароль не принят')  # Так гарніше

# print('Пароль','принят', sep = ' ' if input() == input() else ' не ')

# n = int(input())
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# n = int(input())
# n1 = n // 1000
# n2 = n // 100 % 10
# n3 = n // 10 % 10
# n4 = n % 10
# if (n1 + n4) == (n2 - n3):
#     print('ДА')
# else:
#     print('НЕТ')

# a,b,c,d = input()
# print('ДА' if int(a) + int(d) == int(b) - int(c) else 'НЕТ')  # OMG

# n = int(input())
# if n >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')


# a_n=a_1 + (n-1)d

# a1, n, d = int(input()), int(input()), int(input())  # не привильно
# an = a1 + (n-1) * d
# if an == d + 1 == n + 2 == a1 + 3:
#     print('YES')
# else:
#     print('NO')

# a1=1 n=2 d = 3
# an= 1+(2-1)*3 = 4

# a1=2 n=3 d = 4
# an= 2+(3-1)*4 =10

# Напишите программу, которая определяет,
# являются ли три заданных числа (в указанном порядке)
# последовательными членами арифметической прогрессии.
# а3 - а2 == а2 - а1
# n1, n2, n3 = int(input()), int(input()), int(input())
# if n3 - n2 == n2 - n1:
#     print('YES')
# else:
#     print('NO')

# n1, n2 = int(input()), int(input())
# if n1 > n2:
#     print(n2)
# if n2 > n1:
#     print(n1)

# n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())
# if n1 > n2:
#     n5 = n2
# else:
#     n5 = n1
# if n3 > n4:
#     n6 = n4
# else:
#     n6 = n3
# if n6 > n5:
#     print(n5)
# else:
#     print(n6)

# n1 = int(input())  № не правильно
# if n1 <= 13:
#     print('детство')
# if n1 >= 14 <= 24:
#     print('молодость')
# if n1 >= 25 <= 59:
#     print('зрелость')
# if n1 >= 60:
#     print('старость')

# n1 = int(input())  № не правильно
# if n1 <= 13:
#     print('детство')
# if n1 > 13 < 25:
#     print('молодость')
# if n1 > 25 < 59:
#     print('зрелость')
# if n1 >= 60:
#     print('старость')

# n1 = int(input())  # правильно
# if n1 <= 13:
#     print('детство')
# if 14 <= n1 <= 24:
#     print('молодость')
# if 25 <= n1 <= 59:
#     print('зрелость')
# if n1 >= 60:
#     print('старость')

# n1, n2, n3 = int(input()), int(input()), int(input())
# if n1 >= 0:
#     z1 = n1
# else:
#     z1 = 0
# if n2 >= 0:
#     z2 = n2
# else: z2 = 0
# if n3 >= 0:
#     z3 = n3
# else:
#     z3 = 0
# print(z1 + z2 + z3)

# a, b, c = int(input()), int(input()), int(input())
# print((a if a>0 else 0) + (b if b>0 else 0) + (c if c>0 else 0))  # ще можна писати так

# a, b, c = int(input()), int(input()), int(input())  # так теж гарніше, без зайвих перемінних
# if c < 0:
#     c = 0
# if b < 0:
#     b = 0
# if a < 0:
#     a = 0
# print(a + b + c)

# age = int(input('Сколько вам лет?: '))
# grade = int(input('В каком классе вы учитесь?: '))
# if age >= 12 and grade >= 7:
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')

# city = input('В каком городе вы живете?: ')
# if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')

# age = int(input('Сколько вам лет?: '))
# grade = int(input('В каком классе вы учитесь?: '))
# city = input('В каком городе вы живете?: ')
# if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')

# age = int(input('Сколько вам лет?: '))
# if not (age < 12):
#     print('Доступ разрешен.')
# else:
#     print('Доступ запрещен.')

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:  # 3 or 0
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)
# # p = 7 * 7 + 3 * 3 = 49 + 9

# n = int(input())
# if 100 <= n <= 999:
#     print("tri")
# else:
#     print('ne tri')

# n1 = int(input())
# z1 = n1 // 100
# z2 = n1 // 10 % 10
# z3 = n1 % 10
# if z1 != z2 and z2 != z3 and z1 != z3:
#     print(' razlich')
# else:
#     print(' ne razl')

# x, y = int(input()), int(input())
# if x >= 1 and y >= 1:
#     print('1 chv')
# if x <= -1 and y >= 1:
#     print('2 chv')
# if x <= -1 and y <= -1:
#     print('3 chv')
# if x >= 1 and y <= -1:
#     print('4chv')

# n = int(input())
# if -1 < n < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n = int(input())
# if n <= -3 or n >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n = int(input())
# if (-30 < n <= -2) or (7 < n <= 25):
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n = int(input())
# if (999 < n < 10000) and (n % 7 == 0 or n % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# n1, n2, n3 = int(input()), int(input()), int(input())
# if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1+ n2):
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# x1, y1, x2, y2, = int(input()), int(input()), int(input()), int(input())
# if ((x1 == x2) and (1 <= y1 <= 8 and 1 <= y2 <= 8)) or ((y1 == y2) and (1 <= x1 <= 8 and 1 <= x2 <= 8)):
#     print('YES')
# else:
#     print("NO")

# x1, y1, x2, y2, = int(input()), int(input()), int(input()), int(input())
# if (x1 == (x2 + 1) or x1 == (x2 - 1)) and (y1 == (y2 + 1) or y1 == (y2 - 1)):
#     print('YES')
# else:
#     print('NO') # ne pravulno

# x1, y1, x2, y2, = int(input()), int(input()), int(input()), int(input()) # hid korolya
# if ((x2 - x1 == 1) or (x2 - x1 == - 1) or (x2 - x1 == 0)) and ((y2 - y1 == 1) or (y2 - y1 == - 1) or (y2 - y1 == 0)):
#     print('YES')
# else:
#     print('NO')

# grade = int(input('Введите вашу отметку по 100-балльной системе: '))
# if grade >= 90:
#     print(5)
# else:
#     if grade >= 80:
#         print(4)
#     else:
#         if grade >= 70:
#             print(3)
#         else:
#             if grade >= 60:
#                 print(2)
#             else:
#                 print(1)

# grade = int(input('Введите вашу отметку: '))
#
# if grade >= 90:
#     print(5)
# elif grade >= 80:
#     print(4)
# elif grade >= 70:
#     print(3)
# elif grade >= 60:
#     print(2)
# else:
#     print(1)

# n1, n2, n3 = int(input()), int(input()), int(input())
# if n1 == n2 == n3:
#     print(3)
# elif n1 == n2 or n1 == n3:
#     print(2)
# elif n2 == n3:
#     print(2)
# else:
#     print(1)

# n, k = int(input()), int(input())
# if n > k:
#     print('NO')
# elif k > n:
#     print('YES')
# else:
#     print("Don't know")

# n1, n2, n3 = int(input()), int(input()), int(input())
# if n1 == n2 and n2 == n3 and n1 == n3:
#     print('Равносторонний')
# elif n1 == n2 or n1 == n3 or n2 == n3:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# n1, n2, n3 = int(input()), int(input()), int(input())
# if  n1 < n2 < n3:
#     print(n2)
# elif n2 < n1 < n3:
#     print(n1)
# elif n3 < n2 < n1:
#     print(n2)
# elif n2 < n3 < n1:
#     print(n2)
# elif n3 < n1 < n2:
#     print(n1)
# elif n1 < n3 < n2:
#     print(n3)

# n1 = int(input())
# if n1 == 2:
#     print('28')
# elif n1 == 4 or n1 == 6 or n1 == 9 or n1 == 11:
#     print('30')
# else:
#     print('31')

# n = int(input())
# if n < 60:
#     print('Легкий вес')
# elif n < 64:
#     print('Первый полусредний вес')
# elif n < 69:
#     print('Полусредний вес')

# n1, n2, n = int(input()), int(input()), str(input())
# if n2 == 0 and n == '/':
#     print('На ноль делить нельзя!')
# elif n == "*":
#     print(n1 * n2)
# elif n == '/':
#     print(n1 / n2)
# elif n == '+':
#     print(n1 + n2)
# elif n == '-':
#     print(n1 - n2)
# else:
#     print('Неверная операция')

# n1, n2 = input(), input()
# if n1 == 'красный' and n2 == 'синий':
#     print('фиолетовый')
# elif n1 == 'синий' and n2 == 'красный':
#     print('фиолетовый')
# elif n1 == 'красный' and n2 == 'красный':
#     print('красный')
# elif n1 == 'синий' and n2 == 'синий':
#     print('синий')
# elif n1 == 'желтый' and n2 == 'синий':
#     print('зеленый')
# elif n1 == 'синий' and n2 == 'желтый':
#     print('зеленый')
# elif n1 == 'красный' and n2 == 'желтый':
#     print('оранжевый')
# elif n1 == 'желтый' and n2 == 'красный':
#     print('оранжевый')
# elif n1 == 'желтый' and n2 == 'желтый':
#     print('желтый')
# else:
#     print('ошибка цвета')

# n = int(input())
# if n == 0:
#     print('зеленый')
# elif 0 < n < 11 and n % 2 == 0:
#     print('черный')
# elif 0 < n < 11 and n % 2 != 0:
#     print('красный')
# elif 10 < n < 19 and n % 2 == 0:
#     print("красный")
# elif 10 < n < 19 and n % 2 != 0:
#     print('черный')
# elif 18 < n < 29 and n % 2 == 0:
#     print('черный')
# elif 18 < n < 29 and n % 2 != 0:
#     print('красный')
# elif 28 < n < 37 and n % 2 == 0:
#     print('красный')
# elif 28 < n < 37 and n % 2 != 0:
#     print('черный')
# else:
#     print('ошибка ввода')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a1 < b1 and b1 + 1 == a2 and a2 < b2:
#     print(b1, a2)
# elif a1 < b1 and b1 + 2 == a2 and a2 < b2:
#     print(b1, b1 + 1, a2)
# elif a1 < b1 and b1 + 3 == a2 and a2 < b2:
#     print(b1, b1 + 1, b1 + 2, a2)

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())  # два перчики
# if a1 > a2 and b1 > b2 and a1 == b2:  # 10
#     print(a1)
# elif a1 < b1 and b1 < b2 and b1 == a2:  # 9
#     print(b1)
# elif a1 < a2 and b1 < a2 and b1 < b2 :  # 12
#     print('пустое множество')
# elif a1 > a2 and b1 > b2 and a1 > b2:  # 13
#     print('пустое множество')
# elif a1 < a2 and b1 < b2:  # 1
#     print(a2, b1)
# elif a1 == a2 and b1 == b2:  # 2
#     print(a1, b1)
# elif a1 > a2 and b1 == b2:  # 3
#     print(a1, b1)
# elif a1 > a2 and b1 < b2:  # 4
#     print(a1, b1)
# elif a1 < a2 and b1 > b2:  # 5
#     print(a2, b2)
# elif a1 < a2 and b1 == b2:  # 6
#     print(a2, b2)
# elif a1 > a2 and b1 > b2:  # 7
#     print(a1, b2)
# elif a1 == a2 and b1 < b2:  # 8
#     print(a1, b1)
# elif a1 == a2 and b1 > b2:  # 11
#     print(a1, b2)

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())  # як можна було О_о
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# else:
#     if a1 > a2:
#         a2 = a1
#     if b1 > b2:
#         b1 = b2
#     if a2 == b1:
#         print(a2)
#     else:
#         print(a2, b1)

# n1 = int(input())
# n3 = n1 % 100
# n4 = n1 % 10
# if n3 == 0 and n4 == 0:
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# # if a1 % 2 == 0 and b1 % 2 == 0 and a2 % 2 == 0 and b2 % 2 == 0:
# #     print('YES')
# # elif a1 % 2 != 0 and b1 % 2 != 0 and a2 % 2 != 0 and b2 % 2 != 0:
# #     print('YES')
# # elif a1 % 2 != 0 and b1 % 2 != 0 and a2 % 2 == 0 and b2 % 2 == 0:
# #     print('YES')
# # elif a1 % 2 == 0 and b1 % 2 == 0 and a2 % 2 != 0 and b2 % 2 != 0:
# #     print('YES')
# # else:
# #     print('NO')
# if (a1 + b1 + a2 + b2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# n1, a = int(input()), str(input())
# if 9 < n1 < 16 and a == 'f':
#     print('YES')
# else:
#     print('NO')

# n1 = int(input())
# if n1 == 1:
#     print('I')
# elif n1 == 2:
#     print('II')
# elif n1 == 3:
#     print('III')
# elif n1 == 4:
#     print('IV')
# elif n1 == 5:
#     print('V')
# elif n1 == 6:
#     print('VI')
# elif n1 == 7:
#     print('VII')
# elif n1 == 8:
#     print('VIII')
# elif n1 == 9:
#     print('IX')
# elif n1 == 10:
#     print('X')
# else:
#     print('ошибка')

# n1 = int(input())
# if n1 % 2 != 0:
#     print('YES')
# elif n1 % 2 == 0 and 1 <  n1 < 6:
#     print('NO')
# elif n1 % 2 == 0 and 5 <  n1 < 21:
#     print('YES')
# elif n1 % 2 == 0 and n1 > 20:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (a2 == a1 + 1 and b2 == b1 + 1) or (a2 == a1 + 2 and b2 == b1 + 2) or (a2 == a1 + 3 and b2 == b1 + 3) or (a2 == a1 + 4 and b2 == b1 + 4) or (a2 == a1 + 5 and b2 == b1 + 5) or (a2 == a1 + 6 and b2 == b2 + 6) or (a2 == a1 + 7 and b2 == b1 + 7):
#     print('YES')
# elif (a2 == a1 - 1 and b2 == b1 - 1) or (a2 == a1 - 2 and b2 == b1 - 2) or (a2 == a1 - 3 and b2 == b1 - 3) or (a2 == a1 - 4 and b2 == b1 - 4) or (a2 == a1 - 5 and b2 == b1 - 5) or (a2 == a1 - 6 and b2 == b2 - 6) or (a2 == a1 - 7 and b2 == b1 - 7):
#     print('YES')
# elif (a1 + b1) == (a2 + b2):
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (a2 == a1 + 2 or a2 == a1 - 2) and (b2 == b1 + 1 or b2 == b1 - 1):
#     print('YES')
# elif (a2 == a1 + 1 or a2 == a1 - 1) and (b2 == b1 + 2 or b2 == b1 - 2):
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (a2 == a1 + 1 and b2 == b1 + 1) or (a2 == a1 + 2 and b2 == b1 + 2) or (a2 == a1 + 3 and b2 == b1 + 3) or (a2 == a1 + 4 and b2 == b1 + 4) or (a2 == a1 + 5 and b2 == b1 + 5) or (a2 == a1 + 6 and b2 == b2 + 6) or (a2 == a1 + 7 and b2 == b1 + 7):
#     print('YES')
# elif (a2 == a1 - 1 and b2 == b1 - 1) or (a2 == a1 - 2 and b2 == b1 - 2) or (a2 == a1 - 3 and b2 == b1 - 3) or (a2 == a1 - 4 and b2 == b1 - 4) or (a2 == a1 - 5 and b2 == b1 - 5) or (a2 == a1 - 6 and b2 == b2 - 6) or (a2 == a1 - 7 and b2 == b1 - 7):
#     print('YES')
# elif (a1 + b1) == (a2 + b2):
#     print('YES')
# elif ((a1 == a2) and (1 <= b1 <= 8 and 1 <= b2 <= 8)) or ((b1 == b2) and (1 <= a1 <= 8 and 1 <= a2 <= 8)):
#     print('YES')
# else:
#     print('NO')


