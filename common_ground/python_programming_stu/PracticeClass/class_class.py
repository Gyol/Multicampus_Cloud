class Product(object):
    # 생성자
    def __init__(self, name):
        # name이 private변수
        self.__name = name
    def __str__(self):
        return 'Product의 이름은 {}'.format(self.__name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

