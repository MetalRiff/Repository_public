# USOR - recomandat
# 1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva.
# 2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/

# TEMA OBLIGATORIE - nivel usor spre mediu
# SETS
# 1. Se dau urmatoarele seturi:


zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata'}
weekend = {'sambata','duminica'}

# a. Incearca sa adaugi in setul zile_sapt, ziua de 'duminica'.
# Ce observi? Scrie intr-un comentariu observatiile tale.

zile_sapt.add('duminica') # adauga 'duminica' in setul zile_sapt
print(zile_sapt)

#elementul 'duminica' este adaugat deoarece set urile sunt mutabile putem adauga si sterge elemente

# b. Foloseste un IF si verifica DACA:
# - weekend este un subset al zilelor din saptamana (adica daca elementele din setul weekend se regasesc
# intre elementele din setul zile_sapt)
# - weekend nu este un subset din setul zile_sapt
# Salveaza rezultatul pentru fiecare caz intr-o variabila bool si afiseaz-o intr-un mesaj sugestiv.

if weekend.issubset(zile_sapt):
    print('Weekend este un subset din setul zile_sapt')
else:
    print('Weekend nu este un subset din setul zile_sapt')

# # c. Afiseaza diferentele intre cele doua seturi (adica elementele care sunt in zile_sapt
# # si nu sunt in weekend si invers).

print(f'Elementele care sunt in zile_sapt dar nu sunt in weekend:   {zile_sapt.difference(weekend)}')
print(f'Elementele care sunt in weekend dar nu sunt in zile_sapt:   {weekend.difference(zile_sapt)}')


# d. Afiseaza intersectia elementelor din cele doua seturi (adica elementele care exista in ambele seturi).

print(f'Elementele care sunt in ambele seturi: {zile_sapt.intersection(weekend)}')


# TUPLES
# 2. Calcularea valorii totale a unui cos de cumparaturi
# Un client a cumparat mai multe articole dintr-un magazin si dorim sa calculam valoarea totala a cosului
# de cumparaturi.
# Citeste de la tastatura numele si pretul pentru trei articole, pe rand.
# Salveaza numele si pretul pentru fiecare articol intr-un tuplu. (Astfel vei avea trei tupluri).
# Calculeaza pretul total platit de client si afiseaza rezultatul intr-un mesaj sugestiv.

nume_1 = input('Introduceti nume produs  1: ')
pret_1 = input('Introduceti pretul pentru produsul 1: ')
nume_2 = input('Introduceti nume produs 2: ')
pret_2 = input('Introduceti pretul pentru prosusul 2: ')
nume_3 = input('Introduceti nume produs 3: ')
pret_3 = input('Introduceti pretul pentru produsul 3: ')

produs_1 = (nume_1,pret_1)
produs_2 = (nume_2,pret_2)
produs_3 = (nume_3,pret_3)

print(f'Pretul total platit de client este: {int(produs_1[1]) + int(produs_2[1]) + int(produs_3[1])}')

# 3. Se dau urmatoarele tupluri care caracterizeaza tipul de forma geometrica si lungimile laturilor sale.

forma_1 = ("Patrat", 5)
forma_2 = ("Dreptunghi", 2, 3)

# Calculeaza perimetrul si aria pentru fiecare forma geometrica

perimetru_forma_1 = int(forma_1[1] * 4)
aria_forma_1 = int(forma_1[1] ** 2)

perimetru_forma_2 = int(forma_2[1] * 2) + int(forma_2[2] * 2)
aria_forma_2 = int(forma_2[1]) * int(forma_2[2])

print(f'Perimetru patrat este: {perimetru_forma_1}')
print(f'Aria patrat este: {aria_forma_1}')

print(f'Perimetru dreptunghi este: {perimetru_forma_2}')
print(f'Aria dreptunghi este: {aria_forma_2}')

# 4. Citeste de la tastatura notele obtinute de un student la cele 4 examene date in sesiune.

nota1 = input('Introdu prima nota: ')
nota2 = input('Introdu a doua nota: ')
nota3 = input('Introdu a treia nota: ')
nota4 = input('Introdu a patra nota: ')

# Salveaza notele intr-un tuplu.

note_sesiune = (nota1,nota2,nota3,nota4)

# Calculeaza media studentului la finalul sesiunii.

media = int(int(note_sesiune[0]) + int(note_sesiune[1]) + int(note_sesiune[2]) + int(note_sesiune[3])) / 4
print(media)

# Daca media este intre 8-10 (inclusiv capetele de interval), afiseaza-i un mesajul utilizatorului
# si spune-i ca s-a descurcat foarte bine.
# Daca media este intre 5-8, afiseaza-i un mesaj utilizatorului sa se ambitioneze
# sesiunea urmatoare si sa invete mai mult ca sa obtina bursa.
# Daca media este sub 5, afiseaza-i utilizatorului un mesaj in care sa ii spui sa nu isi faca planuri pe vara ca il
# asteapta sesiunea de restante.

if 8 <= media <= 10:
    print('Felicitari te ai descurcat foarte bine')
