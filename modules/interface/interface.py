from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from  modules.file_gen.creator import creator

def printer(name, str_out):
    fout = open("output/"+ str(name), "w")
    print(str_out, file = fout)
    print("--------------------------------------\nfiles created\n--------------------------------------\n\n")

def start_create(name, sections, x235):
    input_par = []
    input_par.append(name)
    input_par.append(int(sections))
    for i in x235.split():
        input_par.append(float(i))
    temp_data = creator(input_par)
    printer(name, creator(temp_data))

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

def create_output():
    window = Tk()
    window.title("построение графиков")
    window.geometry("250x200")

def interface():
    root = Tk()
    root.title('serpentarium') 
    root.geometry("250x40")

    label_button_input_file = StringVar()
    label_button_input_file.set("Создать входной файл")
    button_input = ttk.Button(textvariable = label_button_input_file, command = create_input)
    button_input.grid(column = 1, row = 1)

    label_button_output_file = StringVar()
    label_button_output_file.set("Построить графики")
    button_graphs = ttk.Button(textvariable = label_button_output_file, command = create_output)
    button_graphs.grid(column = 2, row =1)
    
    root.mainloop()




    return True
