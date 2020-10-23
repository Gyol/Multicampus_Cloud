# 1~100까지 임의의 숫자를 맞추시오
# 1부터 100사이 값을 랜덤하게 추출(정수 난수)
# 사용자가 숫자 입력
# 랜덤하게 추출한 숫자와 입력받는 숫자가 같으면 game종료
# 정답을 알려주고, 몇 번 만에 맞추었는지 출력
# while 입력받은 숫자 != 랜덤추출숫자 -> keep going
# 입력받은 숫자 > 랜덤숫자면 '숫자가 너무 큽니다'
# 입력받은 숫자 < 랜덤숫자면 '숫자가 너무 작습니다'

import random

random_nb = random.randint(1, 100)
nb_list = list(range(1,101))
input_nb = int(input())
count = 1

while input_nb != random_nb:
    if input_nb not in nb_list:
        print("You're an idiot")
    elif random_nb > input_nb:
        print('Your number is smaller')
        nb_list = nb_list[input_nb:max(nb_list)+1]
    else:
        print('Your number is bigger')
        nb_list = nb_list[min(nb_list)-1:input_nb-1]
    count += 1
    input_nb = int(input())

print("Trial", count, 'is correct')

# 2020.07.16 10:07 완성
