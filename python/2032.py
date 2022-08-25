import sys

def EratosthenesSieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    prime[1] = prime[0] = False
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    return prime

primes = EratosthenesSieve(100_000)

def take(x,cadena):
    v = []
    for i in range(len(cadena)-x+1):
        if cadena[i:i+x] not in v and primes[int(cadena[i:i+x])] and cadena[i:i+x][0] != '0':
            v.append(cadena[i:i+x])
    return v

x = iter(sys.stdin.readlines())
n = int(next(x))
for i in range(n):
    t = int(next(x))
    total = []
    for j in range(1,6):
        total += take(j,str(t))
    print(len(total))
