import math

for i in range(int(input())):
    a, b = map(int,input().split())
    print(math.pow(a,a)*math.log(a)+math.log(a) > b*math.log(b)+math.log(b))