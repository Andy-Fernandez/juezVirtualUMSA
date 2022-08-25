import sys

def BinarioToDecimal(num):
    return int(num, 2)

for m in sys.stdin:
    if m == '\n': break
    palabra = m.replace('\n',"")
    #print(palabra)
    respuesta = ""
    for i in palabra:
        a = ord(i)
        a = bin(a).replace('b',"")
        #print(a)
        #print(BinarioToDecimal(a[4:]+a[:4]))
        respuesta += str(BinarioToDecimal(a[4:]+a[:4])) + " "
    print(respuesta[:-1])
