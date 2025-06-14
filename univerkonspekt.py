# from traceback import print_last
#
# arr = [1,2,3,4,5,"hello", 5.6, 'jfgj', 66, '88']
#
# def filter_by_type(arr):
#     new_arr_str = []
#     new_arr_int = []
#     for some in arr:
#         if type(some) is str:
#             new_arr_str.append(some)
#             print(new_arr_str)
#         elif type(some) is int:
#             new_arr_int.append(some)
#             print(new_arr_int)
#
#
#
# filter_by_type(arr)
from sys import int_info

# players = [19, 19, 26, 25, 20, 18, 30, 24, 27]
# number = 0
# for i in players:
#     if i > 20:
#         number += 1
# print("Кількість футболістів старших 20 років: " + str(number))



# dataset_1 = [
#     {"name": "Максим", "age": 17},
#     {"name": "Тарас", "age": 28},
# ]
# dataset_2 =[
#     {"name": "Петро", "age": 21},
#     {"name": "Василь", "age": 15},
# ]
# combinade_dataset = dataset_1 + dataset_2
# youngest_student = combinade_dataset[0]
# for student in combinade_dataset:
#     if student['age'] < youngest_student['age']:
#         youngest_student = student
# print(youngest_student)




# def find_words_with_letters_fxz(words):
#     words = words.rstrip('.')
#     words_space = words.split(',')
#     result = []
#     for word in words_space:
#         if 'f' in word or 'x' in word or 'z' in word:
#             result.append(word)
#     return result
# words = "book,pen,fox,zoo,apple,fine,good,zebra."
# result = find_words_with_letters_fxz(words)
# print(', '.join(result))


# Метод сортування бульбашкою

# nums = [18, 4, 6, 11, 10, 3, 16]
# n = len(nums)
#
# def bubble_sort(nums):
#     for j in range(n-1):
#         for i in range(n-1):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#     return nums
#
# print("Сортування числе від найменшошо до найбільшого:")
# print(bubble_sort(nums))





# Метод сортування вибіркою
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr


# nums = [18, 4, 6, 11, 10, 3, 16]
#
# def selection_sort(nums):
#     for i in range(len(nums)):
#         min_index = i
#         for j in range(i+1, len(nums)):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums
# print("Сортування числе від найменшошо до найбільшого:")
# print (selection_sort(nums))


# Метод сортування вставками

# nums = [18, 4, 6, 11, 10, 3, 16]
# n = len(nums)
#
# def insertion_sort(nums):
#     for i in range(1, n):
#         for j in range(i, 0, -1):
#             if nums[j] < nums[j - 1]:
#                 nums[j], nums[j - 1] = nums[j - 1],nums[j]
#     return nums
#
# print("Сортування числе від найменшошо до найбільшого:")
# print(insertion_sort(nums))




# Виведення чисел, які є степенями двійки

# def elements_with_power_of_two_indices_for(arr):
#
#   result = []
#   for i in range(len(arr)):
#     if i > 0 and i & (i - 1) == 0:
#       result.append(arr[i])
#   return result
#
# arr = [10, 20, 30, 40, 50, 60, 70, 80]
# print(elements_with_power_of_two_indices_for(arr))


# Бінарий пошук

# def binary_sort(arr, need):
#     first = 0
#     last = len(arr) - 1
#     while first <= last:
#         mid = (first + last) // 2
#         if arr[mid] == need:
#             return mid
#         elif arr[mid] < need:
#             first = mid + 1
#         else:
#             last = mid - 1
#
#     return 'NON'
#
# arr = [1,7,11,26,49,56,61,70,89]
# need = 56
# result = binary_sort(arr, need)
#
# if result != 'NON':
#     print(arr[result])
# else:
#     print('ТАКОГО ЧИСЛА НЕМАЄ')



# N = int(input("Введіть число N: "))  # Вводимо число N
# total_sum = 0  # Ініціалізуємо змінну для зберігання суми
#
# # Використовуємо цикл for для обчислення суми
# for i in range(1, N + 1):
#     total_sum += i  # Додаємо поточне число до суми
#
# print(f"Сума чисел від 1 до {N}: {total_sum}")











# n = int(input())
# a = input().split()
# suma_numbers = 0
# for i in a:
#     suma_numbers += int(i)
# print(suma_numbers - n)


# n = int(input())
# nominals = [500, 200, 100, 50, 20, 10, 5, 2, 1]
# count = 0
# for nominal in nominals:
#         count += n // nominal
#         n %= nominal
# print(count)

# # n = input()
# # m = n.split()
# # a = int(m[0])
# # b = int(m[1])
# # c = int(m[2])
# #
# # if a + b > c:
# #         print('YES')
# # else:
#         print('NO')
#
# name = str(input())
# age = int(input())
# year = 2025
# sto = 100
# year100 = year + sto - age
# print(year100)
# print(2025 + 83)

# arr = [2, 3 , 5, 8, 27, 31, 16]
# # arrspl =
# # for i in arr:
# #     if i % 2 == 0:
# #         print(i)
# lviv, kyiv, donetsk, kharkiv = map(int, input().split())
# sum = lviv + kyiv + donetsk + kharkiv
# print(sum)
# n = input()
# m = n.split()
# a = int(m[0])
# b = int(m[1])
# c = int(m[2])
#
# if a + b > c:
#         print('YES')
# else:
#         print('NO')

# n, m = map(int, input().split())
# zenyk = map(int, input().split())
# marichka = map(int, input().split())
# minzen = min(zenyk)
# minmar = min(marichka)
# print(minzen + minmar)

# a, b = map(int, input().split())
#
# if abs(a - b) <= 1:
#     print(-1)
# else:
#     if a < b:
#         print(a + 1)
#     else:
#         print(b + 1)

# s = input()
# same_word = set(s)
# print(len(same_word))

# k, n = map(int, input().split())
# c = list(map(int, input().split()))
# c.sort()
# count = 0
# for i in c:
#     if k >= i:
#         k -= i
#         count += 1
#     else:
#         break
# print(count)
#
# a, b, k = map(int, input().split())
# print(a + (b*k))

# x = input()
# count = 0
# for i in x:
#     if i == "4" or i == "7":
#         count += 1
# print(count)
# a, b = map(int, input().split())
# if abs(a - b) <= 1:
#     print(-1)
# elif a < b:
#     print(a + 1)
# else:
#     print(b + 1)

# n = int(input())
# m = map(int, input().split())
# for i in m:


# v = int(input())
# print(225000000 / v)

# n = int(input())
# m = list(map(int, input().split()))
# m.sort()
# for i in range(1, len(m)):
#     if m[i] - m[i - 1] < 2:
#         print("NO")
#         break
# else:
#     print("YES")


# n = int(input())
# coordinates = list(map(int, input().split()))
# for i in range(1, n):
#     if coordinates[i] - coordinates[i-1] < 2:
#         print("NO")
#         break
# else:
#     print("YES")

# suma_1, suma_2 = 0, 0
# # try:
# with open('n.txt', 'r', encoding='utf-8') as f:
#     for i in f:
#         suma_1 += int(i[:2])
#         suma_2 += int(i[3:])
#     print(f'{suma_1}:{suma_2}')
# # except:
# #     print("Erorr")



