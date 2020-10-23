# raise를 쓰면 추상메서드라고 지정이되고 추상메서드가 있어야 추상클래스로 지정이 된대
# 근데 그게 뭔데 ㅎㅎ...
# 추상 클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용합니다.
# polymorphism 다형성은 뭐... one interface, multiple implementation
# 다양하게 구현은 되는데 인터페이스는 하나라고? 아이고 난 몰라
# subclass는 자식이 반드시 구현해야

# abstract method를 가진 부모 클래스 선언
class Animal(object):
    def __init__(self, name):
        self.name = name
    # 밑에가 abstract method
    # def sound(self):
    #     raise NotImplementedError('자식클래스에서 반드시 구현해야 함') # 이 에러를 일부러 발생시켰다는데 왜인지 모름
    # 아 오키 이제 안듯 raise로 일부러 에러 발생시키는거 방금 logging 이거 한다고 배움
    # 마치 비밀번호 만들때 반드시 특수문자를 포함해야합니다 처럼 안내문도 띄우고 뭐 그런비슷한걸로 추정
# 상속받자
class Cat(Animal):
    def sound(self):
        return 'Meow'
    def pet(self):
        return 'This is my cat'

class Dog(Animal):
    def sound(self):
        return 'Woof'
    def pet(self):
        return 'This is my dog'

my_ani = Animal('cat')
print(my_ani.name)
# my_ani.sound()
animals = [Cat('ccat'), Dog('ddog'), Dog('ddog')]
for ani in animals:
    print(ani.sound())
    print(ani.pet())