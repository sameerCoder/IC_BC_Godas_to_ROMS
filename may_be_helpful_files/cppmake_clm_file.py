import subprocess
import os
import sys
import subprocess
import numpy as np
from datetime import datetime
import matplotlib
matplotlib.use('Agg')

import pyroms
import pyroms_toolbox

from remap_clm import remap_clm
from remap_clm_uv import remap_clm_uv
'''
lst_year = sys.argv[1:]

data_dir = '/import/AKWATERS/kshedstrom/HYCOM/Svalbard/Monthly_avg/'
dst_dir='./clm/'

lst_file = []

for year in lst_year:
    year = np.str(year)
    lst = subprocess.getoutput('ls ' + data_dir + '*GLBy*' + year + '*')
#   lst = subprocess.getoutput('ls ' + data_dir + '*GLBy*' + year + '*12.nc')
    lst = lst.split()
    lst_file = lst_file + lst

print('Build CLM file from the following file list:')
lst_file=
print(lst_file)
print(' ')

src_grd_file = 'HYCOM_GLBy0.08_vutempsaltssh_2019_001.nc'
'''


file1 = 'Godas_uvsshts_jan_2019_.nc'
dst_dir='./'

print('Build IC file from the following file:')
#print(file1)
print(' ')

#src_grd = pyroms_toolbox.BGrid_SODA.get_nc_BGrid_SODA('/center/w/SODA/SODA_grid.cdf', name='SODA_2.1.6_YELLOW', xrange=(225, 275), yrange=(190, 240))


src_grd = pyroms_toolbox.Grid_HYCOM.get_nc_Grid_HYCOM2('/home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/Godas_uvsshts_jan_2019_.nc')
dst_grd = pyroms.grid.get_ROMS_grid('GODASROMS')
lst_file=['/home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/Godas_uvsshts_jan_2019_.nc']
#lst_file=lst_file.append(file1)
for file in lst_file:
# remap
    print("inside first for:",file)
   
    zeta = remap_clm(file, 'SSH', src_grd, dst_grd, dst_dir=dst_dir)
    print("zeta work done")
    print("$"*35)
    dst_grd = pyroms.grid.get_ROMS_grid('GODASROMS', zeta=zeta)
    print("DST_GRD$"*35)
    remap_clm(file, 'temp', src_grd, dst_grd, dst_dir=dst_dir)
    print("TEMP$"*35)
    remap_clm(file, 'salt', src_grd, dst_grd, dst_dir=dst_dir)
    print("remap_clmSALT$"*35)
    remap_clm_uv(file, src_grd, dst_grd, dst_dir=dst_dir)
    print("remap_clm_uv$"*35)
# merge file
    clim_file = dst_dir + file.rsplit('/')[-1][:-3] + '_clim_' + dst_grd.name + '.nc'

    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_ssh_clim_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-O', out_file, clim_file)
    print(command)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_temp_clim_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, clim_file)
    print(command)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_salt_clim_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, clim_file)
    print(command)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_u_clim_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, clim_file)
    print(command)
    subprocess.check_call(command)
    os.remove(out_file)
    out_file = dst_dir + file.rsplit('/')[-1][:-3] + '_v_clim_' + dst_grd.name + '.nc'
    command = ('ncks', '-a', '-A', out_file, clim_file)
    print(command)
    subprocess.check_call(command)
    os.remove(out_file)
    #below break line added by msa
    print("Yahoo !! work done !!!")
    break
