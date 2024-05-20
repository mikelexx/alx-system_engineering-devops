#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the CSV format.
"""
import json
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        employee_todos = []
        employee_name = ""
        user_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id))
        user = json.loads(user_response.text)
        if user.get("id") == employee_id:
            employee_name = user.get("name")

        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/")
        todos = json.loads(todos_response.text)
        for todo in todos:
            if todo["userId"] == employee_id:
                employee_todos.append(todo)
        filename = "{}.csv".format(employee_id)
        with open(filename, "a") as f:
            for todo in employee_todos:
                f.write('"{}","{}","{}","{}"\n'.format(employee_id,
                                                       employee_name,
                                                       todo.get("completed"),
                                                       todo.get("title")))
