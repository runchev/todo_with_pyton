import functions
import PySimpleGUI as sg

# Add todo elements
label = sg.Text("Add to-do:")
add_todo_input_box = sg.InputText(tooltip="Add to-do",
                                  key="todo")
add_button = sg.Button("Add")

# List todo items
todos_list_box = sg.Listbox(values=functions.get_todos(),
                            key='todo_items',
                            enable_events=True,
                            size=(45, 10))
# Edit Button
edit_button = sg.Button("Edit")
# Close Button
close_button = sg.Button("Close")

window = sg.Window("My todo App",
                   layout=[[label],
                           [add_todo_input_box, add_button],
                           [todos_list_box, edit_button],
                           [close_button]],
                   font=("Roboto", 20)
                   )

while True:
    event, values = window.read()
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todo_items'][0]
            new_item = values['todo']+"\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_item
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
        case "todo_items":
            window['todo'].Update(value=values['todo_items'][0])
        case "Close":
            break
        case sg.WIN_CLOSED:
            break
window.close()
