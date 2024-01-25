# # def fib(count):                                                    # Изначально fib(7)
# #     if count in (1, 2):
# #         return 1
# #     return fib(count - 1) + fib(count - 2)                         # fib(7) = fib(6) + fib(5)
# #                                                                    # fib(count) = fib(count-1) + fib(count-2)

# # num = int(input("Введите порядковый номер числа Фибоначи: "))      #Ввели 7
# # print(fib(num))                                                    #Вызываем функцию fib(7)

# # Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия,
# #  но наоборот: все максимальные – на минимальные.
# # Input: 5 -> 1 3 3 3 4

# # Output: 1 3 3 3 1

# # #Решение 1
# # import random

# # def max_to_min(list_marks):
# #     min_mark = min(set(list_marks)) #находим минимальную оценку
# #     max_mark = max(set(list_marks)) #находим максимальную оценку
# #     return [min_mark if mark == max_mark else mark for mark in list_marks]

# # count_marks = int(input("Введите количество оценок: ")) #создание списка оценок
# # old_list_marks = [random.randint(1,5) for _ in range(count_marks)] #list comprehesions

# # print(old_list_marks)
# # print(max_to_min(old_list_marks))

# # рещение 2

# # import random

# # def max_to_min2(list_marks):
# #     min_mark = list_marks[0]
# #     max_mark = list_marks[0]
# #     i_max_marks = [0]
# #     for i in range(1, len(list_marks)):
# #         if list_marks[i] > max_mark:
# #             max_mark = list_marks[i] 
# #             i_max_marks = [i]
# #         elif list_marks[i] == max_mark: #находим индексы
# #             i_max_marks.append(i)
# #         if list_marks[i] < min_mark:
# #             min_mark = list_marks[i]
# #     for i in i_max_marks:
# #         list_marks[i] = min_mark

    

# # count_marks = int(input("Введите количество оценок: ")) #создание списка оценок
# # old_list_marks = [random.randint(1,5) for _ in range(count_marks)] #list comprehesions

# # print(old_list_marks)
# # max_to_min2(old_list_marks)
# # print(old_list_marks)


# # Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# # Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)


# # Input: 5

# # Output: yes

# # def is_prime_num(num):
# #     if num == 2:
# #         return "yes"
# #     for div in range(2, num):
# #         if num % div == 0:
# #             return "no"
# #     return "yes"


# # n = int(input("Введите число больше 1: "))
# # print(is_prime_num(n))

# # второй вариант
# # def is_prime_num(num):
# #     if num not in (2, 3, 5, 7) \
# #         and (num % 2 == 0 or num % 3 == 0  or num % 5 == 0  or num % 7 == 0):
# #         return "no"
# #     for div in range(3, int(num ** 0.5) + 1, 2):
# #         if num % div == 0:
# #             return "no"
# #     return "yes"


# # n = int(input("Введите число больше 1: "))
# # print(is_prime_num(n))

# # Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# # Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# # Input:    2 -> 3 4
# # Output: 4 3




# def reverse_nums(counter):
#         # pass    #заглушка
#     if counter < 1:
#         return "" 
#     current_num = input("Введите число: ")
#     return reverse_nums(counter - 1) + current_num + " "

# n = int(input("Введите кол-во чисел N: "))
# print(reverse_nums(n))


# def reverse_nums(counter):
#     if counter == 1:
#         current_num = input("Введите число: ")
#         return current_num + " "
#     current_num = input("Введите число: ")
#     return reverse_nums(counter - 1) + current_num + " "

# n = int(input("Введите кол-во чисел N: "))
# print(reverse_nums(n))