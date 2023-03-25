"""
1.Git setup

OBLIGATORIU!
Creati-va cont de github si incarcati intr-un repo nou tot ce am facut pana acum la ore
Curs git/github
https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3
"""

"""
!! 2. Faceti urmatoarele exercitii dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
"""
"""
1. ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria(self):
        pass
    def descrie(self):
        print('Cel mai probabil am colturi')

# """
# 2. INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura
# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
# """

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.__l = latura

    @property
    def latura(self):
        return self.__l

    @latura.getter
    def latura(self):
        print('Get')
        return self.__l

    @latura.setter
    def latura(self,noua_latura):
        print('Set')
        self.__l = noua_latura

    @latura.deleter
    def latura(self):
        print('Deleter: Am sters latura')
        self.__l = None

    def aria(self):
        return self.__l ** 2

# """
# 3. Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
# """

class Cerc(FormaGeometrica):

    def __init__(self,raza):
        self.__r = raza
    @property
    def raza(self):
        return self.__r

    @raza.getter
    def raza(self):
        print('Get')
        return self.__r
    @raza.setter
    def raza(self,noua_raza):
        print('Set')
        self.__r = noua_raza

    @raza.deleter
    def raza(self):
        print('Deleter: Am sters raza')
        self.__r = None

    def aria(self):
        return FormaGeometrica.PI * self.__r ** 2

# """
# 4. POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# Creati un obiect de tip Cerc si jucati-va cu metodele lui
# """
    def descrie(self):
        print('Eu nu am colturi')

patrat1 = Patrat(5)
cerc1 = Cerc(5)

"""
5. Actualizati proiectul pe github facand un push la noul cod
In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public

Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4
"""
#https://github.com/MetalRiff