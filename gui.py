import functions
import PySimpleGUI as sg

label = sg.Text("Add to-do:")
add_button = sg.Button("Add")
input_box = sg.InputText(tooltip="Add to-do")

window = sg.Window("My todo App", layout=[[label], [input_box, add_button]])
window.read()

window.close()
