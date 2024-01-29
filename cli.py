import functions
import time
now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is: ", now)
while True:
    user_action = input("Type add, show, edit, delete todos or exit: ").strip()

    if user_action.startswith('add'):  # add todo
        todo = user_action[4:] + "\n"
        if todo == "\n":
            print("You can not enter empty todo!")
        else:
            todos = functions.get_todos()
            todos.append(todo)
            functions.write_todos(todos)

    elif user_action.startswith('show'):  # show todos
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):  # edit todos
        try:
            todos = functions.get_todos()
            number = int(user_action[5:]) - 1
            if number > len(todos) - 1:
                print("There are no todos with this number")
            else:
                new_todo = input("Add new todo: ") + "\n"
                todos[number] = new_todo
                functions.write_todos(todos)
        except ValueError:
            print("Invalid input!")
            continue

    elif user_action.startswith('delete'):  # delete todos
        try:
            todos = functions.get_todos()
            number = int(user_action[6:]) - 1
            if number > len(todos) - 1:
                print("There are no todos with this number")
            else:
                todo_to_remove = todos[number].strip('\n')
                todos.pop(number)
                functions.write_todos(todos)
                print(f"Todo '{todo_to_remove}' was removes successfully!")
        except TypeError:
            print("Invalid input!")
            continue

    elif user_action.startswith('exit'):  # exit program
        break

    else:
        print("Input not valid!")  # if enter invalid command

print("Bye")
