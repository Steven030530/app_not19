#Libraries
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import logging
import pandas as pd
from source.func_nov import read_base_employee
from source.utils import setup_logging
import os
#App

class App():

    #Constructor
    def __init__(self,root):
        self.root = root
        setup_logging()
        self.box_year = None
        self.box_month = None
        self.box_day = None
        self.image_not19 = None

        # Constantes
        self.PATH = os.getcwd()
        self.YEARS = [2024,2025,2026]
        self.MONTHS = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                      'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        self.DAYS = [i+1 for i in range(31)] 

    #Configure App
    def config_app_main(self):
        try:

            # Configure Window
            width_app = 700
            height_app = 400
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            parameter_x = (screen_width/2) - (width_app/2)
            parameter_y = (screen_height/2) - (height_app/2)
            self.root.geometry('%dx%d+%d+%d' % (width_app,height_app,parameter_x,parameter_y))
            self.root.title('Aplicativo de novedades')
            self.root.configure(background='white')
            self.root.resizable(False,False)

            # Title Main
            title_main = ttk.Label(self.root,text="NOVEDADES NOMINA NOTARIA",background="white",foreground="blue",font=("Constantia",24))
            title_main.place(x=100,y=30)

            # Label Explain

            label_explain = ttk.Label(self.root,text="Este aplicativo te ayudara a registrar \n las novedades de nomina de una manera más eficiente",
                                      font=("Constantia",12),background="white",justify="center")
            label_explain.place(x=150,y=70)

            # Label Select
            label_select_year = ttk.Label(self.root,text="Selecciona el periodo a liquidar:",font=("Constantia",12,"bold"),background="white")
            label_select_year.place(x=220,y=140)

            # Label Select Year
            label_select_year = ttk.Label(self.root,text="Año:",font=("Constantia",11),background="white")
            label_select_year.place(x=120,y=210)

            # Box Year
            str_year = StringVar()
            self.box_year = ttk.Combobox(self.root,state="readonly",textvariable=str_year,values=self.YEARS,width=10)
            self.box_year.place(x=170,y=210)

            # Label Select Month
            label_select_month = ttk.Label(self.root,text="Mes:",font=("Constantia",11),background="white",)
            label_select_month.place(x=310,y=210)

            # Box Month
            str_month = StringVar()
            self.box_month = ttk.Combobox(self.root,state="readonly",textvariable=str_month,values=self.MONTHS,width=15)
            self.box_month.place(x=350,y=210)

             # Label Select Day
            label_select_day = ttk.Label(self.root,text="Dia:",font=("Constantia",11),background="white",)
            label_select_day.place(x=510,y=210)

            # Box Day
            str_day = StringVar()
            self.box_day = ttk.Combobox(self.root,state="readonly",textvariable=str_day,values=self.DAYS,width=10)
            self.box_day.place(x=550,y=210)
            
            self.box_year.bind('<<ComboboxSelected>>')
            self.box_month.bind('<<ComboboxSelected>>')
            self.box_day.bind('<<ComboboxSelected>>')

            
            button_message = Button(self.root,text="Iniciar",command=self.start_app,font=('Arial',12,'bold'),
                                    background='darkblue',fg='white',width=20)
            button_message.place(x=260,y=290)

            logging.info('El aplicativo se inicio correctamente!!!')
            
        except Exception as e:
            logging.error(f'No se logro inicializar la aplicación: {e}')

    # Functions
    def start_app(self):
        try:
            if self.box_day.get() != "" and self.box_month.get() !="" and self.box_year.get() != "":

                data_val = pd.read_excel(os.path.join(self.PATH,"data","BD","validacion fechas.xlsx"))
                code_date = self.box_month.get() + self.box_year.get()
    
                if code_date in list(data_val['ID']):
                    showinfo(title="Advertencia",message="Este periodo ya fue liquidado")
                else:
                    # data_val.loc[len(data_val)] = [(self.box_month.get()+self.box_year.get()),
                    #                             (self.box_day.get() + " " + self.box_month.get() + " " + self.box_year.get())]
                    # data_val.to_excel(os.path.join(self.PATH,"data","BD","validacion fechas.xlsx"),index=False)
                    self.secundary_window()
                    logging.info('Registro exitoso!!!')
            else:
                showinfo(title='Advertencia',message='Debes seleccionar todas las opciones')
        except Exception as e:
            logging.error(f"No se logro registrar e iniciar con las novedades {e}")

    def secundary_window(self):

        secundary_window = Tk()
        secundary_window.title('Registro de novedades')
        width_app = 700
        height_app = 400
        screen_width = secundary_window.winfo_screenwidth()
        screen_height = secundary_window.winfo_screenheight()
        parameter_x = (screen_width/2) - (width_app/2)
        parameter_y = (screen_height/2) - (height_app/2)
        secundary_window.geometry('%dx%d+%d+%d' % (width_app,height_app,parameter_x,parameter_y))
        secundary_window.configure(background='white')
        self.config_w2(secundary_window)

    def config_w2(self,root2):
        if self.image_not19 is None:
            self.image_not19 = ImageTk.PhotoImage(Image.open(os.path.join(self.PATH,'static file','imgs','legal.png')))
        btn_bd_employees = ttk.Label(root2,image=self.image_not19)
        btn_bd_employees.place(x=100,y=100)

if __name__ == '__main__':
    root = Tk()
    myapp = App(root)
    myapp.config_app_main()
    root.mainloop()
    
   

    

    

    
    