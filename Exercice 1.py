def u(n):
    return (2*n**2-1)/(n**2+2)
n=0
while u(n)<1000:
    print(u(n))
    n=n+1

print(n)

print(u(2))

n=10
print(u(n))

n=100
print(u(n))

n=1000
print(u(n))