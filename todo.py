import sys
import json
import os

todos = []


def print_todos():
    for i, case in enumerate(todos):
        print(i, '.', case)


def add_todo(case):
    todos.append(case)


def change_todo(index, case):
    todos[index] = case


def delete_todo(index):
    del todos[index]


def mark_case(index):
    todos[index]['status'] = not todos[index]['status']


# def mark_all_case(todos):
#     todos = list(map(lambda x: x['status'], todos))
#     return todos


def delete_mark_case(todos):
    # for i in todos:
    # if i['status'] == True:
    # todos.remove(i)
    todos = list(filter(lambda x: not x['status'], todos))
    return todos


def ex_todo():
    quit()


menu = "1. Print\n" \
       "2. Add\n" \
       "3. Change\n" \
       "4. Delete\n" \
       "5. Choose a case\n" \
       "6. Choose all case\n" \
       "7. Delete choose case\n" \
       "0. Exit\n"

if os.path.exists('todo.json'):
    with open('todo.json') as todofile:
        try:
            todos = json.load(todofile, )
        except json.JSONDecodeError:
            todos = []
print(todos)

while True:
    print(menu)
    command = input("Enter a number: ")
    if command not in "1234560":
        print("Error")
        continue
    elif command == '1':
        print_todos()
        continue
    elif command == '2':
        case = {'text': input("Write your case: "), 'status': False}
        add_todo(case)
        continue
    elif command == '3':
        index = int(input("Enter case number to change: "))
        case = {'text': input("Write your case: "), 'status': False}
        change_todo(index, case)
        continue
    elif command == '4':
        index = int(input("Enter case number to del: "))
        delete_todo(index)
        continue
    elif command == '5':
        index = int(input("Enter case number to mark: "))
        mark_case(index)
        continue
    # elif command == '6':
    #     mark_all_case()
    #     continue
    elif command == '7':
        todos = delete_mark_case(todos)
    elif command == '0':
        break
with open('todo.json', 'w') as todofile:
    json.dump(todos, todofile)
