# Calcul du diamètre d’un volet roulant autour de son axe lorsque le volet est ouvert
import math
l = 9
def d(n):
    return (d0+2*l*n)

d0 = int(input("Entrer le diametre de l'axe en mm: "))
n = int(input("Entrer nombre de tours n: "))

L = 0
for i in range (n):
    L = L+math.pi*d(i)
    print("Tour:",i+1,"  - ","Diametre [mm]:",round(d(i+1),1),"     - ","Longueur enrouléée [mm]:",round(L,0))
print()
print("Calcul de la longueur L par formule :")
c0=math.pi*d(0)
cn=math.pi*d(n-1)
L=(c0+cn)*(n+0)/2
print("Longeur [mm] pour ",n, "tours :",L )


