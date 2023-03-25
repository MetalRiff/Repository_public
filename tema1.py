# TEMA 1

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza inregistrarea sesiunii 1 si ia notite
# 2. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE" (daca nu ai facut-o deja), sectiunea "Variable si Tipuri de date"
# 3. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE", sectiunea "Operatori si Flow Control".
# LINK curs "PRIMII PASI IN PROGRAMARE": https://www.itfactory.ro/8174437-intro-in-programare/


# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila.

# Variabila este o locatie din memorie unde sunt tinute date.

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool.
# Valorile le alegeti voi dupa preferinte.

a = 'Test'
b = 21
c = 11.3
d = True

# 3. Utilizati functia type(), pentru a verifica daca variabilele declarate la punctul 2 au tipul de date asteptat.

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 4. Rotunjiti variabila definita ca tip float, folosindu-va de functia round() si salvati aceasta modificare in aceeasi
# variabila (suprascriere). Verificati apoi tipul acesteia.

c = round(c)
print(c)

# 5. Folositi functia print() pentru a printa in consola 4 propozitii, folosind cele 4 variabile.
# (Rezolvati nepotrivirile de tip prin ce modalitate doriti)

print(f'Variabila a este {a} ')
print(f'Variabila b este {b}')
print(f'Variabila c este {c}')
print(f'Variabila d este {d}')

# 6.
# a. Defineste o variabila float cu valoarea 1.5 .

e = 1.5

# b. Verifica daca variabila este egala cu 1.5 .

assert e == 1.5
print('Da, variabila e este egala cu 1.5')

# c. Verifica daca variabila este egala cu true. Ce observi?

# Raspuns: assert ul se opreste si da eroare pentru ca afirmatia evaluata este falsa

#assert e == True

# d. Cum poti face ca assert-ul de la punctul c sa treaca?

# Raspuns: Convertim variabila in bool inainte de a apela asser == True

e = bool(e) # conversie variabila la tipul de date boolean
assert e == True
print(f'Am convertit variabila e in boolean si atribuit valoarea True si assert ul a trecut. Noua valoarea a variabilei e este acum  {e}')

# verificam daca variabila este egala cu 1.5

#assert e == 1.5



# C. OPTIONAL (nivel > MEDIU)

# 1. Citeste de la tastatura un string de dimensiune impara. Afiseaza caracterul din mijloc.

cuvant_1 = input('Introdu un cuvant palidrom e.g. rotor: ') #citeste un string de la tastatura

a = len(cuvant_1) # punem lungimea string ului intr o variabila "a" integer

if a % 2 != 0: # punem conditia ca numarul de caractere al variabile sa fie un numar impar

    jumatate = cuvant_1[a//2] # aflam caracterul din mijloc

    print(f'Caracterul din mijloc este: {jumatate}')


# 2. Folosind assert, verificati daca un string este palindrom.

inversat = cuvant_1[::-1] # inversam sirul

assert cuvant_1 == inversat #verificam daca sirul este identic cu sirul inversat

print('Cuvantul introdus este un palidrom')


# 3. Folosind o singura linie de cod, citeste un string de la tastatura (ex: 'alabala portocala') si salveaza fiecare
# cuvant intr-o variabila. Printeaza variabilele generate pentru verificare.

text_1, text_2 = input('Introduceti doua cuvinte: ').split() # definim 2 variabile si introducem datele de la tastatura dupa care folosim functia split ce imparte un string in o lista

print(f'Primul cuvant introdus este: {text_1}')
print(f'Al doilea cuvant introdus: {text_2}')


# 4. Citeste un string de la tastatura (ex: 'alabala portocala'). Salveaza primul caracter din string intr-o variabila.
# Capitalizeaza acest caracter peste tot in string, mai putin primul si ultimul caracter.
# Exemplu 1:
#   input: 'alabala portocala'
#   output: 'alAbAlA portocAla'
# Exemplu 2:
#   input: 'maria are mere'
#   output: 'maria are Mere'
# Exemplu 3:
#   input: 'aritmetica'
#   output: 'aritmetica'

text_3 = input('Introduceti un text in care primula caracter se repeta: ') # citeste un text de la tastatura
var_1 = text_3[0] # salveaza primul caracter intr o variabila
text_3 = text_3.replace(var_1, var_1.capitalize()) # capitalizeaza primul caracter si inlocuieste peste tot in string ul introdus anterior
text_3 = text_3[0].lower() + text_3[1:-1] + text_3[-1].lower() # primul si ultimul caracter din string devine lower case

print(f'Textul rezultat dupa capitalizarea selectiva este: {text_3}')

# 5. Citeste un user de la tastatura. Citeste apoi o parola de la tastatura. Afiseaza: 'Parola pentru userul x este ***
# si are y caractere.', unde x este user-ul citit de la tastatura, iar y lungimea parolei introduse la tastatura.
# Numarul de * din stringul afisat se va calcula dinamic, avand atatea * cate caractere exista in parola.

nume_user = input('Introduceti numele utilizatorului: ') #citeste de la tastatura nume utilizator
parola_user = input('Introduceti parola: ') #citeste de la tastatura parola

hide_parola = '*' * len(parola_user) #Thx to Alin :)) .. eu aici ma blocasem

print(f'Parola user {nume_user} este: {hide_parola} si are {str(len(parola_user))} caractere')

# Exemplu:
#   - daca parola introdusa este 'abcd', vom avea ***
#   - daca parola introdusa este 'abcdef', vom avea ******.