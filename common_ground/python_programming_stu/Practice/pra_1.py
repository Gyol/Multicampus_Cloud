# a, *rest = 1, 2, 3
# print(a, rest)
#
# a, *middle, c = 123, 456, 6542, 465, 213
# print(a, middle, c)
# print(type(a), type(middle), type(c))
#
# a = 100
# b = 200
# print(a, b)
# a, b = b, a
# print(a, b)
# # judgement t,f
# # Bad
# attr = True
# if attr == True:
#     pass
# a
# # Good
# if attr:
#     pass
#
# attr = None
#
# # Good
# if attr is None:
#     pass
sum_list = []
for val in zip((1,2,3),(10,20,30),(100,200,300)):
    print(type(val))

sum_list = [sum(val) for val in zip((1,2,3),(10,20,30),(100,200,300))]
print(sum_list)