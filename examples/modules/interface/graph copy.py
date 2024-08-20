#Для работы скрипта должны быть установлены пакеты matplotlib и serpentTools
from matplotlib import pyplot as plt
import serpentTools
import numpy as np
def graph_generate():
#Здесь указать путь к файлу детектора. Если лежит в одной папке со скриптом, то просто его имя
name_format = 'testburn_det{i}.m'
name_out = "Profil_{i}.png"
name_graph = 'Энерговыделение {i} шага'
for i in range(8):
    detFilePath = name_format.format(i = i)
    detFile = serpentTools.read(detFilePath)

    #Здесь настроить цвета и названия
    #Имена детекторов - в порядке появления во входном файле!

    DetNames = ['fiss']
    DetColors = ['blue']
    DetLabels = [name_graph.format(i=i)]

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

        DetMax = max(DetTal)
        raw_data = [ i / DetMax for i in DetTal]

        Axes.errorbar(DetTal,
                      RGrid,
                      None,
                      DetTal*3*DetErr, 
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
    
    plt.savefig(name_out.format(i = i), dpi=300, facecolor='w', edgecolor='k',orientation='portrait',
                format='png', transparent=True, bbox_inches=None, pad_inches=0.1, metadata=None)

    #Выводим график в окно
    #plt.show()



