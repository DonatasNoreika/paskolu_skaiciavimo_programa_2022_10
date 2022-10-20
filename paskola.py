import csv


class Paskola:
    def __init__(self, suma, terminas, palukanos):
        self.suma = suma
        self.terminas = terminas
        self.palukanos = palukanos
        self.grazintina_dalis = self.suma / self.terminas
        self._bendros_palukanos = 0
        self._bendra_moketina_suma = 0

    def paskolos_informacija(self):
        print("-----------------------")
        print("Suma:", self.suma)
        print("Terminas:", self.terminas)
        print("Palūkanos:", self.palukanos)
        print("Palūkanų suma:", self._bendros_palukanos)
        print("Bendra mokėtina suma:", self._bendra_moketina_suma)

    def mokejimo_grafikas(self):
        bendra_suma = self.suma
        bendros_palukanos = 0
        bendra_moketina_suma = 0
        with open('paskolos_grafikas.csv', "w", encoding="UTF-8", newline='') as file:
            csv_writer = csv.writer(file)
            print('{:12} {:12} {:12} {:12} {:12}'.format("Mėn. Nr.", "Dalis", "Likutis", "Palūkanos", "Bendra"))
            csv_writer.writerow(["Mėn. Nr.", "Dalis", "Likutis", "Palūkanos", "Bendra"])
            for men_nr in range(self.terminas):
                palukanos = round(bendra_suma * self.palukanos * 0.01 / 12, 2)
                bendros_palukanos += palukanos
                bendra_suma -= self.grazintina_dalis
                moketina_suma = self.grazintina_dalis + palukanos
                bendra_moketina_suma += moketina_suma
                print('{:12} {:12} {:12} {:12} {:12}'.format(men_nr + 1, self.grazintina_dalis, bendra_suma, palukanos, moketina_suma))
                csv_writer.writerow([men_nr + 1, self.grazintina_dalis, bendra_suma, palukanos, moketina_suma])
            print('{:12} {:12} {:12} {:12} {:12}'.format("Bendra", self.suma, "", bendros_palukanos, bendra_moketina_suma))
            csv_writer.writerow(["Bendra", self.suma, "", bendros_palukanos, bendra_moketina_suma])
            self._bendros_palukanos = bendros_palukanos
            self._bendra_moketina_suma = bendra_moketina_suma

