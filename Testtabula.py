# -*- coding: utf-8 -*-
import sys
import os
import tabula
import pandas as pd
import Tkinter as tk
import tkMessageBox
import win32com.client
import xlwings as xw
from tkFileDialog import askopenfilename
#from openpyxl import load_workbook
#from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import date

#Fenetre tres simple pour choisir le fichier PDF
def choixfichier():
    root = tk.Tk()
    root.withdraw()                 # pour ne pas afficher la fenêtre Tk
    name = askopenfilename()   # lance la fenêtre
    _, ext = os.path.splitext(name)
    if ext == ".pdf":
        return name
    else:
        return False


def extrairepdf(Cheminpdf):
    # Read pdf into DataFrame
    df = tabula.read_pdf(Cheminpdf, pages='all', multiple_tables=True)
    #on supprime les 3 premieres lignes
    df = [df[i].iloc[3:,] for i in range(len(df))]

    #On merge les tableaux de df
    #merge = pd.DataFrame()
    merge = pd.concat([i for i in df],ignore_index=True)

    # on va essayer de filtrer les identifiants des échantillons, soit bon, soit coulée soit fils de la ligne précédente
    for row in merge.itertuples():
        if len(row[4]) > 4:
            merge.iloc[row[0],3] = merge.iloc[row[0],3].replace(" ", "-")
        else:
            merge.iloc[row[0], 3] = merge.iloc[row[0]-1, 3]
        if type(row[10]) is float:
            merge.iloc[row[0], 9] = merge.iloc[row[0], 10]

    #On supprime la colonne 10 et 4
    merge = merge.drop([4, 10], axis=1)
    return merge

def creerexcel(valeur):
    HeaderExcel = ["Type","Famille","Nuance",'Identifiant échantillon',"PE","Réacteur","Fiole","Observations","Délai"]

    wb = xw.Book(os.path.dirname(os.path.abspath(__file__)) + '\Test.xlsm')
    #Todo: vérifier si la feuille existe déja, sinon erreur
    sht = wb.sheets.add(date.today().strftime("%d-%m-%y"), after=wb.sheets[-1])
    tbl = sht.api.ListObjects.add()
    tbl.Name ="EssaiTable"
    sht.range('A2').options(index=False, header=False).value = valeur
    #Boucle pour changer le nom des colonnes
    for i in range(len(HeaderExcel)):
        tbl.ListColumns(i+1).Name = unicode(HeaderExcel[i], 'utf-8')


    #wb.save(os.path.dirname(os.path.abspath(__file__)) + '\Test2.xlsm')
    #wb.close()

    #Ecrire dans le fichier avec to_excel, desactiver pour essayer xlwings
    # writer = pd.ExcelWriter('merge.xlsx', )
    # valeur.to_excel(writer, date.today().strftime("%d-%m-%y"), header=HeaderExcel, index=False)
    # writer.save()

#Plus utile si utilisation de xlwings pour copier les infos du dataframe
# def executermacro():
#     try:
#         xlapp = win32com.client.DispatchEx('Excel.Application')
#         xlspath = os.path.expanduser(os.path.dirname(os.path.abspath(__file__)) + '\Test.xlsm')
#         wb = xlapp.Workbooks.Open(Filename=xlspath)
#         xlapp.Run('ImportFeuille')
#         wb.Save()
#         xlapp.Quit()
#         print("Macro ran successfully!")
#     except:
#         print("Error found while running the excel macro!")
#         xlapp.Quit()

if __name__ == '__main__':
    Nonfichier = choixfichier()
    if Nonfichier is False:
        tkMessageBox.showerror("Mauvis fichier!", "Mauvais fichier! ce n'est pas un pdf")
        sys.exit()
    else:
        try:
            creerexcel(extrairepdf(Nonfichier))
        except ValueError as exceptmessage:
            tkMessageBox.showerror("Erreur", "Erreur lors de la création du fichier excel :" + str(exceptmessage))
        except:
            tkMessageBox.showerror("ERREUR!", "Erreur lors de la création du fichier excel!")



#writer = pd.ExcelWriter('output.xlsx')
# i = 0
# for tab in df:
#     i += 1
#     tab = tab.iloc[3:,]
#     tab.to_excel(writer, 'Sheet'+str(i))

#writer.save()


