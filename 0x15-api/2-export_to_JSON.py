#!/usr/bin/python3
"""
Using what you did in the task #0, 
extend your Python script to export data in the JSON format.
"""
import csv
import json
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        employee_todos = []
        username = ""
        user_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id))
        user = json.loads(user_response.text)
        if user.get("id") == employee_id:
            username = user.get("username")

        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(employee_id))
        employee_todos = json.loads(todos_response.text)
        export_todos = []
        for todo in employee_todos:
            tmp = {}
            tmp["task"] = todo.get("title")
            tmp["completed"] = todo.get("completed")
            tmp["username"] = username
            export_todos.append(tmp)
        data = {employee_id: export_todos}
        with open("{}.json".format(employee_id), "w") as f:
            f.write(json.dumps(data))
