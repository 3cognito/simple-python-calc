from time import sleep
from typing import List


def read_tasks(filename: str) -> List[str]:
    """Read tasks from the text file and return them as a list."""
    tasks: List[str] = []
    with open(filename, "r") as file:
        for line in file:
            tasks.append(line.strip())
    return tasks


def add_tasks(filename: str, tasks: List[str]) -> None:
    """Write tasks to the text file."""
    with open(filename, "w+") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks: List[str]) -> None:
    """Display the list of tasks to the user."""
    print("To-Do List:")
    for task in tasks:
        sleep(1)
        print(task)


def update_task(index: int, new_task: str, filename: str) -> None:
    """Update a task in the to-do list."""
    task_list = read_tasks(filename)
    if 0 <= index - 1 < len(task_list):
        task_list[index - 1] = new_task
        add_tasks(filename, task_list)
        print(f"Task at index {index} updated to {new_task}")
    else:
        print(f"No task at index {index}")


def delete_task(index, filename) -> None:
    """Delete a task from the to-do list."""
    task_list = read_tasks(filename)
    if 0 <= index - 1 < len(task_list):
        task_list.pop(index - 1)
        add_tasks(filename, task_list)
        print(f"Task at index {index} deleted.")
    else:
        print(f"No task at index {index}")


def main():
    filename = "todo.txt"
    # tasks = read_tasks(filename)
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
            task_list = read_tasks(filename)
            task_list.append(task)
            add_tasks(filename, task_list)

        elif choice == "2":
            view_tasks(read_tasks(filename))

        elif choice == "3":
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task description: ")
            update_task(index, new_task, filename)

        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            delete_task(index, filename)

        elif choice == "5":
            print("Thank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
