from spacer_app.database.database import db
import datetime
from PySide2.QtWidgets import QMessageBox, QDialogButtonBox
from spacer_app.qt_ui.edit_task_ui import editTask


class spacer_db(db):
    def __init__(self, name):
        db.__init__(self, name)
        # For each corresponding level (key) the amount of days
        # the least amount of time you should revisit the task
        self.levels_time_dict = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}

    def create_spacer_tables(self):
        self.create_table(query=f"""
                        CREATE TABLE IF NOT EXISTS   tasks(
                                         task_name   TEXT NOT NULL,
                                        study_time   TEXT NOT NULL,
                                             level   INTEGER DEFAULT 1,
                                       PRIMARY KEY   (task_name));""")

        self.create_table(query="""
                        CREATE TABLE IF NOT EXISTS   to_do_tasks(
                                                id   INTEGER PRIMARY KEY AUTOINCREMENT,
                                         task_name   TEXT UNIQUE NOT NULL,
                                        study_time   TEXT NOT NULL,
                                             notes   TEXT,
                                       FOREIGN KEY   (task_name) REFERENCES tasks(task_name) ON DELETE CASCADE);""")

    ##################################################
    ########### SCHEDULE TABLE FUNCTIONS #############
    ##################################################

    def add_task_to_schedule(self, task_name):
        # Since SQL Lite doesn't allow for custom date strings on selection
        # I decided to to the dates myself
        date = (datetime.datetime.today() + datetime.timedelta(days=1)
                ).strftime('%B %#d, %Y %#I:%M %p')

        task_data = (task_name, date)
        self.edit_table_db(
            """INSERT INTO tasks(task_name,study_time) VALUES (?,?);""", inserts=task_data)

    def delete_task_from_schedule(self, task):
        # turn the task into a tuple. Needed for sql parametrized queries
        task = (task,)
        ""
        self.edit_table_db(
            """DELETE FROM tasks
                 WHERE task_name = (?);""", inserts=task)

    # LEVEL UP/DOWN FUNCTIONALITY

    def update_task_delete_from_schedule(self, task, choice):
        # grab the task
        task_info = self.task_level_schedule_info(task, choice)
        # update the tasks
        updated_task = self.update_task(task_info)
        self.update_tasks_table(updated_task)
        # delete from to_study table
        self.delete_from_tostudy_table(task_info)

    def task_level_schedule_info(self, task, choice):
        # Select info from tasks table where task_name = task
        task_info = self.select_from_db(
            query=f'SELECT * FROM tasks WHERE task_name = "{task}"')
        choice = choice
        task_name = task_info[0][0]
        task_level = task_info[0][2]

        # grabbed the info, now return it to a function that will update
        # the task table
        return (task_name, task_level, choice)

    def update_task(self, task_info):
        # unpack the info
        task_name = task_info[0]
        task_level = task_info[1]
        choice = task_info[2]

        if choice == 'Level Up':
            task_level += 1
        elif choice == 'Level Down':
            task_level += -1

        # TO DO
        # deal with edge cases here
        if task_level == 6:
            self.level6MessageBox(task_name)
        elif task_level == 0:
            task_level = 1
        else:
            # if task level exists we will update it
            try:
                # grab days till study
                study_days_from_now = self.levels_time_dict[task_level]

                new_study_date = (datetime.datetime.today() + datetime.timedelta(days=study_days_from_now)
                                  ).strftime('%B %#d, %Y %#I:%M %p')

                return (task_name, new_study_date, task_level)
            except KeyError:
                return None

    def update_tasks_table(self, updated_task):
        # unpack the tuple

        try:
            name, time, level = updated_task
            query = "UPDATE tasks SET (study_time,level) = (?,?) WHERE task_name = (?)"
            inserts = (time, level, name)
            self.edit_table_db(query, inserts)
        except TypeError:  # will occur if we have already deleted the task
            return None

    ##################################################
    ########### Study Functions ################
    ##################################################

    def add_task_to_study(self, task_name):
        """
        Automatic function that inserts data into the studyWidget
        """
        current_date = datetime.datetime.today().strftime('%B %#d, %Y %#I:%M %p')

        task_data = (task_name, current_date)
        self.edit_table_db(
            """INSERT OR IGNORE INTO to_do_tasks(task_name,study_time) VALUES (?,?);""", inserts=task_data)
        # print(f'{task_data} added')

    def commit_notes(self, task_name, notes):
        """
        Commit the notes saved in the study table
        """
        task_name = str(task_name)
        notes = str(notes)
        self.edit_db(query="""
        UPDATE to_do_tasks SET notes = "{}" WHERE task_name = "{}\"""".format(notes, task_name))

    def delete_from_tostudy_table(self, task_info):
        task_name = task_info[0]
        query = "DELETE FROM to_do_tasks WHERE task_name = (?)"
        self.edit_table_db(query=query, inserts=(task_name,))

    @staticmethod
    def message(title="", message=""):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        return msg

    def level6MessageBox(self, task):
        msg = self.message(
            title=f"Task Mastery", message="Congratulations On Mastering The Task! What would you like to do?")
        studyMoreBtn = msg.addButton('Study More', QMessageBox.YesRole)
        finishTaskBtn = msg.addButton('Finish Task', QMessageBox.NoRole)
        # msg.setStyle('Fusion')
        msg.exec_()

        # edit functionality
        if msg.clickedButton() == studyMoreBtn:
            self.edit_task(task)
        elif msg.clickedButton() == finishTaskBtn:
            self.delete_task_from_schedule(task)

    def edit_task(self, task):
        # grab the old inputs from the database
        old_task_inputs = self.select_from_db(
            f'SELECT task_name, study_time, level FROM tasks WHERE task_name = "{task}"')

        # grab new inputs from user
        new_task_inputs = self.taskEditWindow(old_task_inputs)
        print(new_task_inputs, 'outside the edit')

        # unpack new inputs
        old_task_name = old_task_inputs[0][0]
        task = new_task_inputs[0]
        schedule = new_task_inputs[1]
        level = new_task_inputs[2]
        insert = (task, schedule, level, old_task_name)

        # delete the task from study table, edit table
        self.delete_from_tostudy_table(old_task_inputs[0])
        self.edit_task_table(insert)

    def edit_task_table(self, insert):
        self.edit_table_db(
            "UPDATE tasks SET (task_name,study_time,level) = (?,?,?) WHERE task_name = (?)", inserts=insert)

    def taskEditWindow(self, old_task_inputs):
        run = True
        while run:
            window = editTask()
            # unpack tasks
            task = old_task_inputs[0][0]
            days = old_task_inputs[0][1]
            level = str(old_task_inputs[0][2])
            # set the lines to existing data
            window.ui.taskNameEdit.setText(task)
            window.ui.taskScheduleEdit.setText(days)
            window.ui.taskLevelEdit.setText(level)

            window.ui.buttonBox.accepted.connect(self.pass_function_accepted)
            window.exec_()

            task = window.ui.taskNameEdit.text()
            days = window.ui.taskScheduleEdit.text()
            level = window.ui.taskLevelEdit.text()

            if int(level) in self.levels_time_dict.keys():
                # change the days to schedule
                try:
                    schedule = (datetime.datetime.today() + datetime.timedelta(days=int(days))
                                ).strftime('%B %#d, %Y %#I:%M %p')
                except:
                    schedule = days
                # return tuple with new data
                print(task, schedule, int(level), 'inside the edit')
                run = False
                return (task, schedule, int(level))
            else:
                # error message and redo the task
                msg = self.message("Error", "Please Input A Level 1-5")
                msg.exec_()

    def pass_function_accepted(self):
        pass


def main():
    test = spacer_db('spacer_data.db')
    test.create_spacer_tables()
    test.add_task_to_schedule('foo')
    test.add_task_to_schedule('bar')
    print(test.select_from_db("""SELECT *
                            FROM tasks"""))


if __name__ == "__main__":
    main()
