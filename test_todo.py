import unittest
from io import StringIO
from unittest.mock import patch

from todo import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task("Test Task")
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0]['description'], "Test Task")
        self.assertFalse(self.task_manager.tasks[0]['completed'])

    def test_mark_task_completed(self):
        self.task_manager.add_task("Test Task")
        self.task_manager.mark_task_completed(0)
        self.assertTrue(self.task_manager.tasks[0]['completed'])

    def test_mark_task_completed_non_existent(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.task_manager.mark_task_completed(0)
            self.assertEqual(fake_out.getvalue().strip(), "Task does not exist.")

    def test_list_tasks(self):
        self.task_manager.add_task("Test Task 1")
        self.task_manager.add_task("Test Task 2")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.task_manager.list_tasks()
            output = fake_out.getvalue().strip()
            self.assertIn("0. Test Task 1 [not completed]", output)
            self.assertIn("1. Test Task 2 [not completed]", output)

    def test_remove_task(self):
        self.task_manager.add_task("Test Task")
        self.task_manager.remove_task(0)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_remove_task_non_existent(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.task_manager.remove_task(0)
            self.assertEqual(fake_out.getvalue().strip(), "Task does not exist.")


if __name__ == "__main__":
    unittest.main()
