from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from AdminWindow import Ui_AdminWindow
import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QB9PMOQ;'
                      'Database=mbp1;'
                      'Trusted_Connection=yes;')
cursor = cnxn.cursor()

class AdminWindowClass(QMainWindow, Ui_AdminWindow):
    def __init__(self, parent=None):
        super(AdminWindowClass, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.ShowDataButton.clicked.connect(self.handleShowDataButton)
        self.AddDataButton.clicked.connect(self.handleAddData)


    def loadDataClient(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-QB9PMOQ;'
                              'Database=mbp1;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()


        result = cursor.execute('SELECT * FROM Client')
        self.DataBaseTable.setRowCount(0)
        self.DataBaseTable.setColumnCount(9)
        for row_number, row_data in enumerate(result):
            self.DataBaseTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.DataBaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    def loadDataEmployee(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-QB9PMOQ;'
                              'Database=mbp1;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM Employee')
        self.DataBaseTable.setRowCount(0)
        self.DataBaseTable.setColumnCount(11)
        for row_number, row_data in enumerate(result):
            self.DataBaseTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.DataBaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    def loadDataPharmacy(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-QB9PMOQ;'
                              'Database=mbp1;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM Pharmacy')
        self.DataBaseTable.setRowCount(0)
        self.DataBaseTable.setColumnCount(6)
        for row_number, row_data in enumerate(result):
            self.DataBaseTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.DataBaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    def loadDataProduct(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-QB9PMOQ;'
                              'Database=mbp1;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM Product')
        self.DataBaseTable.setRowCount(0)
        self.DataBaseTable.setColumnCount(12)
        for row_number, row_data in enumerate(result):
            self.DataBaseTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.DataBaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))


    def loadDataSupplier(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-QB9PMOQ;'
                              'Database=mbp1;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM Supplier')
        self.DataBaseTable.setRowCount(0)
        self.DataBaseTable.setColumnCount(9)
        for row_number, row_data in enumerate(result):
            self.DataBaseTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.DataBaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    def loadDataOrder(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-QB9PMOQ;'
                              'Database=mbp1;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM Order_purchase')
        self.DataBaseTable.setRowCount(0)
        self.DataBaseTable.setColumnCount(9)
        for row_number, row_data in enumerate(result):
            self.DataBaseTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.DataBaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    def handleAddData(self):
        chosendata = str(self.ChooseDataComboBox.currentText())
        AddDataText = []
        AddDataTextString = self.AddDataTextEdit.toPlainText()
        AddDataText = AddDataTextString.split(';')
        for i in AddDataText:
            print(type(i))
        print(AddDataText)
        chosendata = str(self.ChooseDataComboBox.currentText())
        if chosendata == "Clients":
            cursor.execute(''' insert into Client  (First_Name, Last_Name, Patronymic, Birthday, Gender, Address, Email, Phone_Number)
                                VALUES (?,?,?,?,?,?,?,?)''', (AddDataText[0], AddDataText[1], AddDataText[2], AddDataText[3], AddDataText[4], AddDataText[5], AddDataText[6], AddDataText[7]))
        if chosendata == "Employees":
            cursor.execute(''' insert into Employee  (First_Name, Second_Name, Patronymic, Email, Gender, Birthday, Phone_Number, Working_Hours, Card_Number, "Position")
                                VALUES (?,?,?,?,?,?,?,?,?,?)''', (AddDataText[0], AddDataText[1], AddDataText[2], AddDataText[3], AddDataText[4], AddDataText[5], AddDataText[6], AddDataText[7], AddDataText[8], AddDataText[9]))
       #     cursor.execute(''' insert into Password  (Hash, Employee_Client)
        #                                               VALUES (?,?)''', (AddDataText[10], 'E'))
        #    cursor.execute('''select password# from password''')
        ##    for row in cursor:
       ##         password_id = int(row[0])
       #     cursor.execute('''select Employee# from Employee''')
       #     for row in cursor:
       #         employee_id = int(row[0])
        #    cursor.execute(
        #        '''insert into Employee_Password (Start_date, End_Date, Password#, Employee#) VALUES (CAST(GETDATE() AS DATE), Null,?,?)''',
         #       (password_id, employee_id))

        if chosendata == "Pharmacies":
            cursor.execute(''' insert into Pharmacy  (Address, Working_Time, Surface_Area, Phone_Number, License#)
                                            VALUES (?,?,?,?,?)''', (AddDataText[0], AddDataText[1], AddDataText[2], AddDataText[3], AddDataText[4]))
        if chosendata == "Products":
            cursor.execute(''' insert into Product  (Title, Wholesale_Price, Retail_Price, Manufacturer, MNN, BdN, Form, Shelf_Life, Prescription_Necessity, License#)
                                            VALUES (?,?,?,?,?,?,?,?,?,?)''', (AddDataText[0], AddDataText[1], AddDataText[2], AddDataText[3], AddDataText[4], AddDataText[5], AddDataText[6], AddDataText[7], AddDataText[8], AddDataText[9]))
        if chosendata == "Suppliers":
            cursor.execute(''' insert into Supplier  ("Name", First_Name, Last_Name, Patronymic, Email, Address, Supply_Schedule, Minimum_Order_Amount, Phone_Number)
                                            VALUES (?,?,?,?,?,?,?,?,?)''', (AddDataText[0], AddDataText[1], AddDataText[2], AddDataText[3], AddDataText[4], AddDataText[5], AddDataText[6], AddDataText[7], AddDataText[8]))
        if chosendata == "Orders":
            cursor.execute(''' insert into Order_purchase (Weight, Delivery_Method, Payment_Method, Order_Status, Payming_Amount, Order_Date, Client#, Offer_Name)
                                            VALUES (?,?,?,?,?,?,?,?)''', (AddDataText[0], AddDataText[1], AddDataText[2], AddDataText[3], AddDataText[4], AddDataText[5], AddDataText[6], AddDataText[7]))
        cnxn.commit()



    def handleShowDataButton(self):
        chosendata = str(self.ChooseDataComboBox.currentText())
        if chosendata == "Clients":
            self.loadDataClient()
        if chosendata == "Employees":
            self.loadDataEmployee()
        if chosendata == "Pharmacies":
            self.loadDataPharmacy()
        if chosendata == "Products":
            self.loadDataProduct()
        if chosendata == "Suppliers":
            self.loadDataSupplier()
        if chosendata == "Orders":
            self.loadDataOrder()

##  def handleAddDataButton(self):




def admin():
    import sys
    app = QtWidgets.QApplication([])
    win = AdminWindowClass()
    win.show()
    sys.exit(app.exec_())


admin()
