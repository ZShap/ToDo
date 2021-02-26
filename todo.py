todos = []

def print_todos(text):
    pass
def add_todo(text):
    todos.append(text)
def change_todo(index, text):
    pass
def delete_todo(index):
    pass
def ex_todo():
    pass

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
        add_todo(text)
        continue
    elif command == '3':
        change_todo(index, text)
        continue
    elif command == '4':
        delete_todo(index)
        continue
    elif command == '5':
        ex_todo()
        continue
