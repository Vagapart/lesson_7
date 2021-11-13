# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 20:21:20 2021

@author: ИнтелАв
"""

# Задание 1
class Matrix():
    def __init__(self, listOfList):
        self.mat = listOfList
    def __str__(self):
        strMat = ""
        for listY in self.mat:
            for x in listY:
                strMat = strMat + str(x) + " "
            strMat = strMat + "\n"
        return strMat
    def __add__(self, mat1):
        newList = []
        for i  in range(len(mat1.mat)):
            newListIn = []
            for j in range(len(mat1.mat[i])):
                 newListIn.append(mat1.mat[i][j] + self.mat[i][j])           
            newList.append(newListIn)
        return Matrix(newList)

m1 = Matrix([[0,1,2],[3,4,5],[6,7,8]])
print(m1)
 
m2 = Matrix([[10,11,12],[13,14,15],[16,17,18]])
print(m2)
 
m3 = m1 + m2
print(m3)

# Задание 2
from abc import ABC, abstractmethod

class Odejda(ABC):
    @abstractmethod
    def rashodTkani(self):
        pass
    
    
class Palto(Odejda):
    V  = 0
    @property
    def rashodTkani(self):
        return self.V/6.5 + 0.5

class Kostym(Odejda):
    H  = 0
    @property
    def rashodTkani(self):
        return self.H * 2  + 0.3
           
palto1 = Palto()
palto1.V = 52
print(palto1.rashodTkani)
        
kostym1 = Kostym()
kostym1.H = 60
print(kostym1.rashodTkani)

# Задание 3
class Kletka():
    def __init__(self, yacheika):
        self.yacheika = yacheika
        
    def __str__(self):
        return "клетка, в которой {0} ячеек".format(self.yacheika)
        
    def __add__(self, kl1):
        return Kletka(self.yacheika + kl1.yacheika)
    
    def __sub__(self, kl1):
        if self.yacheika - kl1.yacheika <= 0:
            print("Разница меньше нуля, вычтать нельзя")
        else:       
            return Kletka(self.yacheika - kl1.yacheika)
        
    def __mul__(self, kl1):
        return Kletka(self.yacheika * kl1.yacheika)
    
    def __truediv__(self, kl1):
        return Kletka(self.yacheika // kl1.yacheika)
    
    def make_order(self, kol):
        return (str("*" * int(kol) + "\n") * (int(self.yacheika) // int(kol)) + ("*" * (int(self.yacheika) % int(kol))))
     
kl1 = Kletka(100)
print(kl1)

kl2 = Kletka(5)
print(kl2)

print(kl1 + kl2)
print(kl1 - kl2)
print(kl1 * kl2)
print(kl1 / kl2)

print(kl1)
print(kl1.make_order(6))
print(kl2)
print(kl2.make_order(3))








