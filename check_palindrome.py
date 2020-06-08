'''
Write a Python function that checks whether a passed in string is palindrome or not.
'''

def check_palindrome(mystr):
    return mystr == mystr[::-1]

def main():
    if(check_palindrome("helleh")):
        print('Palindrome')
    else:
        print('Not Palindrome')

if __name__ == '__main__':
    main()
