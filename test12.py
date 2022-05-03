# x = int(input())
# if x > 0:
#     print(x * 2)
# else:
#     print(x)

# x = int(input())
# if x > 0:
#     print(x * 3)

# x, y = input().split()
# x, y = int(x), int(y)
# if x > y:
#     print('Первое больше')
# if x < y:
#     print('Второе больше')
# if x == y:
#     print('Равны')

# x, y = input().split()
# x, y = int(x), int(y)
# count = 0
# if x > 0:
#     count += 1
# if y > 0:
#     count += 1
# print(count)

# x, y, z = input().split()
# x, y, z = float(x), float(y), float(z)
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2
# print(x, y, z)

# x = int(input())
# if x > 0:
#     print(1)
# elif x < 0:
#     print(-1)
# elif x == 0:
#     print(0)

# x, y, z = int(input()), int(input()), int(input())
# count = 0
# if x < 0:
#     count += x
# if y < 0:
#     count += y
# if z < 0:
#     count += z
# print(count)

# x, y, z = input().split()
# x, y, z = int(x), int(y), int(z)
# count = 0
# if x % 2 == 0:
#     count += 1
# if y % 2 == 0:
#     count += 1
# if z % 2 == 0:
#     count += 1
# print(count)

# x, y = input().split()
# x, y = int(x), int(y)
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# n = int(input())
# list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# print(list[n - 1])

# n = int(input())
# if n > -1:
#     print('неотрицательное')
# else:
#     print('отрицательное')

# n = int(input())
# if n % 2 != 0:
#     print('Нечетное')
# else:
#     print('Четное')

# n = input()
# z = int(n[0]) + int(n[1])
# if len(str(z)) == 2:
#     print('Да')
# else:
#     print('Нет')

# n = input()
# z = int(n[0]) + int(n[1]) + int(n[2])
# if z % 3 == 0:
#     print('Да')
# else:
#     print('Нет')

# n = input()
# if n[0] == n[1] or n[0] == n[2] or n[1] == n[2]:
#     print('Да')
# else:
#     print('Нет')

# x, y, z = input().split()
# if x == y == z:
#     print('равносторонний')
# else:
#     print('неравносторонний')

# n = int(input())
# if -2 < n < 2:
#     print('Да')
# else:
#     print('Нет')

# n = input().split()
# z = []
# for i in n:
#     z.append(float(i))
# z = sorted(z)
# for k in z:
#     if 1.5 <= k <= 2.5:
#         print(k)

# n = int(input())
# if (n % 10 == 2 or n % 10 == 5) or (n // 10 == 2 or n // 10 == 5):
#     print('Да')
# else:
#     print('Нет')

# n = int(input())
# if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
#     print('високосный')
# else:
#     print('невисокосный')

# n = input().split()
# a, b = int(n[0]), int(n[1])
# if a > b:
#     print('больше')
# elif a < b:
#     print('меньше')
# else:
#     print('равны')

# n = int(input())
# list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# print(list[n - 1])

# n = int(input())
# list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# print(list[n - 1])

# n = input()
# if len(n) == 3:
#     print('трехзначное')
# elif len(n) == 2:
#     print('двузначное')
# else:
#     print('однозначное')

# n = input().split()
# a, b, c = int(n[0]), int(n[1]), int(n[2])
# if a == b == c:
#     print('равносторонний')
# elif a == b or a == c or b == c:
#     print('равнобедренный')
# else:
#     print('разносторонний')

# x, y = input().split()
# x, y = int(x), int(y)
# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# elif x > 0 and y < 0:
#     print('4 четверть')
# else:
#     print('лежит на оси')

# n = int(input())
# z = 0
# if n > 0:
#     z = n
# elif n == 0:
#     z = -1
# else:
#     z = n ** 2
# print(z)

# n = int(input())
# if n == 3:
#     print('выигрыш')
# elif n == 1:
#     print('ничья')
# elif n == 0:
#     print('проигрыш')
# else:
#     print()

# n = input().split()
# a, b, c = int(n[0]), int(n[1]), int(n[2])
# d = b ** 2 - 4 * (a * c)
# if d < 0:
#     print('нет корней')
# elif d == 0:
#     print('один корень')
# else:
#     print('два корня')

# n = input().split()
# x = int(input())
# a, b = int(n[0]), int(n[1])
# if x == 1:
#     print(a + b)
# elif x == 2:
#     print(a - b)
# elif x == 3:
#     print(a * b)
# else:
#     print(a / b)

# print(*[10 for i in range(20)], sep='\n')

# x, y = input().split()
# x, y = int(x), int(y)
# for i in range(x, y + 1):
#     print(i)

# print(*[i for i in range(2, 201, 2)], sep=' ')

# print(*[i ** 2 for i in range(1, int(input()) +1)], sep=' ')

# for i in range(1, 10):
#     print('6 *', i, '=', 6 * i)

# n = []
# [n.append(i) for i in range(-100, 101)]
# print(*n[::-1])

# summ = 0
# for i in range(100, 501):
#     summ += i
# print(summ)

# summ = 1
# for i in range(5, 21):
#     summ *= i
# print(summ)

# x, y = input().split()
# x, y = int(x), int(y)
# summ = 0
# count = 0
# for i in range(x, y + 1):
#     summ += i
#     count += 1
# print(summ, count, sep='\n')

# x, y = int(input()), int(input())
# summ = 0
# for i in range(x, y +1):
#     summ += (i ** 2)
# print(summ)

# a = 11
# while a <= 100:
#     print(a, end=" ")
#     a = a + 2
# print(a)

# a, b = map(int, input().split())  # НОД двух чисел
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

