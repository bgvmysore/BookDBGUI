# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookDBGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
data=None

class Ui_BookDB(object):
    def setupUi(self, BookDB):
        BookDB.setObjectName("BookDB")
        BookDB.resize(432, 339)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BookDB.sizePolicy().hasHeightForWidth())
        BookDB.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(BookDB)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Enterbook_layout = QtWidgets.QVBoxLayout()
        self.Enterbook_layout.setObjectName("Enterbook_layout")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.Enterbook_layout.addItem(spacerItem)
        self.Enterbook_title_H = QtWidgets.QHBoxLayout()
        self.Enterbook_title_H.setObjectName("Enterbook_title_H")
        self.booktitleL = QtWidgets.QLabel(BookDB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.booktitleL.sizePolicy().hasHeightForWidth())
        self.booktitleL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.booktitleL.setFont(font)
        self.booktitleL.setObjectName("booktitleL")
        self.Enterbook_title_H.addWidget(self.booktitleL)
        self.titleField_txt1 = QtWidgets.QLineEdit(BookDB)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.titleField_txt1.setFont(font)
        self.titleField_txt1.setObjectName("titleField_txt1")
        self.titleField_txt1.textChanged.connect(self.title_get)
        self.Enterbook_title_H.addWidget(self.titleField_txt1)
        self.price_btn = QtWidgets.QPushButton(BookDB)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.price_btn.setFont(font)
        self.price_btn.setObjectName("price_btn")
        self.price_btn.clicked.connect(self.price_btn_action)
        self.Enterbook_title_H.addWidget(self.price_btn)
        self.Enterbook_layout.addLayout(self.Enterbook_title_H)
        self.price_op = QtWidgets.QLabel(BookDB)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.price_op.setFont(font)
        self.price_op.setObjectName("price_op")
        self.Enterbook_layout.addWidget(self.price_op)
        self.verticalLayout_3.addLayout(self.Enterbook_layout)
        self.mid_line = QtWidgets.QFrame(BookDB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.mid_line.sizePolicy().hasHeightForWidth())
        self.mid_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.mid_line.setFont(font)
        self.mid_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.mid_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mid_line.setObjectName("mid_line")
        self.verticalLayout_3.addWidget(self.mid_line)
        self.Calc_total_layout = QtWidgets.QVBoxLayout()
        self.Calc_total_layout.setObjectName("Calc_total_layout")
        self.Entercopies_book_H = QtWidgets.QHBoxLayout()
        self.Entercopies_book_H.setObjectName("Entercopies_book_H")
        self.quantityL = QtWidgets.QLabel(BookDB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantityL.sizePolicy().hasHeightForWidth())
        self.quantityL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quantityL.setFont(font)
        self.quantityL.setObjectName("quantityL")
        self.Entercopies_book_H.addWidget(self.quantityL)
        self.CopiesField_int_txt2 = QtWidgets.QLineEdit(BookDB)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CopiesField_int_txt2.setFont(font)
        self.CopiesField_int_txt2.setObjectName("CopiesField_int_txt2")
        self.CopiesField_int_txt2.setValidator(QtGui.QIntValidator())
        self.CopiesField_int_txt2.textChanged.connect(self.copies_get)
        self.Entercopies_book_H.addWidget(self.CopiesField_int_txt2)
        self.amt_btn = QtWidgets.QPushButton(BookDB)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.amt_btn.setFont(font)
        self.amt_btn.setObjectName("amt_btn")
        self.amt_btn.clicked.connect(self.amt_btn_action)
        self.Entercopies_book_H.addWidget(self.amt_btn)
        self.Calc_total_layout.addLayout(self.Entercopies_book_H)
        self.amt_op = QtWidgets.QLabel(BookDB)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amt_op.setFont(font)
        self.amt_op.setObjectName("amt_op")
        self.Calc_total_layout.addWidget(self.amt_op)
        self.verticalLayout_3.addLayout(self.Calc_total_layout)

        self.retranslateUi(BookDB)
        QtCore.QMetaObject.connectSlotsByName(BookDB)
    
    def title_get(self,text):
        self.booktitle=text
        return

    def copies_get(self,text):
        self.qnty=text
        return

    def price_btn_action(self):
        global data
        bookdb=sqlite3.connect('MyBookDB.db')
        cur=bookdb.cursor()
        exec_string="SELECT * FROM books WHERE BookTitle='" + self.booktitle + "';"
        cur.execute(exec_string)
        data=cur.fetchone()
        bookdb.close()
        if data==None:
            output_top="Book Not Found!"
        else:
            output_top="Book Title:{}\nAuthor:{}\nBook Price:Rs.{}".format(data[0],data[1],data[2])

        self.price_op.setText(output_top)
        self.titleField_txt1.setText("")
        return
    
    def amt_btn_action(self):
        global data
        if data==None:
            output_bot="Enter a valid Book Title first!"
        else:
            output_bot="Book Title:{}\nNo. of copies:{}\nTotal Amount:Rs.{}".format(data[0],self.qnty,int(self.qnty)*data[2])
        self.amt_op.setText(output_bot)
        self.CopiesField_int_txt2.setText("")
        return

    
    def retranslateUi(self, BookDB):
        _translate = QtCore.QCoreApplication.translate
        BookDB.setWindowTitle(_translate("BookDB", "BookDatabase"))
        self.booktitleL.setText(_translate("BookDB", "Book Title:"))
        self.price_btn.setText(_translate("BookDB", "Get Price"))
        self.price_op.setText(_translate("BookDB", "Price: Rs.0"))
        self.quantityL.setText(_translate("BookDB", "Quantity:"))
        self.amt_btn.setText(_translate("BookDB", "Total Price"))
        self.amt_op.setText(_translate("BookDB", "Price: Rs.0"))



if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    BookDB = QtWidgets.QWidget()
    ui = Ui_BookDB()
    ui.setupUi(BookDB)
    BookDB.show()
    sys.exit(app.exec_())
    

