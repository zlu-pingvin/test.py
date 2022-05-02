# numbers = list(range(5, 12 + 1))
# print(numbers)

# s = 'abcdsdgdfnghfgdzszdxcbnvmbvgdfdr645trdd3etegdgfe'
# chars = list(s)
# print(chars)

# numbers = [0, 1, 3, 14, 2, 7, 9, 8, 10]
# print(numbers)

# s = input()  # Список чисел
# n = int(s)
# numbers = list(range(1, n + 1))
# print(numbers)

# s = int(input())  # Список чисел
# numbers = list(range(1, s + 1))
# print(numbers)

# n = int(input())  # Список букв
# s = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(len(s)):
#     print(list(s[:n]))
#     break

# n = int(input())   # !!!
# s = 'abcdefghijklmnopqrstuvwxyz'
# print(list(s[:n]))

# numbers = [2, 4, 6, 8, 10]
# print(numbers[2:5])

# fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
# fruits[2:5] = ['банан', 'вишня', 'киви']
# print(fruits)

# print([1, 2, 3, 4] + [5, 6, 7, 8])
# print([7, 8] * 3)
# print([0] * 10)

# a = [1, 2, 3, 4]
# b = [7, 8]
# a += b   # добавляем к списку a список b
# b *= 5   # повторяем список b 5 раз
# print(a)
# print(b)

# numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
# print('Минимальный элемент =', min(numbers))
# print('Максимальный элемент =', max(numbers))

# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers[1] = 101     # изменяем 2 элемент (по индексу 1) списка
# print(numbers)

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[18])

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(max(primes))

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[:6])

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print(min(numbers) + max(numbers))

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / 10
# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[6] = 'Фиолетовый'
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print((numbers1 * 2) + (numbers2 * 9) + numbers3)

# numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список
# numbers.append(21)  # добавляем число 21 в конец списка
# numbers.append(34)  # добавляем число 34 в конец списка
# print(numbers)

# numbers = []  # создаем пустой список
# numbers[0] = 1
# numbers[1] = 2
# numbers[2] = 3
# print(numbers)  # помилка

# numbers = [0, 2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7]
# numbers.extend(odds)
# print(numbers)

# words1 = ['iq option', 'stepik', 'beegeek']
# words2 = ['iq option', 'stepik', 'beegeek']
# words1.append('python')
# words2.extend('python')
# print(words1)
# print(words2)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[5:7]    # удаляем элемент имеющий индекс 5, можна слайсами
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # чет
# del numbers[::2]
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # нечет
# del numbers[1::2]
# print(numbers)

# numbers = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o']  # літери
# del numbers[::2]
# print(numbers)

# x = ['potato', 'cucumber', 'carrot']
# print(x[-2][1])  # Вывод: u
# print(x[-1][0])  # Вывод: c
# print(x[-1][:3])  # Вывод: car

# names = []
# names.append('Chromatica')
# print(names[0])

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))  # Вывел длину списка
# # print(5)
# print(numbers[-1])  # Вывел последний элемент списка !!!
# print(numbers[::-1])  # Вывел список в обратном порядке
# if 5 in numbers and 17 in numbers:  # Вывел YES если список содержит числа 5 и 17, и NO в противном случае
#     print('YES')
# else:
#     print('NO')
# print(numbers[1:-1])  # Вывел список с удаленным первым и последним элементами

# n = int(input())  # Список строк
# s = []
# for i in range(1, n + 1):
#     s.append(input())
# print(s)

# n = 1  # Алфавит
# z = []
# for i in range(97, 123):
#     z += [chr(i) * n]
#     n += 1
# print(z)

# n = int(input())  # Список кубов
# k = []
# for i in range(1, n + 1):
#     z = int(input())
#     k += [(z ** 3)]
# print(k)

# s = []  # Алфавит
# n = 1
# for i in range(97, 123):
#     s.append(chr((i)) * n)
#     n += 1
# print(s)

