import zipfile
import pathlib


def make_archive(filepaths, folder_path):
    destination_path = pathlib.Path(folder_path, "compressed.zip")
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for file in filepaths:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)


def extract_archive(filepath, folder_path):
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(folder_path)
