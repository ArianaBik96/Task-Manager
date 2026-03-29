import json
import os
import sys

filename=  "todo_list.json"

def get_resource_path(filename):
    """ Get absolute path to resource, works for both Nuitka and normal execution """
    base_path = os.path.join(os.path.dirname(__file__), 'tasks_output', filename)  
    return base_path

def create_file (file_path, filename):
    list_file= {"tasks": [] }
    try:
        with open (file_path, "a",encoding="utf-8") as file:
            json.dump(list_file, file, indent=4)
            print(f"Created a new file called{filename}")
    except Exception as e:
        print(f"Could not created a new file called{filename}")

def load_tasks(filename):
    try:
        with open (filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Failed to load.\nAn error has occurred: ", e)
        return {"tasks": []}

def store_file(tasks, filepath: str):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump( tasks, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Failed to store\nAn error has occurred:", e)

"""def load_file(filename: str):
    try:
        with open (filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Failed to load.\nAn error has occurred: ", e)
        return {"tasks": []}

import json"""

"""def store_file(new_task, filepath: str):
    try:
        print(new_task)
        # Append new_task as a JSON string on a new line
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(json.dumps(new_task) + "\n")
    except Exception as e:
        print("Failed to save.\nAn error has occurred: ", e)
        return {"tasks": []}"""