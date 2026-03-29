import file_manager

class TaskManger:

    def __init__(self, tasks, filepath):
        self.tasks = tasks
        self.filename = filepath

    def view_tasks(self, tasks):
        task_list = tasks["tasks"]
        if len(task_list) ==0:
            print("There are no tasks in your to do list")
        else:
            print
            for i, task in enumerate(task_list):
              status ="[Completed]" if task["complete"] else "[Pending]"
              print (f'{i +1}. {task["description"]} | {status}')
              """if task["complete"]:
                    status = "Completed"
                else:
                    status = "Pending"""



    def create_task(self, tasks):
        description = input("Enter the task description: ").strip()
        if description:
            new_task = {"description": description, "complete": False}
            tasks["tasks"].append(new_task)
            file_manager.store_file(tasks, self.filename)
            print("Task added successfully")
        else:
            print("Description can't be empty")

    def mark_task_completed(self, tasks):
        self.view_tasks(tasks)
        try:
            tasknum = int(input("Enter the task number to mark it as complete").strip())
            if 1 <= tasknum <= len(tasks):
                tasks["tasks"][tasknum -1]["complete"] =True 
                file_manager.store_file(tasks, self.filename)
                print(f"'{tasks["tasks"][tasknum -1]["description"]}' marked as completed")
            else:
                print("Not a valid number")
        except Exception as e:
               print("Failed to mark.\nAn error has occurred: ", e) 

    def delete_task(self, tasks):
        self.view_tasks(tasks)
        try:
            tasknum = int(input("Which task do you want to delete?"))
            print(tasknum)
            if 0<=tasknum<=len(tasks):
                print("is here")
                todel= tasks["tasks"][tasknum-1]
                del tasks["tasks"][tasknum-1]
                print(f"Delete task: {todel['description']}❌")
                file_manager.store_file(tasks, self.filename)
        except Exception as e:
               print("Failed to delete.\nAn error has occurred: ", e) 


        """for i, task in enumerate(tasks):
            if i == tasknum:
                del(tasks["tasks"][i-1])
                break"""
    