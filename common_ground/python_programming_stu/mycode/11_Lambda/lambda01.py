# 보통 함수
def add(x, y):
    return x + y
print(add(10, 20))

# lambda
add2 = lambda x, y : x + y
print(add2(100, 200))

# 제곱승, 곱하기, 나누기를 람다 함수로 정의해서 호출
print()

multi = lambda x, y : x ** y
print(multi(2, 4))

mul = lambda x, y : x * y
print(mul(18, 2))

dev = lambda x, y : x / y
print(dev(20, 4))

mulmul = lambda x: x * 2
print(mulmul(3))\

print()
llist = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, llist)
print(list(result))
result = list(map(lambda x: x * 2, llist))
print(result)

# [1, 2, 3, 4, 5] + [1, 2, 3, 4, 5]
# add(1, 1) add(2, 2) add(3, 3)
print()
ddist = [13, 14, 15, 16, 17]
f_add = lambda  x, y: x + y
print(f_add(1, 88))
result = list(map(f_add, llist, ddist))
print(result)

# llist 값을 제곱승해서 다른 리스트에 저장
# lambda 함수랑 map()함수 사용
other = lambda x: x ** 2
# 얘네는 한번에
# result = list(map(other, llist))
# print(result)

# 이러면 하나씩
result = map(other, llist)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# filter 함수
print()
result = list(filter(lambda x: x > 2, llist))
print(result)

for a in filter(lambda x: x > 2, llist):
    print(a)

# reduce
# functools.py 라는 모듈 안에 있는 reduce함수를 불러오기
print()
from functools import reduce
result = reduce(lambda x, y: x + y, llist)
print(result)