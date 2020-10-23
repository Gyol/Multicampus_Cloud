# 1. %formatting: C언어 스타일
# 2. String format 함수: {}에 대응하는 값을 format()의 인자로 전달
# 3. f-string: python3.6 이상에서만 사용

# Formatting https://pyformat.info/

temperature = 36
print('1. 온도 값은 %d'%(temperature))
print('2. 온도 값은 {}'.format(temperature))
print(f'3. 온도 값은 {temperature}')

# Padding
print('product {0:10s}, price per unit {1:10.3f}'.format('Apple', 5.243))
print(('product {0:>10s}, price per unit {1:10.3f}').format("Apple", 5.243))

greet = ('\n' + 'Hello')
print(greet)
print(greet + greet)
print("I like 'Apple' ")
print('I like \'Python\'')

my_int = 100
# flag = boolean타입의 함수? https://www.pythonforbeginners.com/basics/boolean
# The bool() function allows you to evaluate any value, and give you True or False in return.
flag = True
print(type(my_int), type(flag))
result = str(my_int) + str(flag)
print(type(result), result)

# 문자열 인덱스
greeting = 'HELLO WORLD!'
print(greeting[1])
print(greeting[11])
# print(greeting[12])

# 문자열 slicing
print(greeting[2:5])
print(greeting[5:])
print(greeting[:5])
print(len(greeting))

# str의 여러 함수들 사용하기
print(' ')
word = 'GOOD manufacturing Practice'
print(word)
print(word.upper())
print(type(word.split(' ')), word.split(' '))
word = word.upper()
print(word)
word = word.lower()
print(word)

# str -> list: packing
print(' ')
my_wordlist = word.split(' ')
print(my_wordlist)

#list -> str: unpacking
print(' ')
str1, str2, str3 = my_wordlist
print(str1)
print(str2)
print(str3)