# n = int(input())
# z = []
# while n > 1:
#     n -= 1
#     z.append(n)
# print(*z[::-1])

# n = int(input())
# z = 1
# while z ** 2 < n:
#     print(z ** 2, end=' ')
#     z += 1

# n = int(input())
# z = 1
# while z ** 2 <= n:
#     z += 1
# print(z ** 2)

# n = int(input())
# while n > 10:
#     n //= 10
# print(n)

# n = int(input())
# summ = 0
# while n != 0:
#     summ += n % 10
#     n = n // 10
# print(summ)

# n = int(input())
# summ = 0
# while n != 0:
#     if n % 10 == 5:
#         summ += 1
#     n //= 10
# print(summ)

# n = int(input())
# summ = 0
# while True:
#     summ += n
#     n = int(input())
#     if n == 0:
#         break
# print(summ)

# n = int(input())
# count = 0
# while True:
#     if n % 5 == 0:
#         count += 1
#     n = int(input())
#     if n == -1:
#         break
# if count == 0:
#     print('нет')
# else:
#     print('да')

# n = int(input())
# count = 0
# z = []
# while True:
#     x = int(input())
#     count += 1
#     if x > n:
#         z.append(count)
#     if x == 500:
#         break
# print(z[0])

# n = int(input())  # !!!
# count = 0
# while True:
#     x = int(input())
#     count += 1
#     if x > n:
#         print(count)
#         break
#     if x == 500:
#         break

# summ = 0
# count = 0
# while True:
#     n = int(input())
#     if n < 0:
#         break
#     count += 1
#     summ += n
# [print('да') if summ % count == 0 else print('нет')]

# a, b = int(input()), int(input())
# count = 0
# for i in range(a, b +1):
#     if i % 2 == 0:
#         count += 1
# print(count)

# n = int(input())
# count = 0
# while n != 0:
#     if n % 2 == 0 and n % 7 == 0:
#         count += 1
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# min = 30000
# while n != 0:
#     if n % 3 == 0 and n < min:
#         min = n
#     n = int(input())
# print(min)

# n = int(input())
# count = 0
# summ = 0
# while n != 0:
#     if n % 9 == 0:
#         summ += n
#         count += 1
#     n = int(input())
# [print('NO') if summ == 0 else print(summ / count)]

# n = int(input())
# count = 0
# summ = 0
# while n != 0:
#     if n % 10 == 1:
#         summ += n
#         count += 1
#     n = int(input())
# [print('NO') if summ == 0 else print(summ / count)]

# n = int(input())
# count = 0
# summ = 0
# while n != 0:
#     if n % 17 == 0:
#         summ += n
#         count += 1
#     n = int(input())
# [print('NO') if summ == 0 else print(summ, count)]

# n = int(input())
# count = 0
# while n != 0:
#     if n % 5 == 0 or n % 7 == 0:
#         count += 1
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# summ = 0
# while n != 0:
#     if len(str(n)) == 2:
#         summ += n
#         count += 1
#     n = int(input())
# [print('NO') if summ == 0 else print(summ / count)]

# answers = [int(input()) for i in range(int(input()))]
# res = [i for i in answers if i == 0]
# print('YES' if res else 'NO')

# max = 0
# answ = 0
# k = int(input())
# for i in range(k):
#     n = int(input())
#     if n == 0:
#         answ += 1
#     if n > max:
#         max = n
# print(max)
# [print('YES') if answ > 0 else print('NO')]

# count = 0
# summ = 0
# k = int(input())
# for i in range(k):
#     n = int(input())
#     if n > 7:
#         count += 1
#         summ += n
# print(count, summ / count, sep='\n')

# summ = 0
# count = 0
# k = int(input())
# for i in range(k):
#     n = int(input())
#     if n < 5:
#         count += 1
#     if n == 10:
#         summ += 1
# print(count)
# [print('YES') if summ > 0 else print('NO')]

# summ = 0
# count = 0
# k = int(input())
# for i in range(k):
#     n = int(input())
#     if n > 0:
#         count += 1
#         summ += n
# print(summ / count, count, sep='\n')

# summ = 0
# count = 0
# zero = 0
# k = int(input())
# for i in range(k):
#     n = int(input())
#     if n > 0:
#         zero += 1
#     summ += n
#     count += 1
# print(summ / count)
# [print('YES') if zero > 4 else print('NO')]

# summ = 0
# k = int(input())
# for i in range(k):
#     n = int(input())
#     if n < summ:
#         summ = n
# print(summ)
# [print('YES') if summ < -15 else print('NO')]

# k = int(input())
# a, b = 1, 1
# min = 10000
# for i in range(k):
#     x, y = input().split()
#     x, y = int(x), int(y)
#     a = x * 60
#     b = y
#     if (a + b) <= min:
#         min = (a + b)
# h = min // 60
# m = min - (h * 60)
# print(h, m)

# n = int(input())
# count = 0
# time = 1110
# for i in range(n):
#     x, y = input().split()
#     x, y = int(x) * 60, int(y)
#     if (x + y) <= time:
#         count += 1
# print(count)

# n = int(input())
# count = 0
# while n > 0:
#     if n % 5 == 0 or n % 9 == 0:
#         count += 1
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# while n != 0:
#     if len(str(n)) == 2:
#         if n % 8 == 0:
#             count += 1
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# while n != 0:
#     if n % 10 == 2 and n % 4 == 0:
#         count += 1
#     n = int(input())
# print(count)

# n = int(input())
# count = 0
# while n != 0:
#     if n % 6 == 0 or n % 11 == 0:
#         count += 1
#     n = int(input())
# print(count)
