import PySimpleGUI as sg
import zip_creator

source_files_label = sg.Text('Select files to compress:')
source_button = sg.FilesBrowse('Choose', key="files")
source_text_box = sg.InputText()

destination_files_label = sg.Text('Select destination folder:')
destination_button = sg.FolderBrowse('Choose', key="folder")
destination_text_box = sg.InputText()
compress_button = sg.Button('Compress')

window = sg.Window("Compress app", layout=[[source_files_label, source_text_box, source_button],
                                           [destination_files_label, destination_text_box, destination_button],
                                           [compress_button]])
while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder_path = values["folder"]
    zip_creator.make_archive(filepaths,folder_path)
    print(filepaths, folder_path)
window.close()
