'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
'''
"""
Spyder Editor

This is a temporary script file.
"""
def spy_game(mylist):
    val_1 = False
    val_2 = False
    val_3 = False
    
    for number in mylist:
        if not val_1:
            if number == 0:
                val_1 = True
        elif not val_2:
            if number == 0:
                val_2 = True
        elif not val_3:
            if number == 7:
                val_3 = True
    
    return val_1 and val_2 and val_3
                         

def main():
    print(spy_game([1,2,4,0,0,7,5]))
    print(spy_game([1,0,2,4,0,5,7]))
    print(spy_game([1,7,2,0,4,5,0]))

if __name__ == '__main__':
    main()
