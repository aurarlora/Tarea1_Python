# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 03:18:33 2019
Examen de conocimientos de la historia de México
@author: Aura
https://www.buzzfeed.com/mx/javieraceves/hidalgo-al-menos-hizo-algo
"""


import json
from random import randint

#with open('preguntas.json') as file:
#    preg = json.load(file)

def random_question():
    with open('preguntas.json') as fp:
        data = json.load(fp)
        
        random_index = randint(0, len(data)-1)
        
        a = data[random_index]['p']
        b = data[random_index]['r']
        
        return (a,b,random_index)
    
def integrar(b):
    y = ""
    
    i=len(b)
    for x in b:
       y = "R"+str(i)+ ":  "+x +"\n" + y
       i= i-1
    print (y)


def calificar(resp):
    ac=[]
    ##        1,2,3,4,5,6,7,8,9,10
    aciertos=[1,2,4,3,1,3,2,1,1,4]
    for i,j in resp:
        if j ==  aciertos[i+1]:
            ac.append(1)
        else:
            ac.append(0)
    return (ac)
    


print  ( "CUESTIONARIO DE HISTORIA \n")
print ("******************************** \n\n")
resp = []

for i in range (0,5):        
    (a,b,c)=random_question()
    print("PREGUNTA_"+str(i+1) +  "\n"+a + "\n")
    integrar(b)
    r = input("Escribe el numero de Respuesta: ")
    print ("___ \n\n")
    r = int(r)-1
    resp.append([c,r]) 

print (resp)
print ("__________________________________ \n\n")
print ("Respuestas: ")

cal =  calificar(resp)


print (cal)

suma = sum(cal)

print ("Tu calificación es:  "+str(suma)) 




