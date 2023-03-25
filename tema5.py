# # a. USOR (RECOMANDAT)
# # 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# # 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# # (Daca nu ai facut-o deja)
# # 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# # Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# # si sigur ti se vor intipari in minte mai bine.
# # https://www.itfactory.ro/8174437-intro-in-programare/
#
# # b. OBLIGATORIU: USOR SPRE MEDIU
#
# # IMPORTANT! -> Pentru TOATE EXERCITIILE, apelati functia de cel putin 2 ori cu valori
# # diferite pentru a testa. Daca functia are return, printati raspunsul!
#
# # 1. Scrie o functie care sa calculeze si sa returneze suma a 2 numere

def suma(a,b): #defineste functia suma cu 2 parametri
    suma = a + b  #calcul suma
    return suma #returneaza valoarea sumei

print(suma(5,6)) #apeleaza functia suma
print(suma(-3,2.5))

# 2. Scrie o functie care sa returneze True daca un numar este par, False daca este impar

def even_odd(a):
    if a % 2 == 0: #conditia ca un numar sa fie par
        return True
    else:
        return False

print(even_odd(2))
print(even_odd(1))

# # 3. Scrie o functie care sa returneze numarul total de caractere din numele tau complet
# # (nume, prenume, nume_mijlociu)


def caractere_nume(nume,prenume,nume_mijlociu):

    numar_caractere = len(nume) + len(prenume) + len(nume_mijlociu)
    return numar_caractere

print(caractere_nume('Stoican','Adrian','Constantin'))
print(caractere_nume('Ana', 'Maria', 'Pop'))

# # 4. Scrie o functie care returneaza aria dreptunghiului

def aria_dreptunghi(latime,lungime):
    aria = latime * lungime
    return aria

print(aria_dreptunghi(2,4))

# 5. Scrie o functie care returneaza aria cercului

def aria_cerc(raza):
    aria = 3.14 * raza**2
    return aria

print(aria_cerc(5))

# # 6. Scrie o functie care returneaza True daca un caracter x se gaseste intr-un string dat, False daca nu.

def caracter_cautat(string,caracter):
    if caracter in string:
        return True
    else:
        return False

print(caracter_cautat('string','s'))
print(caracter_cautat('string','o'))

# # 7. Scrie o functie fara return care primeste ca parametru un string si printeaza pe ecran:
# # - Nr. caractere lower case este x
# # - Nr. caractere upper case este y

def nr_tip_caractere(string):
    lista_upper = [] #declara o lista goala in care vom adauga toate caracterele upper case
    lista_lower = [] #declara o lista goala in care vom adauga toate caracterele lower case
    for x in string: # parcurgem lista string
       if str(x).isupper(): # verificam daca caracterul este upper case
           lista_upper.append(x) # adaugam caracterul uper case in lista upper
           upper_nr = len(lista_upper) # punem numarul de caractere din lista upper in variabila upper_nr
       else:
           lista_lower.append(x) # adaugam caracterul lower case in lista lower
           lower_nr = len(lista_lower)
    print(f'Nr. caractere lower case este: {lower_nr}')
    print(f'Nr. caractere upper case este: {upper_nr}')

nr_tip_caractere('String MajusC') #apelam functia


# # 8. Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele pozitive.

def numere_pozitive(lista_nr):
    lista_nr_pozitive = [] #declaram o lista goala in care vom adauga numerele pozitive
    for x in lista_nr: #parcurgem lista cu numere
        if x > 0: #punem conditia ca numarul sa fie pozitiv
            lista_nr_pozitive.append(x) #adaugam numarul in lista cu numere pozitive
    return lista_nr_pozitive

print(numere_pozitive([-1,2,3,-4,4])) # apelam functia

# # 9. Scrie o functie care nu returneaza nimic. Primeste 2 numere si printeaza:
# # - primul numar x este mai mare decat al doilea y
# # - al doilea numar y este mai mare decat primul numar x
# # - Numerele sunt egale.

def compara(a,b):
    if a > b:
        print(f'primul numar {a} este mai mare decat al doilea numar {b}')
    elif a < b:
        print(f'al doilea numar {b} este mai mare decat primul numar {a}')
    else:
        print('Numerele sunt egale')

compara(5,4)
compara(4,5)
compara(5,5)

# # 10. Scrie o functie care primeste un numar si un set de numere.
# # Printeaza 'am adaugat numarul nou in set' + returneaza True
# # sau printeaza 'Nu am adaugat numarul nou in set. Acesta exista deja' + returneaza False

def set_numere(numar, set_numere):
    if numar in set_numere: #pune conditia ca numar sa fie in setul de numere
        print(f'Nu am adaugat numarul nou in set. Acesta exista deja')
        return True
    else:
        set_numere.add(numar) # daca numarul nu exista in set atunci se va adauga
        print('Am adaugat numarul nou in set')
        return False

