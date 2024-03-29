import PySimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_text_box = sg.InputText(key="feets")

inches_label = sg.Text("Enter inches")
inches_text_box = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
converted_value = sg.Text("", key="converted_value")

exit_button = sg.Button("Exit")
sg.theme("Black")

window = sg.Window("Convertor", [[feet_label, feet_text_box],
                                 [inches_label, inches_text_box],
                                 [convert_button, exit_button, converted_value]])
while True:
    event, values = window.read()
    try:
        match event:
            case "Convert":
                feets = float(values['feets'])
                inches = float(values['inches'])
                result = feets * 0.3048 + inches * 0.0254
                window['converted_value'].update(value=f"{str(result)}m", text_color="white")
            case sg.WIN_CLOSED:
                break
            case "Exit":
                break
    except ValueError:
        sg.popup("Wrong input, please try again")
window.close()
