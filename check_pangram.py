'''
Write a Python function to check whether a string is pangram or not.
'''

def check_pangram(mystr):
    mynewstring = mystr.lower()
    for letter in list(map(chr, range(97, 123))):
        if mynewstring.find(letter) == -1:
            return False
    return True    

def main():
    if(check_pangram('The quick brown fox jumps over the lazy dog')):
        print('pangram')
    else:
        print('Not pangram')
    
if __name__ == '__main__':
    main()
