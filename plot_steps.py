import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from os.path import abspath,dirname
from matplotlib.pyplot import MultipleLocator

plt.rcParams["font.weight"] = 'medium'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

font1 = {
    #"family":"Times New Roman",
    # 'serif':'Times New Roman',
    "weight":"medium", #['light','normal','medium','semibold','bold','heavy','black']
    "size":20,
}

steps = [0,30000,60000,90000,120000]
loss = [2.73,1.06,0.47,0.26,0.18]
loss_mlm = [11.175,7.780,2.463,1.025,0.803]
loss_sp = [1.609,0.281,0.225,0.160,0.095]
mlm_acc = [0.000,0.120,0.638,0.849,0.872]
sp_acc = [0.216,0.851,0.864,0.907,0.958]
f1_cstnet = [0.0002,0.7233,0.7812,0.7869,0.7835]
f1_cpios = [0.0003,0.0003,0.9632,0.9693,0.9771]
fig = plt.figure(figsize=(8, 6))
ax1 = plt.axes()
ax1.plot(steps,f1_cpios,marker='^',linestyle='--',lw=3.5,ms=10,c='crimson',label='F1')
# ax1.set_title('')
ax1.set_xticks(steps)
# ax1.set_yticks()
ax1.tick_params(axis='x',labelsize=16)
ax1.tick_params(axis='y',labelsize=20)
ax1.set_xlabel('Pretrain Steps',fontdict=font1)
ax1.set_ylabel('F1',fontdict=font1)
# ax1.legend(loc='upper right',fontsize = 16)
#-------
ax2 = plt.twinx()
ax2.plot(steps,loss,marker='*',linestyle='-.',lw=3.5,ms=10,c='dodgerblue',label='SUM Loss')
ax2.plot(steps,loss_mlm,marker='D',linestyle=':',lw=3.5,ms=10,c='steelblue',label='MBM Loss')
ax2.plot(steps,loss_sp,marker='o',linestyle=':',lw=3.5,ms=10,c='cornflowerblue',label='SODF Loss')
# ax2.plot(steps,mlm_acc,marker='D',linestyle=':',lw=3.5,ms=10,c='steelblue',label='MBM AC')
# ax2.plot(steps,sp_acc,marker='o',linestyle=':',lw=3.5,ms=10,c='cornflowerblue',label='SODF AC')
# 设置 ax2 的 Y 轴标签和图例位置
ax2.set_ylabel('Loss',fontdict=font1)
ax2.tick_params(axis='y',labelsize=20)
# ax2.legend(loc='upper right',fontsize = 16)
fig.legend(loc=10,bbox_to_anchor=(0.7,0.5),framealpha=0.4,fontsize = 20)
plt.grid() #linestyle = '--'
plt.tight_layout()  # 防止字体超出图片
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/'+'cpios_pretrain_steps_allloss'+'.pdf',format='pdf',dpi=1000)
