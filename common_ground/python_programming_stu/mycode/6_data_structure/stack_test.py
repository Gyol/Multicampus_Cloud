# stack은 Last In First Out LIFO
my_stack = [20, 10, 30, 40, 20]
print(my_stack)
my_stack.append(100)
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)

# print()
# word = input('Input a word: ')
# word_list = list(word)
# for i in range(len(word_list)):
    # print(word_list.pop())

#Queue - First In First Out FIFO
print()
Colors = ['purple', 'yellow', 'green', 'red', 'blue']
print(Colors)
Colors.append('orange')
print(Colors)
Colors.pop(0)
print(Colors)
Colors.pop(0)
print(Colors)
Colors.append('pink')
print(Colors)

# Tuple - read only.. 값변경 불가능

print()
s = set([1,2,3,1,2,3])
print(s)
s.add(1)
print(s)
s.remove(1)
print(s)
s.update([1,4,5,6,7])
print(s)
s.discard(3)
print(s)
s.clear()
print(s)

# discard() 함수는 해당 값이 존재하지 않더라도 에러 X
# remove() 함수는 해당 값이 존재하지 않으면 에러O

print()
s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])
print(s1.union(s2))
print(s1)
print(s1|s2)
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1-s2)
print(s2-s1)

#Dictionary
print()
my_dict = {}
print(my_dict)
my_dict2 = dict()
print(type(my_dict), type(my_dict2))
my_dict['Korea'] = 'Seoul'
my_dict['New Zealand'] = 'Wellington'
my_dict['Taiwan'] = 'Taipei'
my_dict['China'] = 'Beijing'
print('Input Country Name: ')
city = print('Capital: ', my_dict.get(input()))

##################################이거어케하지
# if city == None:
#     print('No Data')
# else:
#    print('Data Exist')
############################################

# print(my_dict.items())




