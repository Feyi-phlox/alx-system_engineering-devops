#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import requests
from sys import argv


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    name_url = base_url + "/users/{}".format(argv[1])
    name_res = requests.get(name_url).json()
    todo_url = base_url + "/user/{}/todos".format(argv[1])
    todo_res = requests.get(todo_url).json()

    todo_num = len(todo_res)
    todo_complete = len([todo for todo in todo_res
                         if todo.get("completed")])
    name = name_res.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_res:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
