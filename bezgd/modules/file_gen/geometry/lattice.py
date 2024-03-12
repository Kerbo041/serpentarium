from modules.file_gen.template import template
from modules.file_gen.default import default
from modules.file_gen.debugger import debugger

def lattice(sections):

    lats_def_data = {
        "c" : "c",
        "g" : "g",
        "w" : "w",
        "i" : "t"
    }
    
    lats = default("lattice_default")
    lats += template("lattice_template", lats_def_data)

    for i in range(sections):
        lats_temp_data = {
            "c" : "c",
            "g" : "g",
            "w" : "w",
            "i" : (i + 1)
        }
        lats += template("lattice_template",lats_temp_data)

    return lats + "\n\n\n"