def ord(n,m,sw):
    if len(datos)==m+2 or (not datos[0] and not datos[len(datos)-1]):
        print(f'n = {m}:\n\t{(datos[1:len(datos)-1])}')
        if len(datos)!=m+2 or m==1: print("\tNo se puede reorganizar la lista para n = ",m)
        else: print("\tSI se puede reorganizar la lista para n =",m)
    else:
        for i in v:
            if 0<i-n<=m and d[i-n]:
                if sw:
                    datos.insert(len(datos)-1,i-n)
                else:
                    datos.insert(1,i-n)
                d[i-n]=False
                break
        else:
            if sw:
                datos[len(datos)-1]=False
            else:
                datos[0]=False
            sw = not sw
        if sw:
            ord(datos[len(datos)-2],m,sw)
        else:
            ord(datos[1],m,sw)
for n in range(1,21):
    v = [36,25,16,9,4]
    datos = [True,n, True]
    d = [True for i in range(n+1)]
    d[n] = False
    ord(n,n,True)