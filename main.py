import mymodule

# from mymodule import password
#
# for i in range(12):
#     print(password())

# from random import *
# words_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие",
#               "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница",
#               "магазин", "председатель", "сотрудник", "республика", "личность"]
# get_word = choice(words_list).upper()
#
# # функция получения текущего состояния
# def display_hangman(tries):
#     stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / \\
#                    -
#                 ''',
#                 # голова, торс, обе руки, одна нога
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     /
#                    -
#                 ''',
#                 # голова, торс, обе руки
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |
#                    -
#                 ''',
#                 # голова, торс и одна рука
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|
#                    |      |
#                    |
#                    -
#                 ''',
#                 # голова и торс
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |
#                    -
#                 ''',
#                 # голова
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |
#                    |
#                    |
#                    -
#                 ''',
#                 # начальное состояние
#                 '''
#                    --------
#                    |      |
#                    |
#                    |
#                    |
#                    |
#                    -
#                 '''
#     ]
#     return stages[tries]
# def play(word):
#     word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
#     guessed = False  # сигнальная метка
#     guessed_letters = []  # список уже названных букв
#     guessed_words = []  # список уже названных слов
#     tries = 6  # количество попыток
#     print('Привет, давай сыграем в висельницу!')
#
#     while guessed == False:
#         word_test = word
#         print(display_hangman(tries))
#         print(word_completion)
#         bukva = input('Угадай букву или назови слово целиком: ')
#         while bukva.isalpha() == False or ((len(bukva) == 1 and bukva in guessed_letters) or (len(bukva) == len(word) and bukva in guessed_words)) or (len(bukva) != 1 and len(bukva) != len(word)):
#             bukva = input('Угадай букву или назови слово целиком: ')
#         if len(bukva) == len(word):
#             guessed_words += [bukva]
#             if bukva.upper() == word:
#                 word_completion = word
#             else:
#                 tries -= 1
#         elif len(bukva) == 1:
#             guessed_letters += bukva
#             while bukva.upper() in word_test:
#                 x = word_test.find(bukva.upper())
#                 word_completion =  word_completion[:x] + bukva.upper() +  word_completion[x + 1:]
#                 word_test = word_test.replace(word_test[x], '_', 1)
#             print(word_completion)
#             if bukva.upper() not in word:
#                 tries -= 1
#         if '_' not in word_completion:
#             print(f'Поздравляем, вы угадали слово {word.upper()}!')
#             guessed = True
#             break
#         if tries == 0:
#             print(f'К сожалению, вы проиграли, было загадано слово {word.upper()}')
#             break
#
# word = get_word
# play(word)
#
# vopros = 'да'
# while vopros == 'да':
#     vopros = input('Сыграем еще? да / нет: ')
#     while vopros != 'да' and vopros != 'нет':
#         vopros = input('Сыграем еще? да / нет: ')
#     if vopros == 'да':
#         get_word = choice(words_list).upper()
#         word = get_word
#         play(word)
# print('Всего хорошего!')




