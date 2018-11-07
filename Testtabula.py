# -*- coding: utf-8 -*-
import sys
import os
import tabula
import pandas as pd
import Tkinter as tk
import tkMessageBox
from tkFileDialog import askopenfilename
#from openpyxl import load_workbook
#from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import date
#TODO : Choix du fichier à lire

#Fenetre tres simple pour choisir le fichier PDF
def choixfichier():
    root = tk.Tk()
    root.withdraw()                 # pour ne pas afficher la fenêtre Tk
    name = askopenfilename()   # lance la fenêtre
    print(name)
    _, ext = os.path.splitext(name)
    print(ext)

    if ext == ".pdf":
        return name
    else:
        return False


def extrairepdf(Cheminpdf):
    # Read pdf into DataFrame
    print(Cheminpdf)
    df = tabula.read_pdf(Cheminpdf, pages='all', multiple_tables=True)
    #on supprime les 3 premieres lignes
    df = [df[i].iloc[3:,] for i in range(len(df))]

    #On merge les tableaux de df
    #merge = pd.DataFrame()
    merge = pd.concat([i for i in df],ignore_index=True)

    # on va essayer de filtrer les identifiants des échantillons, soit bon, soit coulée soit fils de la ligne précédente
    for row in merge.itertuples():
        #print(row)
        #print(merge.iloc[row[0],3])
        #Un casier a maximum 4 chiffre
        if len(row[4]) > 4:
            merge.iloc[row[0],3] = merge.iloc[row[0],3].replace(" ", "-")
        else:
            merge.iloc[row[0], 3] = merge.iloc[row[0]-1, 3]

    #TODO : Si la date n'est pas en colonne 9(10 dans le namedtuple), la copier de la colonne 10(11 dans le namedtuple), puis sup la colonne 10
        #print(type(row[10]))
        if type(row[10]) is float:
            merge.iloc[row[0], 9] = merge.iloc[row[0], 10]

    #On supprime la colonne 10 et 4
    merge = merge.drop([4, 10], axis=1)
    print(merge)
    return merge

def creerexcel(valeur):
    HeaderExcel = ["Type","Famille","Nuance","Identifiant échantillon","PE","Réacteur","Fiole","Observations","Délai"]

    writer = pd.ExcelWriter('merge.xlsx', )
    valeur.to_excel(writer, date.today().strftime("%d-%m-%y"), header=HeaderExcel, index=False)
    writer.save()


if __name__ == '__main__':
    Nonfichier = choixfichier()
    if Nonfichier is False:
        tkMessageBox.showerror("Titre", "Mauvais fichier! ce n'est pas un pdf")
        sys.exit()
    else:
        creerexcel(extrairepdf(Nonfichier))




#writer = pd.ExcelWriter('output.xlsx')
# i = 0
# for tab in df:
#     i += 1
#     tab = tab.iloc[3:,]
#     tab.to_excel(writer, 'Sheet'+str(i))

#writer.save()


