#Below lines of code is use to import the required module
import matplotlib
matplotlib.use('Agg')

import subprocess
import os
import sys
import numpy as np
from multiprocessing import Pool
#import pdb

#increase the maximum number of open files allowed
#import resource
#resource.setrlimit(resource.RLIMIT_NOFILE, (3000,-1))

import pyroms
import pyroms_toolbox

from remap_bdry import remap_bdry
from remap_bdry_uv import remap_bdry_uv

lst_year = sys.argv[1:]
print("lst_year:",lst_year)
lst_year=2021

#below line of code is for mentioning the data file directory location.
data_dir = '/home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/'

#below line of code is for mentioning the destination file directory location.
dst_dir='/home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/bdry/'

lst_file = []

#Below line of code is for assigning name for Godas grid file
source_file=data_dir  +'Godas_uvsshts_jan_2019_.nc'
#BelowLineformonthtoday
#cdo splitday $source_file feb.nc

command = ('cdo', 'splitday',source_file,"Godas_day.nc")
subprocess.check_call(command)
#exit()
for year in lst_year:
  #  lst = subprocess.getoutput('ls ' + data_dir + 'Godas_uvsshts_jan_' + year + '_.nc')
    lst = subprocess.getoutput('ls Godas_day*.nc')
#   lst = subprocess.getoutput('ls ' + data_dir + 'HYCOM_GLBy0.08_' + year + '*')
#    lst = subprocess.getoutput('ls ' + data_dir + 'HYCOM_GLBy0.08_' + year + '_0*')
#    lst = subprocess.getoutput('ls ' + data_dir + 'HYCOM_GLBy0.08_' + year + '_0[4-9]*')
    lst = lst.split()
    lst_file = lst_file + lst


print('Build OBC file from the following file list:')
print(lst_file)
print('00:',lst_file[0][0] )
finalmerge_lst_file=lst_file[0][0:3]


#Below line of code is for assigning name for Godas grid file
src_grd_file = data_dir  +'Godas_uvsshts_jan_2019_.nc'
src_grd = pyroms_toolbox.Grid_HYCOM.get_nc_Grid_HYCOM2(src_grd_file)
dst_grd = pyroms.grid.get_ROMS_grid('GODASROMS')

def do_file(file):
    zeta = remap_bdry(file, 'SSH', src_grd, dst_grd, dst_dir=dst_dir)
    dst_grd2 = pyroms.grid.get_ROMS_grid('GODASROMS', zeta=zeta)
    remap_bdry(file, 'temp', src_grd, dst_grd2, dst_dir=dst_dir)
    remap_bdry(file, 'salt', src_grd, dst_grd2, dst_dir=dst_dir)
#   pdb.set_trace()
    remap_bdry_uv(file, src_grd, dst_grd2, dst_dir=dst_dir)

    # merge file
    bdry_file = dst_dir + file.rsplit('/')[-1][:-3] + '_bdry_' + dst_grd.name + '.nc'

    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_SSH_bdry_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-O', out_file, bdry_file)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_temp_bdry_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, bdry_file)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_salt_bdry_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, bdry_file)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_u_bdry_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, bdry_file)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_v_bdry_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, bdry_file)
    subprocess.check_call(command)
    os.remove(out_file)

processes = 4
p = Pool(processes)
results = p.map(do_file, lst_file)

#nccatfile=finalmerge_lst_file+"*.nc"
#os.chdir(dst_dir)
#print(os.getcwd())
#command=("ncrcat","feb.*.nc","BCfinal.nc")
#subprocess.check_call(command)
#command=("rm","-f",finalmerge_lst_file,"*",".nc")
#subprocess.check_call(command)
