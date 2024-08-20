from modules.file_gen.template import template
from modules.file_gen.default import default
from modules.file_gen.debugger import debugger

def cells(sections, surf4cells):
    cells_out = default("cells_default")

    for i in range(sections):

        cell_temp_data = {
            "iter" : (i + 1),
            "bottom" : surf4cells[i],
            "top" : surf4cells[i + 1],
        }

        cells_out += template(
            "cell_template", 
            cell_temp_data
            )

    return cells_out + "\n\n\n"

