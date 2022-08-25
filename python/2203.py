from sys import stdin

def EratosthenesSieve(n):
    prime = {i:0 for i in range(n+1)}
    p = 2
    while p <= n:
        if prime[p]==0:
            prime[p] = p
            for i in range(p * 2, n+1, p):
                prime[i] += p
        prime[p]+=prime[p-1]
        p += 1
    return prime

numeros = {}
numeros = EratosthenesSieve(1_000_000)

x = int(stdin.readline())
for i in range(x):
    a,b  = map(int, stdin.readline().split())
    print(numeros[b]-numeros[a-1])  