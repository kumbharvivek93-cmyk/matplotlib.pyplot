import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
labels=["vivek","ranjana","dada","teju"]
income=[2400000,1700000,1500000,30000]  # always set legend for the pie charts
colours=["blue","yellow","green","grey"]
plt.title("RANDOM",fontsize=30,color="#000000")
plt.pie(income,labels=labels,explode=[0,0,0,0],shadow=True,startangle=100,colors=colours,textprops={"fontsize":20},autopct="%1.2f%%")
plt.legend()
plt.grid(True)
plt.show()
# use the legend() always while doing with the piecharts and also look for expode list and colours list and startangle and shadows settings if needed
