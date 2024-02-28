def cell_create(iter, bottom, top):
    cell_out = ""
    cell_out += "cell  tvel_section_" + str(iter) + "     0  fill l" + str(iter) + " -tvs_hex     " + bottom + "        -" + top + "	    % tvel section" + str(iter)  + " \n"
    return cell_out



def cells(sections, surf4cells):
    cells_out = ""
    cells_out += "% --- Cells:\n\ncell  tvel_bottom_zone  0  fill lt     -tvs_hex 	tvel_bottom     -fuel_bottom	% tvel bottom lattice\ncell  tvel_top_zone     0  fill lt     -tvs_hex     fuel_top        -tvel_top	    % tvel top lattice\ncell  tvs_bottom_zone   0  wst         -tvs_hex     tvs_bottom      -tvel_bottom    % tvs bottom\ncell  tvs_top_zone      0  wst         -tvs_hex     tvel_top        -tvs_top        % tvs top\ncell 99  0  outside                     tvs_hex 		                            % Outside world\ncell 98  0  outside                    -tvs_hex    -tvs_bottom		                % Outside world\ncell 97  0  outside                    -tvs_hex     tvs_top		                    % Outside world\n"
    for i in range(sections):
        cells_out += cell_create(i+1,surf4cells[i],surf4cells[i+1])
    return cells_out + "\n\n\n"

