# Spatio-Temporal Analysis of Rainfall over India (2011)

## Overview
This project analyzes the spatial and temporal distribution of rainfall over 
India for the year 2011, using gridded IMD (India Meteorological Department) 
rainfall data, and studies how rainfall varies by season and over time during 
the monsoon.

## Objective
- Map the spatial distribution of annual rainfall over India
- Compare rainfall patterns across the four seasons (Winter, Pre-Monsoon, 
  Monsoon, Post-Monsoon)
- Track how monsoon (JJAS) rainfall changes over time for a Central India region
- Identify rainfall anomalies (deviations from the seasonal mean) during the 
  monsoon period

## Data
- **Source:** IMD (India Meteorological Department) gridded rainfall data
- **Resolution:** 1° x 1°
- **Time period:** 2011
- **Region:** India, with a focused sub-region over Central India (18–26°N, 70–90°E)

## Tools & Methods
- **Language:** Python
- **Key libraries:** xarray, numpy, pandas, matplotlib, cartopy
- **Method:** Loaded gridded NetCDF rainfall data, computed time-averaged maps 
  for the full year and for each season (DJF/MAM/JJAS/ON), extracted a Central 
  India sub-region, plotted the monsoon-season time series, and calculated the 
  anomaly by subtracting the mean rainfall from the daily values

## Results
- Produced spatial maps showing where rainfall was concentrated across India 
  in 2011, both annually and by season
- The Monsoon (JJAS) season showed the clearest seasonal signal in the seasonal 
  comparison
- The anomaly plot highlighted specific days within the monsoon where Central 
  India received notably above- or below-average rainfall compared to the 
  season's mean

## Skills Demonstrated
- Working with gridded NetCDF climate data
- Seasonal and spatial data analysis
- Time series and anomaly analysis
- Scientific visualization (spatial maps, time series) using Python

## Author
Aaroksh Chauhan — M.Sc. Atmospheric and Oceanic Sciences, IIT Bhubaneswar
