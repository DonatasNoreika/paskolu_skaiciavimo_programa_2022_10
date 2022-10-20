from paskola import Paskola
from issaugojimas_i_pickle import gauti_paskolas, irasyti_paskolas

paskolos = gauti_paskolas()

while True:
    pasirinkimas = int(input("""    1 - Įvesti paskolos duomenis
    2 - Parodyti paskolos informaciją
    3 - Parodyti paskolos mokėjimo grafiką
    4 - Rodyti visas paskolas
    0 - Baigti darbą\n"""))

    match pasirinkimas:
        case 1:
            print("Įveskite paskolą:")
            paskola = Paskola()
            paskola.suma = float(input("Suma: "))
            paskola.terminas = int(input("Terminas (mėn.): "))
            paskola.palukanos = int(input("Palūkanos (proc.): "))
            paskolos.append(paskola)
            irasyti_paskolas(paskolos)
        case 2:
            paskolos[-1].paskolos_informacija()
        case 3:
            paskolos[-1].mokejimo_grafikas()
        case 4:
            for nr, paskola in enumerate(paskolos, 1):
                print(nr, paskola)
        case 0:
            print("Viso gero")
            break
