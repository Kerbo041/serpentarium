from modules.file_gen.materials.materials import materials
from modules.file_gen.geometry.geometry import geometry
from modules.file_gen.template import template
from modules.file_gen.default import default
from modules.file_gen.debugger import debugger

def creator(input_parameters):
    
    name = input_parameters[0]
    sections = int(input_parameters[1])
    mats = input_parameters[2:]

    str_out = template(
        "file_start_template", 
        {
            "name" : name
        }
    )

    str_out += materials(sections, mats)
    str_out += geometry(sections)
    str_out += default("file_end_default")

    return str_out
