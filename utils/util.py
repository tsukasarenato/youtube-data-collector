import os

def str_clear(text):
    """
    This function removes characters that can cause problems in the JSON file.
    """

    text = str(text)
    text = text.replace('\\', '')
    text = text.replace('\n', ' ')
    return text.replace('"', '')

def check_path(path):
    """
    This function creates directories if it not exists
    """
    
    if not os.path.isdir(path):
        os.makedirs(path)
        print("Directory created")
    else:
        print("Directory exists")
