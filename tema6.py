# A. RECOMANDAT
# 1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva.

# B. OBLIGATORIU (MEDIU)

# ATENTIE!! Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati metodele clasei.

# 1. Clasa Cerc
# atribute: raza, culoare
# constructor pentru ambele atribute
# metode:
# descrie_cerc() -> va PRINTA culoarea si raza
# aria() -> va returna aria
# diametru()
# circumferinta()

class Cerc:

    #Atribute clasa cerc
    raza = None
    culoare = None

    #constructor pentru atribute clasa Cerc
    def __init__(self, raza,culoare):
        self.raza = raza
        self.culoare = culoare

    #Metode:

    def descriere_cerc(self):
        return f'Raza cercului este {self.raza} si culoarea {self.culoare}'

    def aria_cerc(self):
        aria = 3.14 * self.raza
        return aria

    def diametru_cerc(self):
        diametru = self.raza * 2
        return diametru

    def circumferinta_cerc(self):
        circumferinta = 2 * 3.14 * self.raza
        return circumferinta

cerc_1 = Cerc(14, 'albastru')
cerc_2 = Cerc(5, 'verde')

print(cerc_1.descriere_cerc())
print(cerc_1.diametru_cerc())
print(cerc_1.circumferinta_cerc())
print(cerc_1.aria_cerc())


# 2. Clasa Dreptunghi

# atribute: lungime, latime, culoare
# constructor pentru toate atributele

# metode:
# descrie()
# arie()
# perimetru()
# schimba_culoare(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().


class Dreptunghi:

    #Atribute clasa
    lungime = None
    latime = None
    culoare = None

    #contructor pentru clasa dreptunghi
    def __init__(self,lungime, latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    #Metode

    def descriere(self):
        return f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}'

    def arie(self):
        aria = self.lungime * self.latime
        return aria

    def perimetru(self):
        perimetru = 2 * self.latime + 2 * self.lungime
        return perimetru

    def schimba_culoarea(self):
        self.culoare = 'verde'

dreptunghi1 = Dreptunghi(20,10,'rosu')
dreptunghi2 = Dreptunghi(15,5,'albastru')

print(dreptunghi1.descriere())
print(dreptunghi1.arie())
print(dreptunghi1.perimetru())

dreptunghi1.schimba_culoarea()
print(dreptunghi1.descriere())

# 3. Clasa Angajat

# atribute: nume, prenume, salariu

# Connstructor pentru toate atributele

# Metodele:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Angajat:
    #Atribute clasa
    nume = None
    prenume = None
    salariu = None

    #Constructor
    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    #Metode:

    def descriere(self):
        return f'Angajatul are numele {self.nume}, prenumele {self.prenume} si salariul {self.salariu}'

    def nume_complet(self):
        nume_angajat = self.nume + ' ' + self.prenume
        return nume_angajat

    def salariu_lunar(self):
        return f'Salariul lunar este {self.salariu}'

    def salariul_anual(self):
        salariul_anual = self.salariu * 12
        return f'Salariul anual este {salariul_anual}'

    def marire_salariu(self, procent):
        self.salariu = self.salariu + procent * self.salariu / 100
        return


angajat1 = Angajat('Tudor','Mihai', 50)
angajat2 = Angajat('Dumitru','Paul', 100)

print(angajat1.descriere())
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariul_anual())

angajat1.marire_salariu(10)

print(angajat1.descriere())


# 4. Clasa Cont

# atribute: iban, titular_cont, sold

# constructor pentru toate

# metode:
# afisare_sold() -> Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare cont(suma)


class Cont:
    #Atribute
    iban = None
    titular_cont = None
    sold = None

    #Contructor

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    #Metode:

    def afisare_sold(self):
        return f'Titularul {self.titular_cont} are in contul {self.iban} suma {self.sold}'

    def debitare_cont(self,suma):
        self.sold = self.sold - suma
        return

    def creditare_cont(self,suma):
        self.sold = self.sold + suma
        return

cont1 = Cont(122254,'Vasile Ion',1500)

print(cont1.afisare_sold())
cont1.debitare_cont(500)
print(cont1.afisare_sold())

cont1.creditare_cont(1000)
print(cont1.afisare_sold())

# BONUS (daca aveti timp soi doriti sa lucrati suplimentar)

# 5. Clasa Factura
# atribute: seria (va fi constanta, nu trebuie constructir, toate facturile vor avea aceeasi serie),
# numar, nume_produs, cantitate, pret_buc

# Constructor: toate atributele, fara serie

# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti

# Exemplu:
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | Cantitate | Pret Bucata | Total
# Telefon|     7     |    700      | 49000

# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

# 6. Clasa Masina
# atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set),
# inmatriculata (bool)

# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# culori_disponibile = alegeti 5-7 culori
# marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# inmatriculata = False

# constructor: model, viteza_maxima

# Metode:
# descrie() (se vor printa toate atributele, in afara de culori disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vospeste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare este in culori_disponibile,
# altfel afisati un mesaj.
# accelereaza(viteza) - se va accelera la o anumita viteza, daca viteza e negativa - mesaj de eroare,
# daca viteza e mai mare decat viteza maxima - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0

# 7. Clas ToDoList

# Atribute: to_do (dict, chiea e numele task-ului, valoarea e descrierea)
# La inceput nu avem task-uri, dict e gol si nu avem nevoie de constructor.

# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - afiseaza doar cheile
# afiseaza_detalii_suplimentare(nume_task) = in functie de numele task-ului, printam
# detalii suplimentare. Daca task-ul nu e in to_do list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# Daca raspunde da - ii cerem detalii task si salvam nume + detalii in dict