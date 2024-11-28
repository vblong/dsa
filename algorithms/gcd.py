def gcd(a, b):
    # fast
    while a != b:
        if a > b:
            a = b % a
            b = a
        else:
            b = a % b
            a = b

    # slow
    # while a != b:
    #     if a > b:
    #         a -= b
    #     else:
    #         b -= a
    print(a)
    # print(45 % 27)
    # for i in range(1, a):
    #     if a % i == 0:
    #         print(i, end=' ')
    # print()
    # for i in range(1, b):
    #     if b % i == 0:
    #         print(i, end=' ')
    # print()

    # print('------- start', a, b)
    # a = b - a
    # print('-------', a, b)
    # a = b - a
    # print('-------', a, b)
    


    # while a:
    #     a = a % b
    #     b = a
    # print(a, b)

gcd(27, 45)
gcd(21, 54)