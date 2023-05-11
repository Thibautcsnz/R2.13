def c(n):
    if n==0:
        return c0
    else :
        return((c(n-1)+m)*(1+t/100)**(1/12))

print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an")
c0 = int(input("Entrez le placement de départ :"))
m = float(input("Entrez le montant du versement mensuel: :"))
t = float(input("Entrez le taux annuel en %:"))
n = int(input("Entrez le nombre d'années:"))

print(f"Le capital acquis avec intérêts est de {round(c(n*12),2)} euros au bout de {n} ans avec des versements mensuels de {m} euros")
print(f"Les intérêts gagnés au taux annuel de {t} % sont de {round(c(n*12)-n*m*12-c0,2)} euros")
print(f"Sans placement avec intérêts le capital acquis serait de {round(n*m*12+c0,1)} euros")

print(round(n))