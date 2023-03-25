# TEMA 2: Metoda input(), metode string, operatori, conditionale
import numbers

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva.
# 2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'.
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# sigur ti se vor intipari in minte mai bine.
# Link catre video: https://www.itfactory.ro/8174437-intro-in-programare

# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. Citeste de la tastatura numele, citeste apoi de la tastatura prenumele. Afiseaza cate caractere are numele complet
# (nume + prenume), afisand propozitia 'Numele complet are x caractere.', unde x este numarul total de caractere.

nume = input('Introduceti numele: ')
prenume = input('Introduceti prenumele ')

print(f'Numele complet are {len(nume + prenume)} caractere.')

# 2. Citeste de la tastatura lungimea, citeste apoi de la tastatura latimea. Afiseaza aria dreptunghiului cu lungimea si
# latimea citite de la tastatura, afisand propozitia 'Aria dreptunghiului este x.', unde x este valoarea ariei.

lungimea = float(input('Introduceti lungimea: ')) # citeste de la tastatura o valoare a lungimii care va fi convertita in float
latimea = float(input('Introduceti latimea: ')) # citeste de la tastatura o valoare a latimii care va fi convertita in float

print(f'Aria dreptunghiului este: {lungimea * latimea}') # afiseaza aria

# 3. Avand stringul: 'Coral is either the stupidest animal or the smartest rock.', afisati de cate ori apare cuvantul
# 'the' in acesta.

prop_1 = 'Coral is either the stupidest animal or the smartest rock.'
print(prop_1.count('the ')) # afiseaza de cate ori apare 'the ' in prop_1 e vorba despre cuvant ATENTIE lasa un spatiu dupa!!!

# 4. Folosing acelasi string de la punctul 2, inlocuieste cuvantul 'the' cu 'THE' peste tot in propozitie si printeaza
# rezultatul.

print(prop_1.replace('the ','THE ')) #in prop_1 e vorba despre cuvant ATENTIE lasa un spatiu dupa!!!

# 5. Folosind acelasi string de la punctul 2, folositi un assert ca sa verificati daca acest string contine doar
# numere.

#assert prop_1.isnumeric() == True

# 6. Exploreaza urmatoarele metode ajutatoare ale string-ului si scrie cel putin un exemplu de folosire pentru fiecare:

# a. endswith() --> Return True if S ends with the specified suffix, False otherwise

prop_2 = 'TESTE' # defineste o variabila de tip string
print(prop_2.endswith('E')) #--> TRUE

# b. index()

print(prop_2.index('S')) # afiseaza index pentru caracterul S

# c. lower()

print(prop_2.lower()) # afiseaza stringul prop.2 cu caractere mici

# d. replace()

print(prop_2.replace('TES','SE')) # inlocuieste in prop_2 'TES' cu 'SE'

# e. strip()   --> Return a copy of the string with leading and trailing whitespace removed.
#If chars is given and not None, remove characters in chars instead

prop_3 = '     afara ploua     '
print(prop_3.strip()) # remove empty spaces from begining and end
#
prop_4 = 'afara ningea'
print(prop_4.strip('a')) # remove 'a' if found from the begining and end of the string

# f. split() --> Return a list of the substrings in the string, using sep as the separator string.

prop_5 = 'A fost foarte distractiv'
print(prop_5.split()) # --> ['A', 'fost', 'foarte', 'distractiv']

# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.

# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# 6. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.

# IF ELSE --> IF defineste o conditie care trebuie indeplinita (True) pentru putea executa codul in continuare.
# Atunci cand conditia din IF nu este indeplinita (False) codul aflat dupa ELSE va fi executat in continuare.

# 7. Verifica si afiseaza daca x este numar natural sau nu.
# (un numar se considera natural daca este numar intreg mai mare ca 0)

x = 10
if x > 0 :
    print('Numarul este natural')
else:
    print('Numarul nu este natural')

# 8. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru (adica 0).

x = 0
if x > 0:
    print('Numarul este pozitiv')
elif x < 0:
    print('Numarul este negativ')
else:
    print('Numarul este neutru')

# 9. Verifica si afiseaza daca x este intre -2 si 13 (incluzand capetele de interval).

x = 8

if -2 <= x <= 13:
    print('Numarul este inclus intr -2 si 13')
else:
    print('Numarul nu este inclus intre -2 si 13')
#
# # 10.
# # a. Declara o noua variabila numita y, de tip int.
#
x = 10
y = 5

