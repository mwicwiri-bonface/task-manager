# Task Manager

## Overview

The Task Manager is a simple command-line application that allows users to manage tasks. Users can add tasks, mark them as completed, list all tasks with their completion status, and remove tasks. The program runs in a loop until the user chooses to quit.

## Features

1. **Add Task**: Prompt the user to add a task description. The task is then added to the list.
2. **Mark Task as Completed**: Allow the user to mark a task as completed by entering the task index. If the task is already marked as completed, an appropriate message is displayed. If the task does not exist, an error message is shown.
3. **List Tasks**: Display a numbered list of tasks along with their completion status.
4. **Remove Task**: Allow the user to remove a task by entering the task index. An appropriate message is displayed if the task does not exist.
5. **Quit**: Exit the program with a goodbye message.

## Usage

1. Clone the repository or use the downloaded file.
2. Run the program using Python:
   ```sh
   python todo.py
3. Follow the on-screen instructions to manage your tasks.

### Example
```sh
Select an option:
1. Add Task
2. Mark Task as Completed
3. List Tasks
4. Remove Task
5. Quit

Enter your choice: 1
Enter task description: Finish homework
Task "Finish homework" added.

Enter your choice: 3
0. Finish homework [not completed]

Enter your choice: 2
Enter task index to mark as completed: 0
Task 0 marked as completed.

Enter your choice: 3
0. Finish homework [completed]

Enter your choice: 4
Enter task index to remove: 0
Task "Finish homework" removed.

Enter your choice: 5
Goodbye!
```
## Automated Testing
Automated tests are included to verify the functionalities of the Task Manager. The tests use the unittest framework.

## Running Tests
1. Ensure todo.py and test_todo.py are in the same directory.
2. Run the tests using the following command:
```sh
python -m unittest test_todo.py
```
`test_todo.py`

#### The test file contains the following tests:
- `test_add_task`: Tests the addition of a task.
- `test_mark_task_completed`: Tests marking a task as completed.
- `test_mark_task_completed_non_existent`: Tests the scenario where a non-existent task index is marked as completed.
- `test_list_tasks`: Tests listing all tasks.
- `test_remove_task`: Tests removing a task.
- `test_remove_task_non_existent`: Tests the scenario where a non-existent task index is removed.
