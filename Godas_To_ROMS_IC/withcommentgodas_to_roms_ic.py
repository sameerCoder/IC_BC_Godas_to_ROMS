############################################################################################
# This Python script is used to create initial condition of ROMS from GODAS Data           #
# This Python script is written by Sakib.a@incois.gov.in                                   #
############################################################################################

#Below lines of code is for importing required modules.
import subprocess
import os
import sys
import numpy as np
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import pyroms
import pyroms_toolbox
from remap_clm import remap_clm
from remap_clm_uv import remap_clm_uv
import os

#Below line of code is for assigning the Godas grid file name.
#if you want user to input the godas filename then uncomment the file1 line of code,this line of code will ask user when executing the python file.
#file1=input("Enter the Godas full filename:")
file1=("Godas_uvsshts_jan_2019_.nc")
print("Building IC file from the following file {}.".format(file1))
#directory=input("Enter Absolute Godas file path(Directory path):")
#Below line of code is for getting the absolute path of file.
print("os getcwd:",os.getcwd())
directory=os.getcwd()

dst_dir=directory
src_grd=pyroms_toolbox.Grid_HYCOM.get_nc_Grid_HYCOM2(directory+"/"+file1)
dst_grd=pyroms.grid.get_ROMS_grid('GODASROMS')
print("Source grid:",src_grd)

#below line of code for generating the ic as per the parameter
#below line of code to execute properly we need remap_clm.py , remap_clm_uv.py files into same directory of this python file.
zeta=remap_clm(file1,'SSH',src_grd,dst_grd,dst_dir=directory)
print("zeta work done")
print("#"*45)
dst_grd=pyroms.grid.get_ROMS_grid('GODASROMS',zeta=zeta)
################################################################
remap_clm(file1,'temp',src_grd,dst_grd,dst_dir=directory)
print("Temp work done.")
################################################################
remap_clm(file1,'salt',src_grd,dst_grd,dst_dir=directory)
print("Salt work done.")
################################################################
remap_clm_uv(file1,src_grd,dst_grd,dst_dir=directory)
print("UV work done.")
###############################################################

clim_file=dst_dir+"/"+file1.rsplit('/')[-1][:-3]+'_clim_'+dst_grd.name+'.nc'

out_file=dst_dir+"/"+file1.rsplit('/')[-1][:-3]+'_SSH_clim_'+dst_grd.name+".nc"
command=('ncks','-a','-A',out_file,clim_file)
print(command)
subprocess.check_call(command)
os.remove(out_file)
out_file=dst_dir+"/"+file1.rsplit('/')[-1][:-3]+'_temp_clim_'+dst_grd.name+".nc"
command=('ncks','-a','-A',out_file,clim_file)
print(command)
subprocess.check_call(command)
os.remove(out_file)
out_file=dst_dir+"/"+file1.rsplit('/')[-1][:-3]+"_salt_clim_"+dst_grd.name+".nc"
command=('ncks','-a','-A',out_file,clim_file)
subprocess.check_call(command)
os.remove(out_file)

out_file=dst_dir+"/"+file1.rsplit('/')[-1][:-3]+"_u_clim_"+dst_grd.name+".nc"
command=('ncks','-a','-A',out_file,clim_file)
subprocess.check_call(command)
os.remove(out_file)

out_file=dst_dir+"/"+file1.rsplit('/')[-1][:-3]+'_v_clim_'+dst_grd.name+".nc"
command=('ncks','-a','-A',out_file,clim_file)
subprocess.check_call(command)
os.remove(out_file)
print("All task done !!!")



