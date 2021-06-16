import xarray as xr
import xesmf

def regrid_GLBy(fld, method='nearest_s2d'):
    coords = xr.open_dataset('/home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/roms_grd_1x12.nc')
    print("c:",coords)
    coords = coords.rename({'lon_rho': 'lon', 'lat_rho': 'lat'})
    gsource = xr.open_dataset('/home/sakib/Desktop/own_download_pyroms/pyroms/examples/Arctic_HYCOM_GLBy/Godas_uvsshts_jan_2019_.nc')

    gsource=gsource.rename({'xt_ocean':'lon','yt_ocean':'lat'})
#    gsource=gsource.rename_dims({'xu_ocean':'lon'})
#    gsource=gsource.rename_vars({'xu_ocean':'lon'})
#    gsource=gsource.rename_dims({'xt_ocean':'lon'})
#    gsource=gsource.rename_vars({'xt_ocean':'lon'})
#    gsource=gsource.rename_dims({'yt_ocean':'l'})
#    gsource=gsource.rename_vars({'xt_ocean':'lon'})

#    gsource=gsource.rename_dims({'xt':'lon'})
#    gsource=gsource.rename_vars({'xt':'lon'})

    #print("lon:",gsource['lon'])


  #  gsource['longitude']=gsource['xu_ocean']
  #  gsource['longitude']=gsource['xt_ocean']
  #  gsource['longitude']=gsource['xt']
    regrid = xesmf.Regridder(
        gsource,
        coords,
        method=method,
        periodic=False,
        filename='regrid_t.nc',
        reuse_weights=True
    )
    tdest = regrid(fld)
    return tdest
