
import matplotlib.pyplot as plt

import iris
import iris.plot as iplt
import iris.time as irt
import datetime as dt
import numpy as np

fileroot = '/data/users/joshonk/data/u-bu745/'
filename = '20110930T0000Z_100m.nc9'

data_cubelist = iris.load(fileroot+filename)


# Create the missing time axis -- the files are messed up and Iris cannot find it.
time_start = dt.datetime(2011,9,30,5,0,0)
time_axis = [time_start + dt.timedelta(seconds=3.0*istep) for istep in range(12000)]
time_disp = np.arange(5,15,10.0/12000.0)

# Extract the zonal and meridional wind cubes.
windx_cube = data_cubelist[4]
windy_cube = data_cubelist[5]

# Extracting sites using iris.Constraint(site_number=1) does not work for some
#   reason, which is odd, as site_number is clearly one of the dimensions. So
#   let's instead convert the cube to a NumPy array.
windx = windx_cube.data
windy = windy_cube.data

# Calculate wind magnitude and direction.
for itime in range(12000):
    for isite in range(100):
        windm[itime,isite] = np.sqrt(windx[itime,isite]**2 + windy[itime,isite]**2)
        if (windy[itime,isite] > 0):
            winddir[itime,isite] = (180 / np.pi)                                 \
                                   * np.arctan(windx[itime,isite] /
                                               windy[itime,isite]) + 180
        elif ((windy[itime,isite] < 0) & (windx[itime,isite] < 0)):
            winddir[itime,isite] = (180 / np.pi)                                 \
                                   * np.arctan(windx[itime,isite] /
                                               windy[itime,isite]) + 0
        else:
            winddir[itime,isite] = (180 / np.pi)                                 \
                                   * np.arctan(windx[itime,isite] /
                                               windy[itime,isite]) + 360
        #endif
    #endfor
#endfor


# Now let's make a stacked time series of the first five sites.

plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
for isite in range(4):
  plt.plot(time_disp,windx[:,isite],label='Site #'+str(isite+1))
plt.grid(True)
plt.title('Zonal wind at five sites')
plt.xlabel('time')
plt.ylabel('zonal wind speed / m/s')

plt.subplot(1,2,2)
for isite in range(4):
  plt.plot(time_disp,windy[:,isite],label='Site #'+str(isite+1))
plt.grid(True)
plt.title('Meridional wind at five sites')
plt.xlabel('time')
plt.ylabel('meridional wind speed / m/s')
plt.legend()

plt.show()


plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
for isite in range(4):
  plt.plot(time_disp,windm[:,isite],label='Site #'+str(isite+1))
plt.grid(True)
plt.title('Wind speed at five sites')
plt.xlabel('time')
plt.ylabel('wind speed / m/s')

plt.subplot(1,2,2)
for isite in range(4):
  plt.plot(time_disp,winddir[:,isite],label='Site #'+str(isite+1))
plt.grid(True)
plt.title('Wind direction at five sites')
plt.xlabel('time')
plt.ylabel('wind direction / deg')
plt.legend()

plt.show()

#iplt.plot(T2m_timepoint)
#plt.title('Temperature at point 400, 400')
#plt.xlabel('time of day')
#plt.ylabel('temperature / K')
#plt.grid(True)
#plt.show()

# Create stacked time series from points diagonally across the grid.

#f#or ipt in range(100,800,100):
# #   iplt.plot(T2m_cube[:,ipt,ipt], label=ipt)

#plt.title('Temperature at points (n, n) -- see legend for "n"')
#plt.xlabel('time of day')
#plt.ylabel('temperature / K')
#plt.grid(True)
#plt.legend()
#plt.show()


# Create a pair of filled contour plots for 06:00 and 12:00.


#plt.subplot(1,2,1)
#iplt.contourf(T2m_cube_06, np.arange(282,291,1), vmin=282, vmax=290)
#plt.title('Temperature at 06:00')
#plt.xlabel('longitude') 
#plt.ylabel('latitude')
#plt.xticks(np.arange(1.2,1.8,0.1))
#plt.yticks(np.arange(-1.3,0.6,0.1))
#plt.xlim(1.2,1.8)
#plt.ylim(-1.3,-0.6) 
#plt.colorbar(ticks=np.arange(282,291,1), label='temperature / K')

#plt.subplot(1,2,2)
#iplt.contourf(T2m_cube_12, np.arange(287,305,1), vmin=287, vmax=305)
#plt.title('Temperature at 12:00')
#plt.xlabel('longitude')
#plt.ylabel('latitude')
#plt.xticks(np.arange(1.2,1.8,0.1))
#plt.yticks(np.arange(-1.3,0.6,0.1))
#plt.xlim(1.2,1.8)
#plt.ylim(-1.3,-0.6) 
#plt.colorbar(ticks=np.arange(282,291,1), label='temperature / K')

#plt.show()
