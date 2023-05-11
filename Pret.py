def pret():
    print("Calcul d'un prêt immobilier ou d'un crédit à la consommation")
s = int(input("Entrez le montant du prêt ou crédit :"))
taux = float(input("Entrez le taux annuel en % :"))
na = int(input("Entrez le nombre d'années:"))

moi = 1
#tm = taux/12/100  #formule approchée
tm = (1+taux/100)**(1/12)-1   #formule plus précise (vraie)
a = (1+tm)**(12*na)
m = (s * tm * a)/(a-1)
int = s * tm
rembours = m - int
restant = s - rembours
interem = int

print(f"La mensualité avec intérêts est de {round(m,1)} euros")
print(f"Le montant des intérêts remboursés sont de {round(m*12*na-s,2)} euros")
print(f"le taux mensuel est de {tm}")
print(f"Mois - Mensualité - Intérêts - Capital Remboursé - Capital restant du - Intérêts Remboursés")
for i in range(na*12):

    print(f'{moi} \t-\t {round(m,1)} -\t {round(int,1)}\t -\t {round(rembours,1)}\t -\t {round(restant, 1)}\t -\t {round(interem,2)}\t')

    moi = moi + 1

    int = restant * tm

    rembours = m - int

    restant = restant - rembours
    interem = interem + int


