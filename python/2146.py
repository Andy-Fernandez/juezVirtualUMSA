#Ejecicio 2146
def sumRec(x,k,i=0,n=0):
    if i==0:
        i+=1
        return sumRec(x,k,i,x**k)
    else:
        numero = str(n)
        acu = 0
        for j in numero:
            acu+=int(j)
        if i==200:
            return acu
        else:
            i+=1
            return sumRec(x,k,i,acu)

for i in range(int(input())):
    x,k = map(int,input().split())
    print(sumRec(x,k))