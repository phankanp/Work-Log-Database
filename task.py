from datetime import datetime

from task_model import Entry, initialize


class Task:
    def get_employee_name(self):
        """Get employee name from user"""

        employee_name = input("Enter the employee name:")

        if len(employee_name) == 0:
            input("\nEmployee name cannot be empty!\n")
            return self.get_employee_name()
        else:
            return employee_name

    def edit_employee_name(self, entry):
        """Edits employee name"""

        entry.employee_name = self.get_employee_name()

        entry.save()

        return entry

    def get_task_name(self):
        """Get task name from user"""

        task_name = input("Enter the task name:")

        if len(task_name) == 0:
            input("\nTask name cannot be empty!\n")
            return self.get_task_name()
        else:
            return task_name

    def edit_task_name(self, entry):
        """Edits task name name"""

        entry.task_name = self.get_task_name()

        entry.save()

        return entry

    def get_time_spent(self):
        """Get time spent from user"""

        time_spent = input("Enter the time spent in minutes: ")

        try:
            int(time_spent)
        except ValueError:
            input("\nInvalid entry, time spent must be an integer\n")
            return self.get_time_spent()
        else:
            return time_spent

    def edit_time_spent(self, entry):
        """Edits time spent"""

        entry.mins = self.get_time_spent()

        entry.save()

        return entry

    def get_notes(self):
        """Get task notes from user"""

        notes = input("Enter notes for this task: ")

        if len(notes) == 0:
            notes = "None"

        return notes

    def edit_notes(self, entry):
        """Edits notes"""

        entry.notes = self.get_notes()

        entry.save()

        return entry

    def get_date(self):
        """Get task date from user"""

        date = input("Enter a date for the task(MM-DD-YYYY): ")
        date_obj = datetime.strptime(date, "%m-%d-%Y")

        try:
            date = datetime.strftime(date_obj, "%m-%d-%Y")
            return date
        except ValueError:
            input("\nInvalid entry, format of date must be MM-DD-YYYY\n")
            return self.get_date()

    def edit_date(self, entry):
        """Edits date"""

        entry.date = self.get_date()

        entry.save()

        return entry

    @staticmethod
    def add_task(task):
        """Creates task in database table"""

        Entry.create(**task)

        return task

    @staticmethod
    def delete_task(task):
        """Deletes task from database table"""

        task.delete_instance()

        print('Task Deleted')

    @staticmethod
    def find_task(search_method, search_term):
        """Find tasks base on provided search method and search term"""

        if search_method == 'Employee Name':
            return Entry.select().where(Entry.employee_name.contains(search_term))
        elif search_method == 'Keyword':
            return Entry.select().where((Entry.task_name.contains(search_term)) or (Entry.notes.contains(search_term)))
        elif search_method == 'Time Spent':
            return Entry.select().where(Entry.mins == search_term)
        elif search_method == 'Date':
            return Entry.select().where(Entry.date == search_term)
        elif search_method == 'Date Range':
            return Entry.select().where(
                Entry.date.between(search_term[0], search_term[1]))


