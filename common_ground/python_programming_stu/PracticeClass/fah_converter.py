#모듈명에서 특정 함수또는 클래스만 import 하기
#from PracticeClass import module_practice

#모듈명을 import 하면서 alias명 설정
#from PracticeClass import module_practice as fah

#모듈명을 import 하기
#import module_practice

#모듈에서 모든 함수또는 클랫 import 하기
from PracticeClass.module_practice import *

temperature = float(input())
fa = convert_c_to_f(temperature)
print('섭씨온도 : ', temperature)
print('화씨온도 : ', fa)
say_hello()
