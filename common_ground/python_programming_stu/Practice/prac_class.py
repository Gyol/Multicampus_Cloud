from Practice.soccer_player import SoccerPlayer
#
# jisung = SoccerPlayer("JiSung", 'MF', 7)
# print(jisung)
# jisung.change_back_number(10)

names = ['jin', 'sungchul', 'ronald', 'hong', 'seo']
positions = ['mf', 'cb', 'df', 'gk', 'wf']
numbers = [10, 11, 5, 1, 8]

player_objects = \
    [SoccerPlayer(na, po, num) for na, po, num in zip(names, positions, numbers)]

for i in range(len(player_objects)):
    print(player_objects[i])
player_objects[2].change_back_number(77)
