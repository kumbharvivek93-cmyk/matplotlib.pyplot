# import matplotlib.pyplot as plt
# # print(plt.__version__)
# x=[10,20,30,40]
# y=[2,4,8,77]
# plt.plot(x,y,marker="o",markersize=15)
# plt.show()


# 2. markerface colur and other coustamization

# import matplotlib.pyplot as plt
# import numpy as np
# x=[2020,2021,2022,2023]
# y=[20,21,22,23]
# plt.plot(x,y,marker=".",markersize=15,markerfacecolor="#391bcf",markeredgecolor="#6ae30e",linestyle="None")
# plt.show()
# 2

# import matplotlib.pyplot as plt
# import numpy as np

# format=dict( marker="o",mfc="#D31895",ms=15,mec="#391bcf",linestyle="solid",linewidth=4,)


# x=np.array([2020,2021,2022,2023])
# y=np.array([3,24,222,456])
# y1=np.array([45,45,83,345])  # simpally i am just making a dictionary regardint the formating of plot and unpacking it in plot fuction  to do this i have to make a variable catching the formating values with the help of dict() function


# plt.plot(x,y,**format,color="#4aec13") # for unpacking the double underscore is used
# plt.plot(x,y1,**format,color="#d3df2d")

# plt.show()    # that is all about the plot coustomization

#  3. Labels

# import matplotlib.pyplot as plt
# x=[57,564,345,348]
# y=[4,654,456,2]
# plt.title("WAVE OF MASTER VIVEK",family="Arial",fontsize=25,fontweight="bold")
# plt.xlabel("vivek",fontsize=15,family="Arial")
# plt.ylabel("kumbhar",fontsize=15,family="Arial")

# format=dict( marker="o",mfc="#D31895",ms=15,mec="#391bcf",linestyle="solid",linewidth=4,)
# plt.plot(x,y,**format)
 
# plt.show()\

# 4.Gridlines

# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[5,10,15,20,25]
# plt.grid(linestyle="dashdot",axis="both",linewidth=3)
# plt.xticks(x)
# plt.yticks(y)
# plt.plot(x,y)
# plt.show()

# Day one rivision

# import matplotlib.pyplot as plt

# x=[2,4,6,8,10]
# y=[10,54,65,14,45]
# plt.title("RANDOM",color="#000000",fontsize=30,family="Arial")
# plt.xlabel("TYPE1",color="#000000",fontsize=25,family="Arial")
# plt.ylabel("TYPE2",color="#000000",fontsize=25,family="Arial")
# plt.plot(x,y,marker="o",ms=10,mfc="#000000",mec="#000000",linestyle="dashed",linewidth=3)
# plt.legend()
# plt.grid(axis="both",linestyle="dashed")
# plt.show()

# Day 2
# import matplotlib.pyplot as plt

# x=["carb","proteins","dairy","sweets"]
# y=[12,9,5,2]
# plt.title("DAILY INTAKE OF COLORIES",fontsize=30,color="black",fontweight="bold")
# plt.xlabel("food",fontsize=25,color="black",fontweight="bold")
# plt.ylabel("calories",fontsize=25,color="black",fontweight="bold")  # bar charts

# plt.bar(x,y,color="pink")
# plt.show()

# pie charts

# import matplotlib.pyplot as plt
# x=["carb","proteins","dairy","sweets"]
# y=[12,9,5,2]
# plt.pie(y,labels=x,autopct="%1.2f%%")
# plt.show()

# import matplotlib.pyplot as plt
# labels=["vivek","ranjana","dada","teju"]
# income=[2400000,1700000,1500000,30000]  # always set legend for the pie charts
# colours=["blue","yellow","green","grey"]
# plt.title("RANDOM",fontsize=30,color="#000000")
# plt.pie(income,labels=labels,explode=[0,0,0,0],shadow=True,startangle=100,colors=colours,textprops={"fontsize":20},autopct="%1.2f%%")
# plt.legend()
# plt.grid(True)
# plt.show()

#  Rivision day 3
# import matplotlib.pyplot as plt

# x=[5,5,56,5,54,354]
# y=[4,6,54,32,43,35]

# plt.plot(x,y,marker="o",ms=10,mfc="#D22D2D",mec="#000000",linestyle="dashdot",linewidth=2, color="#000000")
# plt.legend()
# plt.grid(linestyle="dashed",axis="y",linewidth=2)
# plt.title("RANDOM VIVEK",fontsize=30, fontweight="bold",family="Arial", color="#000000")
# plt.xlabel("vivek",fontsize=20)
# plt.ylabel("kumbhar",fontsize=20,)
# plt.xticks(x)
# plt.show()

# import matplotlib.pyplot as plt

# x=["VIVEK","OMKAR","VEDANT","TEJAS"]
# Y=[98,85,89,53]
# color=["red","pink","blue","grey"]  # barh is for the horizontal barcharts
# plt.barh(x,Y)
# plt.title("Randon",fontsize=30,fontweight="bold",color="#000000")
# plt.legend()

# plt.show()

# import matplotlib.pyplot as plt
# x=[53,63,22,35,46]
# y=["A","B","C","D","E"]
# plt.pie(x,labels=y,textprops={"fontsize":10,"fontweight":"bold"},autopct="%1.2f%%")
# plt.title("Random",fontsize=30,color="red")
# plt.legend()
# plt.grid()
# plt.show()   # for pie charts plt.legend and plt.textprops={} ... is must

# #  SCATTER GRAPHS
# import matplotlib.pyplot as plt

# x=[1,2,34,56,85]
# y=[21,54,64,75,98]
# x1=[2,3,36,58,88]
# y1=[23,59,69,81,99]  # we can also give x and y labels and also title and coustomize them 
# plt.scatter(x,y,s=200,color="red",marker="o",label="CLASS A")
# plt.scatter(x1,y1,s=200,color="blue",marker="o",label="CLASS B")
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("/home/vivek2006/Desktop/python/pandaspra.csv")
print(df.to_string())
info=df["Total"]
labels=df["Product"]
# plt.bar(labels,info,color="green")
# plt.legend()
# plt.title("VIVEKS ECOMERS",fontsize=30,color="#0F009A",fontweight="bold")
# plt.xlabel("PRODUCTS NAME",fontsize=15)
# plt.ylabel("TOTAL",fontsize=15) # this is the simple code that showing the pandas integrated with the matpotlib
# also in pie format
plt.pie(info,labels=labels,autopct="%1.2f%%",shadow=True,textprops={"fontsize":15})
plt.legend()
plt.title("VIVEKS ECOMERS",fontsize=30,color="#0F009A",fontweight="bold")


plt.show()
