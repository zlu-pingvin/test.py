# s = 'Hello'
# n = len(s)  # значение переменной равно 5
# print(n)

# n = input()
# n1 = n[3 - 1]
# print(int(n1)) # виводить третю цифру, ебто рахує з 1 а не з 0

# s = 'qwerty'
# for i in range(len(s)):
#     print(s[i])

# s = 'qwerty'
# for i in s:
#     print(i)

# s = 'abcdefg'
# print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)

#aaagggdddd

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[7])

# n = input()  # В столбик 1
# for i in range(0, len(n), 2):
#     print(n[i])

# n = input()  # В столбик 2
# for i in range(- 1, -len(n) - 1, - 1):
#     print(n[i])

# n = input()  # ФИО
# f = input()
# p = input()
# print(f[0], n[0], p[0], sep='')

# s = input()  # Цифра 1
# n = int(s)
# summ = 0
# q = 0
# while n != 0:
#     q = n % 10
#     summ += q
#     n //= 10
# print(summ)

# s = input()  # Цифра 2
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         print('Цифра')
#     else:
#         print('Цифр нет')

# s = input()  # Цифра 2
# count = 0
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         count += 1
# if count > 0:
#     print('Цифра')
# else:
#     print('Цифр нет')

# s = input()  # Сколько раз?
# countplus = 0
# countstar = 0
# for i in range(len(s)):
#     if s[i] in '+':
#         countplus += 1
#     if s[i] in '*':
#         countstar += 1
# print('Символ + встречается', countplus, 'раз')
# print('Символ * встречается', countstar, 'раз')

# s = input()  # Одинаковые соседи
# count = 0
# b = '1'
# for i in range(len(s)):
#     a = s[i]
#     if b == a:
#         count += 1
#     b = s[i]
# print(count)

# s = input()  # Гласные и согласные
# caunt_a = 0
# caunt_b = 0
# for i in range(len(s)):
#     if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         caunt_a += 1
#     if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         caunt_b += 1
# print('Количество гласных букв равно', caunt_a)
# print('Количество согласных букв равно', caunt_b)

# n = int(input())  # Decimal to Binary
# count = ''
# while n > 0:
#     count = str(n % 2) + count
#     n = n // 2
# print(count)

# s = 'abcdefghij'
# print(s[2:5])
# print(s[0:6])
# print(s[2:7])
# print(s[2:])
# print(s[:7])
# print(s[-9:-4])
# print(s[-3:])
# print(s[:-3])
# print(s[:-1])
# print(s[0:9:2])
# print(s[::-1])
# print(s[::-3])
# s = s[:4] + 'X' + s[5:]
# print(s)

# s = 'abcdefg'
# print(s[::-3])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# for i in range(len(s)):
#     if i % 7 == 0:
#         print(s[i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# s = input()  # Палиндром
# if s[::1] == s[::-1]:
#     print('YES')
# else:
#     print('NO')

# s = input()  # Делаем срезы 1
# print(len(s))  # к-сть символів
# print(s * 3)  # * 3
# print(s[0:1])  # перший символ
# print(s[:3])  # перших три символа
# print(s[-3:])  # останні три символа
# print(s[::-1])  # в зворотньому
# print(s[1:-1])  # без першого і останнього

# s = input()  # Делаем срезы 2
# print(s[2])  # третий символ этой строки
# print(s[-2])  # предпоследний символ этой строки
# print(s[:5])  # первые пять символов этой строки
# print(s[:-2])  # всю строку, кроме последних двух символов
# print(s[::2])  # все символы с четными индексами
# print(s[1::2])  # 1234567 !!!
# print(s[::-1])  # все символы в обратном порядке
# print(s[::-2])  # все символы строки через один в обратном порядке, начиная с последнего

# s = input()  # Две половинки @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# if len(s) == 1:
#     print(s)
# else:
#     s1 = (len(s) // 2) + (len(s) % 2)
#     print(s[s1:], s[:s1], sep='')

# n = int(input())
# s = n // 2
# a = (n + 1) // 2
# d = n // 2 + n % 2
# r = n % 2
# print(s)
# print(a)
# print(d)
# print(r)

# n, m = int(input()), int(input())
# print(min(n, m))
# print(max(n, m))

