import math
import turtle

def les_inn_flyttall (beskjed):        #legger inn en funksjon. 
    tall_streng =  input(beskjed)
    tallet = float(tall_streng)
    return tallet 

from math import sqrt

lengde_x = les_inn_flyttall ("Skriv inn verdien til linja langs x-aksen: ")
vinkel_degree = les_inn_flyttall ("Skriv in vinkelen mellom linja og hypotenusen i grader ")
vinkel_rad = (vinkel_degree*3.1415)/180


hypotenus = lengde_x/math.cos (vinkel_rad)
motsatt = sqrt((hypotenus**2)-(lengde_x**2))



print (f"Hypotenusen til trekanten er: {hypotenus}. ")
print (f"De to katetene er: {lengde_x} og {motsatt}")
print (f"Vinkelen i grader er: {vinkel_degree}")
print (f"Vinkelen i radianer er: {vinkel_rad}", end="")

Vinkel_B=90+vinkel_degree

turtle.back(lengde_x)
turtle.left(vinkel_degree)
turtle.forward(hypotenus)
turtle.right(Vinkel_B)
turtle.forward(motsatt)
turtle.done()
print("hihi")