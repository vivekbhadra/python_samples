'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''
def has_33(mylist):
    count = 0
    for num in mylist:
        if num == 3:
            count += 1
        else:
            count = 0
    return count >= 2

def main():
    print(has_33([1, 3, 3])) 
    print(has_33([1, 3, 1, 3]))
    print(has_33([3, 1, 3]))

if __name__ == '__main__':
    main()
