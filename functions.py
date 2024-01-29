FILEPATH = "base.txt"


def get_todos(filepath=FILEPATH):
    """ Read text document, and return list of
    to-do items."""
    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(local_todos, filepath=FILEPATH):
    """ Write a list of to-do items in text document."""
    with open(filepath, "w") as local_file:
        local_file.writelines(local_todos)
    return
