# To-Do List Application
# A command-line app to manage your daily tasks

tasks = []


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("       WELCOME TO YOUR TO-DO LIST")
    print("="*40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    print("="*40)


def add_task():
    """Add a new task to the list."""
    try:
        task = input("Enter the task: ").strip()
        if not task:
            print("❌ Task cannot be empty!")
        else:
            tasks.append(task)
            print(f"✅ Task '{task}' added successfully!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        print("Returning to main menu...")


def view_tasks():
    """Display all current tasks."""
    try:
        if not tasks:
            raise ValueError("No tasks found!")
        else:
            print("\n📋 YOUR TASKS:")
            print("-" * 30)
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            print("-" * 30)
    except ValueError as e:
        print(f"⚠️  {e} Add a task first.")
    finally:
        print("Returning to main menu...")


def delete_task():
    """Delete a task by its number."""
    try:
        if not tasks:
            raise ValueError("No tasks to delete!")

        view_tasks()
        task_num = int(input("Enter task number to delete: "))

        if task_num < 1 or task_num > len(tasks):
            raise IndexError("Task number does not exist!")

        removed = tasks.pop(task_num - 1)
        print(f"🗑️  Task '{removed}' deleted successfully!")

    except ValueError as e:
        print(f"❌ Invalid input: {e}")
    except IndexError as e:
        print(f"❌ Error: {e}")
    finally:
        print("Returning to main menu...")


def main():
    """Main function to run the To-Do app."""
    print("\n🎉 Welcome to your To-Do List Application!")

    while True:
        display_menu()
        try:
            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print("\n👋 Goodbye! Stay productive!")
                break
            else:
                raise ValueError("Invalid option selected!")

        except ValueError as e:
            print(f"❌ {e} Please choose between 1 and 4.")
        finally:
            pass


if __name__ == "__main__":
    main()