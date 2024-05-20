class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append({'description': description, 'completed': False})
        print(f'Task "{description}" added.')

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            if self.tasks[index]['completed']:
                print(f'Task {index} is already marked as completed.')
            else:
                self.tasks[index]['completed'] = True
                print(f'Task {index} marked as completed.')
        else:
            print('Task does not exist.')

    def list_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            for i, task in enumerate(self.tasks):
                status = 'completed' if task['completed'] else 'not completed'
                print(f'{i}. {task["description"]} [{status}]')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task["description"]}" removed.')
        else:
            print('Task does not exist.')

    def run(self):
        print("Welcome to simple todo-list manager")
        print("Select an option:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. List Tasks")
        print("4. Remove Task")
        print("5. Quit")

        while True:
            choice = input("\nEnter your choice: ")
            if choice == '1':
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == '2':
                try:
                    index = int(input("Enter task index to mark as completed: "))
                    self.mark_task_completed(index)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == '3':
                self.list_tasks()
            elif choice == '4':
                try:
                    index = int(input("Enter task index to remove: "))
                    self.remove_task(index)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()

