import sys
todos = []

def print_todos():
    for i, text in enumerate(todos):
        print(i, text)
def add_todo(text):
    todos.append(text)
def change_todo(index, text):
    todos[index] = text
def delete_todo(index):
    del todos[index]
def ex_todo():
    quit()

menu = "1. Print\n"\
       "2. Add\n"\
       "3. Change\n"\
       "4. Delete\n"\
       "0. Exit\n"
while True:
    print (menu)
    command = input("Enter a number: ")
    if command not in "12340":
        print("Error")
        continue
    elif command == '1':
        print_todos()
        continue
    elif command == '2':
        text = input()
        add_todo(text)
        continue
    elif command == '3':
        index = int(input())
        text = input()
        change_todo(index, text)
        continue
    elif command == '4':
        index = int(input())
        delete_todo(index)
        continue
    elif command == '0':
        sys.exit()
        continue
