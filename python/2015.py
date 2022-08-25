import sys

def paraElDos(a):
    if a == 0:
        return 1
    a %= 4
    if a == 0:
        return 6
    if a == 1:
        return 2
    if a == 2:
        return 4
    if a == 3:
        return 8

def paraElTres(a):
    a %= 4
    if a == 0:
        return 1
    if a == 1:
        return 3
    if a == 2:
        return 9
    if a == 3:
        return 7
for _ in sys.stdin:
    if _ == '\n':
        break
    a, b = map(int, _.split())
    #for i in range(100):
        #print(2**i,paraElDos(i),i%4)
        #print(3**i,paraElTres(i),i%4)
    c = paraElDos(a)+paraElTres(b)
    print(c%10)
