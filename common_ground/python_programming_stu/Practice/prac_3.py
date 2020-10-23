from functools import*
# my_arr 리스트의 값을 제곱승해서 다른 리스트에 저장하세요
# lambda 함수와 map() 함수 사용

my_arr = [1, 2, 3, 4, 5, 6]
my_result = list(map(lambda x: x ** 2, my_arr))
print(my_result)

result = map(lambda x: x ** 2, my_arr)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

fil_result = list(filter(lambda x: x > 2, my_arr))
print(fil_result)

for val in filter(lambda x: x >10, my_result):
    print(val)

result = reduce(lambda x, y: x + y, my_arr)
print(result)