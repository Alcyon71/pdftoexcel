# -*- coding: utf-8 -*-
import os, os.path
import win32com.client

try:
    xlApp = win32com.client.DispatchEx('Excel.Application')
    xlsPath = os.path.expanduser('C:\Users\Romain\PycharmProjects\pdftoexcel\Test.xlsm')
    wb = xlApp.Workbooks.Open(Filename=xlsPath)
    xlApp.Run('ImportFeuille')
    wb.Save()
    xlApp.Quit()
    print("Macro ran successfully!")
except:
    print("Error found while running the excel macro!")
    xlApp.Quit()