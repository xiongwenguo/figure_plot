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

bigram_5pac = [0,0.4587,0.6203,0.6755,0.6764,0.7177,0.7143,0.7134,0.7343,0.7342,0.7317]
gram_5pac = [0,0.4524,0.6217,0.6610,0.6973, 0.7014,0.7213,0.7289,0.7323,0.7359,0.7397]
gram_10pac= [0,0.4299,0.6233,0.6758,0.7049,0.7133,0.7222,0.7401,0.7411,0.7417,0.7419]

fig = plt.figure(figsize=(8, 6))
ax1 = plt.axes()
ax1.plot(range(11),bigram_5pac,marker='o',linestyle='--',lw=3.5,ms=10,c='red',label='Bigram_5pac')
ax1.plot(range(11),gram_5pac,marker='d',linestyle=':',lw=3.5,ms=10,c='orange',label='Gram_5pac')
ax1.plot(range(11),gram_10pac,marker='s',linestyle='-.',lw=3.5,ms=10,c='blue',label='Gram_10pac')
ax1.tick_params(axis='x',labelsize=20)
ax1.tick_params(axis='y',labelsize=20)
ax1.set_xlabel('Epoch',fontdict=font1)
ax1.set_ylabel('F1',fontdict=font1)

axins = zoomed_inset_axes(ax1, 3, loc=10, bbox_to_anchor=(340,120))  # zoom = 6
axins.plot(range(11),bigram_5pac,marker='o',linestyle='--',lw=3.5,ms=10,c='red',label='Bigram_5pac')
axins.plot(range(11),gram_5pac,marker='d',linestyle=':',lw=3.5,ms=10,c='orange',label='Gram_5pac')
axins.plot(range(11),gram_10pac,marker='s',linestyle='-.',lw=3.5,ms=10,c='blue',label='Gram_10pac')

# sub region of the original image
x1, x2, y1, y2 = 6.9, 10.1, 0.71, 0.75
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

ax1.legend(loc=10,bbox_to_anchor=(0.7,0.5),framealpha=0.4,fontsize = 20)
ax1.grid() #linestyle = '--'
plt.tight_layout()  # 防止字体超出图片
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/'+'cstnet_gram'+'.pdf',format='pdf',dpi=1000)