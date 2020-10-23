# # 일반적인 함수 정의
# def add(x, y):
#     return x + y
#
#
# print(add(10, 20))
#
# # 람다식 사용
# my_add = lambda x, y: x + y
# print(my_add(10, 34))
#
# square = lambda x: x ** 2
# print(square(4))
#
# multi = lambda x, y: x * y
# print(multi(40, 3))
#
# division = lambda  x, y: x / y
# print(division(50, 5))

my_arr = [1, 2, 3, 4, 5]
my_arr2 = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, my_arr)
print(list(result))

result = list(map(lambda x: x * 2, my_arr))
print(result)

result = list(map(lambda x, y: (x + y) * 6, my_arr, my_arr2))
print(result)
