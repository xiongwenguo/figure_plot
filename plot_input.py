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
cstnet_28_64_5 = [0,0.5590,0.7047,0.7319,0.7603,0.7704,0.7786,0.7835,0.7895,0.7936,0.7902]
cstnet_28_32_10 = [0,0.5412,0.7427,0.7855,0.8035,0.8156,0.8263,0.8335,0.8333,0.8339,0.8381]
cstnet_76_64_5 = [0,0.4801,0.5654,0.5861,0.6089,0.6161,0.6059,0.6044,0.6175,0.6267,0.6311]
cstnet_76_32_10 = [0,0.5173,0.6453,0.6734,0.6676,0.6992,0.7109,0.7023,0.7083,0.7114,0.7091]
iscx_app_28_64_5 = [0,0.1046,0.4735,0.6288, 0.6531,0.6678,0.7222,0.7200,0.7394,0.7640,0.7541]
iscx_app_28_32_10 = [0,0.5099,0.4834,0.5152,0.5877,0.5985,0.5566,0.6566,0.6681,0.6894,0.6879]
iscx_app_76_64_5 = [0,0.1725,0.4940,0.6869,0.6920,0.7125,0.7229,0.8019,0.7328,0.7238,0.7154]
iscx_app_76_32_10 = [0,0.2433,0.5732,0.6527,0.7033,0.7584,0.7892,0.7928,0.8298,0.8175,0.8175]

fig = plt.figure(figsize=(8, 6))
ax1 = plt.axes()
ax1.plot(range(11),cstnet_28_64_5,marker='o',linestyle='--',lw=3.5,ms=10,c='firebrick',label='5pac, 14-78')
ax1.plot(range(11),cstnet_28_32_10,marker='o',linestyle=':',lw=3.5,ms=10,c='lightcoral',label='10pac, 14-46')
ax1.plot(range(11),cstnet_76_64_5,marker='s',linestyle='--',lw=3.5,ms=10,c='blue',label='5pac, 38-102')
ax1.plot(range(11),cstnet_76_32_10,marker='s',linestyle=':',lw=3.5,ms=10,c='cornflowerblue',label='10pac, 38-70')
# ax1.set_title('')
# ax1.set_xticks(steps)
# ax1.set_yticks()
plt.axhline(0.7835,lw=3.5,color='blueviolet',linestyle='-',)
ax1.tick_params(axis='x',labelsize=20)
ax1.tick_params(axis='y',labelsize=20)
ax1.set_xlabel('Epoch',fontdict=font1)
ax1.set_ylabel('F1',fontdict=font1)

# axins = zoomed_inset_axes(ax1, 3, loc=10, bbox_to_anchor=(340,120))  # zoom = 6
# axins.plot(range(11),iscx_app_1,marker='^',linestyle='--',lw=3.5,ms=10,c='lightskyblue',label='EA1')
# axins.plot(range(11),iscx_app_2,marker='o',linestyle='--',lw=3.5,ms=10,c='cornflowerblue',label='EA2')
# axins.plot(range(11),iscx_app_4,marker='s',linestyle='--',lw=3.5,ms=10,c='dodgerblue',label='EA4')
# axins.plot(range(11),iscx_app_8,marker='D',linestyle='--',lw=3.5,ms=10,c='blue',label='EA8')

# # sub region of the original image
# x1, x2, y1, y2 = 6.9, 10.1, 0.78, 0.835
# axins.set_xlim(x1, x2)
# axins.set_ylim(y1, y2)
# # fix the number of ticks on the inset axes
# # axins.yaxis.get_major_locator().set_params()
# axins.xaxis.get_major_locator().set_params()
# plt.xticks(visible=False)
# plt.yticks(visible=False)
# # axins.grid()
# # draw a bbox of the region of the inset axes in the parent axes and
# # connecting lines between the bbox and the inset axes area
# mark_inset(ax1, axins, loc1=2, loc2=4, fc="none", ec="0.5")

# ax1.legend(loc='upper right',fontsize = 16)
ax1.legend(loc=10,bbox_to_anchor=(0.7,0.3),framealpha=0.4,fontsize = 20)
ax1.grid() #linestyle = '--'
plt.tight_layout()  # 防止字体超出图片
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/'+'cstnet_input'+'.pdf',format='pdf',dpi=1000)