# n = int(input())  # Список кубов
# k = []
# for i in range(1, n + 1):
#     z = int(input())
#     k.append(z ** 3)
# print(k)

# n = int(input())  # Список делителей
# s = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         s.append(i)
# print(s)

# n = int(input())  # Суммы двух
# v = []
# w = []
# for i in range(1, n + 1):
#     z = int(input())
#     v.append(z)
# for j in range(len(v) - 1):
#     w.append(v[j] + v[j] + 1)
# print(v)
# print(w)

# n = int(input())  # Суммы двух  :(
# count = 0
# v = []
# for i in range(1, n + 1):
#     z = int(input())
#     count += z
#     v.append(count)
#     count = z
# print(v[1:])

# z = int(input())  # Удалите нечетные индексы
# lst = []
# for i in range(1, z + 1):
#     n = int(input())
#     lst.append(n)
# del lst[1::2]
# print(lst)

# n = int(input())  # k-ая буква слова 🌶️🌶️
# lst = []
# for _ in range(n):
#     lst.append(input())
# k = int(input())
# for i in lst:
#     if len(i) < k:
#         continue
#     elif len(i) >= k:
#         for r in range(len(lst)):
#             print(i[k - 1], end='')
#             break

# n = int(input())  # k-ая буква слова 🌶️🌶️
# lst = []
# for _ in range(n):
#     lst.append(input())
# k = int(input())
# for i in lst:
#     if len(i) < k:
#         continue
#     elif len(i) >= k:
#         print(i[k - 1], end='')

# n = int(input())  # Символы всех строк
# lst = []
# for i in range(n):
#     lst.extend(input())
# print(lst)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(numbers)):
#     print(numbers[i])

# numbers = ['q', 'w', 'e', 'r', 't', 'y']
# for i in range(len(numbers)):
#     print(numbers[i])

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers, sep='\n')

# s = 'Python'
# print(*s)
# print()
# print(*s, sep='\n')

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# summ = 0
# for i in range(len(numbers)):
#     summ += numbers[i] ** 2
# print(summ)

# n = int(input())  # Значение функции
# n_in = []
# f_out = []
# for i in range(n):
#     x = int(input())
#     n_in.append(x)
#     f = x ** 2 + 2 * x + 1
#     f_out.append(f)
# print(*n_in, sep='\n')
# print()
# print(*f_out, sep='\n')

# n = int(input())  # Значение функции
# numbers = []
# for i in range(n):
#     numbers.append(int(input()))
# numbers.remove(min(numbers))
# numbers.remove(max(numbers))
# print(*numbers, sep='\n')

# n = int(input())  # Без дубликатов
# z = []
# for i in range(n):
#     s = input()
#     if s in z:
#         continue
#     else:
#         z.append(s)
# print(*z, sep='\n')

# n = int(input())  # Google search - 1
# lst = []
# for i in range(n):
#     lst.append(input())
# s = input().lower()
# for j in range(len(lst)):
#     if s in lst[j].lower():
#         print(lst[j])

# n = int(input())  # Google search - 2
# lst = []
# zap = []
# count = 0
# for i in range(n):
#     lst.append(input())
# k = int(input())
# for j in range(k):
#     zap.append(input().lower())
# for e in range(len(lst)):
#     for p in range(len(zap)):
#         if zap[p] in lst[e].lower():
#             count += 1
#             if count == k:
#                 print(lst[e])
#     count = 0

# lst = []  # Negatives, Zeros and Positives
# for _ in range(int(input())):
#     lst.append(int(input()))
# for i in range(len(lst)):
#     if lst[i] < 0:
#         print(lst[i])
# for j in range(len(lst)):
#     if lst[j] == 0:
#         print(lst[j])
# for k in range(len(lst)):
#     if lst[k] > 0:
#         print(lst[k])

# s = 'Python is the most powerful language'
# words = s.split()
# print(words)

# numbers = input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)

# ip = '192.168.1.24'
# numbers = ip.split('.')    # указываем явно разделитель
# print(numbers)

