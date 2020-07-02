#!/usr/bin/env python
from __future__ import print_function # python3 style print

# Simple model of pi manifold of graphene

from pythtb import * # import TB model class
import matplotlib.pyplot as plt
from PIL import Image


# define lattice vectors
lat=[[1.0,0.0],[0.5,np.sqrt(3.0)/2.0]]
# define coordinates of orbitals
orb=[[1./3.,1./3.],[2./3.,2./3.]]

# make 2D tight-binding graphene model
my_model=tb_model(2,2,lat,orb)

# set model parameters
delta1=-5
delta2=5
t00=-1.0
t01= 0.4
t11= 1.0
my_model.set_onsite([delta1,delta2])
my_model.set_hop(t01, 1, 0, [ 0, 0])
my_model.set_hop(t01, 1, 0, [ 1, 0])
my_model.set_hop(t01, 1, 0, [ 0, 1])

my_model.set_hop(t00, 0, 0, [ 0, 1])
my_model.set_hop(t00, 0, 0, [ 1, 0])
my_model.set_hop(t11, 1, 1, [ 0, 1])
my_model.set_hop(t11, 1, 1, [ 1, 0])

# print out model details
#my_model.display()

# list of k-point nodes and their labels defining the path for the
#   band structure plot
path=[[0.,0.],[2./3.,1./3.],[.5,.5],[0.,0.]]
label=(r'$\Gamma $',r'$K$', r'$M$', r'$\Gamma $')

# construct the k-path
nk=121
(k_vec,k_dist,k_node)=my_model.k_path(path,nk)

# solve for eigenvalues at each point on the path
evals=my_model.solve_all(k_vec)

# generate band structure plot
fig, ax = plt.subplots(figsize=(4.,3.))
# specify horizontal axis details
ax.set_xlim([0,k_node[-1]])
ax.set_ylim([-3.4,3.4])
ax.set_xticks(k_node)
ax.set_xticklabels(label)
# add vertical lines at node positions
for n in range(len(k_node)):
  ax.axvline(x=k_node[n],linewidth=0.5, color='k')
# put titles
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy")

# plot first and second bands
ax.plot(k_dist,evals[0],color='k')
ax.plot(k_dist,evals[1],color='k')

# save figure
fig.tight_layout()
fig.savefig("{}.png")

#make GIF
im=Image.open("{}.png")
images=[]
images.append(Image.open('{}.png'))
images.append(Image.open('{}.png'))
images.append(Image.open('{}.png'))
images.append(Image.open('{}.png'))
#the number as you want
im.save('{}.gif', save_all=True, append_images=images,loop=100,duration=0.1)