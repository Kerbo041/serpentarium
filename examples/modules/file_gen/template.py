
def template(file_name, format_data):
    template_file = open(("templates/" + file_name), "r")
    template_raw = template_file.read()
    template_file.close()
    return template_raw.format(**format_data)