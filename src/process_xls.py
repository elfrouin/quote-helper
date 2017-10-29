#!/usr/bin/env python

from xlrd import open_workbook
from import_xls import ImportDisp

id=ImportDisp('Disponible.xls')
id.load_dispo()
book = open_workbook(id.name_file)
sheet= book.sheet_by_name(book.sheet_names()[0])
#
list_dispo=[]
for row in range(2,sheet.nrows):
    list_dispo.append(sheet.row_values(row)[0:5])
print list_dispo[0]