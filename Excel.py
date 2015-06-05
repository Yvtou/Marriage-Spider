# -*- coding: utf-8 -*-

__author__ = 'Yvtou'


from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "New Title"

d = ws.cell(row = 4, column = 2)
d.value = 3.14

wb.save('balances.xlsx')
