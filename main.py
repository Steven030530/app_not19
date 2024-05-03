'''
Aplicación enfocada a la administración de novedades
'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
import logging
import pandas as pd
from source.code.utils import setup_logging
from source.code.func_nov import read_base_data

#App
class App():
    '''
    Aplicativo que registra las novedades de nomina de la notaria 19
    '''
    #Constructor
    def __init__(self,root_window):
        '''
        Function constructor main page tkinter
        definition variables and constants
        '''
        self.root = root_window
        self.box_day = None
        self.box_month = None
        self.box_year = None
        setup_logging()

        # Constantes
        self.consntants = {
            'PATH': os.getcwd(),
            'YEARS':[2024,2025,2026],
            'MONTHS':['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                      'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
            'DAYS':[i+1 for i in range(31)]
        }
       
        #Varibles GUI
        self.elements_gui = {
            'image_not19':None
        }

    #Configure App
    def config_gen_w(self,root):
        self.root = root
        width_app = 700
        height_app = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        parameter_x = (screen_width/2) - (width_app/2)
        parameter_y = (screen_height/2) - (height_app/2)
        self.root.geometry('%dx%d+%d+%d' % (width_app,height_app,parameter_x,parameter_y))
        self.root.configure(background='white')
        self.root.resizable(False,False)
  
    def design_window_main(self):
        '''
        In this function have all configures for main page
        '''
        try:
            # Configure Window
            self.config_gen_w(self.root)
            self.root.title('Aplicativo de novedades')

            # Title Main
            title_main = ttk.Label(self.root,text="NOVEDADES NOMINA NOTARIA",background="white",
                                   foreground="blue",font=("Constantia",24))
            title_main.place(x=100,y=30)

            # Label Explain
            label_explain = ttk.Label(self.root,
                text=("Este aplicativo te ayudara a registrar"
                "\n las novedades de nomina de una manera más eficiente"),
                font=("Constantia",12),background="white",justify="center")
            label_explain.place(x=150,y=70)

            # Label Select
            label_select_year = ttk.Label(self.root,text="Selecciona el periodo a liquidar:",
                                          font=("Constantia",12,"bold"),background="white")
            label_select_year.place(x=220,y=140)

            # Label Select Year
            label_select_year = ttk.Label(self.root,text="Año:",
                font=("Constantia",11),background="white")
            label_select_year.place(x=120,y=210)

            # Box Year
            str_year = tk.StringVar()
            self.box_year = ttk.Combobox(self.root,state="readonly",
                textvariable=str_year,values=self.consntants['YEARS'],width=10)
            self.box_year.place(x=170,y=210)
            self.box_year.bind('<<ComboboxSelected>>')

            # Label Select Month
            label_select_month = ttk.Label(self.root,text="Mes:",
                font=("Constantia",11),background="white",)
            label_select_month.place(x=310,y=210)

            # Box Month
            str_month = tk.StringVar()
            self.box_month = ttk.Combobox(self.root,state="readonly",
                textvariable=str_month,values=self.consntants['MONTHS'],width=15)
            self.box_month.place(x=350,y=210)
            self.box_month.bind('<<ComboboxSelected>>')

             # Label Select Day
            label_select_day = ttk.Label(self.root,text="Dia:",
                font=("Constantia",11),background="white",)
            label_select_day.place(x=510,y=210)

            # Box Day
            str_day = tk.StringVar()
            self.box_day = ttk.Combobox(self.root,state="readonly",
                textvariable=str_day,values=self.consntants['DAYS'],width=10)
            self.box_day.place(x=550,y=210)
            self.box_day.bind('<<ComboboxSelected>>')


            button_message = tk.Button(self.root,text="Iniciar",
                command=self.start_app,font=('Arial',12,'bold'),
                background='darkblue',fg='white',width=20)
            button_message.place(x=260,y=290)

            logging.info('El aplicativo se inicio correctamente!!!')

        except ValueError as e:
            logging.error('No se logro inicializar la aplicación: %s', e)

    # Functions
    def start_app(self):
        '''
        In this function validate the period for start app
        '''
        try:
            is_boxes_complete = (self.box_day.get() != "") and \
                                (self.box_month.get() !="") and \
                                (self.box_year.get() != "")
            if is_boxes_complete:
                data_val = pd.read_excel(os.path.join(self.consntants['PATH'],
                    "data","BD","validacion fechas.xlsx"))
                code_date = self.box_month.get() + self.box_year.get()

                if code_date in list(data_val['ID']):
                    showinfo(title="Advertencia",message="Este periodo ya fue liquidado")
                else:
                    # try:
                    #     data_val.loc[len(data_val)] = [(self.box_month.get()+self.box_year.get()),
                    #       (self.box_day.get() + " " + self.box_month.get() + " " + self.box_year.get())]
                    #     data_val.to_excel(os.path.join(self.consntants['PATH'],
                    #         "data","BD","validacion fechas.xlsx"),index=False)
                    # except FileNotFoundError as e:
                    #     logging.error('No se encuentra el archivo %s',e)
                    
                    self.secundary_window()
                    logging.info('Capa de novedades exitoso!!!')
            else:
                showinfo(title='Advertencia',message='Debes seleccionar todas las opciones')
        except ValueError as e:
            logging.error("No se logro registrar e iniciar con las novedades: %s",e)

    def secundary_window(self):
        '''
        second page this window contain noveltys employees
        '''
        secundary_window = tk.Tk()
        secundary_window.title('Registro de novedades')
        self.config_gen_w(secundary_window)
        # Label Company
        label_comp = ttk.Label(secundary_window,text="Selecciona una empresa:",
                               font=("Constantia",11),background="white",)
        label_comp.place(x=15,y=21)
        # Box Company
        str_comp = tk.StringVar()
        self.data_company = read_base_data('BD_NOT','Empresas')
        self.box_comp = ttk.Combobox(secundary_window,
                                state='readonly',textvariable=str_comp,values=list(self.data_company['Empresa']),
                                width=50)
        self.box_comp.place(x=230,y=21)
        self.box_comp.bind('<<ComboboxSelected>>')
        
        # Label Employee
        label_emp = ttk.Label(secundary_window,text="Selecciona un colaborador:",
                                font=("Constantia",11),background="white",)
        label_emp.place(x=15,y=51)
            
        # Box Employee
        str_emp = tk.StringVar()
        self.data_emp = read_base_data('BD_NOT','BD_EmpleadosNotaria')
        filter_comp = self.box_comp.get()
        if filter_comp != "":
            cod_comp = self.data_company[self.data_company["Empresa"]==filter_comp]["Codigo"].iloc[0]
            data_emp_r = self.data_emp[self.data_emp["CODIGO_COMPANY"]==cod_comp]
            values_emp =  list(data_emp_r['EMPLEADOS'])
        else:
            values_emp= []
        self.box_emp = ttk.Combobox(secundary_window,state='normal',
                                textvariable=str_emp,values=values_emp,
                                width=50)
        self.box_emp.place(x=230,y=51)
        self.box_comp.bind("<<ComboboxSelected>>", self.update_employee_combobox)
        
        
         # Label Novelty
        label_nov = ttk.Label(secundary_window,text="Selecciona una novedad:",
                                font=("Constantia",11),background="white",)
        label_nov.place(x=15,y=81)
            
        # Box Novelty
        str_nov = tk.StringVar()
        self.data_nov = read_base_data('BD_NOT','Novedad')
        self.filter_emp = self.box_emp.get()
        if self.filter_emp != "":
            self.values_nov =  list(self.data_nov['NOVEDAD'])
        else:
            self.values_nov= []
            
        self.box_nov = ttk.Combobox(secundary_window,state='normal',
                                textvariable=str_nov,values=self.values_nov,
                                width=50)
        self.box_nov.place(x=230,y=81)
        self.box_emp.bind("<<ComboboxSelected>>", self.update_combobox_nov)
        
    def update_employee_combobox(self,event):
        selected_company = self.box_comp.get()
        if selected_company:
            company_code = self.data_company[self.data_company["Empresa"] == selected_company]["Codigo"].iloc[0]
            filtered_employees = self.data_emp[self.data_emp["CODIGO_COMPANY"] == company_code]
            self.box_emp["values"] = list(filtered_employees["EMPLEADOS"])
        else:
            self.box_emp["values"] = []
            
    def update_combobox_nov(self,event):
        selected_emp = self.box_emp.get()
        if selected_emp:
            self.box_nov["values"] = list(self.data_nov["NOVEDAD"])
        else:
            self.box_nov["values"] = []

if __name__ == '__main__':
    root = tk.Tk()
    myapp = App(root)
    myapp.design_window_main()
    root.mainloop()
