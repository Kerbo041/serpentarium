from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import os
#Для работы скрипта должны быть установлены пакеты matplotlib и serpentTools
from matplotlib import pyplot as plt
import serpentTools
import numpy as np
import re
files = []

def get_file():
    files.append(str(filedialog.askopenfile().name))
def get_files():
    root = filedialog.askdirectory()
    for roots, dirs, file_names in os.walk(root):
        for file in file_names:
            if re.search(r'det\d\.m',file):
                files.append(root+"/"+file)
    
    
def delete_files():
    files.clear()

def graph_generate():
    print(files)
    for name_file in files:
        detFilePath = name_file
        detFile = serpentTools.read(detFilePath, "det")
        DetNames = detFile.detectors.keys()

        for detname in DetNames:
            DetLabels = [(str(name_file).split('/')[-1]+" " + detname)]
            fig, Axes = plt.subplots()
            DetCyl = detFile.detectors[detname]
            RGrid = DetCyl.grids['Z'][:,2]
            RInner = DetCyl.grids['Z'][:,0]
            ROuter = DetCyl.grids['Z'][:,1]
            DetTal = DetCyl.tallies
            DetErr = DetCyl.errors

            DetSum = sum(DetTal)
            DetLen = len(DetTal)
            DetAvg = DetSum / DetLen
            data_graph = [ i / DetAvg for i in DetTal]
            data_errors = [data_graph[i] * 3 * DetErr[i] for i in range(len(data_graph))]
            Axes.errorbar(data_graph,
                        RGrid,
                        None,
                        data_errors, 
                        color='blue',
                        marker='o',
                        markersize = 0.75,
                        markeredgecolor='cyan',
                        markerfacecolor='cyan',
                        ecolor="magenta",
                          label = detname
                        )

            Axes.grid(visible=True, which='major', axis='both', color='0.3', linestyle='-', linewidth=0.5)
            Axes.grid(visible=True, which='minor', axis='x', color='0.3', linestyle='-', linewidth=0.5)
            Axes.set(xlabel='Энерговыделение, отн.ед.',
                ylabel = 'Высота, см',
                xscale='linear',
                yscale='linear',
                ylim=(min(RGrid),
                max(RGrid))
                )

            #Размещаем легенду
            Axes.legend(loc='best')

            #Сохраняем файл, можно настроить имя, формат и разрешение

            plt.savefig(name_file.replace(".m", ("_" + detname + ".png") ), dpi=300, facecolor='w', edgecolor='k',orientation='portrait',
                format='png', transparent=True, bbox_inches=None, pad_inches=0.1, metadata=None)
        



def interface():
    root = Tk()
    root.title('serpentarium') 
    root.geometry("600x100")
    
    label_delete = StringVar()
    label_delete.set("очистить выбор файлов")
    button_delete = ttk.Button(textvariable = label_delete, command = delete_files)
    button_delete.grid(column = 1, row = 2)

    label_get_file = StringVar()
    label_get_file.set("выбрать файл")
    button_file = ttk.Button(textvariable = label_get_file, command = get_file)
    button_file.grid(column = 1, row =1)
    
    label_get_root = StringVar()
    label_get_root.set("выбрать папку")
    button_root = ttk.Button(textvariable = label_get_root, command = get_files)
    button_root.grid(column = 2, row =1)
    
    label_graph = StringVar()
    label_graph.set("Построить графики")
    button_graphs = ttk.Button(textvariable = label_graph, command = graph_generate)
    button_graphs.grid(column = 2, row =2)
    
    root.mainloop()

def main():
    interface()
   
if __name__ == "__main__":
    main()
