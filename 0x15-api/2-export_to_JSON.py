#!/usr/bin/python3
"""  script to export data in the JSON format."""
import requests
from sys import argv
from json import dump


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    name_url = base_url + "/users/{}".format(argv[1])
    name_res = requests.get(name_url).json()
    todo_url = base_url + "/user/{}/todos".format(argv[1])
    todo_res = requests.get(todo_url).json()

    todo_list = []
    for todo in todo_res:
        todo_dict = {}
        todo_dict.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": name_res.get("username")})
        todo_list.append(todo_dict)

    with open("{}.json".format(argv[1]), 'w') as f:
        dump({argv[1]: todo_list}, f)
