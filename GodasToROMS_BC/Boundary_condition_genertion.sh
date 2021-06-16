#############################################################
# This is the final file to generate Boundary condition for ROMS from Godas #

#!/bin/bash
cd /home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/bdry
rm -f Godas_day*.nc
cd ..
python3 Boundary_condition_genertion_from_Godas_to_ROMS.py 2019
cd /home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/bdry
ncrcat Godas_day*.nc final_Godas_bdry.nc
