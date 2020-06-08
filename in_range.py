'''
Write a function that checks whether a number is in a given range (inclusive of high and low)
'''
def in_range(num, start, stop):
    if num in range(start, stop + 1): #start and stop inclusive
        return True
    else:
        return False

def main():
    print(in_range(101, 10, 100))
    
if __name__ == '__main__':
    main()
