#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys
if __name__ == "__main__":
    user_todos = []
    username = ""
    users_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/')
    users = json.loads(users_response.text)
    data = {}
    for user in users:
        username = user.get("username")
        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
                user.get("id")))
        user_todos = json.loads(todos_response.text)
        export_todos = []
        for todo in user_todos:
            tmp = {}
            tmp["username"] = username
            tmp["task"] = todo.get("title")
            tmp["completed"] = todo.get("completed")
            export_todos.append(tmp)
        data[user.get("id")] = export_todos
    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(data))
