"""
Spyder Editor

This is a temporary script file.
"""

def check_prime(num):
    if not isinstance(num,int): ## isinstance() function checks if an instance is of the type
        return -1
    else: 
        for div in range(2, num//2 + 1):
            if num % div == 0:
                return 0
    return 1

def main():
    ret = check_prime(53)
    if  ret < 0:
        print('not a valid number')
    elif ret == 0:
        print('not prime')
    else:
        print('prime')
    
if __name__ == '__main__':
    main()
