from argparse import ArgumentParser
import os
import sys
import json
from tabulate import tabulate
from datetime import datetime

TASK_FILE = "tasks.json"



def read_json_file(file:str):
    fstream = open(file,"r")
    data = json.load(fstream)
    fstream.close()
    return data

def write_json_file(file:str, arrObj:list):
    fstream = open(file,"w")
    fstream.write(json.dumps(arrObj))
    fstream.close()


def load_tasks(file:str)->list:
    if not os.path.exists(file):
        write_json_file(file,[])
        return []
    else:
        return read_json_file(file)

def add_task(description:str):
    tasks = load_tasks(TASK_FILE)
    task_id = len(tasks) + 1
    now = datetime.now().isoformat()
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    write_json_file(TASK_FILE,tasks)
    print(tabulate([new_task],tablefmt="rounded_grid",headers='keys'))

def update_task(id, description):
    tasks = load_tasks(TASK_FILE)
    for task in tasks:
        if(task['id'] == int(id)):
            task['description'] = description
            now = datetime.now().isoformat()
            task["updatedAt"] = now
    write_json_file(TASK_FILE,tasks)
    print(tabulate(tasks,tablefmt="rounded_grid",headers='keys'))

def delete_task(id:str):
    tasks = load_tasks(TASK_FILE)
    for task in tasks:
        if task['id'] == int(id):
            tasks.remove(task)

    write_json_file(TASK_FILE,tasks)
    print(tabulate(tasks,tablefmt="rounded_grid",headers='keys'))

def list_tasks(status:str):
    tasks = load_tasks(TASK_FILE)
    filtered_tasks = []

    if status == "all":
        filtered_tasks.extend(tasks)
    else :
        for task in tasks:
            if task["status"] == status :
                filtered_tasks.append(task)

    print(tabulate(filtered_tasks,tablefmt="rounded_grid",headers='keys') or 'Nothing to display')

def mark_in_progress_task(id):
    tasks = load_tasks(TASK_FILE)
    for task in tasks:
        if(task['id'] == int(id)):
            task["status"] = 'in-progress'
    write_json_file(TASK_FILE,tasks)
    print(tabulate(tasks,tablefmt="rounded_grid",headers='keys'))

def mark_done_task(id):
    tasks = load_tasks(TASK_FILE)
    for task in tasks:
        if(task['id'] == int(id)):
            task["status"] = 'done'
    write_json_file(TASK_FILE,tasks)
    print(tabulate(tasks,tablefmt="rounded_grid",headers='keys'))

def get_supported_queries() -> dict[str, dict]:
    return {
        "add": {
            "help": "Add a new task to your task list",
            "args": [
                {"name_or_flags": ["description"], "help": "Description of the task"}
            ],
        },
        "delete": {
            "help": "Delete a task from your task list",
            "args": [
                {
                    "name_or_flags": ["id"],
                    "help": "ID of the task you want to delete",
                }
            ],
        },
        "update": {
            "help": "Update the description of a task",
            "args": [
                {
                    "name_or_flags": ["id"],
                    "help": "ID of the task to update",
                },
                {
                    "name_or_flags": ["description"],
                    "help": "New description for the task",
                },
            ],
        },
        "list": {
            "help": "List all tasks or filter them by status",
            "args": [
                {
                    "name_or_flags": ["--status", "-s"],
                    "help": "Filter tasks by status (default is 'all')",
                    "choices": ["all", "done", "todo", "in-progress"],
                    "type": str.lower,
                    "default": "all",
                }
            ],
        },
        "mark-in-progress": {
            "help": "Mark a task as 'in-progress'",
            "args": [{"name_or_flags": ["id"], "help": "ID of the task"}],
        },
        "mark-done": {
            "help": "Mark a task as 'done'",
            "args": [{"name_or_flags": ["id"], "help": "ID of the task"}],
        },
    }

def main():
    parser = ArgumentParser(description="A CLI app to manage tasks effectively")
    sub_parser = parser.add_subparsers(title="commands",dest="command",required=True)

    
    for name, properties in get_supported_queries().items():
        p = sub_parser.add_parser(name,help=properties['help'])

        for arg in properties["args"]:
            p.add_argument(*arg.pop("name_or_flags"), **arg)


    args: dict = parser.parse_args().__dict__
    print(args)

    if args['command'] == 'add':
        add_task(args['description'])
    elif args['command'] == 'update':
        update_task(args['id'], args["description"])
    elif args['command'] == 'delete':
        delete_task(args["id"])
    elif args['command'] == 'list':
        list_tasks(args["status"])
    elif args['command'] == 'mark-in-progress':
        mark_in_progress_task(args['id'])
    elif args['command'] == 'mark-done':
        mark_done_task(args['id'])
    else :
        print('No command found')


if __name__ == "__main__":
    main()
