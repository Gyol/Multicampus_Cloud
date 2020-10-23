# 저장된 데이터를 읽어오기

import pickle

file = open('important', 'rb') # rb는 읽으니까
data = pickle.load(file)
file.close()

print('Showing the pickeled data')
for a, item in enumerate(data):
    print(a, item)