
def default(file_name):
    default_file = open(("default/" + file_name), "r")
    default_str = default_file.read()
    default_file.close()
    return default_str