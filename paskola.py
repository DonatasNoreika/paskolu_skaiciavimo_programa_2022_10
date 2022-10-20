
class Paskola:
    def __init__(self, suma, terminas, palukanos):
        self.suma = suma
        self.terminas = terminas
        self.palukanos = palukanos
        self.grazintina_dalis = self.suma / self.terminas

    def paskolos_informacija(self):
        pass

    def mokejimo_grafikas(self):
        bendra_suma = self.suma
        bendros_palukanos = 0
        bendra_moketina_suma = 0

        print('{:12} {:12} {:12} {:12} {:12}'.format("Mėn. Nr.", "Dalis", "Likutis", "Palūkanos", "Bendra"))
        for men_nr in range(self.terminas):
            palukanos = round(bendra_suma * self.palukanos * 0.01 / 12, 2)
            bendros_palukanos += palukanos
            bendra_suma -= self.grazintina_dalis
            moketina_suma = self.grazintina_dalis + palukanos
            bendra_moketina_suma += moketina_suma
            print('{:12} {:12} {:12} {:12} {:12}'.format(men_nr + 1, self.grazintina_dalis, bendra_suma, palukanos, moketina_suma))
        print('{:12} {:12} {:12} {:12} {:12}'.format("Bendra", self.suma, "", bendros_palukanos, bendra_moketina_suma))

