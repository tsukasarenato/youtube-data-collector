def str_clear(text):
    """
    This function removes characters that can cause problems in the JSON file.
    """

    text = str(text)
    text = text.replace('\\', '')
    text = text.replace('\n', ' ')
    return text.replace('"', '')
