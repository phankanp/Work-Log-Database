import os
from datetime import datetime

from task import Task
from task_model import initialize


def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


class Worklog:
    def main_menu(self):
        """Main program menu, prompts user for input"""

        clear_screen()
        print('\nWork Log With Database\n')

        options = {'1': 'Add a new task', '2': 'Find a task', '3': 'Quit'}

        for k, v in options.items():
            print(k + ". " + v)

        while True:
            print()
            user_choice = input("Please enter the number of choice: ").lower().strip()

            if user_choice == '1':
                task = self.get_task_info()
                self.task.add_task(task)
                print('Task successfully added')
                self.main_menu()
            elif user_choice == '2':
                search_method_choice = self.search_method_menu()
                self.search_tasks(search_method_choice)
            elif user_choice == '3':
                print("\nExiting Work Logger")
                exit()
            else:
                print("\nInvalid choice, please try again.")

    def get_task_info(self):
        """Prompts user for task info"""

        print()
        employee_name = self.task.get_employee_name()
        task_name = self.task.get_task_name()
        mins = self.task.get_time_spent()
        notes = self.task.get_notes()
        date = self.task.get_date()

        task = {
            'employee_name': employee_name,
            'task_name': task_name,
            'mins': mins,
            'notes': notes,
            'date': date
        }

        return task

    def search_method_menu(self):
        """Provides search method menu and gets user's choice"""

        print()
        options = {'1': 'Employee Name', '2': 'Keyword', '3': 'Time Spent',
                   '4': 'Date', '5': 'Date Range', '6': 'Exit to main menu'}

        while True:

            for k, v in options.items():
                print(k + ". " + v)

            user_choice = input('\nPlease enter the number of choice: ').lower().strip()

            if user_choice in options.keys():
                return options.get(user_choice)
            else:
                print('\nInvalid choice! Please try again.\n')

    def search_tasks(self, search_method):
        """Finds tasks based on search method choice and calls print method"""

        if search_method == 'Employee Name':
            employee_name = self.search_employee_name()
            result = self.task.find_task(search_method, employee_name)

            if not result:
                print(f'\nNo task found with employee name "{employee_name}"')
                self.search_again()

        elif search_method == 'Keyword':
            keyword = self.search_keyword()
            result = self.task.find_task(search_method, keyword)

            if not result:
                print(f'\nNo task found with "{keyword}" in task name or notes')
                self.search_again()

        elif search_method == 'Time Spent':
            time_spent = self.search_time_spent()
            result = self.task.find_task(search_method, time_spent)

            if not result:
                print(f'\nNo task found with "{time_spent}" minutes time spent')
                self.search_again()

        elif search_method == 'Date':
            date = self.search_date()
            result = self.task.find_task(search_method, date)

            if not result:
                print(f'\nNo task found with date of "{date}"')
                self.search_again()

        elif search_method == 'Date Range':
            date1 = self.search_date("starting date")
            date2 = self.search_date("ending date")
            dates = [date1, date2]
            result = self.task.find_task(search_method, dates)

            if not result:
                print(f'\nNo task found between dates "{date1}" and "{date2}"')
                self.search_again()
        else:
            self.main_menu()

        self.print_tasks(result)

    def paging_options(self, index, tasks):
        """Prints out available paging options"""

        options = {"P": "Previous Entry", "N": "Next Entry",
                   "E": "Edit Entry", "D": "Delete Entry", "M": "Main Menu"}

        if index == 0:
            del options["P"]

        if index == len(tasks) - 1:
            del options["N"]

        for k, v in options.items():
            print(" " + k + ". " + v)

    def print_task(self, index, tasks):
        """Prints single task"""

        clear_screen()

        print('\n' + ('=' * 40))

        print(f' Task {index+1} of {len(tasks)}:\n')

        print(f' Employee Name: {tasks[index].employee_name}\n'
              f' Task Name: {tasks[index].task_name}\n'
              f' Time Spent: {tasks[index].mins}\n'
              f' Date: {tasks[index].date}\n'
              f' Notes: {tasks[index].notes}')

        print(('=' * 40) + '\n')

    def print_tasks(self, tasks):
        """Iterates through entries, selecting appropriate entry to print"""

        index = 0

        while True:
            self.print_task(index, tasks)

            self.paging_options(index, tasks)

            user_choice = input("\nPlease select one of the paging options: ").lower().strip()

            if index == 0 and user_choice == 'n':
                index += 1
            elif 0 < index < len(tasks) - 1 and user_choice == 'n':
                index += 1
            elif 0 < index <= len(tasks) - 1 and user_choice == 'p':
                index -= 1
            elif user_choice == 'e':
                self.edit_task(index, tasks)
            elif user_choice == 'd':
                self.task.delete_task(tasks[index])
                self.main_menu()
            elif user_choice == 'm':
                self.main_menu()
            else:
                input("\nInvalid choice, please try again :")

    def edit_task(self, index, tasks):
        """Provides entry editing options, gets user input and updates entry"""

        edit_options = {'1': 'Employee Name', '2': "Task Name", '3': "Time Spent", '4': "Notes", '5': "Date"}

        print()

        for k, v in edit_options.items():
            print(k + ". " + v)

        while True:
            user_choice = input("\nEnter the number of the value you would like to edit: ")

            print()

            if user_choice == '1':
                self.task.edit_employee_name(tasks[index])
                input('\nTask name has been updated(Enter to continue).')
                self.main_menu()
            elif user_choice == '2':
                self.task.edit_task_name(tasks[index])
                input('\nTime spent has been updated(Enter to continue).')
                self.main_menu()
            elif user_choice == '3':
                self.task.edit_time_spent(tasks[index])
                input('\nTime spent has been updated(Enter to continue).')
                self.main_menu()
            elif user_choice == '4':
                self.task.edit_notes(tasks[index])
                input('\nTask date has been updated(Enter to continue).')
                self.main_menu()
            elif user_choice == '5':
                self.task.edit_date(tasks[index])
                input('\nTask date has been updated(Enter to continue).')
                self.main_menu()
            else:
                self.main_menu()

    def search_again(self):
        """Checks if user wants to perform another search"""

        response = input(
            "\nWould you like to search for something else? (Yes or No): ")

        while response.lower().strip() != 'yes' or response.lower().strip() != 'no':

            if response.lower().strip() == 'yes':
                search_method_choice = self.search_method_menu()
                self.search_tasks(search_method_choice)
            elif response.lower().strip() == "no":
                self.main_menu()
            else:
                response = input("\nInvalid choice, please try again: ")

    def search_employee_name(self):
        """Get employee name from user"""

        employee_name = input("\nEnter an employee name:")

        if len(employee_name) == 0:
            input("\nEmployee name cannot be empty!\n")
            return self.search_employee_name()
        else:
            return employee_name

    def search_task_name(self):
        """Get task name from user"""

        task_name = input("\nEnter a task name:")

        if len(task_name) == 0:
            input("\nTask name cannot be empty!\n")
            return self.search_task_name()
        else:
            return

    def search_keyword(self):
        """Get task name from user"""

        task_name = input("\nEnter a search term:")

        if len(task_name) == 0:
            input("\nSearch Term cannot be empty!\n")
            return self.search_keyword()
        else:
            return task_name

    def search_time_spent(self):
        """Get time spent from user"""

        time_spent = input("\nEnter time spent: ")

        try:
            int(time_spent)
        except ValueError:
            input("\nTime spent must be an integer\n")
            return self.search_time_spent()
        else:
            return time_spent

    def search_date(self, text='date'):
        """Get task date from user"""

        date = input(f"\nEnter a {text} (MM-DD-YYYY): ")
        date_obj = datetime.strptime(date,  "%m-%d-%Y")

        try:
            date = datetime.strftime(date_obj, "%m-%d-%Y")
            return date
        except ValueError:
            input("\nFormat of date must be MM-DD-YYYY\n")
            return self.search_date()

    def __init__(self):
        self.task = Task()
        self.main_menu()


if __name__ == "__main__":
    initialize()
    Worklog()
