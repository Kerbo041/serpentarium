from modules.file_gen.geometry.pins import pins
from modules.file_gen.geometry.lattice import lattice 
from modules.file_gen.geometry.surfaces import surfaces 
from modules.file_gen.geometry.cells import cells
from modules.file_gen.debugger import debugger

def geometry(sections):
    geometry_out = ""
    geometry_out += pins(sections)
    geometry_out += lattice(sections)
    surfaces_out = surfaces(sections)
    geometry_out += surfaces_out[0]
    geometry_out += cells(sections, surfaces_out[1])
    return geometry_out