# s1 = 'a'
# s2 = s1.upper()
# print(s1, s2)

# s = input()  # Заглавные буквы
# if s == s.title():
#     print('YES')
# else:
#     print('NO')

# s = input()  # Заглавные буквы
# if s.istitle() == True:
#     print('YES')
# else:
#     print('NO')

# s = input()  # sWAP cASE
# print(s.swapcase())

# s = input()  # Хороший оттенок
# ok = 'хорош'
# if ok in s.lower():
#     print('YES')
# else:
#     print('NO')

# s: str = input()  # Нижний регистр
# count = 0
# for i in range(len(s)):
#     if s[i] in 'abcdefghijklmnopqrstuvwxyz':
#         count +=1
# print(count)

# s = 'foo goo moo'
# print(s.count('oo'))
# print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ

# s = input()
# print(s.count('от'))
# print(s.count('бо'))
# print(s.count('сс'))
# print(s.count('нн'))

# s = 'foobar'
# print(s.startswith('foo'))
# print(s.startswith('baz'))

# s = 'foo bar foo baz foo qux'
# print(s.find('foo'))
# print(s.find('bar'))
# print(s.find('qu'))
# print(s.find('python'))  # -1

# s = 'foo bar foo baz foo qux'
# print(s.rfind('foo'))
# print(s.rfind('bar'))
# print(s.rfind('qu'))
# print(s.index('python'))  # Error

# s = '     foo bar foo baz foo qux      '
# print(s.lstrip())

# s = '      foo bar foo baz foo qux      '
# print(s.rstrip())

# s = 'foo bar foo baz foo qux'
# print(s.replace('foo', 'grault', 2))  # дві заміни foo --> grault

# s = input()  # Количество слов
# print(s.count(' ') + 1)

# s = input()  # Минутка генетики
# s = s.lower()
# print('Аденин:', s.count('а'))
# print('Гуанин:', s.count('г'))
# print('Цитозин:', s.count('ц'))
# print('Тимин:', s.count('т'))

# n = int(input())  # Очень странные дела
# count = 0
# for i in range(n):
#     s = input()
#     if s.count('11') >= 3:
#         count += 1
# print(count)

# s = input()  # Количество цифр
# count = 0
# for i in range(len(s)):
#     if s[i] in '1234567890':
#         count += 1
# print(count)

# s = input()  # .com or .ru
# if s.endswith('.ru') or s.endswith('.com'):
#     print('YES')
# else:
#     print('NO')

# s = input()  # Самый частотный символ
# count = 0
# letter = ''
# for i in range(len(s)):
#     if s.count(s[i]) >= count:
#         count = s.count(s[i])
#         letter = s[i]
# print(letter)

# s = input()  # Первое и последнее вхождение
# for i in range(len(s)):
#     if s.count('f') == 1:
#         print(s.find('f'))
#         break
#     elif s.count('f') > 1:
#         print(s.find('f'), s.rfind('f'))
#         break
#     else:
#         print('NO')
#         break

# s = input()  # Первое и последнее вхождение
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') > 1:
#     print(s.find('f'), s.rfind('f'))
# else:
#     print('NO')

# s = input()  # Удаление фрагмента
# a = s.find('h')
# z = s.rfind('h')
# print(s[:a], s[z + 1:], sep='')

# age = 27
# txt = 'My name is Timur, I am ' + str(age)
# print(txt)

# age = 27
# txt = 'My name is Timur, I am {}'.format(age)
# print(txt)

# age = 27
# name = 'Timur'
# profession = 'math teacher'
# txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
# print(txt)

# age = 27
# name = 'Timur'
# profession = 'math teacher'
# txt = 'My name is {0}, I am {1}, I work as a {2}'.format(name, age, profession)
# print(txt)

# In 2010, someone paid 10k Bitcoin for two pizzas.
# year = 2010
# summ = '10k'
# b = 'Bitcoin'
# s = 'In {0}, someone paid {1} {2} for two pizzas.' .format(year, summ, b)
# print(s)

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

# num1 = ord('A')
# num2 = ord('B')
# num3 = ord('a')
# print(num1, num2, num3)

