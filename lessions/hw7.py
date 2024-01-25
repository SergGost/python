#  Винни Пух

# # Инструкция по использованию платформы



# # Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

# # Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# # Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# # Фразы отделяются друг от друга пробелами.

# # Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# # Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# # Пример

# # На входе:


# # stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# # На выходе:


# # Парам пам-пам

# # #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# # #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# # #stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# # # Введите ваше решение ниже


# def cntVowLet(phrase):
#     vowLet = "аеёиоуыэюя"
#     cnt=0
#     for let in phrase:
#         if let in vowLet:
#             cnt += 1
#     return cnt


# def check_rifm(poem):
#     vowel_0 = cntVowLet(poem[0])
#     for phrase in poem[1:]:
#         if cntVowLet(phrase) != vowel_0:
#             return "Пам парам"
#     return "Парам пам-пам"



# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# print(check_rifm(stroka))

# # 2ой вариант

# def rhyme_check(rhyme_list):
#     if len(rhyme_list) >= 2:
#         count_ = list(map(lambda x: x in vow_list, rhyme_list[0])).count(True)
#     for str_ in rhyme_list[1:]:
#         if count_ != list(map(lambda x: x in vow_list, str_)).count(True):
#             return "Пам парам"
#         return "Парам пам-пам"
#     else:
#         return "Количество фраз должно быть больше одной!"

# vow_list = "аеёиоуыэюя"

# splited_list = list(stroka.lower().split())
# print(rhyme_check(splited_list))






# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Пример

# На входе:


# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:


# 1 2 3
# 2 4 6 
# 3 6 9


# #При отправке кода на Выполнение раскомментируйте строку ниже,
# чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно -
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# #print_operation_table(lambda x, y: x * y, 3, 3)


# def basic_table(x, y):
#     basic_list = [[]]
#     for i in range(x+1):
#         basic_list.append([i+2])
#     for j in range(1, y +1):
#         basic_list[0].append([j])

#     for i in range(1,x):
#         for j in range(1, y):
#             basic_list[i].append("")
#     return(basic_list)


# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     res_list = basic_table(num_rows, num_columns)
#     print(*res_list[0])
#     for i in range(1, num_rows):
#         for j in range(1, num_columns):
#             res_list[i][j] = operation(i+1, j+1) 
#     print(*res_list[i])
    
    


# def basic_table(x,y):
#     basic_list = [[]]
#     for i in range(x+1):
#         basic_list.append([i+2])
#     for j in range(1,y + 1):
#         basic_list[0].append(j)
    
#     for i in range(1,x):
#         for j in range(1,y):
#             basic_list[i].append("0")
#     return(basic_list)


# def print_operation_table(operation, num_rows, num_colums):
#     if num_rows < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     if num_rows and num_colums == 0:
#         print("Ошибка")
#     res_list = basic_table(num_rows, num_colums)
#     print(*res_list[0])
#     for i in range(1,num_rows):
#         for j in range(1,num_colums):
#             res_list[i][j] = operation(i + 1, j + 1)
#         print(*res_list[i])




#print_operation_table(lambda x, y: x * y, 3, 3)

#print_operation_table(lambda x, y: x * y)

def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))

print_operation_table(lambda x, y: x * y)