# b. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

if x - y < 5:
    print('Diferenta dintre x si y este mai mica de 5')
else:
    print('Diferenta dintre x si y este mai mare sau egala cu 5')
#
# # 11. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
#
x = 26

# assert not(x >= 5 and x <= 27)

#SAU varianta cu IF:

if not (x >= 5 and x <= 27):
    print('x nu este intre 5 si 27')
else:
    print('x este intre 5 si 27')

# 12.
# a. Declara o noua variabila numita y, de tip int.

x = 5
y = 10

# b. Verifica si afiseaza daca x si y sunt egale. Daca nu, afiseaza care din ele este mai mare.

if x == y:
    print('x si y sunt egale')
else:
    if x > y:
        print('x este mai mare decat y')
    else:
        print('y este mai mare decat x')

# 13. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul
# este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).

x = 11
y = 13
z = 12

if (x == y and x != z) or (y == z and x != y) or (x == z and y != x):
    print('Triunghiul este isoscel')
elif x == y == z:
    print('Triunghiul este echilateral')
else:
    print('Triunghiul este oarecare')
#
# # 14. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# # Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
#
litera = input('Introduceti o litera: ').lower() # citeste de la tastaura o litera si converteste litera in lowercase

if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u' or litera == 'ă' or litera == 'î' or litera == 'â':
    print('Litera este o vocala')
else:
    print('Litera est o consoana')

# 15. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:

nota = float (input('Introduceti nota din sistem romanesc: '))
#
# # Peste 9 => A
# # Peste 8 => B
# # Peste 7 => C
# # Peste 6 => D
# # Peste 4 => E
# # 4 sau sub => F
#
if 9 < nota <= 10:
    nota = 'A'
    print(f'Nota in sistem american este:  {nota}')
elif 8 < nota <= 9:
    nota = 'B'
    print(f'Nota in sistem american este:  {nota}')
elif 7 < nota <= 8:
    nota = 'C'
    print(f'Nota in sistem american este:  {nota}')
elif 6 < nota <= 7:
    nota = 'D'
    print(f'Nota in sistem american este:  {nota}')
elif 4 < nota <= 6:
    nota = 'E'
    print(f'Nota in sistem american este:  {nota}')
elif 0 < nota <= 4:
    nota = 'F'
    print(f'Nota in sistem american este:  {nota}')
else:
    print('Valoarea introdusa trebuie sa fie intre 1 si 10')


# C. OPTIONAL (nivel > MEDIU) (s-ar putea sa ai nevoie de Google)

# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.
# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre).

x = 24

if len(str(x)) >= 4:
    print('Numarul are minim patru cifre')
else:
    print('Numarul are mai putin de patru cifre')

# 2. Verifica daca x are exact 6 cifre.

if len(str(x)) == 6:
    print('Numarul are 6 cifre')
else:
    print('Numarul nu are 6 cifre')

# 3. Verifica daca x este numar par sau impar.

if x % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

# 4. Avand trei variabile x, y, z (toate int) (le poti declara in cod sau citi de la tastatura),
# afiseaza in consola care este cel mai mare dintre ele.

x = 10
y = 4
z = 13
#
if x > y and x > z:
    print('Numarul cel mai mare este x')
elif y > x and y > z:
    print('Numarul cel mai mare este y')
elif z > x and z > y:
    print('Numarul cel mai mare este z')
else:
    if x == y and x > z:
        print('Numerele x si y sunt egale si au valoarea cea mai mare')
    elif y == z and y > x:
         print('Numerele y si z sunt egale si au valoarea cea mai mare')
    elif x == z and x > y:
         print('Numerele x si z sunt egale si au valoarea cea mai mare')
    else:
        print('Numerele x,y si z sunt egale')

# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid
# sau nu. (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau
# daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi).

x = 10
y = 12
z = 8

if (x + y > z) and (y + z > x) and (x + z > y):
    print('Triunghi valid')
else:
    print('Nu poate fi construit un triunghi cu lungimile laturilor introduse')

# 6.
# a. Avand stringul: 'Coral is either the stupidest animal or the smartest rock', citește de la tastatura
# un număr x de tip int.

text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introdu numarul: ')) # citeste de la tastatura un string si converteste in int

#
# # b. Afișează stringul fără ultimele x caractere.
# # Exemplu: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'
#
print(text[0:-x]) # afiseaza stringul mai putin x caractere

# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din
# primele 5 caractere + ultimele 5 caractere.

text = 'Coral is either the stupidest animal or the smartest rock'
text_nou = text[0:5] + ' ' + text[-4::] # string format din primele 5 si ultimele 5 caractere din 'text'
print(text_nou)

# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start
# al cuvântului rock - adică poziția in string la care începe cuvântul rock.
# (hint: este o funcție care te ajuta sa faci asta).
# Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant.
# Output asteptat: 'Coral is either the stupidest animal or the smartest '

text = 'Coral is either the stupidest animal or the smartest rock'
start_index_rock = text.index('rock') # salveaza indexul de start al cuvantului rock

print(start_index_rock) # afiseaza valoare indexului de start cuvant rock
print(text[0:start_index_rock]) # afiseaza textul pana la indexul de start al cuvantului rock

# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel.
# Se va folosi un assert.
# Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul
# si ultimul caracter este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)

text_1 = input('Introduceti un text: ')
text_1 = text_1.lower() # convert toate caracterele in lowercase

#assert text_1[0] == text_1[-1] # verifica daca primul si ultimul caracter sunt la fel

# 10. Avand stringul '0123456789', afiseaza doar numerele pare si apoi doar numerele impare.
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

text_2 = '0123456789'
numere_pare = text_2[0:10:2]
numere_impare = text_2[1:10:2]

print(numere_pare)
print(numere_impare)

# D. EXERCITII BONUS

# 1. Vrem sa cream o aplicatie pentru achizitionare de bilete de avion care sa primeasca drept inputuri
# urmatoarele informatii:
# a. Varsta

varsta = int(input('Introduceti varsta: '))
#
# # b. Insotit de mama
#
insotitor_mama = bool(input('Raspundeti cu Da daca este cazul sau doar apasati tasta enter: Aveti ca insotitor mama ? :'))
#
# # c. Insotit de tata
#
insotitor_tata = bool(input('Raspundeti cu Da daca este cazul sau doar apasati tasta enter: Aveti ca insotitor tata ? :'))
#
# # d. Pasaport
#
pasaport = bool(input('Raspundeti cu Da daca este cazul sau doar apasati tasta enter: Aveti pasaport ? :'))
#
# # e. Act permisiune mama
#
permisiune_mama = bool(input('Raspundeti cu Da daca este cazul sau doar apasati tasta enter: Aveti permisiune mama ? :'))
#
# # f. Act permisiune tata
#
permisiune_tata = bool(input('Raspundeti cu Da daca este cazul sau doar apasati tasta enter: Aveti permisiune tata ? :'))

# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport.
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti.
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la
# celalat parinte.
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care crezi
# ca ar trebui testate.
# Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca expected results
# sunt egale cu actual results.
# Exemple:
# 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

if varsta >= 18 and pasaport == True:
     print('Va puteti imbarca')
elif varsta < 18 and insotitor_tata == True and insotitor_mama == True:
    print('Va puteti imbarca')
elif varsta < 18 and pasaport == True and (insotitor_mama == True or insotitor_tata == True) and (permisiune_mama == True or permisiune_tata == True):
    print('Va puteti imbarca')
else:
    print('Nu va pueti imbarca')







# 2. Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random.
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online.
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator.
# - Verifica si afiseaza daca utilizatorul a ghicit numarul.
# - Vor exista 3 optiuni care vor trebui tratate:
# a. Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# b. Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# c. Ai ghicit. Felicitari! Ai ales x si zarul a fost y.

# 3. Verifica daca varsta introdusa de utilizator este mai mare
# decat 18 ani.

# 4. Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.

# 5.
# a. Citeste un numar de la tastatura.
# b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.

# 6.
# a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
# b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
# c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".

# 7. Citeste de la tastatura varsta utilizatorului si afiseaza categoria
# de varsta in care se incadreaza.
# Tine cont de aceste categorii de varsta:
# intre 0-18 ani: minor
# intre 18-65 ani: adult
# peste 65 ani: senior

# 8. Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
# cosul de cumparaturi, in functie de totalul cosului de cumparaturi
# Reducerea se aplica in felul urmator:
# - Total este intre 100 si 200 lei -> reducere 10%
# - Total intre 200 - 300 lei -> reducere 15%
# - Total intre 300-400 -> reducere 20 %
# - Total mai mare de 400 -> reducere 30 %.
# a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
# b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
# dupa aplicarea reducerii.