elif 5 <= media < 8:
    print('Trebuie sa inveti mai mult pentru a lua bursa')
else:
    print('Ne vedem in restante')


# CONDITII REPETITIVE
#
# # 5. Se da lista:

masini = ['Audi', 'Volvo', 'Dacia', 'Mercedes', 'Fiat', 'Trabant', 'Lastun']

# # a. Folosind un for si lungimea listei, itereaza prin lista si pentru fiecare element
# # afiseaza mesajul 'Masina mea preferata este x', unde x este masina.

for i in range(0, len(masini)):
    print(f'Masina preferata este: {masini[i]}')

# # b. Faceti acelasi lucru folosind un for each.

for i in masini:
    print(f'Masina preferata este: {i}')

# c. Faceti acelasi lucru folosind un while.

x = 0 # initializare index lista masini

while x < len(masini): # conditie pentru executie "while"
    print(f'Masina este: {masini[x]}') # afiseaza elementul cu indexul x din lista masini
    x += 1 # incrementeaza indexul x
else:
    print('Lista de masini a fost parcursa')

# # 6. Folosind lista de la exercitiul 5, modifica elementele din lista astfel incat sa fie scrise cu majuscule,
# # exceptand primul si ultimul element din lista.
# # Printati varianta finala a listei.

masini_modificate = [] #defineste o lista goala

for x in masini: # pentru fiecare masina x in lista masini
    if x == masini[0]: # daca x este primul element din lista
        x = x.lower() # scrie x cu litere mici
        masini_modificate.append(x) # adauga pe x la noua lista de masini modificate

    elif x == masini[-1]: # daca x este ultimul element in lista masini
        x = x.lower() # scrie x cu litere mici
        masini_modificate.append(x) # adauga pe x la noua lista de masini modificate
    else:
        x = x.upper() #pentru restul elementelo x dinin list masini scrie cu litere mari
        masini_modificate.append(x) # adauga pe x la noua lista de masini modificate

print(masini_modificate) #afiseaza noua lista de masini

#
# # 7. Folosind lista de la exercitiul 5:
# # Vine un cumparator care vrea sa cumpere un Mercedes.
# # Itereaza prin lista cu for each, verifica daca masina e mercedes.
# # Daca da, afiseaza mesajul
# # "Am gasit masina dorita de dumneavoastra" si iesim din ciclu folosind un cuvant cheie care face acest lucru.
# # Daca nu, afiseaza "Am gasit masina X. Mai cautam."

for a in masini:
    if a == 'Mercedes':
        print('Am gasit masina dumneavoastra !!!')
        break
    else:
        print(f'Am gasit masina {a}. Mai cautam')

# # 8. Folosind lista de la exercitiul 5:
# # Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# # Daca masina e Trabant sau Lastun
# #   Folositi un cuvant cheie care sa dea skip la ce urmeaza
# # In celalalte cazuri, printati mesajul "S-ar putea sa va placa masina x.".

for b in masini:
    if b == 'Trabant' or b == 'Lastun':
        continue
    else:
        print(f'S ar putea sa va placa masina {b}')

# # 9. Modernizati parcul de masini.
# # Creati o lista goala, masini_vechi.
# # Iterati prin masini. (lista de la exercitiul 5)
# # Cand gasiti Lastun sau Trabant:
# #   Salvati aceste masini in masini_vechi.
# #   Suprascrieti cu 'Tesla' (in lista initiala de masini)
# # Printati: "Modele vechi: x"
# # Printati: "Modele noi: y"

masini_vechi = [] #generare lista goala masini vechi

for c in masini: # pentru fiecare masina c din lista de masini
    if c == 'Trabant': #daca c este 'Trabant'
        masini_vechi.append(c) #adauga c la lista masini vechi
        masini.remove(c) #sterge c din lista de masini existenta
        masini.append('Tesla') #adauga in lista de masini masina Tesla
        for c in masini:
            if c == 'Lastun':
                masini_vechi.append(c)
                masini.remove(c)
                masini.append('Tesla')
                print(f'Modele vechi: {masini_vechi}')
                print(f'Modele noi: {masini}')
#
# # 10. Avand dictionarul:

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

# # Vine un client cu bugetul de 15 000 euro.
# # Prezentati doar masinile care se incadreaza in acest buget:
# # Iterati prin dict.items() si accesati masina si pretul.
# # Printati "Pentru un buget de sub 15 000 euro puteti alege masina x"
#
client_buget = 15000

for model_masina, pret_masina in pret_masini.items():
    if pret_masina <= client_buget:
        print(f'Pentru un buget de sub 15 000 euro puteti alege masina {model_masina}')

import random

# # 11. Avand lista:
#
numere = [5, 7, 9, 3, 3, 1, 0, -4, 3]

# Afisati de cate ori apare 3. (! NU aveti voie sa folositi metoda count()!)

count_cifra_3 = 0 #declarare si initializare variabila unde vom tine de cate ori apare cifra 3

