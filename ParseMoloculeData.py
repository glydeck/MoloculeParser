import os
import csv
import math

import bpy
from bpy import context

#----------------------------------------------------------
#
#  Parse Molocule Data.py
#  
#
#  Created by George Lydecker on 4/27/13.
#  Copyright (c) 2013 glydeck.. GNU (Go ahead and use it.)
#
#----------------------------------------------------------



## Open the file with read only permit

f = open('/Users/glydeck/Desktop/PythonFiles/dna.txt','r')

## Read the first line 

line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty

while line:
    print (line)
    a, b, c, d, g, h, j, = line.split(",")
    
    print('Size of Atom')
    size=float(a)
    print(size)

    print('Color of Atom')
    red=float(b)
    green=float(c)
    blue=float(d)
    print("red =",red)
    print("green =",green)
    print("blue =",blue)

    print('Atom Coordinates')
    x=float(g)
    y=float(h)
    z=float(j)
    
    print(x)
    print(y)
    print(z)
    print('\n')
    
    #----------------------------------------------------------
    # Make and locate Atom
    #----------------------------------------------------------
    
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=size, view_align=False, enter_editmode=False, location=(x, y, z), rotation=(0, 0, 0))
    
    #----------------------------------------------------------
    # Make Material
    #----------------------------------------------------------
    
    mat = bpy.data.materials.new('Color01')
    mat.diffuse_color = (red,green,blue)
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = (1,1,1)
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = (1)
    mat.ambient = 1
    
    bpy.context.object.data.materials.append(mat)
    
    line = f.readline()

f.close()
