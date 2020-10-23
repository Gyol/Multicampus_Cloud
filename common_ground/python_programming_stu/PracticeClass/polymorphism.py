# abstract method를 가진 부모 클래스 선언
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('자식클래스에서 구현이 안되있음!')


class Cat(Animal):
    def talk(self):
        return '야옹'


class Dog(Animal):
    def talk(self):
        return '멍ㅁ멍'

    def pet(self):
        return 'I am pet'


my_ani = [Cat('고양이'), Dog('강아지'), Dog('멍멍이')]
for ani in my_ani:
    print(ani.talk())