# words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
# s = ' '.join(words)
# print(s)

# words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
# s = '///'.join(words)
# print(s)

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# s = input()  # Построчный вывод
# n = s.split()
# print(*n, sep='\n')

# n = input()  # Инициалы
# s = n.split()
# for i in range(len(s)):
#     print(s[i][0], end='.')

# for c in input().split():  # Инициалы !!!!!!!!!!
#     print(c[0], end='.')

# s = input()  # Windows OS
# n = s.split('\\')
# print(*n, sep='\n')

# s = input() # Диаграмма
# n = s.split()
# for i in n:
#     print(int(i) * '+')

# s = input() # Корректный ip-адрес
# n = s.split('.')
# count = 0
# for i in range(len(n)):
#     if int(n[i]) >= 0 and int(n[i]) < 266:
#         count += 1
# if count == len(n):
#     print('ДА')
# else:
#     print('НЕТ')

# s = input()  # Добавь разделитель
# n = input()
# w = []
# for i in range(len(s)):
#     w.extend(s[i])
# print(n.join(w))

# number = input()  # Количество совпадающих пар
# s = []
# s = number.split(' ')
# count = 0
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             count += 1
# print(count)

# numbers = input().split()
# print(numbers)

# names = ['Gvido', 'Roman' , 'Timur']
# names.clear()
# print(names)

# numbers = [8, 9, 10, 11]  # Все сразу 2 🌶️
# numbers[1] = 17  # Заменил второй элемент списка на 17
# n = 4, 5, 6
# numbers.extend(n)  # Добавил числа 4, 5 и 6 в конец списка
# del numbers[0]  # Удалил первый элемент списка
# numbers.extend(numbers)  # Удвоил список
# numbers.insert(3, 25)  # Вставил число 25 по индексу 3
# print(numbers)

# n = input().split()  # Переставить min и max
# s = []
# a = 0  # макс число
# b = 100000000000990000000000000  # мін число
# c = 0  # індекс макс числа
# d = 0  # індекс мін числа
# for _ in range(len(n)):
#     s.append(int(n[_]))
# for i in range(len(s)):
#     if s[i] > a:
#         a = s[i]
#         c = i
# for j in range(len(s)):
#     if s[j] < b:
#         b = s[j]
#         d = j
# s[c], s[d] = s[d], s[c]
# print(*s)




# a = [10, 20]
# b = a
# b = b + [30, 40]
# print(a)
# print(b)

# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)

# a = 2
# b = 3
# c = 2
# d = 3
#
# b = a
# b = b + 4
#
# d = c
# d += 4
#
# print(a)
# print(b)
# print(c)
# print(d)

# s = input().lower().split()  # Количество артиклей
# a = s.count('a')
# an = s.count('an')
# the = s.count('the')
# print(f'Общее количество артиклей:', a + an + the)

# Взлом Братства Стали 🌶️
#12
# print("Введите своё имя")
# name = input()
# print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
# password = input()
# if password == "hoover":
#     print("Здравствуйте, рыцарь", name)         #долой Макнамару
# elif password == "noncr":
#     print("Здравствуйте, паладин", name)
# elif password == "gelios":
#     print("Здравствуйте, старейшина", name)          #Элайджа вперёд
# else:
#     print("Здравствуйте, послушник", name)

# n = input()
# n = int(n[1:])
# # n = int(n)
# txt = []
# for i in range(n):
#     s = input()
#     if '#' not in s:
#         txt.append(s)
#     elif '#' in s:
#         octo = s.index('#')
#         s = s[:octo]
#         s = s.rstrip()
#         txt.append(s)
# print(*txt, sep='\n')

# print(0.2 + 0.3)
# print(0.1 + 0.3)
# print(0.1 + 0.2)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# a.sort()
# print('Отсортированный список:', a)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# a.sort(reverse = True)   # сортируем по убыванию
# print('Отсортированный список:', a)

