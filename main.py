#Libraries
from tkinter import *
from tkinter import ttk
import logging
from source.func_nov import read_bd_employee
from source.utils import setup_logging

#App

class App():

    #Constructor
    def __init__(self,root):
        self.root = root
        setup_logging()

    #Configure App
    def config_app(self):
        try:

            # Constantes

            YEARS = [2024,2025,2026]
            MONTHS = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                      'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
            DAYS = [i++1 for i in range(31)]
        
            # Configure Window
            width_app = 500
            height_app = 600
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            parameter_x = (screen_width/2) - (width_app/2)
            parameter_y = (screen_height/2) - (height_app/2)
            self.root.geometry('%dx%d+%d+%d' % (width_app,height_app,parameter_x,parameter_y))
            self.root.title('Aplicativo de novedades')
            self.root.configure(background='white')

            # Title Main
            title_main = ttk.Label(self.root,text="NOVEDADES NOMINA NOTARIA",background="white",foreground="blue",font=("Constantia",19))
            title_main.pack(padx=50,pady=30)

            # Label Explain

            label_explain = ttk.Label(self.root,text="Este aplicativo te ayudara a registrar \n las novedades de nomina de una manera más eficiente",
                                      font=("Constantia",11),background="white",justify="center")
            label_explain.pack(padx=20,pady=5)

            # Label Select Year
            label_select_year = ttk.Label(self.root,text="Selecciona un Año:",font=("Constantia",11),background="white",)
            label_select_year.pack(padx=10,pady=30)

            # Box Year
            box_year = ttk.Combobox()

            logging.info('El aplicativo se inicio correctamente!!!')

        except Exception as e:
            logging.error(f'No se logro inicializar la aplicación: {e}')

if __name__ == '__main__':
    root = Tk()
    myapp = App(root)
    myapp.config_app()
    root.mainloop()
   

    

    

    
    