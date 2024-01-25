# # # # # # # Дан список чисел. Определите, сколько в нем встречается различных чисел.

# # # # # # # Input: [1, 1, 2, 0, -1, 3, 4, 4]

# # # # # # # Output: 6



# # # # # # # Примечание: Пользователь может вводить значения списка или список задан изначально.

# # # # # # import random
# # # # # # list_1 = []
# # # # # # size = random.randint(5,11)
# # # # # # for _ in range(size):
# # # # # #     num = random.randint(-10,10)
# # # # # #     list_1.append(num)
# # # # # # print(list_1)

# # # # # # list_2 = [random.randint(-10,10) for _ in range(size)]
# # # # # # list_3 = []
# # # # # # for num in list_1:
# # # # # #     if num not in list_3:
# # # # # #         list_3.append(num)
# # # # # # print(list_3)
# # # # # # print(len(list_3))

# # # # # import random
# # # # # list_1 = []
# # # # # size = random.randint(5,11)
# # # # # for _ in range(size):
# # # # #     num = random.randint(-10,10)
# # # # #     list_1.append(num)
# # # # # print(list_1)

# # # # # list_2 = [random.randint(-10,10) for _ in range(size)]
# # # # # list_3 = []
# # # # # for num in list_1:
# # # # #     if num not in list_3:
# # # # #         list_3.append(num)
# # # # # print(list_3)
# # # # # print(len(list_3))

# # # # # print(len(set(list_1)))
# # # # # # list_4 = [1 for num in list_1 if num not in list_3]
# # # # # # print(list_4)
# # # # # # print(sum(list_4))
# # # # # # list_5 = [1 if num not in list_3 else 0 for num in list_1]
# # # # # # print(list_5)
# # # # # #
# # # # # # list_6 = [4 if num%4 == 0  
# # # # # #           else 2 if num%2 == 0 
# # # # # #           else 1 
# # # # # #           for num in list_1]
# # # # # # print(list_6)


# # # # # Дана последовательность из N целых чисел и число K. Необходимо сдвинуть 
# # # # # всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# # # # # Input:   [1, 2, 3, 4, 5] k = 3

# # # # # Output:  [3, 4, 5, 1, 2]

# # # # # Примечание: Пользователь может вводить значения списка или список задан изначально.


# # # # list_1 = [1, 2, 3, 4, 5]
# # # # k = int(input("Введите сдвиг : ")) % len(list_1)
# # # # for _ in range(k):
# # # #     last_num = list_1.pop()
# # # #     list_1.insert(0, last_num)
# # # #     # list_1.insert(0, list_1.pop())   или
# # # # print(list_1)


# # # Напишите программу для печати всех уникальных значений в словаре. 

# # # Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# # # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# # # Примечание: Список словарей задан изначально. Пользователь его не вводит



# # list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001", "VX":"S00712"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# # set_values = set() 
# # # 1
# # for dict_i in list_dicts:
# #     # print(dict_i)
# #     for key in dict_i:
# #         set_values.add(dict_i[key])
# # print(set_values)
# # # 2
# # for dict_i in list_dicts:
# #     set_values.update(dict_i.values())
    
# # print(set_values)


# list_1 = [0, -1, 5, 2, 3]
# count = 0

# #1
# for i in range(len(list_1)-1):
#     if list_1[i+1] > list_1[i]:
#         count +=  1

# print(count)

# #2 
# list_new = [1 for i in range(len(list_1)-1) if list_1[i+1] > list_1[i]]
# print(list_new)
# print(sum(list_new))


n = int(16)
count = 0
num = 1
while num < n:
    num =2**count
    if(num <= n):
        print(num)
        print(count)
    count =+1
    