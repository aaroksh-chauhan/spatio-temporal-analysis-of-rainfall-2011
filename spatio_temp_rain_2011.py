# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:41:30 2026

@author: user
"""

import xarray as xr 

data = r"C:\Users\user\Desktop\25CL05014-NMD\lab4_2feb\RFone_imd_rf_1x1_2011.nc"
ds = xr.open_dataset(data)
print(ds)

ds.data_vars
rain = ds['RAINFALL']          #REDEFINING THE RAINFALL VARIABLE
long = ds['LONGITUDE']         
lat = ds['LATITUDE']           
time = ds['TIME']    
          
'''
Q1
'''

import matplotlib.pyplot as plt 
import cartopy.crs as cc
import cartopy.feature as cf

sp1 = rain.mean(dim = 'TIME')           #TAKING THE MEAN ALONG TIME
plt.figure(figsize = (12,8))            # DEFINING THE FIGURE SIZE 
ax = plt.axes(projection = cc.Mercator()) # USING THE MERCATOR PROJECTION 
ax.gridlines(draw_labels = True)
cp = sp1.plot.contourf(transform = cc.PlateCarree(),cmap = 'Blues',levels = 180,add_colorbar = False,extend = 'both')  # DEFINING THE COLORMAP, TRANSFORM TO PLATECARREE, AND LEVELS IN COLORBAR 
ax.add_feature(cf.BORDERS)              #HIGHLIGHTING THE BORDERS
ax.add_feature(cf.COASTLINE)            #HIGHLIGHTING THE COASTLINES
ax.add_feature(cf.LAND, color = 'gray') #HIGHLIGHTING THE LAND WITH GRAY COLOR 
plt.colorbar(cp,label = "Rainfall in mm",pad = 0.06)  #CUSTOMISING COLORBAR
plt.title("Spatial map depicting rainfall in year 2011")


'''
Q2
'''

djf = [12,1,2]                 # WINTER SEASON MONTHS
mam = [3,4,5]                  # PRE MONSOON/SUMMER SEASON MONTHS
jjas = [6,7,8,9]               # MONSOON SEASON MONTHS
on = [10,11]                   # POST MONSOON SEASON MONTHS

rain_djf = rain.sel(TIME = rain['TIME.month'].isin(djf)).mean(dim = 'TIME')  #EXTRACTING THE WINTER SEASON RAINFALL DATA
rain_mam = rain.sel(TIME = rain['TIME.month'].isin(mam)).mean(dim = 'TIME')  #EXTRACTING THE PRE MONSOON SEASON RAINFALL DATA
rain_jjas = rain.sel(TIME = rain['TIME.month'].isin(jjas)).mean(dim = 'TIME')#EXTRACTING THE MONSOON SEASON RAINFALL DATA
rain_on = rain.sel(TIME = rain['TIME.month'].isin(on)).mean(dim = 'TIME')    #EXTRACTING THE POST MONSOON SEASON RAINFALL DATA


plt.figure(figsize = (18,12))
plt.suptitle("Seasonal spatial plot of Rainfall in year 2011")  # SUPER TITLE FOR THE FIGURE 

ax = plt.subplot(2,2,1 , projection = cc.Mercator())    # SUBPLOTTING THE WINTER SEASON PLOT 
cp1 = rain_djf.plot.contourf(transform = cc.PlateCarree(),cmap = 'Blues',add_colorbar = False,extend = 'both')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.LAND , color = 'gray')
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.COASTLINE)
plt.colorbar(cp1, label = 'Rainfall in mm',pad = 0.09)
plt.title('Rainfall in Winter [DJF]')

ax = plt.subplot(2,2,2 , projection = cc.Mercator())   # SUBPLOTTING THE PRE MONSOON/SUMMER SEASON PLOT 
cp2 = rain_mam.plot.contourf(transform = cc.PlateCarree(),cmap = 'Blues',add_colorbar = False,extend = 'both')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.LAND , color = 'gray')
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.COASTLINE)
plt.colorbar(cp2, label = 'Rainfall in mm',pad = 0.09)
plt.title('Rainfall in Pre Monsoon [MAM]')

ax = plt.subplot(2,2,3 , projection = cc.Mercator())    # SUBPLOTTING THE MONSOON SEASON PLOT 
cp3 = rain_jjas.plot.contourf(transform = cc.PlateCarree(),cmap = 'Blues',add_colorbar = False,extend = 'both')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.LAND , color = 'gray')
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.COASTLINE)
plt.colorbar(cp3, label = 'Rainfall in mm',pad = 0.09)
plt.title('Rainfall in Monsoon [JJAS]')

ax = plt.subplot(2,2,4 , projection = cc.Mercator())    # SUBPLOTTING THE POST MONSOON SEASON PLOT 
cp4 = rain_on.plot.contourf(transform = cc.PlateCarree(),cmap = 'Blues',add_colorbar = False,extend = 'both')
ax.gridlines(draw_labels = True)
ax.add_feature(cf.LAND , color = 'gray')
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.COASTLINE)
plt.colorbar(cp4, label = 'Rainfall in mm',pad = 0.09)
plt.title('Rainfall in Post Monsoon [ON]')


'''
Q3
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#EXTRACTING THE RAINFALL FOR CENTRAL INDIA AND TAKING THE SPATIAL MEAN FOR THE SAME FOR PLOTTING TIME SERIES
cent_ind = rain.sel(TIME = slice('2011-06-01','2011-09-30'),LATITUDE = slice(18,26),LONGITUDE = slice(70,90)).mean(dim = ('LONGITUDE','LATITUDE'))


cent_ind.plot()
xs = pd.to_datetime(['2011-06-01', '2011-06-15', '2011-07-01', '2011-07-15', '2011-08-01', '2011-08-15', '2011-09-01', '2011-09-15', '2011-09-30'])  # DEFINING THE INTERVALS IN TERMS OF DATES TAKEN 
xs2 = ['01/06', '15/06', '01/07', '15/07', '01/08', '15/08', '01/09', '15/09', '30/09']                                                              # DEFINING THE TITLE FOR THOSE INTERVALS 
plt.xticks(xs,xs2)  #PUTTING THE TICKS TOGETHER
plt.title('Time series plot of Rainfall in JJAS in year 2011')
plt.xlabel('Time')
plt.ylabel('Rainfall in mm')
plt.grid(True)
plt.show()

'''
Q4
'''

mean_rain = np.mean(cent_ind)   #CALCULATING THE MEAN VALUE OF RAINFALL FROM JJAS DATA  
anom_rain = cent_ind - mean_rain  #CALCULATING THE ANOMALY BY SUBTRACTING FROM MEAN VALUE


anom_rain.plot(label = 'Anomaly')
cent_ind.plot(label = 'Normal rain')
xs = pd.to_datetime(['2011-06-01', '2011-06-15', '2011-07-01', '2011-07-15', '2011-08-01', '2011-08-15', '2011-09-01', '2011-09-15', '2011-09-30'])
xs2 = ['01/06', '15/06', '01/07', '15/07', '01/08', '15/08', '01/09', '15/09', '30/09']
plt.xticks(xs,xs2)
plt.title('Anomaly plot of Rainfall in JJAS in year 2011')
plt.xlabel('Time')
plt.ylabel('Rainfall in mm')
plt.legend(loc = 'upper right',framealpha = 0.6,fontsize = 'small')  # DECREASING THE FONTSIZE AND TRANSPARENCY OF THE LEGEND BAR
plt.grid(True)
plt.show()
