# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editTask.ui',
# licensing of 'editTask.ui' applies.
#
# Created: Thu Apr 23 23:57:07 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(257, 162)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.taskNameEdit = QtWidgets.QLineEdit(Dialog)
        self.taskNameEdit.setObjectName("taskNameEdit")
        self.gridLayout.addWidget(self.taskNameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.taskScheduleEdit = QtWidgets.QLineEdit(Dialog)
        self.taskScheduleEdit.setObjectName("taskScheduleEdit")
        self.gridLayout.addWidget(self.taskScheduleEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.taskLevelEdit = QtWidgets.QLineEdit(Dialog)
        self.taskLevelEdit.setObjectName("taskLevelEdit")
        self.gridLayout.addWidget(self.taskLevelEdit, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(
            self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate(
            "Dialog", "Edit Task", None, -1))
        self.label.setText(QtWidgets.QApplication.translate(
            "Dialog", "Task", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate(
            "Dialog", "Days From Now", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate(
            "Dialog", "Level", None, -1))


class editTask(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = ui()
        self.ui.setupUi(self)
