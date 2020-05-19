# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spacer_ui_base3.ui',
# licensing of 'spacer_ui_base3.ui' applies.
#
# Created: Wed May  6 08:58:57 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, Spacer):
        Spacer.setObjectName("Spacer")
        Spacer.resize(666, 601)
        Spacer.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Spacer)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scheduleGrid = QtWidgets.QGridLayout()
        self.scheduleGrid.setContentsMargins(20, -1, 20, 10)
        self.scheduleGrid.setVerticalSpacing(6)
        self.scheduleGrid.setObjectName("scheduleGrid")
        self.scheduleWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.scheduleWidget.setStyleSheet("QTableWidget {\n"
                                          "border-style: solid;\n"
                                          "border-width: 1px;\n"
                                          "border-color:rgb(184, 184, 184);\n"
                                          "border-radius: 25px;\n"
                                          "background-color: white;\n"
                                          "}\n"
                                          "\n"
                                          "QHeaderView::section {\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.scheduleWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scheduleWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scheduleWidget.setAlternatingRowColors(True)
        self.scheduleWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.scheduleWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.scheduleWidget.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.scheduleWidget.setShowGrid(True)
        self.scheduleWidget.setRowCount(0)
        self.scheduleWidget.setColumnCount(3)
        self.scheduleWidget.setObjectName("scheduleWidget")
        self.scheduleWidget.setColumnCount(3)
        self.scheduleWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleWidget.setHorizontalHeaderItem(2, item)
        self.scheduleWidget.horizontalHeader().setSortIndicatorShown(False)
        self.scheduleWidget.horizontalHeader().setStretchLastSection(False)
        self.scheduleWidget.verticalHeader().setSortIndicatorShown(False)
        self.scheduleWidget.verticalHeader().setStretchLastSection(False)
        self.scheduleGrid.addWidget(self.scheduleWidget, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(54, 54, 54);\n"
                                   "font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.scheduleGrid.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(54, 54, 54);\n"
                                 "font: 12pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scheduleGrid.addWidget(self.label, 1, 0, 1, 1)
        self.studyWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.studyWidget.setStyleSheet("QTableWidget {\n"
                                       "border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color:rgb(184, 184, 184);\n"
                                       "border-radius: 25px;\n"
                                       "background-color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "}\n"
                                       "")
        self.studyWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.studyWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.studyWidget.setAlternatingRowColors(True)
        self.studyWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.studyWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.studyWidget.setShowGrid(True)
        self.studyWidget.setRowCount(0)
        self.studyWidget.setColumnCount(4)
        self.studyWidget.setObjectName("studyWidget")
        self.studyWidget.setColumnCount(4)
        self.studyWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.studyWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studyWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studyWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studyWidget.setHorizontalHeaderItem(3, item)
        self.studyWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.studyWidget.horizontalHeader().setStretchLastSection(False)
        self.studyWidget.verticalHeader().setCascadingSectionResizes(False)
        self.studyWidget.verticalHeader().setHighlightSections(True)
        self.studyWidget.verticalHeader().setSortIndicatorShown(False)
        self.scheduleGrid.addWidget(self.studyWidget, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(22)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateWidget = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateWidget.setMinimumSize(QtCore.QSize(0, 18))
        self.dateWidget.setAutoFillBackground(False)
        self.dateWidget.setStyleSheet("border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-color:rgb(184, 184, 184);\n"
                                      "border-radius: 8px;\n"
                                      "background-color: white;")
        self.dateWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.dateWidget.setReadOnly(False)
        self.dateWidget.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateWidget.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.dateWidget.setCalendarPopup(False)
        self.dateWidget.setObjectName("dateWidget")
        self.horizontalLayout_2.addWidget(self.dateWidget)
        self.taskEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.taskEdit.sizePolicy().hasHeightForWidth())
        self.taskEdit.setSizePolicy(sizePolicy)
        self.taskEdit.setStyleSheet("border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color:rgb(184, 184, 184);\n"
                                    "border-radius: 8px;\n"
                                    "background-color: rgb(255,255,255);")
        self.taskEdit.setText("")
        self.taskEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.taskEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.taskEdit.setObjectName("taskEdit")
        self.horizontalLayout_2.addWidget(self.taskEdit)
        self.btn_addTask = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_addTask.sizePolicy().hasHeightForWidth())
        self.btn_addTask.setSizePolicy(sizePolicy)
        self.btn_addTask.setMinimumSize(QtCore.QSize(0, 18))
        self.btn_addTask.setAutoFillBackground(False)
        self.btn_addTask.setStyleSheet("border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color:rgb(184, 184, 184);\n"
                                       "border-radius: 8px;\n"
                                       "background-color: rgba(225, 225, 225, 212);")
        self.btn_addTask.setObjectName("btn_addTask")
        self.horizontalLayout_2.addWidget(self.btn_addTask)
        self.scheduleGrid.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.scheduleGrid, 2, 1, 1, 1)
        Spacer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Spacer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Spacer.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(Spacer)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Spacer)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCode = QtWidgets.QAction(Spacer)
        self.actionCode.setObjectName("actionCode")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionCode)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Spacer)
        QtCore.QMetaObject.connectSlotsByName(Spacer)

    def retranslateUi(self, Spacer):
        Spacer.setWindowTitle(QtWidgets.QApplication.translate(
            "Spacer", "Spacer", None, -1))
        self.scheduleWidget.setSortingEnabled(False)
        self.scheduleWidget.horizontalHeaderItem(0).setText(
            QtWidgets.QApplication.translate("Spacer", "Task Name", None, -1))
        self.scheduleWidget.horizontalHeaderItem(1).setText(
            QtWidgets.QApplication.translate("Spacer", "Next Scheduled Study Session", None, -1))
        self.scheduleWidget.horizontalHeaderItem(2).setText(
            QtWidgets.QApplication.translate("Spacer", "Level", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate(
            "Spacer", "To Do Tasks", None, -1))
        self.label.setText(QtWidgets.QApplication.translate(
            "Spacer", "Task Scheduler", None, -1))
        self.studyWidget.horizontalHeaderItem(0).setText(
            QtWidgets.QApplication.translate("Spacer", "Task Name", None, -1))
        self.studyWidget.horizontalHeaderItem(1).setText(
            QtWidgets.QApplication.translate("Spacer", "Time When Scheduled", None, -1))
        self.studyWidget.horizontalHeaderItem(2).setText(
            QtWidgets.QApplication.translate("Spacer", "Notes", None, -1))
        self.dateWidget.setDisplayFormat(QtWidgets.QApplication.translate(
            "Spacer", "MMMM dd, yyyy h:mm AP", None, -1))
        self.btn_addTask.setText(QtWidgets.QApplication.translate(
            "Spacer", "Add Task", None, -1))
        self.menuFile.setTitle(
            QtWidgets.QApplication.translate("Spacer", "File", None, -1))
        self.actionExit.setText(
            QtWidgets.QApplication.translate("Spacer", "Exit", None, -1))
        self.actionAbout.setText(
            QtWidgets.QApplication.translate("Spacer", "About", None, -1))
        self.actionCode.setText(
            QtWidgets.QApplication.translate("Spacer", "Code", None, -1))
