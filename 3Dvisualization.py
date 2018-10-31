from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import sklearn 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
job= np.asarray(pd.read_csv('job.csv'))[:,1:]
y_train= np.asarray(pd.read_csv('y_train.csv'))[:,1:].reshape(-1,)
fig = plt.figure(figsize=(10,7))
ax = Axes3D(fig)
ax.scatter(job[:, 0], job[:, 1], job[:, 2],marker='o',c=y_train)
def animate(i):
    ax.view_init(azim=i)

rot_animation = animation.FuncAnimation(fig,animate, frames=np.arange(0,362,2),interval=100)
rot_animation.save('rotation.gif', dpi=80, writer='imagemagick')