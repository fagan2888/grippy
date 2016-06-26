#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import interpolate
import matplotlib.colors as colors
import matplotlib.pyplot as plt

def gen_cmap(clrs=["orange","darkorange","k","dodgerblue","lightblue"],
             piv=None, gam=1.0, see=False):
    """
    Generate a color map from a list of input colors.

    :param clrs: (optional)
        A list of colors for the color map.  First item on list corresponds 
        to the floor of the color map, last to the ceiling.

    :param piv: (optional)
        The pivot points for the color transitions.  Should be the same 
        length as clrs and in the range [0,1].  E.g., clrs=["r","g","b"], 
        piv=[0.0,0.8,1.0] would produce a color map with green mapped to 
        the 80% value.

    :param gam: (optional)
        The gamma factor (exponent) used to transition across the clrs.  
        This is ignored if piv is set.  gam=1.0 produces evenly spaced colors.

    :param see: (optional)
        Display the colormap (lowest value is at the bottom, highest value is
        at the top).
    """
    
    # -- utilities
    lam = np.arange(256)/255.0


    # -- set up rgb for interpolation
    rgb = zip(*[colors.colorConverter.to_rgb(clr) for clr in clrs])
    piv = piv if piv else np.linspace(0.0,1.0,len(clrs))**gam


    # -- interpolate
    r,g,b = [np.interp(lam,piv,i) for i in rgb]


    # -- generate color map
    cdict   = {"red":zip(lam,r,r),"green":zip(lam,g,g),"blue":zip(lam,b,b)}
    my_cmap = colors.LinearSegmentedColormap("dum",cdict,256)


    # -- plot if desired
    if see:
        img     = (np.arange(5000,0,-1).reshape(100,50)//50) / 5000.
        fig, ax = plt.subplots(figsize=(2.5,5))
        im      = ax.imshow(img,cmap=my_cmap,interpolation="nearest")
        ax.axis("off")
        fig.subplots_adjust(0,0,1,1)
        fig.canvas.draw()
        plt.show()

    return my_cmap
