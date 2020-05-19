from spacer_app.qt_ui.ui_mainwindow import Ui
from PySide2.QtWidgets import (QMainWindow, QTableWidgetItem, QMessageBox, QMenu, QAction,
                               QApplication, QAbstractItemView, QPushButton)
from PySide2.QtGui import QCursor, QFont
from PySide2.QtCore import Qt, QDateTime, QTimer
from spacer_app.database.db_models import spacer_db
import datetime
from dateutil.parser import parse
import webbrowser


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui()
        self.ui.setupUi(self)

        # Database for application
        self.helper = spacer_db('spacer_data.db')
        self.helper.create_spacer_tables()
        self.helper.edit_db("PRAGMA foreign_keys = ON")
        # Assume direct control of changing ui from here
        ui = self.ui

        # scheduleWidget Options
        ui.scheduleWidget.horizontalHeader().setStretchLastSection(True)
        ui.scheduleWidget.resizeColumnsToContents()

        ui.scheduleWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.contextMenuScheduleWidget()

        # SCHEDULE WIDGET AUTO FUNCTIONS

        # check for selected items
        ui.scheduleWidget.itemSelectionChanged.connect(
            self.scheduleWidget_selection)

        # studyWidget Options
        ui.studyWidget.horizontalHeader().setStretchLastSection(True)
        ui.studyWidget.resizeColumnsToContents()
        ui.studyWidget.setColumnWidth(1, 375)
        ui.studyWidget.setColumnWidth(2, 1000)

        # File Menu Actions
        ui.actionExit.triggered.connect(self.exit_app)
        ui.actionExit.setShortcut('Ctrl+Q')
        ui.actionAbout.triggered.connect(self.msgActionAbout)
        ui.actionCode.triggered.connect(
            (lambda: webbrowser.open('https://github.com/darwin-a/spacer_app')))

        # real time clock updates
        self.updateTime()
        self.timer = QTimer(self)
        self.timer.start(5000)
        self.timer.timeout.connect(self.updateTime)

        # ADD ABOUT
        # ADD CODE
        # change this to add a task
        ui.btn_addTask.clicked.connect(self.add_task)

        # SCHEDULE WIDGET AUTO FUNCTIONS

        # check for selected items
        ui.scheduleWidget.itemSelectionChanged.connect(
            self.scheduleWidget_selection)

        ######################################

        # STUDY WIDGET AUTO FUNCTIONS

        # check for selected items
        ui.studyWidget.itemSelectionChanged.connect(
            self.studyWidget_selection)

        #######################################

        # TO DO: Write code to automate refreshing table on creating notes
        #

    def updateTime(self):
        self.ui.dateWidget.setDateTime(QDateTime.currentDateTime())

    @staticmethod
    def message(title="", message=""):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        return msg

    def msgActionAbout(self):
        about_text = """
Spacer App: Application dedicated to applying the Spacer Effect
towards learning concepts and tasks organization. 

Original motivation: I wanted to create an app to help 
keep track of my projects so I can visit them in a timely manner.
I have a habit of starting projects and getting a good amount done,then revisiting every so often."""

        msg = self.message(title="Spacer About", message=about_text)
        msg.setStyleSheet("""QLabel
                            {min-width: 700px;}""")
        msg.exec_()

    # close event, want to save notes

    def exit_app(self):
        self.saveNotes()
        QApplication.exit()

    # close event, want to save notes
    def closeEvent(self, e):
        self.saveNotes()
        # print('Saving Notes')
        e.accept()

    def clear_table(self):
        ui = self.ui
        while (ui.scheduleWidget.rowCount() > 0):
            ui.scheduleWidget.removeRow(0)
        while(ui.studyWidget.rowCount() > 0):
            ui.studyWidget.removeRow(0)

    def load_data(self):
        self.loadScheduleData()
        self.loadStudyData()
        self.resizeTables()

    def resizeTables(self):
        self.ui.scheduleWidget.resizeRowsToContents()
        # resize the notes column
        self.ui.studyWidget.resizeRowsToContents()

    def refreshTables(self):
        self.saveNotes()
        self.checkTasksForUpdate()  # THINK ABOUT THIS FUNCTION AND WHERE IT BELONGS
        self.clear_table()
        self.load_data()
    ##################################################
    ########### SCHEDULE WIDGET FUNCTIONS ############
    ##################################################

    def loadScheduleData(self):
        """
        Function for loading data from our database and
        into the application

        Parameters
        ----------
        database : [SQL Lite Object]
            Database object that we connect to it
            through the db_model

        Return
        ----------
        None
        """
        # initialize ui
        ui = self.ui
        helper = self.helper
        tasks = helper.select_from_db(
            """SELECT * FROM tasks""")

        for row_number, task in enumerate(tasks):
            # insert rows into the application for as
            # many tasks as we have
            ui.scheduleWidget.insertRow(row_number)

            # loop through the task to get the amount of columns
            # since we have rows and columns we insert data
            # piece by piece
            for column_number, data in enumerate(task):
                # store the data the appropriate object
                # numerics don't get viewed properly in tablewidget items
                data = str(data)

                # cell manipulation options
                cell = QTableWidgetItem(data)
                cell.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                cell.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                # add the data into the cell
                ui.scheduleWidget.setItem(row_number, column_number, cell)

    def add_task(self):
        # set ui
        ui = self.ui

        # set database
        helper = self.helper

        # check if string is empty
        if ui.taskEdit.text() == "":
            msg = self.message('Error', 'No Task Entered')
            msg.setIcon(msg.Icon.Warning)
            msg.exec_()
            return None
        else:
            task = ui.taskEdit.text()
            # have the database add the task
            try:
                helper.add_task_to_schedule(task)
            except:
                msg = self.message('Error', 'Task Already Exists')
                msg.setIcon(msg.Icon.Warning)
                msg.exec_()

            # clear the line, table and reload the data
            ui.taskEdit.clear()
            self.refreshTables()

    def scheduleWidget_selection(self):
        print(self.scheduleWidget_get_task())

    def scheduleWidget_get_task(self):
        """
        prints out the row selected in the scheduleWidget
        """
        # print(self.ui.scheduleWidget.item(
        #     self.scheduleWidget_get_selected_row(), 1).text())
        return self.ui.scheduleWidget.item(self.scheduleWidget_get_selected_row(), 0).text()

    def scheduleWidget_get_selected_row(self):
        """
        returns the index for the current row selected
        in the scheduleWidget
        """
        return self.ui.scheduleWidget.currentRow()

    def contextMenuScheduleWidget(self):
        """
        Delete Menu For Tasks
        """
        table = self.ui.scheduleWidget
        editAction = QAction('Edit', self)
        editAction.triggered.connect(self.editTask)
        delAction = QAction('Delete', self)
        delAction.triggered.connect(self.deleteTask)
        refreshAction = QAction('Refresh', self)
        refreshAction.triggered.connect(self.refreshTables)

        table.addAction(editAction)
        table.addAction(delAction)
        table.addAction(refreshAction)

    def editTask(self):

        helper = self.helper

        try:
            task_edit = self.scheduleWidget_get_task()
            # print(f'Task Delete: {task_delete}')

            # give a choice to delete the task for security
            choice = QMessageBox.question(self, f'Edit {task_edit}?',
                                          f"Are you sure you want to edit this task?",
                                          QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                helper.edit_task(task_edit)
                self.refreshTables()
            else:
                pass
        except:
            msg = self.message('Error', 'Please Select A Task To Delete')
            msg.setIcon(msg.Icon.Warning)
            msg.exec_()
            return None

    def deleteTask(self):
        helper = self.helper

        try:
            task_delete = self.scheduleWidget_get_task()
            # print(f'Task Delete: {task_delete}')

            # give a choice to delete the task for security
            choice = QMessageBox.question(self, f'Delete {task_delete}?',
                                          f"Are you sure you want to delete this task?",
                                          QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                helper.delete_task_from_schedule(task_delete)
                self.refreshTables()
            else:
                pass
        except:
            msg = self.message('Error', 'Please Select A Task To Delete')
            msg.setIcon(msg.Icon.Warning)
            msg.exec_()
            return None

    def scheduleWidget_get_schedule(self):
        """
        prints out the row selected in the scheduleWidget
        """
        return self.ui.scheduleWidget.item(self.scheduleWidget_get_selected_row(), 1).text()

    ##################################################
    ########### SCHEDULE WIDGET FUNCTIONS ############
    ##################################################

    # You need to think about where you should implement this feature
    # The code doesnt break but it gets annoying for popups so
    # we commented out the except block
    def checkTasksForUpdate(self):
        # initialize ui
        ui = self.ui
        helper = self.helper
        tasks = helper.select_from_db(
            """SELECT * FROM tasks""")

        for task in (tasks):
            # grab the contents of the first column and second column, (task_name,study_date)
            # for each row
            task_name = task[0]
            task_schedule = task[1]
            current_date = datetime.datetime.today()
            # + datetime.timedelta(days=1) # testing purposes for above

            # if true, add task to update table
            if current_date > parse(task_schedule):
                try:  # add
                    helper.add_task_to_study(task_name)
                except:
                    pass
                    # # Commented out because its annoying on reload
                    # msg = self.message('Error', 'Task Already Exists')
                    # msg.setIcon(msg.Icon.Warning)
                    # msg.exec_()

    def loadStudyData(self):
        """
        Function for loading data from our database and
        into the application

        Parameters
        ----------
        database : [SQL Lite Object]
            Database object that we connect to it
            through the db_model

        Return
        ----------
        None
        """
        # initialize ui
        ui = self.ui
        helper = self.helper
        tasks = helper.select_from_db(
            """SELECT task_name, study_time, notes FROM to_do_tasks""")

        for row_number, task in enumerate(tasks):
            # insert rows into the application for as
            # many tasks as we have
            ui.studyWidget.insertRow(row_number)

            # loop through the task to get the amount of columns
            # since we have rows and columns we insert data
            # piece by piece
            for column_number, data in enumerate(task):
                # store the data the appropriate object
                # numerics don't get viewed properly in tablewidget items
                cell = QTableWidgetItem()
                cell.setText(data)
                cell.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                # disable functionality for all cells except the notes cell
                # and also edit the alignment for the notes
                if column_number == 2:
                    cell.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
                else:
                    # disable options
                    cell.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                # add the data into the cell
                ui.studyWidget.setItem(row_number, column_number, cell)

                # Load finished task functionality into the table
                finishedTask = QPushButton('Finished Task')
                finishedTask.clicked.connect(self.levelMessageBox)
                ui.studyWidget.setCellWidget(
                    row_number, 3, finishedTask)\


    def studyWidget_selection(self):
        print(self.studyWidget_get_task())

    def studyWidget_get_task(self):
        """
        prints out the row selected in the scheduleWidget
        """
        # print(self.ui.scheduleWidget.item(
        #     self.scheduleWidget_get_selected_row(), 1).text())
        return self.ui.studyWidget.item(self.studyWidget_get_selected_row(), 0).text()

    def studyWidget_get_selected_row(self):
        """
        returns the index for the current row selected
        in the studyWidget
        """

        return self.ui.studyWidget.currentRow()

    def saveNotes(self):
        # saves notes in the notes column
        ui = self.ui
        helper = self.helper
        tasks = helper.select_from_db(
            """SELECT task_name, study_time FROM to_do_tasks""")

        for row_number, _task in enumerate(tasks):
            # insert rows into the application for as
            # many tasks as we have
            task_name = ui.studyWidget.item(row_number, 0).text()
            notes = ui.studyWidget.item(row_number, 2).text()

            # commit the notes
            helper.commit_notes(task_name, notes)

    ###########################################
    ######## TO DO FUNCTIONS ##################
    ###########################################

    def grabFinishedTask(self):
        button = self.sender()
        index = self.ui.studyWidget.indexAt(button.pos())
        if index.isValid():
            # grab the task from the corresponding position
            return self.ui.studyWidget.item(index.row(), 0).text()

    def levelMessageBox(self, task):
        helper = self.helper
        task = self.grabFinishedTask()

        msg = self.message(
            title=f"Level Message Box: {task}", message="Should you move up or down a level?")
        lvlUpBtn = msg.addButton('Level Up', QMessageBox.YesRole)
        lvlDownBtn = msg.addButton('Level Down', QMessageBox.NoRole)

        msg.exec_()

        if msg.clickedButton() == lvlUpBtn:
            choice = 'Level Up'
            helper.update_task_delete_from_schedule(task, choice)
            self.refreshTables()
        elif msg.clickedButton() == lvlDownBtn:
            choice = 'Level Down'
            helper.update_task_delete_from_schedule(task, choice)
            self.refreshTables()
        else:  # Add exit functionality?
            pass

            # TO DO DEAL WITH EDGE CASES
            # LEVEL 1 LEVELING DOWN
            # LEVEL 5 LEVELING UP
            # update the tables through
