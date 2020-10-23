# Product 클래스 선언
class Product(object):
    # 생성자
    def __init__(self, name):
        # 밑에꺼가 private 변수지 __가 있으니까
        self.__name = name
    def __str__(self):
        return 'Product의 이름은 {}'.format(self.__name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

# 객체생성
product = Product('TV')
# print(product.__name)
# Traceback (most recent call last):
#   File "D:/Python_MC/mypython/python_programming_stu/mycode/class_oop/encapsulation.py", line 12, in <module>
#     print(product.__name)
# AttributeError: 'Product' object has no attribute '__name'
# 10-12줄 없이 이 주석 최상단처럼 만들어서 실행하면 이런 오류가 떠여
# 아래는 getter 함수 호출
print(product.name)
# setter 함수 호출
