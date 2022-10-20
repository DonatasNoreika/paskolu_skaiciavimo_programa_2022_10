import csv


class Paskola:
    def __init__(self):
        self.suma = 0
        self.terminas = 0
        self.palukanos = 0
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
        grazintina_dalis = self.suma / self.terminas
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
                bendra_suma -= grazintina_dalis
                moketina_suma = grazintina_dalis + palukanos
                bendra_moketina_suma += moketina_suma
                print('{:12} {:12} {:12} {:12} {:12}'.format(men_nr + 1, grazintina_dalis, round(bendra_suma, 2), round(palukanos, 2), round(moketina_suma, 2)))
                csv_writer.writerow([men_nr + 1, grazintina_dalis, round(bendra_suma, 2), round(palukanos, 2), round(moketina_suma, 2)])
            print('{:12} {:12} {:12} {:12} {:12}'.format("Bendra", self.suma, "", round(bendros_palukanos, 2), round(bendra_moketina_suma, 2)))
            csv_writer.writerow(["Bendra", self.suma, "", round(bendros_palukanos, 2), round(bendra_moketina_suma, 2)])
            self._bendros_palukanos = bendros_palukanos
            self._bendra_moketina_suma = bendra_moketina_suma

    def __str__(self):
        return f"Suma: {self.suma}, terminas: {self.terminas}, palūkanos: {self.palukanos}"

