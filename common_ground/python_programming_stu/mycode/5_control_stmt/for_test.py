import random

#for ~ in 구문 사용

for val in [0,1,2]:
    print(val, end=' ')

#range(start, end, 증가치) function
print()
for val in range(0,10):
    print(val, end=' ')

print()
for val in range(0, 20, 4):
    print(val, end=' ')


#문자열 타입
print()
fav_hobby = ['drinking', 'sleeping', 'reading']
for hobby in fav_hobby:
    print('{} is my favorite hobby'.format(hobby))

#dict 타입
bucketlist_city = {'Busan':'Korea', 'Auckland':'New Zealand'}
print(type(bucketlist_city))
print(bucketlist_city['Busan'])
#key, value를 출력할 때 keys() 함수
print()
for city in bucketlist_city.keys():
    print('{} is in {}'.format(city, bucketlist_city[city]))

#key, value를 출력할 때 items() 함수
print()
for city, country in bucketlist_city.items():
    print(f'{city} in {country}')

print()
for val in range(-1, 4):
    ticket = random.randint(1,100)
    print('Your ticket number is ', ticket)

#while
print()
idx = 0
while idx < 10:
    if idx == 7: break
    print(idx, end=' ')
    idx += 2

print()
print('continue--------')
for val in range(10):
    if val == 5:
        continue
    print(val, end=' ')
