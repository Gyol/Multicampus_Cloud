import pickle

# 사용자로부터 문자열을 몇 번 입력할지를 숫자로 받음

num_data = int(input('Enter the number of the data: '))
# 입력받은 데이터를 저장할 list 선언
data = []

# 입력받은 숫자 만큼 for loop으로 문자열 입력받음

for a in range(num_data):
    input_num = input('Enter data ' + str(a))
    data.append(input_num)

# pickle의 dump()함수를 이용해서 문자열을 저장한 list 생성
file = open('important', 'wb') # important는 문서명이고요 wb는 쓸거라서
pickle.dump(data, file)
file.close()