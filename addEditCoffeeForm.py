# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 211)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.name_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.name_lbl.setObjectName("name_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_lbl)
        self.roast_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.roast_lbl.setObjectName("roast_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.roast_lbl)
        self.substance_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.substance_lbl.setObjectName("substance_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.substance_lbl)
        self.taste_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.taste_lbl.setObjectName("taste_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.taste_lbl)
        self.price_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.price_lbl.setObjectName("price_lbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.price_lbl)
        self.volume_lbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.volume_lbl.setObjectName("volume_lbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.volume_lbl)
        self.name_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_edit.setObjectName("name_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_edit)
        self.roast_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.roast_edit.setObjectName("roast_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roast_edit)
        self.substance_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.substance_edit.setObjectName("substance_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.substance_edit)
        self.taste_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.taste_edit.setObjectName("taste_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taste_edit)
        self.price_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price_edit.setObjectName("price_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price_edit)
        self.volume_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.volume_edit.setObjectName("volume_edit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.volume_edit)
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(270, 180, 121, 23))
        self.save_btn.setObjectName("save_btn")
        self.error_lbl = QtWidgets.QLabel(Dialog)
        self.error_lbl.setGeometry(QtCore.QRect(10, 180, 251, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.error_lbl.setPalette(palette)
        self.error_lbl.setText("")
        self.error_lbl.setObjectName("error_lbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Изменение базы данных"))
        self.name_lbl.setText(_translate("Dialog", "Название сорта"))
        self.roast_lbl.setText(_translate("Dialog", "Степень обжарки"))
        self.substance_lbl.setText(_translate("Dialog", "Консистенция"))
        self.taste_lbl.setText(_translate("Dialog", "Вкус"))
        self.price_lbl.setText(_translate("Dialog", "Цена упаковки"))
        self.volume_lbl.setText(_translate("Dialog", "Объем упаковки"))
        self.save_btn.setText(_translate("Dialog", "Сохранить изменения"))
