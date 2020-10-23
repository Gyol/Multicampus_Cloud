# join() 함수

colors = ['purple', 'yellow', 'blue']
result = ' '.join(colors)
print(result)
result = '/'.join(colors)
print(result)

# split() 함수
print()
langs = 'python, java, c#, go'
# 공백으로 구분하는 문자열인 경우에는 split()구분자를 주지 않아도 됨
result = langs.split(', ')
print(type(result), result)

# 일반적인 for loop
print()
my_list = []
for val in range(10):
    my_list.append(val)

print(my_list)

# List Comprehension (포괄적인 리스트)
print()
my_list2 = [val for val in range(10)]
print(my_list2)

my_list3 = [val if val % 2 == 0 else 10 for val in range(10)]
print(my_list3)


# LC - 문자열 타입
word1 = 'Hello'
word2 = 'World'
# for i in word1:
#    for j in word2:
#         print(i+j, end=' ')
m5y_list = [i+j for i in word1 for j in word2]
print(m5y_list)

m6y_list = [i+j for i in word1 for j in word2 if i == j]
print(m6y_list)

m7y_list = [i+j for i in word1 for j in word2 if i != j]
print(m7y_list)

# YESTERDAY
print()

lyric = 'Yesterday love was such an easy game to play'.split()
print(lyric)

for w in lyric:
    print(w.upper(), w.lower(), len(w), end=' - ')

print()
wlits = [] # 나중에 항목을 넣기 위해 일단 특정 변수를 공백 리스트로 만들어도 되겠구만...
for w in lyric:
    wlit = [w.upper(), w.lower(), len(w)]
#    print(wlist)
    wlits.append(wlit)
print(wlits)

print()
stuff = [[w.upper()] for w in lyric]
print(stuff)


#indexed traversal
print()
l_list = 'English Korean Japanese Chinese Spanish'.split()
# not recommended
for index in range(len(l_list)):
    print(f'idx = {index}, value = {l_list[index]}', end=' ')

print()
# recommended
for index, lang in enumerate(l_list):
    print(f'idx = {index}, value = {lang}', end=' ')

print()

print(enumerate(l_list))
print(list(enumerate(l_list)))

# Dict Comprehension
print()

m_dict = {index: val for index, val in \
          enumerate('Yesterday love was such an easy game to play'.split())}
print(m_dict)

# Variable Exchange
print()
a = 10
b = 20

#bad
tmp = a
a = b
b = tmp

a = 100
b = 200

# good
a, b = b, a
print(a, b)

# Sequence Unpacking
print()
a, b, *rest = [1, 2, 3]
print(a, rest)

a, *middle, c, d = [1, 2, 3, 4]
print(a, middle, d)

# do not recommend
print()
attr = 1
if attr == True :
    pass

# recommended
if attr:
    pass

attr = None

# not recommended
if attr == None:
    pass
# recommended
if attr is None:
    pass

# zip() 함수
print()
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(type(a), a, b, c)

for val in zip((1, 2, 3), (10, 20, 30), (100, 200, 300)):
    print(type(val), val)
