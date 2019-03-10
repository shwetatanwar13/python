def gensquares(N):
    for i in range(0,N+1):
        yield i**2

print(list(gensquares(5)))