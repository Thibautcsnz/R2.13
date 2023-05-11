def u(n):
    if n==0:
        return 2
    else:
        return 3*u(n-1)-2

print(u(0))
print(u(1))
print(u(2))

n=10
print(u(n))

u=2
n=10
for i in range(n):
    u=(2*u**2-1)/(u**2+2)
    print(u)