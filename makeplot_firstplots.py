
import matplotlib.pyplot as plt

import iris
import iris.plot as iplt
import iris.time as irt
import datetime as dt

fileroot = '/data/users/joshonk/data/u-bu745/'
filename = '20110930T0000Z_100m.pp0'

constr = iris.Constraint(name="surface_temperature")
T2m_cube = iris.load_cube(fileroot+filename, constr)

def nearval(cell):
    return 1.4445 < cell < 1.4450

T2m_latslice = T2m_cube.extract(iris.Constraint(grid_longitude=nearval))

T2m_cube_06 = T2m_cube.extract(iris.Constraint(time=dt.datetime(2011,9,30,6,0,0))))
T2m_cube_12 = T2m_cube.extract(iris.Constraint(time=dt.datetime(2011,9,30,12,0,0))))


# Create a time series at the middle of the grid.

T2m_timepoint = T2m_cube[:,400,400]

iplt.plot(T2m_timepoint)
plt.title('Temperature at point 400, 400')
plt.xlabel('time of day')
plt.ylabel('temperature / K')
plt.grid(True)
plt.show()

# Create stacked time series from points diagonally across the grid.

for ipt in range(100,800,100):
    iplt.plot(T2m_cube[:,ipt,ipt], label=ipt)

plt.title('Temperature at points (n, n) -- see legend for "n"')
plt.xlabel('time of day')
plt.ylabel('temperature / K')
plt.grid(True)
plt.legend()
plt.show()


# Create a pair of filled contour plots for 06:00 and 12:00.

plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
iplt.contourf(T2m_cube_06, np.arange(282,291,1), vmin=282, vmax=290)
plt.title('Temperature at 06:00')
plt.xlabel('longitude') 
plt.ylabel('latitude')
plt.xticks(np.arange(1.2,1.8,0.1))
plt.yticks(np.arange(-1.3,0.6,0.1))
plt.xlim(1.2,1.8)
plt.ylim(-1.3,-0.6) 
plt.colorbar(ticks=np.arange(282,291,1), label='temperature / K')

plt.subplot(1,2,2)
iplt.contourf(T2m_cube_12, np.arange(287,305,1), vmin=287, vmax=305)
plt.title('Temperature at 12:00')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.xticks(np.arange(1.2,1.8,0.1))
plt.yticks(np.arange(-1.3,0.6,0.1))
plt.xlim(1.2,1.8)
plt.ylim(-1.3,-0.6) 
plt.colorbar(ticks=np.arange(282,291,1), label='temperature / K')

plt.show()
