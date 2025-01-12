import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from os.path import abspath,dirname
from matplotlib.pyplot import MultipleLocator
from matplotlib.pyplot import MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import seaborn as sns
from matplotlib.colors import LogNorm
import matplotlib.colors as colors

plt.rcParams["font.weight"] = 'medium'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

font1 = {
    #"family":"Times New Roman",
    # 'serif':'Times New Roman',
    "weight":"medium", #['light','normal','medium','semibold','bold','heavy','black']
    "size":20,
}

def sort_by_abs(array):
    # 计算数组的绝对值
    abs_array = np.abs(array)
    # 获取数组的长度
    n = len(array)
    # 创建一个空的列表，用来存储排序后的结果
    result = []
    # 循环 n 次，每次找出绝对值最大的元素及其位置，并添加到结果列表中，然后从数组中删除该元素
    for i in range(n):
        # 找出绝对值最大的元素及其位置
        max_value = np.max(abs_array)
        max_index = np.argmax(abs_array)
        # 将元素的值和位置以元组的形式添加到结果列表中
        result.append((array[max_index], max_index))
        # 从数组中删除该元素
        array = np.delete(array, max_index)
        abs_array = np.delete(abs_array, max_index)
    # 返回结果列表
    return result


with open("/mnt/data/zgm/ET-BERT/fine-tuning/attentions/attention_cp-ios.pkl","rb") as f:
    attentions = pickle.load(f)

#print(attentions[-1][0][0][0])
result = np.abs(attentions[-1][0,0,0,].cpu().numpy())
sorted_result = np.sort(result)
sorted_result_index = np.argsort(result)
# 输出前 10 个最大值的值和位置
print("The top 10 values and their positions are:")
for i in range(len(result))[-5:]:
    print(f"Value: {sorted_result[i]}, Position: {sorted_result_index[i]}, {result[sorted_result_index[i]]}")

fig, ax = plt.subplots(figsize=(10,8))
# 画出热力图，使用指定的颜色映射
norm = colors.Normalize(vmin=0, vmax=0.36) #按数据调节最大值
im = ax.imshow(attentions[-1][:,:6,0,].cpu().numpy().reshape(192, 320), norm=LogNorm(vmin=5e-3, vmax=0.85),cmap="binary",origin="lower") #viridis,binary
ax.set_xticks([0,64,128,196,256,320])
ax.set_xticklabels(['0', '1', '2', '3','4','5'])
ax.set_yticks([0,32,64,96,128,160,192,224,256,288,320,352,384][:7])
ax.set_yticklabels(['0', '1', '2', '3','4','5','6','7','8','9','10','11','12'][:7])
ax.tick_params(axis='x',labelsize=20)
ax.tick_params(axis='y',labelsize=20)
#plt.text(-400, 0, "Packet 5", ha="center", va="center") # 在 x=5, y=0 的位置添加文本，水平居中，垂
# 添加颜色条，显示颜色对应的数值
cbar= fig.colorbar(im, ax=ax,orientation="horizontal",pad=0.07)
plt.setp(cbar.ax.get_xticklabels(), fontsize=20)

## 上下两个图，上面是不同头同一个数据，下面是同一个头不同数据
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 3),sharex=True, gridspec_kw={"height_ratios": [3,8]})
# fig.subplots_adjust(hspace=0.01)
# # 创建一个颜色映射
# cmap = plt.get_cmap("viridis")

# # 在第一个子图上使用 ax.imshow 绘制第一个热力图，不显示颜色条
# im1 = ax1.imshow(attentions[-1][0,:,0,].cpu().numpy(), cmap=cmap, norm=colors.Normalize(vmin=0, vmax=0.85),origin="lower")

# # 在第二个子图上使用 ax.imshow 绘制第二个热力图，不显示颜色条
# im2 = ax2.imshow(attentions[-1][:,0,0,].cpu().numpy(), cmap=cmap, norm=colors.Normalize(vmin=0, vmax=0.85),origin="lower")

# # 在下边添加一个共用的颜色条
# cbar = fig.colorbar(im2, ax=[ax1, ax2], orientation="horizontal")


# 调整子图之间的间距
fig.tight_layout()
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/'+'cp-ios-atten_binary'+'.pdf',format='pdf',dpi=1000)