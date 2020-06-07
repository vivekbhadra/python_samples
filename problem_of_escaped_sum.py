'''
SUMMER OF '69: Return the sum of the numbers in the array, except 
ignore sections of numbers starting with a 6 and extending to the 
next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
'''
"""
Spyder Editor

This is a temporary script file.
"""
def summer_69(mylist):
    flag = False
    val = 0
    for number in mylist:
        if number == 6:
            flag = True
        elif flag == False:
            val += number
        elif number == 9:
            flag = False
    return val
                         

def main():
    print(summer_69([1, 3, 5]))
    print(summer_69([4, 5, 6, 7, 8, 9]))
    print(summer_69([2, 1, 6, 9, 11]))

if __name__ == '__main__':
    main()
