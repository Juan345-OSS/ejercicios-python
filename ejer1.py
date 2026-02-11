for i in range(1,101,1):
    if i % 3 == 0:
        print(f'{i} es "fizz"')

    if i % 5 ==0:
        print(f'{i} es "buzz"')

    if i % 3 == 0 and i % 5 ==0 :
        print(f'{i} es "fizzbuzz"')