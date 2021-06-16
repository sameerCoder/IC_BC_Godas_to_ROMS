
from netCDF4 import num2date
for i in range(30):
    day = daily_data.isel(time=i)
    the_date = num2date(day.time.data, units='hours since 1900-01-01 00:00:00')
    day.to_netcdf(str(the_date.date())+'.nc', format='NETCDF4')
