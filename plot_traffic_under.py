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

cstnet_dir_tf = [0.9976,0.9994,0.9996,0.9996,0.9996]
cstnet_loss_tf = [0.8509,0.8795,0.8880,0.8871,0.8923]
cstnet_order2_tf = [0.8182,0.8632,0.8744,0.8801,0.8837]
cstnet_mlm_tf = [0.2315,0.3130,0.4344,0.5417,0.5915,0.6366,0.6603,0.6763,0.6849,0.6885]

cicmal_dir_tf = [1.0000,1.0000,1.0000,1.0000,1.0000]
cicmal_loss_tf = [0.9877,0.9891,0.9893,0.9897,0.9901]
cicmal_order2_tf = [0.9863,0.9878,0.9890,0.9885,0.9892]
cicmal_mlm_tf = [0.2985,0.4286,0.5854,0.6427,0.6640,0.6716,0.6823,0.6879,0.6890,0.6918]

cstnet_dir_etbert = [0.9994,0.9996,0.9996,0.9994,0.9998]
cstnet_loss_etbert = [0.8290,0.8723,0.8814,0.8836,0.8862]
cstnet_order2_etbert = [0.7328,0.8245,0.8451,0.8582,0.8622]
cstnet_mlm_etbert = [0.2213, 0.2636,0.3112,0.3484,0.3815,0.4052,0.4301,0.4440,0.4541,0.4583]

cicmal_dir_etbert = [1.0000,1.0000,1.0000,1.0000,1.0000]
cicmal_loss_etbert = [0.9854,0.9868,0.9875,0.9878,0.9890]
cicmal_order2_etbert = [0.9790,0.9835,0.9862,0.9860,0.9874]
cicmal_mlm_etbert = [0.3018,0.4026,0.4718,0.5141,0.5393,0.5591,0.5765,0.5844,0.5948,0.5970]

fig = plt.figure(figsize=(8, 6))
ax1 = plt.axes()

# ax1.plot(range(6)[1:],cstnet_dir_tf,marker='o',linestyle='--',lw=3.5,ms=10,c='firebrick',label='TF-CSTNET')
# ax1.plot(range(6)[1:],cstnet_dir_etbert,marker='o',linestyle=':',lw=3.5,ms=10,c='lightcoral',label='ETBERT-CSTNET')
# ax1.plot(range(6)[1:],cicmal_dir_tf,marker='s',linestyle='--',lw=3.5,ms=10,c='blue',label='TF-CIC')
# ax1.plot(range(6)[1:],cicmal_dir_etbert,marker='s',linestyle=':',lw=3.5,ms=10,c='cornflowerblue',label='ETBERT-CIC')
# ax1.set_xticks([1,2,3,4,5])
# ax1.set_yticks([0.94,0.96,0.98,1.0])
# ax1.set_ylim(bottom=0.94,top=1.01)

# ax1.plot(range(6)[1:],cstnet_loss_tf,marker='o',linestyle='--',lw=3.5,ms=10,c='firebrick',label='TF-CSTNET')
# ax1.plot(range(6)[1:],cstnet_loss_etbert,marker='o',linestyle=':',lw=3.5,ms=10,c='lightcoral',label='ETBERT-CSTNET')
# ax1.plot(range(6)[1:],cicmal_loss_tf,marker='s',linestyle='--',lw=3.5,ms=10,c='blue',label='TF-CIC')
# ax1.plot(range(6)[1:],cicmal_loss_etbert,marker='s',linestyle=':',lw=3.5,ms=10,c='cornflowerblue',label='ETBERT-CIC')
# ax1.set_xticks([1,2,3,4,5])
# ax1.set_yticks([0.82,0.85,0.88,0.91,0.94,0.97,1.0])
# ax1.set_ylim(bottom=0.82,top=1.01)

# ax1.plot(range(6)[1:],cstnet_order2_tf,marker='o',linestyle='--',lw=3.5,ms=10,c='firebrick',label='TF-CSTNET')
# ax1.plot(range(6)[1:],cstnet_order2_etbert,marker='o',linestyle=':',lw=3.5,ms=10,c='lightcoral',label='ETBERT-CSTNET')
# ax1.plot(range(6)[1:],cicmal_order2_tf,marker='s',linestyle='--',lw=3.5,ms=10,c='blue',label='TF-CIC')
# ax1.plot(range(6)[1:],cicmal_order2_etbert,marker='s',linestyle=':',lw=3.5,ms=10,c='cornflowerblue',label='ETBERT-CIC')
# ax1.set_xticks([1,2,3,4,5])
# ax1.set_yticks([0.73,0.78,0.83,0.88,0.93,0.98])
# ax1.set_ylim(bottom=0.73,top=1.01)

ax1.plot(range(11)[1:],cstnet_mlm_tf,marker='o',linestyle='--',lw=3.5,ms=10,c='firebrick',label='TF-CSTNET')
ax1.plot(range(11)[1:],cstnet_mlm_etbert,marker='o',linestyle=':',lw=3.5,ms=10,c='lightcoral',label='ETBERT-CSTNET')
ax1.plot(range(11)[1:],cicmal_mlm_tf,marker='s',linestyle='--',lw=3.5,ms=10,c='blue',label='TF-CIC')
ax1.plot(range(11)[1:],cicmal_mlm_etbert,marker='s',linestyle=':',lw=3.5,ms=10,c='cornflowerblue',label='ETBERT-CIC')
ax1.set_xticks(range(11)[1:])
ax1.set_yticks([0.2,0.3,0.4,0.5,0.6,0.7])
ax1.set_ylim(bottom=0.2,top=0.7)

ax1.tick_params(axis='x',labelsize=20)
ax1.tick_params(axis='y',labelsize=20)
ax1.set_xlabel('Epoch',fontdict=font1)
ax1.set_ylabel('AC',fontdict=font1)
ax1.legend(loc=10,bbox_to_anchor=(0.7,0.2),framealpha=0.4,fontsize = 20)
ax1.grid() #linestyle = '--'
plt.tight_layout()  # 防止字体超出图片
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/'+'mlm'+'.pdf',format='pdf',dpi=1000)