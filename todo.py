import sys
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
def choose_case():
    pass
def delete_choose():
    pass
def ex_todo():
    quit()

menu = "1. Print\n"\
       "2. Add\n"\
       "3. Change\n"\
       "4. Delete\n"\
       "5. Choose a case\n"\
       "6. Delete choose case\n"\
       "0. Exit\n"
while True:
    print(menu)
    command = input("Enter a number: ")
    if command not in "12340":
        print("Error")
        continue
    elif command == '1':
        print_todos()
        continue
    elif command == '2':
      #text = input("Write your case: ")
        case = {input("Write your case: "): False}
        add_todo(case)
        continue
    elif command == '3':
        index = int(input("Enter case number to change: "))
        case = {input("Write your case: "): False}
        change_todo(index, case)
        continue
    elif command == '4':
        index = int(input("Enter case number to del: "))
        delete_todo(index)
        continue
    elif command == '5':
        continue
    elif command == '6':
        continue
    elif command == '0':
        sys.exit()
        continue
