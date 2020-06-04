# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:42:25 2020

@author: handsome-linen
vib-data
Time Domain Plot for Accelerometer Data
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

healthy_accl = pd.read_csv('healthy_accl.csv')
healthy_accl_arr = np.array(healthy_accl)
time_healthy = healthy_accl_arr[:,0]*1e-9 # time in seconds
x_healthy = healthy_accl_arr[:,1]         # x column of data
y_healthy = healthy_accl_arr[:,2]         # y column of data
z_healthy = healthy_accl_arr[:,3]         # z column of data

plt.figure(0)
plt.plot(time_healthy, x_healthy)
plt.title('Time Domain (x) - healty')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.xlim(0, time_healthy[-1])

plt.figure(1)
plt.plot(time_healthy, y_healthy)
plt.title('Time Domain (y) - healty')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.xlim(0, time_healthy[-1])

plt.figure(2)
plt.plot(time_healthy, z_healthy)
plt.title('Time Domain (z) - healty')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.xlim(0, time_healthy[-1])

umbalance_accl = pd.read_csv('mass_umbalance_accl.csv')
umbalance_accl_arr = np.array(umbalance_accl)
time_umbalance = umbalance_accl_arr[:,0]*1e-9 # time in seconds
x_umbalance = umbalance_accl_arr[:,1]         # x column of data
y_umbalance = umbalance_accl_arr[:,2]         # y column of data
z_umbalance = umbalance_accl_arr[:,3]         # z column of data

plt.figure(3)
plt.plot(time_umbalance, x_umbalance)
plt.title('Time Domain (x) - mass umbalance')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.xlim(0, time_umbalance[-1])

plt.figure(4)
plt.plot(time_umbalance, y_umbalance)
plt.title('Time Domain (y) - mass umbalance')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.xlim(0, time_umbalance[-1])

plt.figure(5)
plt.plot(time_umbalance, z_umbalance)
plt.title('Time Domain (z) - mass umbalance')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.xlim(0, time_umbalance[-1])