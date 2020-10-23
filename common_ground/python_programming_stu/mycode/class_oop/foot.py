# 2차원 리스트를 사용해서 player 5명 정보 저장

names = ['a', 'b', 'c', 'd', 'e']
positions = ['mf', 'df', 'cf', 'wf', 'gk']
numbers = [10, 15, 20, 3, 1]

players = [[name, position, number]\
           for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])

print()
for na, po, bn in zip(names, positions, numbers):
    print(na, po, bn)

# class 이거 할라면 soccerplayer를 내가 쓴거에서 import해야돼
print()
from mycode.class_oop.classs import SoccerPlayer

player1 = SoccerPlayer('Player1', 'MF', 10)
print(player1)
player1.change_back_number('ss')

print()

players_object = [SoccerPlayer(na, po, bn) for na, po, bn in zip(names, positions, numbers)]
print(players_object)

print()

for na, po, nu in zip(names, positions, numbers):
    print(f'{na} is a {po} player. Her uniform number is {nu}.')

print()
for list in zip(names, positions, numbers):
    print(list)