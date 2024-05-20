#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        employee_completed_todos = []
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
        total_tasks_count = 0
        done_tasks_count = 0

        for todo in todos:
            if todo["userId"] == employee_id:
                total_tasks_count += 1
                if todo["completed"] is True:
                    employee_completed_todos.append(todo["title"])
                    done_tasks_count += 1

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, done_tasks_count, total_tasks_count))
        for todo in employee_completed_todos:
            print("\t {}".format(todo))