for i in numere: # pentru pentru fiecare i in lista de numere --> in i o sa se tine pe rand fiecare element din lista numere
    if i == 3: # verificam cand i o sa primeasca cifra 3 din lista numere
        count_cifra_3 += 1 # de fiecare data cand i primeste cifra 3 din lista vom incrementa cu 1 pentru a contoriza acest lucru in variabila count_cifra_3
print(count_cifra_3)

# 12. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin lista si calculati suma numerelor din lista.
# ! NU aveti voie sa folositi functia sum()!

suma = 0 # declaram si initializam variabila suma care va tine suma numereleor din lista numere

for i in numere: #parcurgem lista numere si atribuim variabilei i pe rand vaaloarea fiecarui element din lista numere
    suma += i #adunam la variabila suma,  i din lista numere
print(suma)

# 13. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin lista si afisati cel mai mare numar.
# ! NU aveti voie sa folositi functia max()!

numere = [5, 7, 9, 3, 3, 1, 0, -4, 3]

cel_mai_mare_nr = 0 # declaram si initializam variabila cel_mai_mare_nr care va tine cele mai mari numere detectate

for i in numere:
    if i > cel_mai_mare_nr:
        cel_mai_mare_nr = i

#e.g. in for, i ia valoarea primului element al listei numere care este 5.
# si in if se verifica daca 5 > decat cel_mai_mare_nr care este initializat cu valoarea 0 si daca da atunci se suprascrie cel_mai_mare_nr cu valoarea curenta a lui i care este 5 in prima iteratie

print(f'Cel mai mare numar este:  {cel_mai_mare_nr}')

# 14. Folosind aceeasi lista de la exercitiul 11:
# - iterati prin ea
# - daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa.
# Exemplu: Daca e 3, sa devina -3.
# Afisati noua lista.

numere = [5, 7, 9, 3, 3, 1, 0, -4, 3]

convert_to_negativ = 0 # declaram si initializam o variabila in care vom tine elementele din noua lista
lista_noua = [] # declaram o lista goala in care vom adauga elementele din noua lista

for i in numere:
    if i >= 0:
        convert_to_negativ = - i # converteste valoare lui i in negativ si o scrie un variabila convert_to_negativ
        lista_noua.append(convert_to_negativ) #adauga elementul covertit anterior in noua lista
    else:
        convert_to_negativ = i # aici nu se mai face conversia deoarece valoarea lui i este un numar negativ
        lista_noua.append(convert_to_negativ) #adauga elementul in noua lista

print(lista_noua)


# # TEMA OPTIONALA - DE GRUP (MAY NEED GOOGLE)

# 1. Se dau listele:

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

# Populati corect listele goale pe baza elementelor din lista alte_numere.
# Afisati cele 4 liste la final.

numere = 0

for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)


# 2. Folosind lista alte_numere de la exercitiul anterior:
# Ordonati lista crescator, fara sa folositi sort.
# Va puteti inspira vizual de aici: https://www.youtube.com/watch?v=lyZQPjUT5B4

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

# Am copiat aceasta rezolvare din tema rezolvata !!!!

for i in range(len(alte_numere)): #parcurgem lista alte numere si i o sa ia pe rand o valoare a indexului acestei liste
    for j in range(0, len(alte_numere) - i - 1): # nu am inteles exact ce se intampla aici !!!!
        if alte_numere[j] > alte_numere[j + 1]:
            temp = alte_numere[j]
            alte_numere[j] = alte_numere[j + 1]
            alte_numere[j + 1] = temp

print(alte_numere)


# 3. Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# numar_ghicit = None
# Folosind un while:
#   User-ul introduce un numar
#   Programul ii spune:
#   Numarul secret e mai mare
#   Numarul secret e mai mic
#   Ai ghicit.
# Daca utilizatorul a ghicit, while-ul trebuie sa se opreasca!

numar_secret = random.randint(1,30) # salveaza in numar_secret un numar random intre 1 si 30
numar_ghicit = None

while numar_ghicit != numar_secret: # atata timp cat numarul ghicit este diferit de numarul secret
    numar_ghicit = input('Introduceti un numar: ') # introduceti de la tastatura un numar
    if int(numar_ghicit) < numar_secret:
        print('Numarul secret este mai mare')
    elif int(numar_ghicit) > numar_secret:
        print('Numarul secret este mai mic')
    else:
        print('Ai ghicit')
        break


# 4. Alegeti un numar de la tastatura si generati o piramida, conform exemplului:
# Daca utilizatorul va introduce numarul 7, se va genera/ afisa urmatoarea piramida:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

numar_introdus = input('Introduceti un numar: ')

for i in range(1, int(numar_introdus) + 1):
    print(str(i)*i) #convertim i in string si il multiplicam de i ori

# 5.
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Iterati prin lista 2d.
# Printati "Cifra curenta este x"
# (HINT: nested for - adica for in for)

for i in tastatura_telefon: # se parcurge lista tastatura_telefon si variabilei (i) i se atribuie pe rand valoarea fiecarui element din aceasta list
    for j in i: # se parcurge lista care este in variabila i si se atribuie pe rand in variabila (j) valoarea fiecarui element al listei (i)
        print(f'cifra curenta e {j} ')






