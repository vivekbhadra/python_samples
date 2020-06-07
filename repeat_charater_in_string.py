'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''
"""
Spyder Editor

This is a temporary script file.
"""
def paper_doll(mystr):
    newstr = ''
    for letter in mystr:
        newstr += letter * 3
    return newstr

def main():
    print(paper_doll('Hello'))
    print(paper_doll('Mississippi'))

if __name__ == '__main__':
    main()
