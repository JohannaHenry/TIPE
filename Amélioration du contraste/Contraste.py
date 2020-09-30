# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:33:28 2020

@author: Johanna
"""

import numpy as np

from PIL import Image


def contraste(fichier):
    im=Image.open(fichier)
    tab=np.array(im)
    for i in range (tab.shape[0]):
        for j in range (tab.shape[1]):
            if tab[i][j][0] <=130 and tab[i][j][1] <=130 and tab[i][j][2] <=130:
                tab[i][j][0]=0 #
                tab[i][j][1]=0 #le pixel devient noir
                tab[i][j][2]=0 #
            else:
                    tab[i][j][0]=255 #
                    tab[i][j][1]=255 #le pixel devient blanc
                    tab[i][j][2]=255 #
    new_im=Image.fromarray(tab)
    new_im.show()
    new_im.save(fichier.split('.')[0] + "_contraste.png")
    #split('.') transforme "exemple.png" en [exemple,png]
    