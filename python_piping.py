#!/usr/bin/env python
__author__ = "Vivek Bhadra"
__copyright__ = "Copyright (C) 2019 Vivek Bhadra"
__license__ = "Public Domain"
__version__ = "1.0"

import subprocess as sp

def grep_and_return():
    o = sp.Popen(['ps', '-eaf'], stdout=sp.PIPE, stderr=sp.PIPE)
    out = sp.Popen(['grep', '-w', 'SCREEN'], stdin=o.stdout, stdout=sp.PIPE)
    output = sp.Popen(['awk', '{print $8 " " $9}'], stdin=out.stdout, stdout=sp.PIPE)
    r, e = output.communicate()
    ret = r.split()
    if ret[0] == "SCREEN":
        print ret[1]
        #output = sp.check_call(['fuser', '-k', ret[1]])
    
def main():
    ret = grep_and_return()

if __name__ == "__main__":
    main()
