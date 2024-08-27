#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print('Happy New Year!')


# happy_new_year()


def square_integers(int_list):
    # code goes here!
    pass
    squared_integers = [int*int for int in int_list]
    # print(squared_integers)
    return squared_integers

# square_integers([2, 3, 4, 5, 6])


def fizzbuzz():
    # code goes here!
    pass
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)


fizzbuzz()
