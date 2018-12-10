#
# This script determines if a url is valid or not
#
import sys

domain_names=["com", "org", "net"]
url=sys.argv[1]
print url
header=url[0:7]
print header
if header == "http://":
    link_main=url[7:]
    print link_main
    l=link_main.split(".")
    if len(l) == 3:
        if(l[0] == "www"):
            if l[2] in domain_names:
                print "Valid URL"
            else:
                print "Invalid URL"
        else:
            print "Invalid URL"
    else:
        print "Invalid URL"
else:
    print "Invalid URL"
