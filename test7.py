# def qwe():
#     for _ in range(5):
#         print('*' * 7)
# qwe()
# print()
# qwe()
# print()
# qwe()
# print()

# def draw_box():
#     for _ in range(12):
#         print('*        *')
#
#
# print('**********')
# draw_box()
# print('**********')

# def draw_triangle():
#     for _ in range(1, 11):
#         print('*' * _)
#
#
# draw_triangle()

# n, m = 3, 6
# def draw_box(height, width):    # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)
#
# draw_box(3, 15)
# print()
# draw_box(5, 8)
# print()
# draw_box(10, 10)
# print()
# draw_box(10, 15)
# print()
# draw_box(n, m - 2)

# def print_hello(n):
#     print('Hello' * n)
#
#
# print_hello(2)
# print_hello(5)
# times = 2
# print_hello(times)

# def print_text(txt, n):
#     print(txt * n)
#
#
# print_text('Hello', 5)
# print_text('A', 10)

# def draw_box(height, width):
#     height = 2
#     width = 10
#     for i in range(height):
#         print('*' * width)
#
# n = 5
# m = 7
# draw_box(n, m)
# print()
# print(n, m)

# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)
#
#
# print_number(2, 3, 11)

# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)

# Звездный треугольник
# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(fill * i)
#     for j in range(base // 2, 0, -1):
#         print(fill * j)
#
# fill = input()
# base = int(input())
#
# draw_triangle(fill, base)

# Звездный треугольник
# def draw_triangle(fill, base):
#     n = base // 2 + 1
#     print(*[fill * i for i in range(1, n)], sep='\n')
#     print(*[fill * i for i in range(n, 0, -1)], sep='\n')
#
# fill = input()
# base = int(input())
#
# draw_triangle(fill, base)

# ФИО
# def print_fio(name, surname, patronymic):
#     print(surname[0].title(), name[0].title(), patronymic[0].title(), sep='')
#
# name, surname, patronymic = input(), input(), input()
# print_fio(name, surname, patronymic)

# # Сумма цифр ((((((((
# def print_digit_sum(num):
#     summ = 0
#     summ += n[i] for i in range(n)
#     print(summ)
#
# n = int(input())
# print_digit_sum()

# # Сумма цифр (((((((((((((((((((
# def print_digit_sum(num):
#     summ = 0
#     for i in range(len(n)):
#         n[i] = int(n[i])
#         for j in range(len(n)):
#             summ += int(n[i])
#     print(summ)
#     print(n[i] + 1)
#
# n = input().split()
# print_digit_sum(n)

# Сумма цифр
# def print_digit_sum(n):
#     summ = 0
#     while n > 0:
#         z = n % 10
#         summ += z
#         n = n // 10
#     print(summ)
#
# n = int(input())
# print_digit_sum(n)

# def print_digit_sum(num):
#     print(sum([int(i) for i in num]))
#
# print_digit_sum(input())

# функция перевода градусов Фаренгейта в градусы Цельсия
# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
#
# # основная программа
# temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
# celsius = convert_to_celsius(temp)
# print(celsius)  # градусы Цельсия

# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
#
# C = convert_to_celsius(temp=float(input()))
# print(C)

# def compute_average(numbers):
#     return sum(numbers) / len(numbers)
#
#
# numbers = [1, 3, 5]
# print(compute_average(numbers))

# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)
#
#
# print(get_sum(1, 2, 3))

# # Конвертер километров
# def convert_to_miles(km):
#     return f'{(num * 0.6214):.3f}'
#
#
# num = int(input())
# print(convert_to_miles(num))

# Конвертер километров
# def convert_to_miles(km):
#     return round(num * 0.6214, 4)
#
#
# num = int(input())
# print(convert_to_miles(num))

# # Количество дней
# def get_days(month):
#     if num in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif num in [4, 6, 9, 11]:
#         return 30
#     elif num in [2]:
#         return 28
#
# # считываем данные
# num = int(input())
# # вызываем функцию
# print(get_days(num))

# Делители 1
# объявление функции
# def get_factors(num):
#     s = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             s.append(i)
#     return s
#
#
# n = int(input())
# print(get_factors(n))

# Количество дней
# def get_days(month):
#     while 1 <= num <= 12:
#         return 31 if num in [1, 3, 5, 7, 8, 10, 12] else 28 if num == 2 else 30
#
#
# # считываем данные
# num = int(input())
# # вызываем функцию
# print(get_days(num))

