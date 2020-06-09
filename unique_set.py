'''
Write a Python function that takes a list and returns a new list with unique 
elements of the first list.
'''
def unique_set(mylist):
    newlist = []
    for item in mylist:
        if item not in newlist:
            newlist.append(item)
    return newlist

def main():
    print(unique_set([1,1,1,1,2,2,3,3,3,3,4,5]))

if __name__ == '__main__':
    main()