# s = input().lower().split() # сортируем по убыванию строки
# n = []
# for i in range(len(s)):
#     n.append(s[i])
# n.sort()
# print(n)

# a = [5, 3, 1, 2, 4]
# b = sorted(a)
# print(b)  # [1, 2, 3, 4, 5]
# print(a)  # [5, 3, 1, 2, 4]

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)
# print(numbers)

# n = input().split()  # Сортировка чисел
# for i in range(len(n)):
#     n[i] = int(n[i])
# a = sorted(n)
# b = sorted(n, reverse= True)
# print(*a)
# print(*b)

# zeros = []
# for i in range(10):
#     zeros.append(0)
# print(zeros)

# zeros = [0] * 10
# print(zeros)

# numbers = []
# for i in range(1, 11):
#     numbers.append(i)
# print(numbers)

# numbers = [i for i in range(1, 21)]
# print(numbers)

# squares = [i ** 2 for i in range(1, 21)]
# print(squares)

# chars = [c for c in 'abcdefg']
# print(chars)

# n = int(input())
# lines = [input() for _ in range(n)]
# print(lines)

# lines = [input() for i in range(int(input()))]
# print(lines)

# n = [int(input()) for _ in range(int(input()))]
# print(n)

# n = [i for i in range(33) if i % 3 == 0]
# print(n)

# n = [i ** j for i in range(2, 6) for j in range(3, 9)]
# print(n)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [keywords [i][1:] for i in range(len(keywords))]
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(keywords[i]) for i in range(len(keywords))]
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# print([i for i in keywords if len(i) > 4])


# print([i for i in range(100, 1000) if str(i)[0] == str(i)[2]])

# print(sep='\n', *[i ** 2 for i in range(1, int(input()) + 1)])

# n = int(input())
# for i in range(1, n + 1):
#     v = i ** 2
#     print(v)

# for i in range(1, int(input()) + 1):
#     v = i ** 2
#     print(v)

# print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')

# [print(_**2) for _ in range(1, int(input())+1)]

# n = input().split()
# z = []
# for j in range(len(n)):
#     n[j] = int(n[j])
# z.extend(n)
# z = ([z[i] ** 3 for i in range(len(n))])
# print(*z)

# n = input().split()
# z = []
# for j in range(len(n)):
#     n[j] = int(n[j])
# z.extend(n)
# print(*[z[i] ** 3 for i in range(len(n))])

# n = input().split()
# print(*[int(n[i]) ** 3 for i in range(len(n))])

# В одну строку 1
# print(*[i for i in input().split()], sep='\n')

# В одну строку 2
# print(*[i for i in input() if i in '0123456789'], sep='')

# В одну строку 3
# print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4], sep=' ')

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
# print('Отсортированный список:', a)

# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
# n = len(a)
# cnt = 0
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             cnt += 1
#             if cnt == 0:
#                 break
#             cnt = 0
# print(a)

# a = [3, 2, 1, 4, 5]
# n = len(a)
# flag = True
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
#         else:
#             flag = False
#         if flag == False:
#             break
# print(a)

# a = [1, 3, 2, 4, 5]
# n = len(a)
#
# for i in range(n - 1):
#     cnt = 0
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             cnt += 1
#             if cnt == 0:
#                 break
#             cnt = 0
# print(a)

# a = [1, 3, 2, 4, 5]
# n = len(a)
# for i in range(n - 1):
#     used = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             used = True
#     if used == False:
#         break
# print(a)

# a = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]  # Ваня
# n = len(a)
# print('original:')
# print(a)
# n = len(a)
# for i in range(n - 1):
#     Swapped = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             Swapped = True
#     print(Swapped)
#     print(a)
#     if Swapped == False:
#         break
# print('result:')
# print(a)

# a = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
# n = len(a)
# for i in range(n - 1):
#     flag = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
#     if flag == False:
#         break

# a = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
# n = len(a)
# for i in range(n - 1):
#     flag = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
#     if flag == False:
#         break
# print(a)

