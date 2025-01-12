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
cstnet_1 = [0,0.3584,0.5575,0.6731,0.7051,0.7308,0.7430,0.7477,0.7558,0.7518,0.7525]
cstnet_2 = [0,0.5210,0.6950,0.7400,0.7593,0.7746,0.7794,0.7935,0.7951,0.7977,0.8005]
cstnet_4 = [0,0.6244,0.7574,0.7927,0.8103,0.8090,0.8168,0.8153,0.8182,0.8212,0.8201]
cstnet_8 = [0,0.7157,0.8113,0.8099,0.8085,0.8009,0.8069,0.8075,0.8170,0.8149,0.8149]
iscx_app_1 = [0,0.1118,0.3767,0.4764,0.5581,0.5898,0.6678,0.6878,0.6816,0.6966,0.6966]
iscx_app_2 = [0,0.4310,0.5453,0.7123,0.7207,0.7176,0.6991,0.7356,0.7511,0.7176,0.7176]
iscx_app_4 = [0,0.5638,0.7296,0.7450,0.7364,0.7492,0.7708,0.7437,0.7437,0.7479,0.7515]
iscx_app_8 = [0,0.6977,0.7786,0.7813,0.8196,0.8244,0.8291,0.8099,0.8405,0.8570,0.8570]

fig = plt.figure(figsize=(8, 6))
ax1 = plt.axes()
ax1.plot(range(11),cstnet_1,marker='^',linestyle='--',lw=3.5,ms=10,c='lightskyblue',label='EA1')
ax1.plot(range(11),cstnet_2,marker='o',linestyle='--',lw=3.5,ms=10,c='cornflowerblue',label='EA2')
ax1.plot(range(11),cstnet_4,marker='s',linestyle='--',lw=3.5,ms=10,c='dodgerblue',label='EA4')
ax1.plot(range(11),cstnet_8,marker='D',linestyle='--',lw=3.5,ms=10,c='blue',label='EA8')
# ax1.set_title('')
# ax1.set_xticks(steps)
# ax1.set_yticks()
plt.axhline(0.8283,lw=3.5,color='crimson',linestyle='-',)
ax1.tick_params(axis='x',labelsize=20)
ax1.tick_params(axis='y',labelsize=20)
ax1.set_xlabel('Epoch',fontdict=font1)
ax1.set_ylabel('F1',fontdict=font1)

axins = zoomed_inset_axes(ax1, 3, loc=10, bbox_to_anchor=(340,120))  # zoom = 6
axins.plot(range(11),cstnet_1,marker='^',linestyle='--',lw=3.5,ms=10,c='lightskyblue',label='EA1')
axins.plot(range(11),cstnet_2,marker='o',linestyle='--',lw=3.5,ms=10,c='cornflowerblue',label='EA2')
axins.plot(range(11),cstnet_4,marker='s',linestyle='--',lw=3.5,ms=10,c='dodgerblue',label='EA4')
axins.plot(range(11),cstnet_8,marker='D',linestyle='--',lw=3.5,ms=10,c='blue',label='EA8')

# sub region of the original image
x1, x2, y1, y2 = 6.9, 10.1, 0.78, 0.835
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

# ax1.legend(loc='upper right',fontsize = 16)
ax1.legend(loc=10,bbox_to_anchor=(0.8,0.5),framealpha=0.4,fontsize = 20)
ax1.grid() #linestyle = '--'
plt.tight_layout()  # 防止字体超出图片
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/'+'cstnet_enhance'+'.pdf',format='pdf',dpi=1000)
