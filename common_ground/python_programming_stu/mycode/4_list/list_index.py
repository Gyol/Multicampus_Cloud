colors = ["red", "blue", "green"]
print(colors[0])
print(colors[2])
print(len(colors))

#list의 Nth element값 변경
colors[0] = 'Yellow'
print(colors)

#element추가
colors.append('black')
print(colors)

#element 삭제
colors.remove('blue')
print(colors)
del colors[1]
print(colors)

#element 여러개 추가
colors.extend(['orange', 'red'])
print(colors)
colors.insert(1, 'Purple')
print(colors)

print()
names = ['Peter', 'Parker', 'Spiderman']
print(names*2)
print(colors + names)

#slicing으로 삭제
del colors[:2]
print(colors)

#in구문 True/False
print('Peter' in names)
print('peter' in names)