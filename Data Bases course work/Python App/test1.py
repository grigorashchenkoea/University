from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from MainWindow import Ui_MainWindow
from RegistrationWindow import Ui_RegistrationWindow
from UserWindow import Ui_UserWindow
from OrderWindow import Ui_OrderWindow
import pyodbc
import datetime
from AdminWindow import Ui_AdminWindow

# cnxn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-QB9PMOQ;'
#                       'Database=mbp;'
#                       'Trusted_Connection=yes;')
# cursor = cnxn.cursor()
database = "mbp2"
server = "RUSLAN71C8"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                     SERVER=' + server + ';\
                     DATABASE=' + database + ';\
                     Trusted_Connection=yes;')
cursor = cnxn.cursor()


# добавили класс админ виндоу чтобы после авторизации работника открывался интерфейс
class AdminWindowClass(QMainWindow, Ui_AdminWindow):
    def __init__(self, parent=None):
        super(AdminWindowClass, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.ShowDataButton.clicked.connect(self.handleShowDataButton)
        self.AddDataButton.clicked.connect(self.handleAddData)

    def loadData(self, sql):
        cursor.execute(sql)
        rows = 0
        self.DataBaseTable.clear()
        self.DataBaseTable.setRowCount(0)
        self.DataBaseTable.setColumnCount(0)
        for row in cursor:
            columns = len(row)
            rows += 1
        if rows > 0:
            self.DataBaseTable.clear()
            self.DataBaseTable.setRowCount(rows)
            self.DataBaseTable.setColumnCount(columns)
        cursor.execute(sql)
        # сделал общую функцию
        for row_number, row_data in enumerate(cursor):
            for column_number, column_data in enumerate(row_data):
                self.DataBaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    def handleShowDataButton(self):
        chosendata = str(self.ChooseDataComboBox.currentText())
        if chosendata == "Clients":
            sql = 'SELECT * FROM Client'
            self.loadData(sql)
        if chosendata == "Employees":
            sql = 'SELECT * FROM Employee'
            self.loadData(sql)
        if chosendata == "Pharmacies":
            sql = 'SELECT * FROM Pharmacy'
            self.loadData(sql)
        if chosendata == "Products":
            sql = 'SELECT * FROM Product'
            self.loadData(sql)
        if chosendata == "Suppliers":
            sql = 'SELECT * FROM Supplier'
            self.loadData(sql)
        if chosendata == "Orders":
            sql = 'SELECT * FROM Order_purchase'
            self.loadData(sql)

    def handleAddData(self):
        AddDataTextString = self.AddDataTextEdit.toPlainText()
        AddDataText = AddDataTextString.split(';')
        print(AddDataText)
        chosendata = str(self.ChooseDataComboBox.currentText())

        if chosendata == "Clients":
            FIRST_NAME = 0  # Vlada;Oscar;meow;02-02-2021;F;Izh;mail;8912;meow
            print(AddDataText[FIRST_NAME])
            LAST_NAME = 1
            PATRONYMIC = 2
            BIRTHDAY = 3
            GENDER = 4
            ADDRESS = 5
            EMAIL = 6
            PHONE_NUMBER = 7
            PASSWORD = 8
            print('starting...')
            cursor.execute('''Insert Into Client (First_Name, Second_Name, Patronymic, Birthday, Gender, Address, Email, Phone_Number)
                                VALUES (?,?,?,?,?,?,?,?)''', (AddDataText[FIRST_NAME], AddDataText[LAST_NAME],
                                                              AddDataText[PATRONYMIC], AddDataText[BIRTHDAY],
                                                              AddDataText[GENDER], AddDataText[ADDRESS],
                                                              AddDataText[EMAIL], AddDataText[PHONE_NUMBER]))
            print(1)
            # вставили пользователя в бд
            cursor.execute('''Insert into Password (HASH, Employee_Client) values (?,?)''',
                           (AddDataText[PASSWORD], 'E'))
            # вставили пароль в бд
            print(2)
            cursor.execute('''select password# from Password''')
            for row in cursor:
                password_id = int(row[0])
            cursor.execute('''select Client# from Client''')
            for row in cursor:
                client_id = int(row[0])
            # собраил айди пользователя, айди пароля из бд для таблицы клиент пароль
            cursor.execute(
                '''insert into Client_Password (Start_Date, End_Date, Client#, Password#) VALUES (CAST(GETDATE() AS DATE), Null,?,?)''',
                (client_id, password_id))
            # вставили значеие в таблицу пароль - клиент
            print(3)
            cnxn.commit()
            print(f'Пользватель {AddDataText[FIRST_NAME]} Создан!')
        if chosendata == "Employees":
            pass


class RegistrationWindowClass(QMainWindow, Ui_RegistrationWindow):
    def __init__(self, parent=None):
        super(RegistrationWindowClass, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.RegisterButton.clicked.connect(self.on_click_register)

    def on_click_register(self):
        First_Name = self.FirstNameTextEdit.toPlainText()
        # print(First_Name)
        Last_Name = self.LastNameTextEdit.toPlainText()
        # print(Last_Name)
        Patronymic = self.PatronymicTextEdit.toPlainText()
        # print(type(Patronymic))
        Gender = self.GenderTextedit.toPlainText()
        # print(Gender)
        Birth_date = self.BirthdayEdit.date().getDate()
        # print(Birth_date)
        Email = self.EmailTextEdit.toPlainText()
        # print(Email)
        Phone_number = self.PhoneNumberTextEdit.toPlainText()
        # print(type(Phone_number))
        Address = self.AddressTesxtEdit.toPlainText()
        # print(Address)
        Password = self.PasswordTextEdit.toPlainText()
        # print(Password)
        birthday = str(Birth_date[1]) + '-' + str(Birth_date[2]) + '-' + str(Birth_date[0])
        # print(birthday)
        print('starting...')
        cursor.execute('''Insert Into Client (First_Name, Second_Name, Patronymic, Birthday, Gender, Address, Email, Phone_Number)
                            VALUES (?,?,?,?,?,?,?,?)''',
                       (First_Name, Last_Name, Patronymic, birthday, Gender, Address, Email, Phone_number))
        # вставили пользователя в бд
        cursor.execute('''Insert into password (HASH, Employee_Client) values (?,?)''', (Password, 'C'))
        # вставили пароль в бд
        cursor.execute('''select password# from password''')
        for row in cursor:
            password_id = int(row[0])
        cursor.execute('''select Client# from client''')
        for row in cursor:
            client_id = int(row[0])
        # собраил айди пользователя, айди пароля из бд для таблицы клиент пароль
        cursor.execute(
            '''insert into Client_Password (Start_Date, End_Date, Client#, Password#) VALUES (CAST(GETDATE() AS DATE), Null,?,?)''',
            (client_id, password_id))
        # вставили значеие в таблицу пароль - клиент
        cnxn.commit()
        print(f'Пользватель {First_Name} Создан!')


class MainWindowClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowClass, self).__init__(parent)
        self.setupUi(self)
        self.SignUpButton.clicked.connect(self.handleSignUpButton)
        self.SignInButton.clicked.connect(self.handleSignInButton)

    def handleSignInButton(self):
        count = 0
        CLIENT_ID = 0
        FISRT_NAME = 1
        LAST_NAME = 2
        EMAIL = 3
        PASSWORD = 4
        # переменные для селект запроса
        requested_login = self.LoginTextEdit.toPlainText()
        requested_password = self.PasswordTextEdit.toPlainText()
        # беру пароль введный пользвателем и делаю запрос паролей из бд. в коде сначала клиенты потом сотрудники
        sql_request_client = cursor.execute(
            '''select C.Client#, C.First_Name, C.Second_Name, Email, Hash from Client_Password CP join Client C on CP.Client# = C.Client# join Password P on CP.Password# = P.Password#''')
        for row in sql_request_client:
            first_name = row[FISRT_NAME]
            last_name = row[LAST_NAME]
            user_id = row[CLIENT_ID]
            login = row[EMAIL]
            password = row[PASSWORD]
            # прогоняю введенные данные на совпадение с данными из бд для клиента
            if login == requested_login:
                if password == requested_password:
                    print(f'Welcome {first_name} {last_name}! We are glad to see you. Your client id is {user_id}')
                    window = UserWindowClass(login, first_name, self)
                    window.show()
                    count += 1
        sql_request_employee = cursor.execute(
            '''select E.Employee#, E.First_Name, E.Second_Name, E.Email, P.Hash from Employee_Password EP join Employee E on EP.Employee# = E.Employee# join Password P on EP.Password# = P.Password#''')
        for row in sql_request_employee:
            first_name = row[FISRT_NAME]
            last_name = row[LAST_NAME]
            user_id = row[CLIENT_ID]
            login = row[EMAIL]
            password = row[PASSWORD]
            # прогоняю введенные данные на совпадение с данными из бд для сотрудника
            if login == requested_login:
                if password == requested_password:
                    print(f'Welcome {first_name} {last_name}! We are glad to see you. Your Employee id is {user_id}')
                    window = AdminWindowClass(self)
                    window.show()
                    count += 1
        if count == 0:
            print('Wrong login or password')
        # если это сотрудник, то открывается окно админки

    def handleSignUpButton(self):
        window = RegistrationWindowClass(self)
        window.show()


# Окно с приветствием и историей заказов, открывается после входа юзера
class UserWindowClass(QMainWindow, Ui_UserWindow):
    def __init__(self, login, first_name,  parent=None):
        super(UserWindowClass, self).__init__(parent)
        self.setupUi(self)
        self.MyOrdersButton_2.clicked.connect(self.handleMyOrdersButton_2)
        self.loadHistoryOfOrdersData(login)
        self.login = login
        self.first_name = first_name
        self.label.setText('Hello, ' + self.first_name + '!')

    def handleMyOrdersButton_2(self):
        window = OrderWindowClass(self)
        window.show()

    # Функция, загружающая историю последних 10 заказов юзера
    def loadHistoryOfOrdersData(self, login):
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(9)
        rowcounter = -1
        cursor.execute('''select Order_Purchase#,
         Client.Client#, Order_Status,
         Delivery_Method, Weight, Payment_Method,
         Payming_Amount, Order_Date,
         Email from Order_Purchase join Client on Order_Purchase.Client# = Client.Client#''')
        for row_number, row_data in enumerate(cursor):
            if row_data[8] == login:
                rowcounter = rowcounter + 1
                # self.tableWidget.insertRow(rowcounter)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(rowcounter, column_number, QtWidgets.QTableWidgetItem(str(column_data)))


# Окно для заказа, которое открывается при нажатии кнопки New Order в окне с привествие и историей заказа
class OrderWindowClass(QMainWindow, Ui_OrderWindow):
    def __init__(self, parent=None):
        super(OrderWindowClass, self).__init__(parent)
        self.setupUi(self)
        # self.loadAssortiment()
 #       self.ShowDataButton.clicked.connect(self.handleAddToOrder)

    # Функция загружающая ассортмент товаров доступных для покупки в интернет-магазине
    def loadAssortiment(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        cursor.execute('''select Product.Product#, Title, Quantity, Retail_Price from Warehouse join Product on Warehouse.Product# = Product.Product#  where Quantity != 0 ''')
        for row_number, row_data in enumerate(cursor):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
# Ебаный ордер
    # def Matrix(self, matrix, row):
    #     matrix = matrix.append(row)
    #     return matrix
    #
    # def handleAddToOrder(self):
    #     self.tableWidget_2.setRowCount(0)
    #     self.tableWidget_2.setColumnCount(3)
    #     matrix = []
    #     AddToOrder = self.textEdit.toPlainText()
    #     AddToOrder = AddToOrder.split(';')
    #     row_number = 0
    #     ProductTitle = ''
    #     ProductRetailPrice = ''
    #     Order = []
    #     OrderItem = []
    #     tablefororder = cursor.execute(
    #         '''select Product.Product#, Title,  Retail_Price from Warehouse join Product on Warehouse.Product# = Product.Product#  where Quantity != 0 ''')
    #     for row in tablefororder:
    #         if AddToOrder[0] == row[0]:
    #             row_number = row_number + 1
    #             self.tableWidget_2.insertRow(row_number)
    #             self.tableWidget_2.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(AddToOrder[0])))
    #             self.tableWidget_2.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(AddToOrder[0])))

        # for row_number, row_data in enumerate(tablefororder):
        #     if AddToOrder[0] == row_data[0]:
        #         Order.append([])
        #         #self.tableWidget_2.insertRow(row_number)
        #         for column_number, column_data in enumerate(row_data):
        #             ProductTitle = column_data[1]
        #             ProductRetailPrice = column_data[2]
        #             OrderItem = []
        #             OrderItem.append(AddToOrder[0])
        #             OrderItem.append(ProductTitle)
        #             OrderItem.append(AddToOrder[1])
        #         Order.append(OrderItem)
        #
        # for row_number, row_data in enumerate(Order):
        #         self.tableWidget_2.insertRow(row_number)
        #         for column_number, column_data in enumerate(row_data):
        #             self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))


def main():
    import sys
    app = QtWidgets.QApplication([])
    win = MainWindowClass()
    win.show()
    sys.exit(app.exec_())


main()