# chr1 = chr(65)
# chr2 = chr(75)
# chr3 = chr(110)
# print(chr1, chr2, chr3)

# for i in range(26):
#     print(chr(ord('A') + i))

# for i in range(100):
#     print(chr(ord('А')-50 + i), end = " ")

# a, b = int(input()), int(input())  # Символы в диапазоне
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# s = input()  # Простой шифр
# for i in range(len(s)):
#     print(ord(s[i]), end='')

# n, s = int(input()), input()  # Шифр Цезаря 🌶️  :(
# for c in s:
#     if ord(c) - n < 97:
#         print(chr(122 - (96 - ord(c) + n)), end='')
#     else:
#         print(chr(ord(c) - n), end='')

# s = 'Python rocks!'
# print(len(s))

# s = 'Python rocks!'
# print(s[3])

# s = 'Python rocks!'
# print(s[1:5])

# s = '    Python rocks!     '
# print(s.strip())

# s = 'Python rocks!'
# print(s[:4], '@', s[5:8], '@', s[9:], sep='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# for i in range(len(s)):
#     if i % 7 == 0:
#         print(s[i], end='')

# s = input()
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')

# s = input()
# print(s.replace('@', ''))

# s = input()
# count = 0
# for i in range(len(s)):
#     if 'f' in i:
#         count += 1
#         if count == 0:
#             print('-2')

# s = input()
# count = 0
# if s.count('f') == 1:
#     print('-1')
# if s.count('f') == 0:
#     print('-2')
# if s.count('f') >= 2:
#     print(s.find('f', s.find('f') + 1))

# s = input()
# n = s.find('h')
# f = s.rfind('h')
# print(s[:n + 1], s[f - 1:n:- 1], s[f:], sep='')

# print(s.find('h', 1), s.rfind('h'))
# print(n, f)

# n = int(input())
# print(f'Сейчас мне {n}')
# print(f'В следующем году будет {n + 1}')

# a, b = input().split('+')
# a = int(a)
# b = int(b)
# print(a + b)

# h, m = input().split(':')
# m = int(m)
# h = int(h)
# print(h * 60 + m)

# h, m, s = input().split(':')
# print(f'{h} часов')
# print(f'{m} минут')
# print(f'{s} секунд')

# a, b = input().split()
# a = int(a)
# b = int(b)
# print((a - b ** 2) / (2 * a))

# n, k = input().split()
# n = int(n)
# k = int(k)
# print(f'{n * 40 + k * 120} рублей')

# n = int(input())
# print(f'Длина ребра {n}')
# print(f'Площадь грани {n * n}')
# print(f'Площадь полной поверхности {n * n * 6}')
# print(f'Объем куба {n * n * n}')

# n = int(input())
# print('50' * n)

# print('    Ж')
# print('   ЖЖЖ')
# print('  ЖЖЖЖЖ')
# print(' ЖЖЖЖЖЖЖ')
# print('...ППП...')

# n = int(input())
# print('    Ж    ' * n)
# print('   ЖЖЖ   ' * n)
# print('  ЖЖЖЖЖ  ' * n)
# print(' ЖЖЖЖЖЖЖ ' * n)
# print('...ППП...' * n)

# name = input()
# s = f'Привет, {name}! Приятно познакомиться, {name}!'.format(name)
# print(s)

# a, b, c, d = input().split()
# a1 = int(a)
# b1 = int(b)
# c1 = int(c)
# d1 = int(d)
# print(f'{a} + {b} + {c} + {d} = {a1 + b1 + c1 + d1}')

# n = int(input())
# print(f'{n} суток = {n * 24} часов = {n * 1440} минут = {n * 86400} секунд')

# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(f'Площадь треугольника со сторонами a={a}, b={b}, c={c} равна {s}.')

# a, b, c = input().split()
# x, y, z = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# x = int(x)
# y = int(y)
# z = int(z)
# print(f'{x} стульев по {a} руб., стоимость {x * a} рублей.')
# print(f'{y} кресел по {b} руб., стоимость {y * b} рублей.')
# print(f'{z} столов по {c} руб., стоимость {z * c} рублей.')
# print(f'Стоимость гарнитура {(x * a) + (y * b) + (z * c)} рублей.')
