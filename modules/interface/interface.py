from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from  modules.file_gen.creator import creator
import os

def printer(name, str_out):
    try:
        fout = open("output/"+ str(name), "w")
    except:
        os.mkdir("output")
        fout = open("output/"+ str(name), "w")
    print(str_out, file = fout)
    print("--------------------------------------\nfiles created\n--------------------------------------\n\n")

def start_create(name, sections, x235):
    input_par = []
    input_par.append(name)
    input_par.append(int(sections))
    for i in x235.split():
        input_par.append(float(i))
    printer(name, creator(input_par))
    pass



def create_input():
    window = Tk()
    window.title("Создание входного файла")
    window.geometry("800x500")

    name_label = ttk.Label(window, text = "введите имя файла")
    name_label.grid(column = 1, row = 1, ipadx=6, ipady=6, padx=4, pady=4)


    name_input = ttk.Entry(window)
    name_input.grid(column = 2, row = 1, ipadx=6, ipady=6, padx=4, pady=4)
    


    sections_label = ttk.Label(window, text = "введите число секций по высоте")
    sections_label.grid(column = 1, row = 2, ipadx=6, ipady=6, padx=4, pady=4)

    sections_input = ttk.Entry(window)
    sections_input.grid(column = 2, row = 2, ipadx=6, ipady=6, padx=4, pady=4)



    x235_label = ttk.Label(window, text = "введите обогащение секций по высоте")
    x235_label.grid(column = 1, row = 3, ipadx=6, ipady=6, padx=4, pady=4)

    
    x235_input = ScrolledText(window, width=50,  height=10)
    x235_input.grid(column = 2, row = 3, ipadx=6, ipady=6, padx=4, pady=4)

    
    
    button_input = ttk.Button(
        window, text = "Создать входной файл", 
        command = lambda: start_create(
            name_input.get(),
            sections_input.get(),
            x235_input.get(1.0,END)
        )
        )
    button_input.grid(column = 2, row = 4, ipadx=6, ipady=6, padx=4, pady=4)

#Для работы скрипта должны быть установлены пакеты matplotlib и serpentTools
from matplotlib import pyplot as plt
import serpentTools
import numpy as np



def graph_generate():
    name_file = filedialog.askopenfile()
    #Здесь указать путь к файлу детектора. Если лежит в одной папке со скриптом, то просто его имя
    detFilePath = name_file
    detFile = serpentTools.read(detFilePath)

    #Здесь настроить цвета и названия
    #Имена детекторов - в порядке появления во входном файле!

    DetNames = ['fiss']
    DetColors = ['blue']
    DetLabels = [name_file]

    fig, Axes = plt.subplots()

    K = len(DetNames)

    #DetCyl,RGrid,RInner,Router,DetTal,DetErr = [0],[0],[0],[0],[0],[0]

    for h in range(K):
        DetCyl = detFile.detectors[DetNames[h]]
        RGrid = DetCyl.grids['Z'][:,2]
        RInner = DetCyl.grids['Z'][:,0]
        ROuter = DetCyl.grids['Z'][:,1]
        DetTal = DetCyl.tallies
        DetErr = DetCyl.errors

        DetSum = sum(DetTal)
        DetLen = len(DetTal)
        DetAvg = DetSum / DetLen
        data_graph = [ i / DetAvg for i in DetTal]

        Axes.errorbar(data_graph,
                        RGrid,
                        None,
                        data_graph*3*DetErr, 
                        color=DetColors[h],
                        marker='o',
                        markersize = 0.75,
                        markeredgecolor='cyan',
                        markerfacecolor='cyan',
                        ecolor="magenta",
                        #c='black',
                        label=DetLabels[h]
                        )

    #Здесь настроить основные линии сетки
    Axes.grid(visible=True, which='major', axis='both', color='0.3', linestyle='-', linewidth=0.5)

    #Здесь настроить вспомогательные линии сетки
    Axes.grid(visible=True, which='minor', axis='x', color='0.3', linestyle='-', linewidth=0.5)

    #Здесь настроить пределы и подписи осей, логарифмические или нет
    Axes.set(xlabel='ed',
                ylabel = 'Высота, см',
                xscale='linear',
                yscale='linear',
                ylim=(min(RGrid),
                max(RGrid))
                )

    #Размещаем легенду
    Axes.legend(loc='best')

    #Сохраняем файл, можно настроить имя, формат и разрешение

    plt.savefig(name_file.replace(".m", ".png"), dpi=300, facecolor='w', edgecolor='k',orientation='portrait',
                format='png', transparent=True, bbox_inches=None, pad_inches=0.1, metadata=None)

    #Выводим график в окно
    #plt.show()



def interface():
    root = Tk()
    root.title('serpentarium') 
    root.geometry("400x100")

    label_button_input_file = StringVar()
    label_button_input_file.set("Создать входной файл")
    button_input = ttk.Button(textvariable = label_button_input_file, command = create_input)
    button_input.grid(column = 1, row = 1)

    label_button_output_file = StringVar()
    label_button_output_file.set("Построить графики")
    button_graphs = ttk.Button(textvariable = label_button_output_file, command = graph_generate)
    button_graphs.grid(column = 2, row =1)

    root.mainloop()




    return True