# s = [1, 2, 3, 4, 12]
# n = [5, 6, 7, 8, 9, 10]
# print(zip(s, n))
# print(list(zip(s, n)))

# a = [5, 3, 2, 4, 1]
# n = len(a)
# for i in range(n - 1):
#     max = 0
#     max_i = 0
#     for j in range(i, n):
#         if n[j] > max:
#             max = n[j]
#             max_i = [j]
#             n -= n
# print(a)

# a = [51, 31, 21, 41, 11]
# n = len(a)
# for i in range(n - 1):
#     max = 0
#     max_i = 0
#     for j in range(n):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
#             # n -= n
#             print(a[i])
#             print(a[j])
#             n -= n
# print(a)

# алгоритм сортировки выбором
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# # n = len(a)
# # for i in range(n - 1):
# #     for k in range(i + 1, n):
# #         if a[k] < a[i]:
# #             a[k], a[i] = a[i], a[k]
# # print(a)

# print((240 * 140) / (150 * 85))

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]  # Сортировка простыми вставками
# n = len(a)
# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem
# print('Отсортированный список:', a)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# print('Начинаем цикл перебора всех элементов списка, начиная со второго (неотсортированный список)')
# for i in range(1, n):
#     print(a, i, 'итерация: a[i] =', a[i])
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     print('Запоминаем проверяемый элемент списка в доп память - elem = a[i] =', a[i])
#     j = i
#     if a[j - 1] <= elem:
#         print(f'В while не заходим, тк проверяемое число ({a[i]}) больше предыдущего ({a[i - 1]})')
#     while j >= 1 and a[j - 1] > elem:
#         print(f'while: сравниваем индекс = {j}: на место a[j] = {a[j]} записываем число {a[j - 1]}, и получаем', end=' ')
#         a[j] = a[j - 1]
#         print(a)
#         j -= 1
#     print(f'Извлекаем из доп памяти elem = {elem} в индекс {j}')
#     a[j] = elem
# print(a)

#  алгоритм сортировки выбором
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# print('Начинаем цикл перебора всех элементов списка без последнего (минус один)')
# for i in range(n - 1):
#     print(f'внешний цикл {i}')
#     for k in range(i + 1, n):
#         print(f'начинаем внутренний цикл: {a}, {k} итерация')
#         if a[k] < a[i]:
#             print(f'сравниваем a[k] (из внутренного цикла) с a[i] (из внешнего цикла). Если {a[k]} меньше {a[i]}, тогда:')
#             a[k], a[i] = a[i], a[k]
#             print(f'меняем местами {a[k]} и {a[i]} ({a[i]} идет в начало списка) и получаем список')
#             print(a)
# print(f'В итоге получаем отсортированный список {a}')

# s = [1, 2, 3, 4, 12]
# n = [5, 6, 7, 8, 9, 10]
# x = [13, 14, 15, 16]
# print(zip(s, n))
# print(list(zip(s, n, x)))

# print([i for i in range(2, int(input()) + 1, 2)])

# l = input().split()
# m = input().split()
# for i in range(len(l)):
#     print()
# for j in range(len(m)):
#         print(int(l[i]) + int(m[j]))

# l = input().split()
# m = input().split()
# for i in range(len(l)):
#     print(int(l[i]) + int(m[i]), end=' ')

# s = input().split()  # Сумма чисел
# n = 0
# for  i in range(len(s)):
#     s[i] = int(s[i])
#     n += s[i]
# print(*s, sep='+', end='=')
# print(n)

# Самый длинный
# print(max([len(i) for i in input().split()]))

# Молодежный жаргон
# print(*[i[1:] + i[0] + 'ки' for i in input().split()])

# Валидный номер 🌶️🌶️
# s = input()
# s1 = s.replace('-', '')
# if s1.isdigit() == False:
#     # break
#     print('NO')
# else:
#     n = s.split('-')
#     n2 = []
#     for i in range(len(n)):
#         n2.append(len(n[i]))
#     if n2 == [1, 3, 3, 4] and n[0] == '7' or n2 == [3, 3, 4]:
#         print('YES')
#     else:
#         print('NO')

