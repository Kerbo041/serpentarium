from modules.file_gen.template import template
from modules.file_gen.default import default
from modules.file_gen.debugger import debugger





def surfaces(sections):

    surf_out = default("surfaces_default")

    surf_need = sections + 1
    surf4cells = []
    surf4cells.append("fuel_bottom")
    if surf_need > 2:
        
        len = 368
        len_one = len / sections

        surf_numb = surf_need - 2
        surf_len = []

        for i in range(surf_numb):
            surf_len = (i+1) * len_one - len/2

            surf_out += template(
                "surface_template", 
                {"iter": (i+1), "height" : surf_len} 
                )
            
            surf4cells.append("fuel_surf_"+str(i+1))


    surf4cells.append("fuel_top")

    return [surf_out, surf4cells]