'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime.
'''
"""
Spyder Editor

This is a temporary script file.
"""
def isprime(num):
    flag = True
    for n in range(2, (num // 2) + 1):
        if num % n == 0:
            flag = False
    if flag:
        print('{} is prime'.format(num))
    
    return flag

def count_primes(num):
    count = 0
    for n in range(1, num):
        if isprime(n):
            count += 1
    return count
    
                         

def main():
    print(count_primes(100))

if __name__ == '__main__':
    main()
