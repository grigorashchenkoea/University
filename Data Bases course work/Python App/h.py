import datetime
import sys
import pyodbc
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


database = "mbp"
server = "RUSLAN71C8"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                      SERVER=' + server + ';\
                      DATABASE=' + database + ';\
                      Trusted_Connection=yes;')
cursor = cnxn.cursor()
type = 'best_one_new'
exp = '02-02-2002'
prod = '01-01-2001'
# cursor.execute("exec insert_license 'dot', '1-1-2000', '2-2-2002'")

# ниже как вставлять переменные в процедуру! Полезно
# cursor.execute("exec insert_license ?, ?, ?", (type, prod, exp))
# cnxn.commit()

# type = 'strong_python_new'
# exp = '02-02-2021'
# prod = '02-02-2020'
#Ниже как вставлять переменные в инсерт! Полезно
# cursor.execute(''' Insert INTO license (Type, Issue_Date, Expiration_Date) VALUES (?,?,?)''', (type, exp, prod))
# cnxn.commit()
# cursor.execute(''' exec insert_product "zvezdochka", 100, 120, "USSR", "MNN", "T", "Krem", 2000, "1", 1 ''')
# cnxn.commit()
#
# cursor.execute('select * from Product')
# for row in cursor:
#     print(row)


