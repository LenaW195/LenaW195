# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:38:42 2024

@author: s_wernerle22
"""
# Version 1 mit append funktion

quad_zahl = [] #leere Liste erstellen
for z in range(1, 11):   #liste durchgehen,  z als Index erstellen, range könnte auch vordefiniert werden
    if (z%2==0):  # testen ob gerade Zahlen
        quad_zahl.append(z)   # gerade Zahlen werden so gespeichert
    else:
       quad_zahl.append(z**2) # wenn ungerade soll es quadriert werden

print(quad_zahl)  # Output siehe Aufgabenstellung



# mit Listen-Abstraktionen

quad_zahl_neu = [z if z%2 ==0 else z**2 for z in range(1,11)]  # [if ((z%2==0) == False) z**2 for z in range(1. 11)]

print(quad_zahl_neu)