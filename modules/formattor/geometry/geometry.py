from modules.formattor.geometry.pins import pins
from modules.formattor.geometry.lattice import lattice 
from modules.formattor.geometry.surfaces import surfaces 
from modules.formattor.geometry.cells import cells



 





def geometry(sections):
    geometry_out = ""
    geometry_out += pins.pins(sections)
    geometry_out += lattice(sections)
    surfaces_out = surfaces(sections)
    geometry_out += surfaces_out[0]
    geometry_out += cells(sections, surfaces_out[1])
    return geometry_out