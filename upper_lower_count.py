'''
Write a Python function that accepts a string and calculates the number 
of upper case letters and lower case letters.
'''

def upper_lower_count(mystr):
    uCount = lCount = 0
    for letter in mystr:
        if letter >= 'a' and letter <= 'z':
            lCount += 1
        elif letter >= 'A' and letter <= 'Z':
            uCount += 1
        else:
            pass
    print("Upper count = {} lower count = {}".format(uCount, lCount))
    
def main():
    upper_lower_count("AnandA")

if __name__ == '__main__':
    main()
