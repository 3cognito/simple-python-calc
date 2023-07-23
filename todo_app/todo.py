from time import sleep
from typing import List


class ToDoList:
    def __init__(self, filename: str):
        self.filename = filename

    def read_tasks(self) -> List[str]:
        """Read tasks from the text file and return them as a list."""
        tasks: List[str] = []
        with open(self.filename, "r") as file:
            for line in file:
                tasks.append(line.strip())
        return tasks

    def add_tasks(self, tasks: List[str]) -> None:
        """Add a new task to the list and write to the text file."""
        with open(self.filename, "w+") as file:
            for task in tasks:
                file.write(task + "\n")

    def view_tasks(self) -> None:
        """Display the list of tasks to the user."""
        tasks = self.read_tasks()
        print("To-Do List:")
        for task in tasks:
            sleep(1)
            print(task)

    def update_task(self, index: int, new_task: str) -> None:
        """Update a task in the to-do list."""
        task_list = self.read_tasks()
        if 0 <= index - 1 < len(task_list):
            task_list[index - 1] = new_task
            self.add_tasks(task_list)
            print(f"Task at index {index} updated to {new_task}")
        else:
            print(f"No task at index {index}")

    def delete_task(self, index: int) -> None:
        """Delete a task from the to-do list."""
        task_list = self.read_tasks()
        if 0 <= index - 1 < len(task_list):
            task_list.pop(index - 1)
            self.add_tasks(task_list)
            print(f"Task at index {index} deleted.")
        else:
            print(f"No task at index {index}")


def main():
    filename = "todo.txt"
    todo_list = ToDoList(filename)

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the new task: ")
            task_list = todo_list.read_tasks()
            task_list.append(task)
            todo_list.add_tasks(task_list)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task description: ")
            todo_list.update_task(index, new_task)

        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)

        elif choice == "5":
            print("Thank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
