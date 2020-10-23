n, m = map(int, input().split())
card = list(map(int, input().split(' ')))

my_sum = 0
my_compare = 0
for i in range(n-2):
    for j in range(n-1):
        for k in range(n):
            my_sum = card[i] + card[j] + card[k]
            if int(m) >= my_sum > my_compare:
                my_compare = my_sum
print(my_compare)