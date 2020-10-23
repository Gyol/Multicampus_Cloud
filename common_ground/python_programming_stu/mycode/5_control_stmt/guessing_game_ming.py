import random
a = 1
b = 100

random_nb = random.randint(a, b)
input_nb = int(input())
count = 1

while input_nb != random_nb:
    if a > input_nb or input_nb > b:
        print("You're an idiot")
    elif random_nb > input_nb:
        print("Your number is smaller")
        a = input_nb
    else:
        print("Your number is bigger")
        b = input_nb
    count += 1
    input_nb = int(input())
else:
    print('Trial', count, 'is correct')