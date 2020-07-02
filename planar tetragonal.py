# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:12:47 2020

@author: 刘毓杰
"""
from __future__ import print_function # python3 style print

from pythtb import * # import TB model class
import matplotlib.pyplot as plt
from PIL import Image

# You should change the path by yourself
# set geometry of tetragonal
a=1
lat=[[a,0.0],[0.0,a]]
orb=[[0.0,0.0],[0.5,0.5]]
my_model=tbmodel(2,2,lat,orb)

# set model
Delta1 =-5
Delta2 = 5.0
t00    = 1.0
t11    = 1.0
t10 = 0.4
my_model.set_onsite([Delta1,Delta2])
my_model.set_hop(-t00, 0, 0, [ 1, 0])
my_model.set_hop(-t00, 0, 0, [ 0, 1])
my_model.set_hop( t11, 1, 1, [ 1, 0])
my_model.set_hop( t11, 1, 1, [ 0, 1])
my_model.set_hop( t10, 1, 0, [ 1, 1])
my_model.set_hop( t10, 1, 0, [ 0, 1])
my_model.set_hop(-t10, 1, 0, [ 0, 0])
my_model.set_hop(-t10, 1, 0, [ 1, 0])
my_model.display()

# generate k-point path and labels and solve Hamiltonian
path=[[0.0,0.0],[0.0,0.5],[0.5,0.5],[0.0,0.0]]
k_lab=(r'$\Gamma $',r'$X$', r'$M$', r'$\Gamma $')
(k_vec,k_dist,k_node)=my_model.k_path(path,121)
evals=my_model.solve_all(k_vec)

# plot band structure
fig, ax = plt.subplots(figsize=(4.,3.))
ax.set_xlim([0,k_node[-1]])
ax.set_xticks(k_node)
ax.set_xticklabels(k_lab)
for n in range(len(k_node)):
  ax.axvline(x=k_node[n], linewidth=0.5, color='k')
ax.plot(k_dist,evals[0],color='k')
ax.plot(k_dist,evals[1],color='k')
#You should first save the figure to make gif
fig.savefig("{}.png")


#make GIF
im=Image.open("{}.png")
images=[]
images.append(Image.open('{}.png'))
images.append(Image.open('{}.png'))
images.append(Image.open('{}.png'))
images.append(Image.open('{}.png'))
images.append(Image.open('{}.png'))

#the number as you want
im.save('{}.gif', save_all=True, append_images=images,loop=100,duration=0.1)
