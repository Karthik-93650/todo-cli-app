def show_menu():
    print("To-Do List App17")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Mark Task as Completed")
    print("5.Exit")


def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, item in enumerate(tasks, start=1):
        status = "✔" if item["completed"] else "✘"
        print(f"{index}. {item['task']} [{status}]")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_complete(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()