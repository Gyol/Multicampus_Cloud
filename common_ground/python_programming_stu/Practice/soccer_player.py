class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return 'my name is {}, i play in {}, my number is {}'.format(self.name, self.position, self.back_number)

    def change_back_number(self, new_number):
        print('선수의 등번호를 변경합니다 : from {} to {}'.format(self.back_number, new_number))
        self.back_number = new_number
