# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:17:40 2020

@author: Johanna
"""

import numpy as np
from PIL import Image #importation du sous-module Image du module PIL


def nombredepoints3(fichier,v):
    im=Image.open(fichier)
    tab=np.array(im)
    L=[]
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            if tab[i][j][0]>=195 and tab[i][j][1]<=100 and tab[i][j][2]<=100:
                #le pixel est rouge, ses coordonnées sont stockées dans L
                L.append([i,j])
    nb,L3=Elim3(L,v)
    return nb, L3 #renvoie le nb de points rouges et leurs coordonnées



def Elim3(liste,v):
    L2=[]
    for i in range(len(liste)-1):
        if liste[i][0]<=liste[i+1][0]+v and liste[i][0]>=liste[i+1][0]-v: 
            if liste[i][1]<=liste[i+1][1]+v and liste[i][1]>=liste[i+1][1]-v: 
                #la coordonnée d'indice i est en double
                L2.append(i) #renvoie l'indice des coordonnées à supprimées
    S=0 #del diminue len(L2) à chaque itération
    for j in L2:
            del liste[j-S]
            S+=1
    return len(liste), liste #renvoie les coordonnées non supprimées



def compare(fichier1,fichier2,v,v2):
    nb1,L1 =nombredepoints3(fichier1,v)
    #nb et coordonnées des points rouges de la 1ere image
    nb2,L2 =nombredepoints3(fichier2,v)
    #nb et coordonnées des points rouges de la 2nd image
    L=[]
    x,y=abs(L1[0][0]-L2[0][0]),abs(L1[0][1]-L2[0][1])
    #décalages des lignes et des colonnes entre les 2 images
    for i in range(1,len(L1)):
        if L1[i][0]<=L2[i][0]+x+v2 and L1[i][0]>=L2[i][0]-x-v2: 
            if L1[i][1]<=L2[i][1]+y+v2 and L1[i][1]>=L2[i][1]-y-v2:
                L.append(i)
    if len(L)+1==nb2 : 
        return "les deux empreintes appartiennent à la même personne"
    else:
        return "les deux empreintes n'appartiennent pas à la même personne"