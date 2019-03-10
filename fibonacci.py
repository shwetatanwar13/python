def fibonacci(n):
    a=0
    b=1
    for i in range(1,n+1):
        yield a
        a,b=b,a+b

g=fibonacci(4)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print(list(fibonacci(4)))
k=fibonacci(4)
for i in k:
    print(i)