set_numere(2,{1,2,3,4,5})
set_numere(8,{1,3,4,5})



# c. OPTIONALE (STUDIU DE ECHIPA) -> may need google

# 1. Scrie o functie care primeste o luna din an si returneaza cate zile are acea luna.

from calendar import monthrange

def luna_anului(luna):
    rezultat = monthrange(2023, luna)
    return print(rezultat[1])

luna_anului(3)

# 2. Scrie o functie calculator care sa returneze 4 valori: suma, diferenta, inmultirea a 2 numere.
# In final vei putea face:

def calculator(a,b):
    suma = a + b
    diferenta = a - b
    inmultirea = a * b
    if b != 0:
        impartirea = a / b
    else:
        impartirea = None

    return suma, diferenta, inmultirea, impartirea

a, b, c, d = calculator(10, 0)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

# 3. Scrie o functie care primeste o lista cu cifre (adica doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un dictionar care ne spune de cate ori apare fiecare cifra
# =>
# dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def dictionar_cifre(lista_nr):
    lista_valori = [] #declara o lista goala in care vom adauga doar valorile intre 0 si 9 gasite
    dict_cifre =  {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    } # declara un dictionar cu key de la 0..9 si valorile 0
    for x in lista_nr: #parcurgem lista_nr
        if 0 <= int(x) <= 9: #punem conditia ca x sa fie cuprins intre 0 si 9
            lista_valori.append(x) #il adaugam pe x in lista_valori
            dict_cifre[x] = lista_valori.count(x) #pentru fiecare cheie x innumara in lista_valori de cate ori se regaseste valoarea x
    return dict_cifre

print(dictionar_cifre([-1,1,1,1,2,1,2,9,10,0,25])) #apeleaza functia dictionar_cifre


# 4. Scrie o functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.

def compara_trei(a,b,c):
    if a > b and a > c:
        rezultat = a
    elif b > a and b > c:
        rezultat = b
    elif c > a and c > b:
        rezultat = c
    elif a > b and a == c:
        rezultat = a
    elif a == b and a > c:
        rezultat = a
    elif b == c and b > a:
        rezultat = b
    else:
        rezultat = a

    return print(f'Valoarea maxima este: {rezultat}')

compara_trei(9,9,9)
compara_trei(1,2,3)

#SAU

def get_max(a, b, c):
    numbers = [a, b, c]
    return max(numbers)

print(get_max(1, 2, 3))
print(get_max(5, 200, -300))


# 5. Scrie o functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3, suma va fi 6 (0 + 1 + 2 + 3)

def suma_numere(a):
    if a > 0 and a == int(a): #pune conditia ca nr sa fie natural (mai mare decat 0 si sa fie intreg)
        suma = int(a*(a+1)/2) #suma numerelor naturale
        rezultat = print(suma)
    else:
        rezultat = print('Numarul introdus nu este natural')
    return rezultat

suma_numere(-2)
suma_numere(2.3)
suma_numere(4)

# 6. Scrie o functie care primeste 2 liste de numere (numerele pot fi dublate).
# Returnati valorile comune

# exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}

def list_intersect(lista1, lista2):
    rezultat = set(lista1).intersection(set(lista2)) #rezultat este intersectia a doua seturi, cele doua liste fiind convertite in set
    return rezultat

print(list_intersect([1, 1, 2, 3], [2, 2, 3, 4]))

# 7. Scrie o functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10 %, pretul va fi 90.
# Tratati cazurile in care reducerea este invalida. De exemplu o reducere de 110 % e invalida.

def reducere_pret(pret,reducere):
    if pret > 0 and 0 < reducere <= 100:
        reducere = pret * reducere/100
        aplica_reducere = pret - reducere
        rezultat = print(aplica_reducere)

    elif pret <= 0 or reducere > 100:
        rezultat = print('Pretul introdus incorect sau reducerea aplicata mai mare de 100%')

    else:
        rezultat = print('Reducerea aplicata este mai mica de 0%')


reducere_pret(-1,10)
reducere_pret(100,200)
reducere_pret(100,-10)

# 8. Scrie o functie care sa afiseze dara si ora curenta din RO.
# (bonus: afisati si data si ora curenta din China)

from time import strftime
import time

def data_ora_curenta():
    azi = strftime("%a, %d %b %Y %I:%M:%S %p %Z\n")
    print(azi)

data_ora_curenta()

# 9. Scrie o functie care sa afiseze cate zile mai sunt pana la ziua ta/ sau pana la craciun daca nu vrei sa ne zici
# cand e ziua ta :D.

from datetime import date

def count_zile():
    azi = date.today() #pune intr o variabila azi data curenta
    zi_nastere = date(2023,6,30) #pune intr o variabila data zilei de nastere
    timp_ramas = zi_nastere - azi #calculeaza diferenta dintre cele doue (timedelta)

    print(timp_ramas)

count_zile() #apeleaza functia