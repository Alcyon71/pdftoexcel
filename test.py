# -*- coding: utf-8 -*-
import os, os.path
# import win32com.client
#
# print(os.path.dirname(os.path.abspath(__file__)) + '\Test.xlsm')
#
# try:
#     xlApp = win32com.client.DispatchEx('Excel.Application')
#     xlsPath = os.path.expanduser(os.path.dirname(os.path.abspath(__file__)) + '\Test.xlsm')
#     wb = xlApp.Workbooks.Open(Filename=xlsPath)
#     xlApp.Run('ImportFeuille')
#     wb.Save()
#     xlApp.Quit()
#     print("Macro ran successfully!")
# except:
#     print("Error found while running the excel macro!")
#     xlApp.Quit()

# import xlwings as xw
#
# wb = xw.Book(os.path.dirname(os.path.abspath(__file__)) + '\Test.xlsm')
# sht = wb.sheets.add('TestSheets')
# sht.range('A1').value = 'Foo 1'
# wb.save(os.path.dirname(os.path.abspath(__file__)) + '\Test2.xlsm')
# wb.close()

