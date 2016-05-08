import sys

def Hello(s):
    if s == 'Alice' or s == "Nick":
        print "Alert : mode"
        s = s + "???"
    else:
        DoesNotExists(s)
    s = s + '!!!!!'
    print 'Hello', s



# define main
def main() :
    Hello(sys.argv[1])



if __name__ == '__main__':
    main()


