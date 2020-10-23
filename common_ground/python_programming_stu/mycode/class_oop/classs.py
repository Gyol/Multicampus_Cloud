# class 선언
class SoccerPlayer(object):
    # 생성자 선언 - 객체가 생성될 때 자동으로 호출되는 함수
    def __init__(self, name, position, back_number):
        # access modifier가 public = class를 호출한 페이지(?)에서도 쓸 수 있다 이런 차이
        # python에서는 private이라는 키워드가 없어서 클래스 내부에서만 사용되는 변수를 만들려면
        # 변수명 앞에 __를 붙임.. ex) self.__year = year같은 식.
        # 자바에서는 아예 public int getYear() 같은 식으로...
        # 변수를 직접 변경하려면 하여간에
        # def year():
            # return self.__year 이런식으로 섹터? 를 먼저 정해주고 하라는거야
        # def year(year):
            # self.__year = year 이런식으로 변경했으면
        # myDate.__year(2005) 이런식으로 못한다는거여
        self.name = name
        self.position = position
        self.back_number = back_number

    # 일반함수 (instance methon), back_number 값을 입력받아서 변경하는 함수
    # 함수의 첫 번째 파라미터에 self가 있어야 클래스에 속한 함수가 됨
    # 첫 번째 파라미터의 이름은 self가 아니어도 노상관
    def change_back_number(self, new_number):
        print(f'선수의 등번호를 변경합니다. from {self.back_number} to {new_number}')
        self.back_number = new_number

    # toString() 매서드와 동일한 역할
    # 객체의 주소가 아니라 객체가 가진 특정 인스턴스 값을 출력
    def __str__(self):
        return f'My name is {self.name}, I am a {self.position}'

def main(): # 이걸 하는 이유는 여기있는 클래스를 호출하면 밑에 애들도 같이 오기 때문이여 근데 얘는 안 부르고 싶자너
    # 객체생성
    dooly = SoccerPlayer('둘리', 'MF', 10)
    print(dooly)
    print(dooly.__str__())

    print('현재 선수의 등번호는 {}'.format(dooly.back_number))
