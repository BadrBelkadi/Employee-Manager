import mysql.connector
from mysql.connector import MySQLConnection, Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ajouter import *
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QPushButton, QMessageBox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pandas.io.sql as sql


class Ui_MainWindow(object):
    def connect(self):
        try:
            mydb = mysql.connector.connect(host='localhost',
                                           database='projet',
                                           user='root',
                                           password='')
        except Error as e:
            print("Error while connecting to MySQL", e)

        return mydb

    def delete(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setText("Are you sure you want to delete ?")

        msg.setIcon(QMessageBox.Warning)
        i = msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        x = msg.exec_()
        if x == QMessageBox.Yes:
            mydb = self.connect()

            cur = mydb.cursor()

            row = self.tableWidget.currentRow()
            id = self.tableWidget.item(row, 0).text()

            sql = "DELETE FROM PERSONNE WHERE id="+id

            cur.execute(sql)
            mydb.commit()
            cur.close()
            mydb.close()

            self.show_data()

    def show_data(self):
        mydb = self.connect()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM PERSONNE ORDER BY Nom")

        result = mycursor.fetchall()

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))

    def ex(self):
        mydb = self.connect()

        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM PERSONNE WHERE id="+id)

        result = mycursor.fetchall()

        canva = canvas.Canvas("repport.pdf", pagesize=letter)

        canva.setLineWidth(.3)
        canva.setFont('Helvetica', 12)
        canva.drawString(275, 725, 'Gestion des employees')
        for row in result:

            canva.drawString(200, 600, "Nom                  :")
            canva.drawString(300, 600, str(row[1]))

            canva.drawString(200, 580, "Prenom               :")
            canva.drawString(300, 580, str(row[2]))

            canva.drawString(200, 560, "CNE                  :")
            canva.drawString(300, 560, str(row[3]))

            canva.drawString(200, 540, "Fonction             :")
            canva.drawString(300, 540, str(row[4]))

            canva.drawString(200, 520, "Date de Naissance    :")
            canva.drawString(340, 520, str(row[5]))

        canva.save()

    def export(self):
        mydb = self.connect()

        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()

        query = sql.read_sql('select * from personne where id='+id, mydb)

        query.to_excel('rapport.xls')

    def ajouter(self):

        self.window = QtWidgets.QDialog()
        self.ui = Ui_AjouterWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

        self.show_data()

    def update_2(self):
        row = self.tableWidget.currentRow()
        id = self.tableWidget.item(row, 0).text()
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AjouterWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.ui.show_datas(id)
        self.ui.alter(id)
        self.window.exec_()
        self.show_data()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(640, 40, 111, 51))
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.ajouter)
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(640, 120, 111, 51))
        self.edit_button.setObjectName("edit_button")
        self.edit_button.clicked.connect(self.update_2)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(640, 200, 111, 51))
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.delete)
        self.print_button = QtWidgets.QPushButton(self.centralwidget)
        self.print_button.setGeometry(QtCore.QRect(640, 280, 111, 51))
        self.print_button.setObjectName("print_button")
        self.print_button.clicked.connect(self.ex)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 601, 441))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(640, 410, 111, 51))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(MainWindow.hide)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_button.setText(_translate("MainWindow", "Ajouter"))
        self.edit_button.setText(_translate("MainWindow", "Modifier"))
        self.delete_button.setText(_translate("MainWindow", "Supprimer"))
        self.print_button.setText(_translate("MainWindow", "Imprimer"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CNE"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fonction"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date Naissance"))
        self.exit_button.setText(_translate("MainWindow", "Quitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.show_data()
    sys.exit(app.exec_())
