import matplotlib.pyplot as plt 

def get_loss(filename):
    steps = []
    losses = []
    with open("../logs/"+filename,"r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0]=="|":
                step = line.split("|")[1].split('/')[0].strip()
                loss = line.split("|")[4].split('    ')[1]
                steps.append(int(step))
                losses.append(float(loss))
    return steps,losses

file1 = "bs64_3GPU_bertflow_no_moe.log"
file2 = "bs64_3GPU_bertflow_nomoe_noenhance.log"
file3 = "bs64_3GPU_bertflow_nomoe_90000steps.log"
steps1,losses1 = get_loss(file1)
steps2,losses2 = get_loss(file2)
steps3,losses3 = get_loss(file3)
plt.plot(steps1[:120],losses1[:120],color = "r",label="repeat2_500000steps")
plt.plot(steps2,losses2,label="noenhance_500000steps")
plt.plot(steps3[:120],losses3[:120],label="repeat2_90000steps")
plt.legend()
plt.tight_layout()  # 防止字体超出图片
foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig('./figures/loss.pdf',format='pdf',dpi=1000)
