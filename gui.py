import functions
import PySimpleGUI as sg
import time

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
edit_button = sg.Button("Edit", key="Edit", disabled=True)
# Close Button
close_button = sg.Button("Close")
# Complete button
complete_button = sg.Button("Complete", key="Complete", disabled=True)
# Time label
time_label = sg.Text('', key="time")
#Theme selection
sg.theme("Black")
window = sg.Window("My todo App",
                   layout=[[time_label],
                           [label],
                           [add_todo_input_box, add_button],
                           [todos_list_box, edit_button, complete_button],
                           [close_button]],
                   font=("Roboto", 20)
                   )

while True:
    event, values = window.read(timeout=200)
    window["time"].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
            window['todo_items'].update(values=todos)
            window['todo'].update(value=[])
            window['Complete'].update(disabled=True)
            window['Edit'].update(disabled=True)
        case "Edit":
            try:
                todo_to_edit = values['todo_items'][0]
                new_item = values['todo']+"\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_item
                functions.write_todos(todos)
                window['todo_items'].update(values=todos)
                window['todo'].update(value=[])
                window['Complete'].update(disabled=True)
                window['Edit'].update(disabled=True)
            except IndexError:
                sg.popup_error("Please select an item!")
        case "todo_items":
            window['todo'].Update(value=values['todo_items'][0].replace('\n', ''))
            window['Complete'].update(disabled=False)
            window['Edit'].update(disabled=False)
        case "Complete":
            try:
                completed_todo = values['todo_items'][0]
                todos = functions.get_todos()
                index = todos.index(completed_todo)
                todos.pop(index)
                functions.write_todos(todos)
                window['todo_items'].update(values=todos)
                window['todo'].update(value=[])
                window['Complete'].update(disabled=True)
                window['Edit'].update(disabled=True)
            except IndexError:
                sg.popup_error("Please select an item!")
        case "Close":
            break
        case sg.WIN_CLOSED:
            break
window.close()