# # Делители 2
# def get_factors(num):
#     return len([n for n in range(1, num + 1) if num % n == 0])
#
#
# n = int(input())
# print(get_factors(n))

# # Найти всех
# def find_all(target, symbol):
#     z = []
#     for i in range(len(s)):
#         if s[i] == char:
#             z.append(i)
#     return z
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))

# Найти всех
# def find_all(target, symbol):
#     return [i for i in range(len(s)) if s[i] == char]
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))

# Merge lists 1
# def merge(list1, list2):
#     return sorted(numbers1 + numbers2)
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))

# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
#
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
# list3 = quick_merge(list1, list2)
# print(list3)

# # Merge lists 2
# def quick_merge():
#     z = []
#     for i in range(n):
#         # ch = [int(c) for c in input().split()]
#         # z.extend(ch)
#         z += [int(c) for c in input().split()]
#     return sorted(z)

#
# n = int(input())
# print(*quick_merge())

# Is Valid Triangle?
# def is_valid_triangle(side1, side2, side3):
#     if side1 < (side2 + side3) and side2 < (side1 + side3) and side3 < (side1 + side2):
#         return True
#     else:
#         return False
#
# a, b, c = int(input()), int(input()), int(input())
#
# print(is_valid_triangle(a, b, c))

# Is Valid Triangle?
# def is_valid_triangle(side1, side2, side3):
#     return side1 < (side2 + side3) and side2 < (side1 + side3) and side3 < (side1 + side2)
#
#
# a, b, c = int(input()), int(input()), int(input())
#
# print(is_valid_triangle(a, b, c))

# Is a Number Prime? 🌶️
# def is_prime(num):
#     flag = True
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             flag = False
#     if flag == True and num > 1:
#         return True
#     else:
#         return False
#
#
# num = int(input())
# print(is_prime(num))

# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# num = int(input())
# print(is_prime(num))

# Next Prime 🌶️🌶️
# def get_next_prime(num):
#     for i in range(num + 1, num + 33):
#         if is_prime(i):
#             return i
#
#
# num = int(input())
# print(get_next_prime(num))

# Good password 🌶️
# def is_password_good(password):
#     flagup = False
#     flaglow = False
#     flagdig = False
#     if len(password) < 8:
#         return False
#     for i in range(len(password)):
#         if password[i].isalpha() and password[i].isupper():
#             flagup = True
#             # continue
#         if password[i].isalpha() and password[i].islower():
#             flaglow = True
#             # continue
#         if password[i].isdigit():
#             flagdig = True
#             # continue
#     if flagup and flaglow and flagdig:
#         return True
#     else:
#         return False
#
#
# password = input()
# print(is_password_good(password))

# Ровно в одном
# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     for k in range(len(word1)):
#         if word1[k] != word2[k]:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         return False
#
#
# txt1 = input()
# txt2 = input()
#
# print(is_one_away(txt1, txt2))

# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     [count += 1 if word1[i] != word2[i] for i in range(len(word1))]
#     if count == 1:
#         return True
#     else:
#         return False
#
#
# txt1 = input()
# txt2 = input()
#
# print(is_one_away(txt1, txt2))

# print('Выбери ответ "Да" или "Нет"')
# print('Ты пидор?')
# s = input()
# if s != 'Да' and s != 'Нет':
#     print('Укажите правильный ответ')
# elif s == 'Да':
#     print('Какие планы на вечер, пративный?')
# else:
#     print('Пидора ответ')

# Палиндром 🌶️
# def is_palindrome(text):
#     n = [i for i in text if i.isalpha()]
#     return n == n[::-1]
#
#
# text = input().lower()
# print(is_palindrome(text))

# def add(x, y):
#     return x / y
# print(add(1,3))

# def add(x, y):
#   if x < 100:
#     return x + y
#   else:
#     return false
# print(add(1,2))

# def add(x, y):
#     return
# print(add(1,2))

# def say(text, time = 2):
#     print(text * time)
# text = input()
#
# say(text)

