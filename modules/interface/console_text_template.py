
def text(file_name, format_data):
    text_file = open(("modules/interface/console_text" + file_name), "r")
    text_raw = text_file.read()
    text_file.close()
    return text_raw.format(**format_data)