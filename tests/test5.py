import PySimpleGUI as sg
import zip_creator

source_file_label = sg.Text('Select file to extract:')
source_button = sg.FileBrowse('Choose', key="archive_path")
source_text_box = sg.InputText()

destination_folder_label = sg.Text('Select destination folder:')
destination_button = sg.FolderBrowse('Choose', key="destination_folder")
destination_text_box = sg.InputText()
extract_button = sg.Button('Extract')

window = sg.Window("Extract app", layout=[[source_file_label, source_text_box, source_button],
                                           [destination_folder_label, destination_text_box, destination_button],
                                           [extract_button]])
event, values = window.read()
filepath = values["archive_path"]
folder_path = values["destination_folder"]
zip_creator.extract_archive(filepath,folder_path)
window.close()