# BEEGEEK
# def is_valid_password(password):
#     if password[0] != password[0][::-1]:
#         return False
#     for i in range(len(password)):
#         password[i] = int(password[i])
#     if len(password) != 3:
#         return False
#     elif password[1] == 1:
#         return False
#     for i in range(2, password[1] // 2 + 1):
#         if password[1] % i == 0:
#             return False
#     if password[2] % 2 != 0:
#         return False
#     return True
#
# password = input().split(':')
# print(is_valid_password(password))

# password = input().split(':')
# for i in range(len(password)):
#     password[i] = int(password[i])
# if len(password) != 3:
#     print('Fa')
# elif password[1] == 1:
#     print('Fa')
# for i in range(2, password[1] // 2 + 1):
#     if password[1] % i == 0:
#         print('sdfsdf')
#     else:
#         print('wwwwwwwwwwwww')

# video_x = 1920
# video_y = 1080
#
# video_tabl_x = video_x / 2
# video_tabl_y = video_y / 2
#
# video_mob_x = video_x / 3
# video_mob_y = video_y / 3
#
# print(f'планшет: {video_tabl_x} x {video_tabl_y}')
# print(f'моб {video_mob_x} x {video_mob_y}')

# import pip
# pip install speedtest-cli

# pip.main(['install','Speedtest'])
#
# from speedtest import Speedtest
# st = Speedtest()
# print('Download:', st.download())
# print('Upload:', st.upload())
# st.get_servers([])
# print('Ping:', st.results.ping)

# def is_correct_bracket(text):  # Правильная скобочная последовательность 🌶️
#     count = 0
#     for i in range(len(text)):
#         if text[i] == '(':
#             count += 1
#         if text[i] == ')':
#             count -= 1
#         if count == -1:
#             return False
#     return count == 0
#
# text = input()
#
# print(is_correct_bracket(text))

# def convert_to_python_case(text):  # Змеиный регистр
#     s = []
#     for i in range(len(text)):
#         if text[i].isupper():
#             s.append('_')
#             s.append(text[i].lower())
#         if text[i].islower():
#             s.append(text[i])
#         if text[i].isdigit():
#             s.append(text[i])
#     print(*s[1:], sep='')
#
#
# text = input()
# convert_to_python_case(text)

# def get_powers(num):
#     return num**2, num**3, num**4, 'g' * num ** 4
#
#
# a, b, c, d = get_powers(2)
# print(a)
# print(b)
# print(c)
# print(d)

# def solve(a, b, c, d, e, f):
#     x = (d * e - b * f)/(a * d - b * c)
#     y = (a * f - c * e)/(a * d - b * c)
#     return x, y
#
#
# xsol, ysol = solve(32, 13, 4, 1, 22, 15)
# print('Решением системы являются числа', 'x =', xsol, 'y =', ysol)

# def get_middle_point(x1, y1, x2, y2):  # Середина отрезка
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y
#
#
# x1, y1 = int(input()), int(input())
# x2, y2 = int(input()), int(input())
#
#
# x, y = get_middle_point(x1, y1, x2, y2)
# print(x, y)

# import math
# def get_circle(radius):  # Площадь и длина
#     length = 2 * math.pi * r
#     square = math.pi * r ** 2
#     return length, square
#
#
# r = float(input())
# length, square = get_circle(r)
# print(length, square)

# from math import sqrt
# def solve(a, b, c):  # Корни уравнения 🌶️🌶️
#     d = b ** 2 - 4 * (a * c)
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     return (min(x2, x1), max(x2, x1))
#
#
# a, b, c = int(input()), int(input()), int(input())
# x1, x2 = solve(a, b, c)
# print(x1, x2)

############################################################################

