#!/usr/bin/python3

'''
Even/Odd/Prime number checker
'''

def EOP_Checker(n):

    try:
        i = int(n)
        if i == 1 or i == 0:
            print(str(i) + " Number is prime number" + '\n')
        for j in range(2, i + 1):
            if i % 2 == 0 or i == 2:
                print(str(i) + " Number is even number" + '\n')
                break
            if i % 3 == 0:
                print(str(i) + " Number is odd number" + '\n')
                break
            q = i / j  # quotient
            r = i % j  # remainder
            # if quotient q is >= j and remainder r = 0 will exit for loop and number is not prime
            if q > 1 and r == 0:
                continue
            # if quotient q is = j and remainder r = 0 number is prime
            if q == 1 and r == 0: print(str(i) + " Number is prime number" + '\n')
    except Exception as Error:
        print(Error)


