from modules.file_gen.template import template
from modules.file_gen.default import default
from modules.file_gen.debugger import debugger

def pins(sections):

    pins_out = ""
    pins_out = default("pins_default")

    for i in range(sections):
        
        pins_out += template("pin_template", {"iter": (i+1)} )

    return pins_out + "\n\n\n"