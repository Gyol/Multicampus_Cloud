#평균을 계산하는 함수를 정의

# def my_average(numbers):
#     #local variable
#     total = 0
#     for num in numbers:
#         total += num
#     retun total

# prices = [100, 3000, 2500. 450]
# result = my_average(prices)

# print(result)
# SyntaxError: invalid syntax

# 함수 외부에서는 local 변수를 사용할 수 없음
# print(total)

def my_average(numbers):
    #local variable
    total = 0
    for num in numbers:
        total += num
    my_avg = total / len(numbers)
    return int(my_avg)

def connnect(server, port):
    return 'http://{}:{}'.format(server, port)





def main():
    prices = [100, 3000, 2500, 450]
    result = my_average(prices)

    print(result)

    # 위치 파라미터
#    result1 = connect('server.com', '9080')
#    print(result1)
#    # 키워드 파라미터
#    result1 = connect(port='8087', server='aa.com')
#    print(result1)


# 함수 파라미터 *p: tuple type parameter.. argument 갯수가 달라질 수 있어여
def var_pm(*p):
    return p

# 가변 파라미터 **p: dict type parameter..

def var_param_dict(**p):
    print(type(p), p)

    result3 = var_pm(1,)
    print(type(result3))

    result3 = var_pm(1, 2, 3)
    print(type(result3))

    var_param_dict(n1=10, n2=20, n3=30)

    result4 = swap(200, 100)
    print(type(result4), result4)
    x, y = swap(35, 21)
    print(f'x는 {x}, y는 {y}')



main()

