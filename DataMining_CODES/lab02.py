import anaconda
import matplotlib
import matplotlib .pyplot as plt
import numpy as np

matplotlib .rc('xtick', labelsize =30)
matplotlib .rc('ytick', labelsize =30)
matplotlib .rc('axes', titlesize =30)
matplotlib .rc('legend' , fontsize =30)

#a=[1,3,2,4,6]
#plt.plot(a)
#plt.show()

fig = plt.figure(figsize=(10,10))
fig.subplots_adjust(hspace=.5)

axes = plt.subplot (1,1, 1)
#axes = plt.subplot (511) 
x=np.linspace(0,10,100)
y=np.sin(x)
axes.plot(x,y, linewidth =4.0 , ls='--', color='b', marker="o")
axes.legend("cos(x)",loc="upper right")
axes.set_title ("Title for (2 ,1) subplot")
axes.set_xlabel ('X')
axes.set_ylabel ('sin(X)')

axes.set_autoscaley_on(False)
axes.set_ylim([0 ,1])
axes.xaxis.set(ticks=range(0 ,10))
axes.yaxis.set(ticks=range(-1 ,2))

plt.savefig('cosine.png', dpi =400 , bbox_inches ='tight')


plt.show()