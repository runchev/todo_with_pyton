# import random
# lower_bound = int(input("Insert lower bound: "))
# higher_bound = int(input("Insert higher bound: "))
#
# try:
#     print(random.randint(lower_bound, higher_bound))
# except ValueError:
#     print("Invalid input, try again!")

# import json
#
# with open("questions.json", "r") as file:
#     content = file.read()
# tocen_odgovor = 0
# netocen_odgovor = 0
# data = json.loads(content)
# for question in data:
#     print(question['question_text'])
#     for index, ponudeni_odgovori in enumerate(question['ponudeni_odgovori']):
#         print(int(index)+1, "-", ponudeni_odgovori)
#     odgovor = input("Vnesi go odgovorot: ")
#     if int(odgovor) == question['tocen_odgovor']:
#         tocen_odgovor = tocen_odgovor+1
#     else:
#         netocen_odgovor = netocen_odgovor+1
#     print("Tocni odgovori: ", str(tocen_odgovor), "/", len(data))
#     print("Netocni odgovori: ", str(netocen_odgovor), "/", len(data))

import PySimpleGUI as sg

source_files_label = sg.Text('Select files to compres:')
source_button = sg.FileBrowse('Choose')
source_text_box = sg.InputText()

destination_files_label = sg.Text('Select destination folder:')
destination_button = sg.FileBrowse('Choose')
destination_text_box = sg.InputText()
compress_button = sg.Button('Compress')

feet_label = sg.Text("Enter feet: ")
feet_text_box = sg.InputText()

inches_label = sg.Text("Enter inches")
inches_text_box = sg.InputText()

convert_button = sg.Button("Convert")

# window = sg.Window("Compression program",[[source_files_label,source_text_box,source_button],
#                                           [destination_files_label,destination_text_box,destination_button],
#                                           [compress_button]])


window = sg.Window("Convertor",[[feet_label,feet_text_box],
                                          [inches_label,inches_text_box],
                                          [convert_button]])

window.read()
window.close()