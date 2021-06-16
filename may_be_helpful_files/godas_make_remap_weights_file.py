import matplotlib
matplotlib.use('Agg')
import pyroms
import pyroms_toolbox

print("Modules imported")
# load the grid
#comment by msa srcgrd = pyroms_toolbox.Grid_HYCOM.get_nc_Grid_HYCOM2('/import/AKWATERS/kshedstrom/HYCOM/Svalbard/data/HYCOM_GLBv0.08_2019_365.nc')

srcgrd = pyroms_toolbox.Grid_HYCOM.get_nc_Grid_HYCOM2('/home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/Godas_uvsshts_jan_2019_.nc')

dstgrd = pyroms.grid.get_ROMS_grid('GODASROMS')
print("$"*33)
# make remap grid file for scrip
pyroms_toolbox.Grid_HYCOM.make_remap_grid_file(srcgrd)
pyroms.remapping.make_remap_grid_file(dstgrd, Cpos='rho')
pyroms.remapping.make_remap_grid_file(dstgrd, Cpos='u')
pyroms.remapping.make_remap_grid_file(dstgrd, Cpos='v')

print("print1 checking")
# compute remap weights
# input namelist variables for bilinear remapping at rho points
grid1_file = 'remap_grid_GLBv0.08_NEP_t.nc'
grid2_file = 'remap_grid_ARCTIC4_rho.nc'
interp_file1 = 'remap_weights_GLBv0.08_to_ARCTIC4_bilinear_t_to_rho.nc'
interp_file2 = 'remap_weights_ARCTIC4_to_GLBv0.08_bilinear_rho_to_t.nc'
map1_name = 'GLBv0.08 to ARCTIC4 Bilinear Mapping'
map2_name = 'ARCTIC4 to GLBv0.08 Bilinear Mapping'
num_maps = 1
map_method = 'bilinear'

pyroms.remapping.compute_remap_weights(grid1_file, grid2_file, \
              interp_file1, interp_file2, map1_name, \
              map2_name, num_maps, map_method)


# compute remap weights
# input namelist variables for bilinear remapping at rho points
grid1_file = 'remap_grid_GLBv0.08_NEP_t.nc'
grid2_file = 'remap_grid_ARCTIC4_u.nc'
interp_file1 = 'remap_weights_GLBv0.08_to_ARCTIC4_bilinear_t_to_u.nc'
interp_file2 = 'remap_weights_ARCTIC4_to_GLBv0.08_bilinear_u_to_t.nc'
map1_name = 'GLBv0.08 to ARCTIC4 Bilinear Mapping'
map2_name = 'ARCTIC4 to GLBv0.08 Bilinear Mapping'
num_maps = 1
map_method = 'bilinear'

pyroms.remapping.compute_remap_weights(grid1_file, grid2_file, \
              interp_file1, interp_file2, map1_name, \
              map2_name, num_maps, map_method)

print("print2 checking")

# compute remap weights
# input namelist variables for bilinear remapping at rho points
grid1_file = 'remap_grid_GLBv0.08_NEP_t.nc'
grid2_file = 'remap_grid_ARCTIC4_v.nc'
interp_file1 = 'remap_weights_GLBv0.08_to_ARCTIC4_bilinear_t_to_v.nc'
interp_file2 = 'remap_weights_ARCTIC4_to_GLBv0.08_bilinear_v_to_t.nc'
map1_name = 'GLBv0.08 to ARCTIC4 Bilinear Mapping'
map2_name = 'ARCTIC4 to GLBv0.08 Bilinear Mapping'
num_maps = 1
map_method = 'bilinear'

pyroms.remapping.compute_remap_weights(grid1_file, grid2_file, \
              interp_file1, interp_file2, map1_name, \
              map2_name, num_maps, map_method)

print("print3 checking")