# def email(log):
#     count_sobaka = 0
#
#     if 3 >= len(log) or len(log) > 32:
#         print('Длина логина (емейла) обязательно не менее 3 символов и не более 32 символов включительно.')
#         return False
#     elif '@' not in log:
#         print('Емейл должен содеражать символ @')
#         return False
#     elif log[0] == '@' or log[-1] == '@':
#         print('Wrong email')
#         return False
#     elif log.count('.') < 1 or log[0] == '.' or log[-1] == '.':
#         print('Wrong email')
#         return False
#     for i in log:
#         if '@' in i:
#             count_sobaka += 1
#             if count_sobaka != 1:
#                 print('Wrong email')
#                 return False
#     for j in log:
#         if j in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяґҐїЇєЄ':
#             print('Логин может содержать цифры, латинские буквы (большие и маленькие) и следующие знаки: ~!@#%^*()_+=[];:\|,.>/?-')
#             return False
#             break
#     return True
#
# def password(passw):
#     countpassw = 0
#     for r in passw:
#         if r in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяґҐїЇєЄ':
#             print('Пароль может содержать цифры, латинские буквы (большие и маленькие) и следующие знаки: ~!@#%^*()_+=[];:\|,.>/?-')
#             return False
#             break
#     for o in passw:
#         if o in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#%^*()_+=[];:\|,.>/?-':
#             countpassw += 1
#     if countpassw < 6 or countpassw > 64:
#         print('Длина пароля обязательно не менее 6 символов и не более 64 включительно.')
#         return False
#     return True
#
# log = input('Укажите логин (емейл):\n')
# passw = input('Укажите пароль:\n')
# email_check = email(log)
# password_check = password(passw)
# print(email_check, password_check, sep='\n')
# if email_check and password_check:
#     print('Поздравляем! Аккаунт успешно зарегистрирован!')

#######################################################################

# print(*[True if int(input()) >= 1 else False])  # *********************

# n = int(input())
# if n == 10:
#     print(True)
# else:
#     print(False)

# print(int(input()) > 0)

# print(*[int(input()) % 10 == 3])

# x, y = input().split()
# # x, y = int(x), int(y)
# # print(*[x ** 2 + y ** 2 <= 4])

# x, y = input().split()
# x, y = int(x), int(y)
# print(*[x >= 0 <= y])

# print(*[0 <= int(input()) <= 15])

# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)
# print(*[a < 0 or b < 0 or c < 0])

# n = int(input())
# print(*[n % 3 == 0 and n % 10 == 5])

# def C(m, n):  # Вычисление биномиального коэффициента ******
#     if m == 0 or m == n:
#         return 1
#     else:
#         return C(m, n - 1) + C(m - 1, n - 1)
#
#
# print(C(4, 17)) # m менше n!

# def draw_triangle():
#     for i in range(8):
#         print(' ' * (n - 1 - i) + '*' * (1 + i * 2))
#
# n = int(input())
# draw_triangle()

# def draw_triangle():  # Звездный треугольник 🌶️
#     for i in range(8):
#         print(' ' * (8 - 1 - i) + '*' * (1 + i * 2))
#
# draw_triangle()

# def get_shipping_cost(quantity):  # Калькулятор доставки
#     quantity = (n - 1) * 120 + 1000
#     return quantity
#
# n = int(input())
#
#
# print(get_shipping_cost(n))


# def C(m, n):  # Биномиальный коэффициент 🌶️
#     if m == 0 or m == n:
#         return 1
#     else:
#         return C(m, n - 1) + C(m - 1, n - 1)
#
# n = int(input())
# m = int(input())
# print(C(m, n))

# import math
# def compute_binom(n, k):  # Биномиальный коэффициент 🌶️
#     return int(math.factorial(n) / (math.factorial(k) * (math.factorial(n - k))))
#
#
# n = int(input())
# k = int(input())
# print(compute_binom(n, k))

# def number_to_words(num):  # Число словами 🌶️
#     lst_1_19 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     lst_10 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num < 20:
#         print(lst_1_19[num - 1])
#     elif num > 19 and num % 10 == 0:
#         s = num // 10
#         print(lst_10[s - 2])
#     elif num > 19 and num % 10 != 0:
#         s = num // 10
#         l = num % 10
#         print(*[lst_10[s - 2], lst_1_19[l - 1]])
#
#
#
# num = int(input())
#
# [number_to_words(num)]

# def get_month(language, number):  #Искомый месяц
#     ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
#                  'ноябрь', 'декабрь']
#
#     en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#                  'november', 'december']
#     if lan == 'ru':
#         return ru[num - 1]
#     elif lan == 'en':
#         return en[num - 1]
#
# lan = input()
# num = int(input())
#
# print(get_month(lan, num))

# def is_magic(date):  # Магические даты
#     x, y, z = int(date[0]), int(date[1]), int(date[2])
#     return x * y == z % 100
#
#
# date = input().split('.')
# print(is_magic(date))


# def is_pangram(text):  # Панграммы
#     abc = 'abcdefghijklmnopqrstuvwxyz'
#     for i in abc:
#         if i not in text.lower():
#             # print(i)
#             return False
#     return True
#
#
# text = input()
# print(is_pangram(text))



