# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
#  Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

##1

# list_text = "a a a b c a a d c d d".split()
# print(list_text)
# dict1 = {}
# for letter in list_text:
#     if letter not in dict1:
#         dict1[letter] = 0
#         print(letter, end=' ')
#     else:
#         dict1[letter] += 1
#         #print(letter, dict1[letter], end=' ', sep='_') #первый варинт
#         print(f"{letter}_{dict1[letter]}", end=' ')       # второй вариант
        
        
# ## 2

# list_text = "a a a b c a a d c d d".split()
# print(list_text)
# dict1 = {}
# for letter in list_text:    
#     if letter not in dict1:
#         print(letter, end=' ')
#     else:
#         print(f"{letter}_{dict1[letter]}", end=' ')
#     dict_get = dict1.get(letter, 0) # берет из списка и возвращает его (обьект, и на что меняем)
#     dict1[letter] = dict_get + 1 
    
    
# Пользователь вводит текст(строка). Словом считается последовательность непробельных 
# символов идущих подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells\
#         I'm sure So if she sells sea shells on the sea shore\
#         I'm sure that the shells are sea shore shells")
# list_text = text.lower().split()
# #print(list_text)
# print(set(list_text))

# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells "
#         "I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells").lower().split()
# # sum = 0
# # dict1 = {}
# # for n in text:
# #     if n not in dict1:
# #         dict1[n] = 1
# #         sum += dict1[n]
# # print(sum)

# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells"\
#         " sea shells on the sea shore I'm sure that the shells are sea shore shells")
# list_text = text.lower().split() #делаем все буквы нижним ригистром( маленькие )
# print(list_text)

# print(set(list_text)) # делаем множесто( список )
# print(len(set(list_text)))  #считаем длину строки

# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells "
#         "I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells")
# text_list = text.lower().split()
# summa = 0
# doubles = []
# for letter in text_list:
#     if letter not in doubles:
#         doubles.append(letter)
#         summa += 1
# print(summa)

# print(len(set(text.lower().split())))


# 2) Задача – «На вход программе подаются натуральные числа,как только пользователь введёт 0 ввод прекращается. Вывести наибольший элемент получившейся последовательности». 
# Есть два кода с ошибками, нужно определить  где ошибок меньше.

# Примечание: Программные коды на следующих слайдах

# Ваня:

# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)

# n = int(input())
# max_number = n   # max_number = 1000 1 ошибка
# while n != 0:
#    n = int(input())
#    if max_number < n:  # искали самое маленькое
#        max_number = n
# print(f"{max_number = }")




# Петя:

# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)



n = int(input())
max_number = -1
while n != 0: # 1 while n < 0:
    if max_number < n:
       max_number = n # 3 n = max_number
    n = int(input()) # 2 не тут стояла строка
print(f"{max_number= }") # 4 print(n)





