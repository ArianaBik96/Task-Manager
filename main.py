import task_manager
import file_manager
import os

def main():
    filename = "todo_list.json"
    file_path = file_manager.get_resource_path(filename)
    tasks =[]
    if os.path.exists(file_path):
        print("File exists")
        tasks = file_manager.load_tasks(file_path)
    else:
        print("File does't exists")
        print(file_path)
        file_manager.create_file(file_path, filename)

    manager = task_manager.TaskManger(tasks, file_path)  # ✅ Create an instance

    while True:
        print("\nTo do List Manager ✨")
        print("1. View Tasks 📋")
        print("2. Add Tasks ✏️")
        print("3. Mark Task as Completed ✅")
        print("4. Delete a task ❌")
        print("5. Exit 🏃‍♀️")

        choice = input("Enter your choice (enter a number): ").strip()

        if choice == "1":
            manager.view_tasks(tasks)  # ✅ Call on instance
        elif choice == "2":
            manager.create_task(manager.tasks)
        elif choice == "3":
            manager.mark_task_completed(tasks)
        elif choice == "4":
            manager.delete_task(tasks)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Something went wrong. Please enter a number.")

main()
