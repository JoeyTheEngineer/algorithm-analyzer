from time import time
from fileWriter import writeConclusion
import numpy as np
import pandas as pd
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from scipy import stats

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

def correlation_finder(y,identity):
    # carry out all sorts of regression on data to find big o
    # return correlation coefficient
    x=[]
    options=['Logarithmic','Linear','Log-linear','Quadratic', 'Cubic', 'Exponential','Factorial']
    correctness=[]
    item=identity[0].split("_")[0]
    scope=(identity[0].split("_")[1]).split(".")[0]+"-"+(identity[0].split("_")[1]).split(".")[1]

    for i in range (0,len(identity)):
        x.append(identity[i].split("_")[3])

    # print(str(x)+" "+str(len(x)))
    # print(str(y)+" "+str(len(y)))

    #create DataFrame
    df = pd.DataFrame({
        'x': x,
        'y': y

    })

    df['y']= df['y'].apply(np.double)
    df['x']= df['x'].apply(np.double)
    
    # print(df.x)
    # print(df.y)
    # y: time
    # x: size
    
    #logarithmic
    slope, intercept, r, p, std_err = stats.linregress(np.log(df.x), df.y)
    correctness.append(r)

    #linear
    slope, intercept, r, p, std_err = stats.linregress(df.x, df.y)
    correctness.append(r)

    #log-linear
    slope, intercept, r, p, std_err = stats.linregress(np.log(df.x), df.y/df.x)
    correctness.append(r)

    #quadratic
    slope, intercept, r, p, std_err = stats.linregress(df.x, np.sqrt(df.y))
    correctness.append(r)

    #cubic
    slope, intercept, r, p, std_err = stats.linregress(df.x, np.cbrt(df.y))
    correctness.append(r)

    #exponential
    slope, intercept, r, p, std_err = stats.linregress(df.x, np.log(df.y))
    correctness.append(r)

    # polyline = np.linspace(0, 5, 50)

    # plt.scatter(df.x, df.y)
    # plt.show()
    # plt.scatter(2*df.x, df.y)
    # plt.show()

    # fig, axs = plt.subplots(2)
    # fig.suptitle('Vertically stacked subplots')
    # axs[0].plot(df.x, df.y)
    # axs[1].plot(df.x, df.y)

    # plt.show()
    
    # print(scope)

    #max correctness
    writeConclusion(identity[-1], x, y, options[np.argmax(correctness)])
   
types = ['average','best','worst']
# sizes = [16, 32, 128, 256, 512, 1024, 2048, 3072, 4096]
sizes = [512, 768, 1024, 1536, 2048, 2304, 3072, 3840, 4096]

# datafiles = [f for f in listdir("data_for_analysis/") if isfile(join("data_for_analysis/", f)) and f.endswith(".txt")]

#takes the name of the items detected earlier
items = [f for f in listdir("data_for_analysis/")]
identity=[]
y=[]
# for i in range (0,len(datafiles)):
# for item in items:
#     for type in types:
#         for size in sizes:
#             path=f"data_for_analysis/{item}/{type}/n{size}.txt"
#             # fin=open(path, "rt")
            
#             # data=(fin.read().splitlines())
#             # print(np.loadtxt(path, dtype=np.double))

#             # x for a size y: a time
#             y.append(np.average(np.loadtxt(path, dtype=np.double)))
#             identity.append(f'{item}_{type}_{size}')
#         correlation_finder(y,identity)
#         #before we launch the next iteration to find the next type of data, we need to reset the x and y
#         y=[]
#         identity=[]

num_items=len(items)

# plt.rcParams["figure.figsize"] = [15, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = Figure(figsize = (7,8),dpi = 100) #x,y
a, axs = plt.subplots(int(num_items))
placement=int(num_items)*100+11


#items
for i in range(0,len(items)):
    axs[i] = fig.add_subplot(placement)
    placement+=1
    
    path=f'conclusion/{items[i]}'

    #expecting 3 plots per item
    plots = [f for f in listdir(path)]
    
    #plots
    for j in range(0, len(plots)):
        x=[]
        y=[]
        type,conclusion=plots[j].split('_')
        coordinates=np.loadtxt(f'{path}/{plots[j]}', dtype=object)

        for coordinate in coordinates:
            x.append(coordinate.split('_')[0])
            y.append(float(coordinate.split('_')[1]))
        

        df = pd.DataFrame({
            'x': x,
            'y': y

        })

        df['y']= df['y'].apply(np.double)
        df['x']= df['x'].apply(np.double)

        

        axs[i].set_title(items[i])
        # polyline = np.linspace(1, 60, 81)
        axs[i].plot(df.x, df.y, '-', label=f'{conclusion.split(".")[0]} ({type})')
        
    # axs[i].legend()
    axs[i].legend(bbox_to_anchor=(1.04,1), borderaxespad=0)


def quit_me():
    print('q')
    window.quit()
    window.destroy()
def populate(frame):
    '''Put in some fake data'''
    for row in range(100):
        tk.Label(frame, text="%s" % row, width=3, borderwidth="1", 
                 relief="solid").grid(row=row, column=0)
        t="this is the second column for row %s" %row
        tk.Label(frame, text=t).grid(row=row, column=1)
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

window = Tk()
  
# setting the title 
window.title('Algorithm Analyzer')
window.iconbitmap('analyzer.ico')
# dimensions of the main window
window.geometry("950x500")
window.configure(bg='#ffffff')
  
# creating the Tkinter canvas
# containing the Matplotlib figure

canvas_more = tk.Canvas(window, bd=0, highlightthickness=0, relief='ridge',bg="#ffffff")
frame = tk.Frame(canvas_more, background="#ffffff")

#-----
canvas = FigureCanvasTkAgg(fig,frame)  
#-----

vsb = Scrollbar(window, orient="vertical", command=canvas_more.yview)
canvas_more.configure(yscrollcommand=vsb.set,background="#ffffff")

vsb.pack(side="right", fill="y")
canvas_more.pack(side="left", fill="both", expand=True)
canvas_more.create_window((5,5), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas_more=canvas_more: onFrameConfigure(canvas_more))

# populate(frame)





canvas.draw()

canvas.get_tk_widget().pack()

window.protocol("WM_DELETE_WINDOW", quit_me)
window.resizable(False, False)
window.mainloop()

# plt.show() 

