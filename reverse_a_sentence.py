'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'

This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"
'''

"""
Spyder Editor

This is a temporary script file.
"""
def master_yoda(sentence):
    words = list(sentence.split())
    revw = words[::-1]
    revs = ' '.join(revw)
    return revs
    

def main():
    ret = master_yoda('I am Vivek')
    print(ret)

if __name__ == '__main__':
    main()