# s = input()  # None
# s1 = s.replace('-', '')
# if s1.isdigit() == False:
#     print('NO')
# else:
#     n = s.split('-')
#     n2 = []
#     for i in range(len(n)):
#         n2.append(len(n[i]))
#     print(*['YES' if n2 == [1, 3, 3, 4] and n[0] == '7' or n2 == [3, 3, 4] else print('NO')])

########################################################
########################################################
########################################################

# a, b = input().split()
# a, b = int(a), int(b)
# k = 30
# print(f'Можно отрезать {(a // k) * (b // k)} квадратов.')

# n = 450 * 33
# s = 30 * 30
# z = n // s
# print(z)

# print(*[input()[::-1]])

# n = int(input())
# print(n % 10, n // 10, n % 10 + n // 10, (n % 10) * (n // 10), sep='\n')

# n = int(input())
# print(n % 10, n % 100 // 10, n // 100, sep='')

# n = int(input())
# print(n % 100 // 10, n % 10, sep='')

# [print(0) if int(input()) % 2 == 0 else print(1)]

# s = input()  # None
# s1 = s.replace('-', '')
# if s1.isdigit() == False:
#     print('NO')
# else:
#     n = s.split('-')
#     n2 = []
#     for i in range(len(n)):
#         n2.append(len(n[i]))
#     [print('YES') if n2 == [1, 3, 3, 4] and n[0] == '7' or n2 == [3, 3, 4] else print('NO')]

# n = int(input())
# print(n % 10000 // 1000)

# n = int(input())
# s = 60
# print(int(n / s))

# n = int(input())
# print(n % 1000 // 100)
# print(n % 10000 // 1000)

# n = int(input())
# print((n % 100) * 10)

# n = int(input())
# print(n % 100 // 10, n // 100, n % 10, sep='')

# n = input().split()
# x = int(n[0]) + int(n[1])
# print(x // 10, x % 10, sep='\n')

# n = int(input())
# h = 3600
# m = 60
# s = 1
# print(f'{n // h} часов')
# print(f'{(n % h) // m} минут')
# print(f'{((n % h) % m) // s} секунд')

# n = int(input())
# h = 3600
# m = 60
# s = 1
# print(n // h, ':', (n % h) // m, sep='')
# print(f'{(n % h) // m} минут')
# print(f'{((n % h) % m) // s} секунд')

# n = int(input())
# h = 3600
# m = 60
# print((n // h // 10), (n // h) % 10, ':', n % h // m // 10, (n % h) // m % 10, sep='')

# n = int(input())
# od = n // 1000
# des = n // 100 % 10
# sot = n % 100 // 10
# tus = n % 10 % 1000
# print(f'Сумма цифр в числе {n} равна {od + des + sot + tus}')
# print(f'Произведение цифр в числе {n} равно {od * des * sot * tus}')

# n = int(input())
# print(n % 10, n // 100, n % 100 // 10, sep='')

# n = int(input())
# print(n % 100 // 10, n % 10 % 1000, n // 1000, n // 100 % 10, sep='')

# n = int(input())
# st = 100
# pt = 50
# des = 10
# od = 1
# print(f'{n // st} купюры по 100 рублей')
# print(f'{(n % st) // pt} купюры по 50 рублей')
# print(f'{((n % st) % pt) // des} купюры по 10 рублей')
# print(f'{(((n % st) % pt) % des) // od} купюры по 1 рублей')

# n = int(input())
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(b)

# n = int(input())
# b = ''
# for i in range(8):
#     b = str(n % 2) + b
#     n = n // 2
# print(b)

# n = int(input())
# x = bin(n)
# print(x)

# a, b, c = input().split()
# d, e = input().split()
# n = int(a + b + c)
# z = int(d + e)
# x = n + z
# print(x // 100, x // 10 % 10, x % 10, sep=' ')

