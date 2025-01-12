import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from os.path import abspath,dirname
from matplotlib.pyplot import MultipleLocator
from matplotlib.pyplot import MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


plt.rcParams["font.weight"] = 'medium'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

font1 = {
    #"family":"Times New Roman",
    # 'serif':'Times New Roman',
    "weight":"medium", #['light','normal','medium','semibold','bold','heavy','black']
    "size":20,
}

pool_first = [0,0.4664,0.6297,0.6838,0.7124,0.7177,0.7438,0.7460,0.7547,0.7537,0.7566]
pool_mean = [0,0.4411,0.6196,0.6802,0.7031,0.7209,0.7242,0.7219,0.7207,0.7278,0.7289]
pool_max = [0,0.3872,0.5973,0.6640,0.6971,0.7148,0.7231,0.7254,0.7361,0.7382,0.7426]

fig = plt.figure(figsize=(8, 6))
ax1 = plt.axes()
ax1.plot(range(11),pool_first,marker='o',linestyle='--',lw=3.5,ms=10,c='red',label='First')
ax1.plot(range(11),pool_max,marker='d',linestyle=':',lw=3.5,ms=10,c='orange',label='Max')
ax1.plot(range(11),pool_mean,marker='s',linestyle='-.',lw=3.5,ms=10,c='blue',label='Mean')
ax1.tick_params(axis='x',labelsize=20)
ax1.tick_params(axis='y',labelsize=20)
ax1.set_xlabel('Epoch',fontdict=font1)
ax1.set_ylabel('F1',fontdict=font1)

axins = zoomed_inset_axes(ax1, 3, loc=10, bbox_to_anchor=(340,120))  # zoom = 6
axins.plot(range(11),pool_first,marker='o',linestyle='--',lw=3.5,ms=10,c='red',label='First')
axins.plot(range(11),pool_max,marker='d',linestyle=':',lw=3.5,ms=10,c='orange',label='Max')
axins.plot(range(11),pool_mean,marker='s',linestyle='-.',lw=3.5,ms=10,c='blue',label='Mean')

# sub region of the original image
x1, x2, y1, y2 = 6.9, 10.1, 0.71, 0.77
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
# fix the number of ticks on the inset axes
# axins.yaxis.get_major_locator().set_params()
axins.xaxis.get_major_locator().set_params()
plt.xticks(visible=False)
plt.yticks(visible=False)
# axins.grid()
# draw a bbox of the region of the inset axes in the parent axes and
# connecting lines between the bbox and the inset axes area
mark_inset(ax1, axins, loc1=2, loc2=4, fc="none", ec="0.5")

ax1.legend(loc=10,bbox_to_anchor=(0.8,0.5),framealpha=0.4,fontsize = 20)
ax1.grid() #linestyle = '--'
plt.tight_layout()  # 防止字体超出图片
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/'+'cstnet_pooling'+'.pdf',format='pdf',dpi=1000)