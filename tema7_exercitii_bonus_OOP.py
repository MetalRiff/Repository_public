"""
EXERCITII BONUS - OOP

Aceste exercitii sunt OPTIONALE!

"""

"""
1. 
a. Defineste clasa User.
Clasa User va avea urmatoarele atribute:
username (public) - se seteaza in constructor
email (public) - se seteaza in constructor
password (privat) - Nu primim atribut pentru el in constructor,
ci il initializam noi cu None (self.__password == None).

"""
class User:

    def __init__(self,username, email):
        self.username = username
        self.email = email
        self.__password = None

# """
# b. Implementeaza proprietatea password care va incapsula atributul privat
# password.
# Va avea:
# - getter:
# In getter verificam daca parola a fost setata (daca are valoare).
# Daca are valoare, atunci vom returna ***, unde numarul de * va fi egal
# cu lungimea parolei.
# Daca nu e setata, atunci afisam un mesaj ca parola nu e setata.
# - setter:
# In setter vom verifica, inainte sa setam parola, ca aceasta indeplineste
# urmatoarele conditii:
#     -- are minim 10 caractere
#     -- are cel putin o litera mare
# Daca aceste conditii se indeplinesc atunci setam parola.
# Daca nu, afisam un mesaj corespunzator pentru fiecare situatie.
#
# """
    @property
    def password(self):
        return self.__password

    @password.getter
    def password(self):
        if self.__password != None:
            return len(self.__password) * '*'
        else:
            return 'Parola nu este setata'

    @password.setter
    def password(self,new_password):
        if len(new_password) >= 10:
            for i in new_password:
                if str(i).isupper():
                    self.__password = new_password
                    return new_password
                else:
                    print('Parola trebuie sa aiba minim un caracter cu majuscula')
                    break
        else:
            print('Parola trebuie sa aiba minim 10 caractere')

# """
# c. Metode:
# - Metoda login: verificam ca user-ul are atat username, email si parola.
# Daca are, atunci afisam mesajul "Conectat".
# Daca nu, afisam mesajul "Lipsesc credentiale de conectare. Nu va putem conecta"
#
# d. Asigura-te ca creezi cel putin doua obiecte din clasa User.
# Afiseaza toate atributele/metodele/proprietatile.
# """
    def login(self):
        if self.username != None and self.email != None and self.__password != None:
            print('Conectat')
        else:
            print('Lipsesc credentiale de conectare. Nu va putem conecta')



user1 = User('Vasile','vasile@yahoo.com')

print(user1.password)

user1.password = 'A12345678'
user1.login()

user1.password = '12345678888'
user1.login()

user1.password = 'A123456789'
print(user1.password)

user1.login()


# """
# 2.
# a. Defineste clasa abstracta Person.
# Metode abstracte: wake_up, sleep, eat.
# Metoda: describe -> afiseaza mesajul "O persoana se trezeste, mananca si doarme."

from abc import ABC, abstractmethod

class Person:
    @abstractmethod
    def wake_up(self):
        pass
    def sleep(self):
        pass
    def eat(self):
        pass

    def describe(self):
        print('O persoana se trezeste, mananca si doarme.')

# b. Defineste clasa Student.
# Clasa Student implementeaza clasa abstracta Person.
# Atribute in constructor: name, university, grade.
# Metode describe -> afiseaza SI mesajul:
# Studentul x, studiaza la universitatea y si are nota generala z.

class Student(Person):

    def __init__(self,name,university,grade):
        self.name = name
        self.university = university
        self.grade = grade
    def describe(self):
        print(f'Studentul {self.name}, studiaza la {self.university}, si are nota generala {self.grade}')

# c. Defineste clasa Employee.
# Clasa Employee implementeaza cls abstracta Person.
# Atribute in constructor: name, experience, salary.
# Salary este un atribut privat!
# Metoda describe -> afiseaza SI mesajul:
# Angajatul x lucreaza de y ani.

class Employee(Person):
    def __init__(self,name,expierence,salary):
        self.name = name
        self.expierence = expierence
        self.__salary = salary

    def describe(self):
        print(f'Angajatul {self.name} lucreaza de {self.expierence} ani')

# d. Creeaza proprietatea salary care sa incapsuleze atributul privat salary.
# """
    @property
    def salary(self):
        return self.__salary
    @salary.getter
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary
        return new_salary
    @salary.deleter
    def salary(self):
        self.__salary = None


persoana1 = Student('Adi','Transilvania',10)
persoana1.describe()

pers2 = Employee('Gigel', 7, 1200)
pers2.describe()

pers2.salary = 1500

del pers2.salary

print(pers2.salary)

