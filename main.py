from paskola import Paskola

paskola = Paskola()

while True:
    pasirinkimas = int(input("1 - Įvesti paskolos duomenis\n2 - Parodyti paskolos informaciją\n3 - Parodyti paskolos mokėjimo grafiką\n4 - Baigti darbą\n"))
    match pasirinkimas:
        case 1:
            print("Įveskite paskolą:")
            paskola.suma = float(input("Suma: "))
            paskola.terminas = int(input("Terminas (mėn.): "))
            paskola.palukanos = int(input("Palūkanos (proc.): "))
        case 2:
            paskola.paskolos_informacija()
        case 3:
            paskola.mokejimo_grafikas()
        case 4:
            print("Viso gero")
            break




# paskola1 = Paskola(758, 20, 2)
#
# paskola1.mokejimo_grafikas()
# paskola1.paskolos_informacija()