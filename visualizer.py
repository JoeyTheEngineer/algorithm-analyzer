from time import time
from tkinter.ttk import Labelframe
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
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 

def correlation_finder(y,identity):
    # carry out all sorts of regression on data to find time complexity
    # return coefficient of determination
    x=[]
    options=['Logarithmic','Linear','Log-linear','Quadratic', 'Cubic', 'Exponential','Factorial']
    correctness=[]

    item=identity[0].split("_")[0]
    scope=(identity[0].split("_")[1]).split(".")[0]+"-"+(identity[0].split("_")[1]).split(".")[1]

    for i in range (0,len(identity)):
        x.append(identity[i].split("_")[3])

    #create DataFrame
    df = pd.DataFrame({
        'x': x,
        'y': y

    })

    df['y']= df['y'].apply(np.double)
    df['x']= df['x'].apply(np.double)
       
    #logarithmic
    slope, intercept, r, p, std_err = stats.linregress(np.log(df.x), df.y)
    correctness.append(np.double(r)**2)

    #linear
    slope, intercept, r, p, std_err = stats.linregress(df.x, df.y)
    correctness.append(np.double(r)**2)

    #log-linear
    slope, intercept, r, p, std_err = stats.linregress(np.log(df.x), df.y/df.x)
    correctness.append(np.double(r)**2)

    #quadratic
    slope, intercept, r, p, std_err = stats.linregress(df.x, np.sqrt(df.y))
    correctness.append(np.double(r)**2)

    #cubic
    slope, intercept, r, p, std_err = stats.linregress(df.x, np.cbrt(df.y))
    correctness.append(np.double(r)**2)

    #exponential
    slope, intercept, r, p, std_err = stats.linregress(df.x, np.log(df.y))
    correctness.append(np.double(r)**2)

    writeConclusion(identity[-1], x, y, options[np.argmax(correctness)])
   
types = ['average','best','worst']
sizes = [512, 768, 1024, 1536, 2048, 2304, 3072, 3840, 4096, 7164, 16384, 20000, 32768, 50000, 100000]
# sizes = [512, 768, 1024, 1536, 2048, 2304, 3072, 3840, 4096, 7164, 16384, 20000]

items = [f for f in listdir("data_for_analysis/")]
identity=[]
y=[]

for item in items:
    for type in types:
        for size in sizes:
            path=f"data_for_analysis/{item}/{type}/n{size}.txt"

            y.append(np.average(np.loadtxt(path, dtype=np.double)))
            identity.append(f'{item}_{type}_{size}')
        correlation_finder(y,identity)
        y=[]
        identity=[]

num_items=len(items)

stretch_factor=int(4)+int((num_items-1)*4)


# plt.rcParams["figure.figsize"] = [5, 20]
plt.rcParams["figure.autolayout"] = True
fig = Figure(figsize = (7.5,stretch_factor),dpi = 100) #x,y
# fig = Figure(dpi = 100) #x,y

# a, axs = plt.subplots(nrows=int(num_items), ncols=1, figsize=(7, 8))

if(num_items>1):
    a, axs = plt.subplots(nrows=int(num_items), ncols=1)
else:
    a, axs = plt.subplots(2)

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


        name, scope = items[i].split('_')

        if(scope.split('.')[0]==scope.split('.')[1]):
            scope=int(scope.split('.')[0])+1
        else:
            start = int(scope.split('.')[0])+1
            end = scope.split('.')[1]
            scope=f'{start}-{end}'

        axs[i].set_title(f'{name}: line {scope}')
        axs[i].plot(df.x, df.y, '-', label=f'{conclusion.split(".")[0]} ({type})')
        axs[i].set_xlabel("Input Size")
        axs[i].set_ylabel("Exucution Time")
    # axs[i].legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
    axs[i].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # axs[i].legend(bbox_to_anchor=(1.54,1), borderaxespad=0)

# plt.tight_layout()

# plt.subplots_adjust(left=0.1,
#                     bottom=0, 
#                     right=0.62, 
#                     top=0.95, 
#                     wspace=0.9, 
#                     hspace=0.45)
# plt.show()
def quit_me():
    # print('q')
    w.quit()
    w.destroy()

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

w = Tk()
w.title('Algorithm Analyzer')
w.iconbitmap('analyzer.ico')
# w.resizable(False, False)
w.geometry("950x500")

canvas=Canvas(w,bd=0, highlightthickness=0, relief='ridge', background="#ffffff")
canvas.pack(side=LEFT, fill=BOTH, expand='yes')

yscroll=tk.Scrollbar(canvas, orient='vertical', command=canvas.yview)
yscroll.pack(side=RIGHT, fill='y')

canvas.configure(yscrollcommand=yscroll.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame=Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

figcanvas = FigureCanvasTkAgg(fig, master = frame)

figcanvas.get_tk_widget().grid()

w.protocol("WM_DELETE_WINDOW", quit_me)
w.mainloop()