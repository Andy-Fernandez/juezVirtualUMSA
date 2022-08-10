import math
##Resuleto! :)
for l in range(int(input())):
    n = int(input()) #17
    respuesta = []
    for i in range(1,int(n/3)+1):
        j = i-1
        k = n-2*i+1
        while(j!=k and j!=(k-1)):
            j+=1
            k-=1
            b = math.sqrt(i*j*k)
            if int(b) - b ==0:
                #print("b: ",b)
                a = j*k+i*k+i*j
                #print("a:",a)
                respuesta.append([int(a),int(b)])
    respuesta.sort()
    r = ""
    for i in respuesta:
        r+=f'({i[0]}, {i[1]})'
    print(r)

