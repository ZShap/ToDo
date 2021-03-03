import sys
todos = []
#with open('test.txt') as f:
def print_todos():
   for i, case in enumerate(todos):
        print(i, '.', case)
def add_todo(case):
    todos.append(case)
    #with open('test.txt') as f:
        #f.write()
def change_todo(index, case):
    todos[index] = case
def delete_todo(index):
    del todos[index]
def mark_case(index):
    if todos[index]['status'] == False:
        todos[index]['status'] = True
    else:
        todos[index]['status'] = False
def delete_mark_case():
    for i in todos:
        if i['status'] == True:
            todos.remove(i)

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
    if command not in "1234560":
        print("Error")
        continue
    elif command == '1':
        print_todos()
        continue
    elif command == '2':
      #text = input("Write your case: ")
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
    elif command == '6':
        delete_mark_case()
    elif command == '0':
        sys.exit()
        continue
