# python_programming_stu 밑에 import하려는게 있으면 from 안하고 그냥 import해도 됨
# 근데 이건 그 밑에 별도의 폴더안에 있으니까 from해줘
# 1. 모듈명 import하기
from mycode import fahconverter
# 2. 모듈명을 import하면서 alias명 설정하기
from mycode import fahconverter as nah
# 3. 모듈에 속한 함수만 import하기
from mycode.fahconverter import convert_c_to_f
# 4. 모듈에 속한 모든 함수 import하기
from mycode.fahconverter import * # 저 별이 무슨 역할을 하길래 저 위에꺼가 비활성화된거지? 설명 들은 것 같은디




print('변환하고 싶은 섭씨 온도를 입력해 주세요: ')
temperature = int(input())

# -1. 모듈명.convert_c_to_f() 함수 호출
fah = fahconverter.convert_c_to_f(temperature)
# -2. aliaing된 모듈명.convert_c_to_f() 함수 호출
fah = nah.convert_c_to_f(temperature)
# -3. import된 함수 호출
fah = convert_c_to_f(temperature)

# print(temperature)
print('섭씨온도: ', temperature)
print('화씨온도: ', fah)
print('화씨온도 = {:.2f}'.format(fah))

print(say_hello('Bye'))