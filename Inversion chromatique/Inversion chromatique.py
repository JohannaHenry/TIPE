# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np

from PIL import Image #importation du sous-module Image du module PIL


    
    
def renomme(fichier,transformee):
    fi=fichier.split('.')[0] #split transforme "exemple.png" en [exemple,png]
    return fi+"_"+transformee+".png" 
    
    
def inverse(fichier):
    im=Image.open(fichier) #ouverture d’une image au format png dans Python.
    tab=np.array(im)
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            tab[i][j][0]=255-tab[i][j][0] #inversion du rouge            
            tab[i][j][1]=255-tab[i][j][1] #inversion du vert 
            tab[i][j][2]=255-tab[i][j][2] #inversion du bleu 
    new_im=Image.fromarray(tab)
    new_im.show()
    #new_im.save(renomme(fichier,"negatif"))
    
    
    
    
    
    
    
    