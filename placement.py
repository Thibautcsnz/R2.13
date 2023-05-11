def assu():
    print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an")

    pla = int(input("Entrez le placement de départ :"))
    verm = float(input("Entrez le montant du versement mensuel: :"))
    ta = float(input("Entrez le taux annuel en %:"))
    an = int(input("Entrez le nombre d'années:"))

    #calcul
    intcumul = 0
    for i in range(an):
        tau = ta/100
        pla = pla+(verm*12)
        capint = pla+pla*tau
        intcumul = intcumul + pla * tau
        pla = capint


    print(f"Le capital acquis avec intérêts est de {round(pla,2)} euros au bout de {an} ans avec des versements mensuels de {verm} euros")
    print(f"Les intérêts gagnés au taux annuel de {ta} % sont de {round(intcumul,2)} euros")
    print(f"Sans placement avec intérêts le capital acquis serait de {pla-intcumul} euros")

assu()