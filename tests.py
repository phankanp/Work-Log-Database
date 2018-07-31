import unittest
import unittest.mock as mock

from task import Task
from task_model import Entry

DATA = {
    "employee_name": "Test employee",
    "task_name": "Test task",
    "mins": "6",
    "notes": "Test notes",
    "date": "04-12-1991"
}


class WorkLogTests(unittest.TestCase):
    def setUp(self):
        self.task = Task()
        self.new = Entry.create(
            employee_name=DATA["employee_name"],
            task_name=DATA["task_name"],
            mins=DATA["mins"],
            notes=DATA["notes"],
            date=DATA["date"]
        )

    def test_get_employee_name(self):
        with mock.patch('builtins.input', side_effect=["Test employee"], return_value=DATA["employee_name"]):
            assert self.task.get_employee_name() == DATA["employee_name"]

    def test_edit_employee_name(self):
        with mock.patch('builtins.input', side_effect=["Test Name Edit"]):
            self.assertEqual(self.task.edit_employee_name(self.new).employee_name, 'Test Name Edit')

    def test_get_task_name(self):
        with mock.patch('builtins.input', side_effect=["Test task"], return_value=DATA["task_name"]):
            assert self.task.get_task_name() == DATA["task_name"]

    def test_edit_task_name(self):
        with mock.patch('builtins.input', side_effect=["Test Task Name Edit"]):
            self.assertEqual(self.task.edit_task_name(self.new).task_name, 'Test Task Name Edit')

    def test_get_time_spent(self):
        with mock.patch('builtins.input', side_effect=["6"], return_value=DATA["mins"]):
            assert self.task.get_time_spent() == DATA["mins"]

    def test_edit_time_spent(self):
        with mock.patch('builtins.input', side_effect=["5"]):
            self.assertEqual(self.task.edit_time_spent(self.new).mins, '5')

    def test_get_notes(self):
        with mock.patch('builtins.input', side_effect=["Test notes"], return_value=DATA["notes"]):
            assert self.task.get_notes() == DATA["notes"]

    def test_edit_notes(self):
        with mock.patch('builtins.input', side_effect=["Test Note Edit"]):
            self.assertEqual(self.task.edit_notes(self.new).notes, 'Test Note Edit')

    def test_get_date(self):
        with mock.patch('builtins.input', side_effect=["04-12-1991"], return_value=DATA["date"]):
            self.assertRaises(TypeError)
            assert self.task.get_date() == DATA["date"]

    def test_edit_date(self):
        with mock.patch('builtins.input', side_effect=["04-13-1991"]):
            self.assertEqual(self.task.edit_date(self.new).date, '04-13-1991')

    def test_add_task(self):
        test = {
            "employee_name": "Test employee",
            "task_name": "Test task",
            "mins": "6",
            "notes": "Test notes",
            "date": "04-12-1991"
        }
        assert self.task.add_task(test)["task_name"] == DATA["task_name"]

    def test_find_employee_name(self):
        employee_name = self.task.find_task('Employee Name', 'Test employee')
        self.assertTrue(employee_name)

    def test_find_task_name(self):
        task_name = self.task.find_task('Keyword', 'Test task')
        self.assertTrue(task_name)

    def test_find_date(self):
        date = self.task.find_task('Date', '04-12-1991')
        self.assertTrue(date)

    def test_find_date_range(self):
        date = self.task.find_task('Date Range', ['04-02-1991', '04-20-1991'])
        self.assertTrue(date)
