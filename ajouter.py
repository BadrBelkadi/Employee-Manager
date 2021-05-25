import mysql.connector
from mysql.connector import MySQLConnection, Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import *


class Ui_AjouterWindow(object):
    def connect(self):
        try:
            mydb = mysql.connector.connect(host='localhost',
                                           database='projet',
                                           user='root',
                                           password='')
        except Error as e:
            print("Error while connecting to MySQL", e)

        return mydb

    def insert_data(self):
        mydb = self.connect()

        mycursor = mydb.cursor()

        nom = self.textEdit_2.toPlainText()
        prenom = self.textEdit_3.toPlainText()
        CNE = self.textEdit_4.toPlainText()
        id_fct = self.comboBox.currentText()
        dateB = self.dateEdit.dateTime()
        dt_string = dateB.toString('yyyy/MM/dd')

        query = "INSERT INTO PERSONNE (Nom,Prenom,CNE,fonction,Date_Naissance) VALUES ( %s, %s, %s, %s, %s)"

        value = (nom, prenom, CNE, id_fct, dt_string)

        mycursor.execute(query, value)

        mydb.commit()

    def show_datas(self, m):

        mydb = self.connect()

        mycursor = mydb.cursor()
        sql = "SELECT * FROM PERSONNE WHERE Id="+m
        # print(m)
        mycursor.execute(sql)
        row = mycursor.fetchone()

        if row:
            self.textEdit_2.setText(row[1])
            self.textEdit_3.setText(row[2])
            self.textEdit_4.setText(row[3])
            self.comboBox.clear()
            self.comboBox.addItem(row[4])
            self.dateEdit.setDate(row[5])
            options = ["Président", "Directeur",
                       "Ing Informatique", "Comptable", "Ouvrier"]
            for option in options:
                if row[4] == option:
                    continue
                else:
                    self.comboBox.addItem(option)

    def alter(self, m):
        mydb = self.connect()

        cur = mydb.cursor()
        sql = "DELETE FROM PERSONNE WHERE id="+m
        cur.execute(sql)

        mydb.commit()

        cur.close()
        mydb.close()

    def update(self):

        mydb = self.connect()
        cur = mydb.cursor()

        nom = self.lineEdit_2.text()
        prenom = self.lineEdit_3.text()
        CNE = self.lineEdit_4.text()
        fonction = self.comboBox.currentText()
        dateB = self.dateEdit.dateTime()
        dt_string = dateB.toString('yyyy/MM/dd')

        query = "INSERT INTO PERSONNE (Nom,Prenom,CNE,fonction,Date_Naissance) VALUES ( %s, %s, %s, %s, %s)"

        value = (nom, prenom, CNE, fonction, dt_string)

        cur.execute(query, value)
        mydb.commit()

        cur.close()
        mydb.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 101, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 50, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(200, 100, 191, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(200, 150, 191, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(70, 300, 161, 61))
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.insert_data)
        self.btn_add.clicked.connect(MainWindow.hide)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 250, 101, 16))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(200, 201, 191, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 250, 191, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(300, 300, 161, 61))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(self.insert_data)
        self.btn_exit.clicked.connect(MainWindow.hide)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Ajouter/Modifier une personne"))
        self.label_2.setText(_translate("MainWindow", "Nom"))
        self.label_3.setText(_translate("MainWindow", "Prenom"))
        self.label_4.setText(_translate("MainWindow", "CNE"))
        self.label_5.setText(_translate("MainWindow", "Date de Naissance"))
        self.btn_add.setText(_translate("MainWindow", "Enregistrer"))
        self.label_6.setText(_translate("MainWindow", "Fonction"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Président"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Directeur"))
        self.comboBox.setItemText(2, _translate(
            "MainWindow", "Ing Informatique"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Comptable"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Ouvrier"))
        self.btn_exit.setText(_translate("MainWindow", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AjouterWindow = QtWidgets.QDialog()
    a = Ui_AjouterWindow()
    a.setupUi(AjouterWindow)
    AjouterWindow.show()
    sys.exit(app.exec_())
