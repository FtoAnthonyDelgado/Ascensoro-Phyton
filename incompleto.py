# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:45:07 2021

@author: USER
"""
import tkinter as tk 
from tkinter import ttk 
import tkinter
import time 
import os 

class Elevador:
    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.geometry('800x600')
        self.frame2 =tk.Frame(self.ventana)
        ttk.Label(self.frame2, text = "Bienvenidos",  
                  background = 'green', foreground ="white",  
                  font = ("Times New Roman", 15)).grid(row = 0, column = 1)   
        # Label 1
        ttk.Label(self.frame2, text = "Ingrese el piso que desea :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25)
        #Label 2                                             
        ttk.Label(self.frame2, text = "Ingrese el nombre del visitante :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 15, padx = 20, pady = 30)
        ttk.Label(self.frame2, text= "Ingrese el piso que desee: ",
                  font =("Times New Roman",10)).grid(column = 0,
                  row=16,padx=20, pady=30)                                       
        # Creacion del combox
        self.selecionpiso = ttk.Combobox(self.frame2, width = 27) 
        self.selecionpiso['values'] = ('Piso 0',' Piso 1',' Piso 2',' Piso 3',' Piso 4',' Piso 5',' Piso 6',' Piso 7')
        self.selecionpiso.bind('<<ComboboxSelected>>',self.borrar_piso)
        self.selecionpiso.grid(column = 1, row = 5)
        ################################################################################################################################
        self.texto1=tk.StringVar()
        self.texto1=tkinter.Entry(self.frame2,font=('Arial',12),width=30,borderwidth=5,textvariable=self.texto1)
        self.texto1.place(x=200,y=120)
        ################################################################################################################################
        self.texto2=tk.StringVar()
        self.texto2=tkinter.Entry(self.frame2,font=('Arial',12),width=30,borderwidth=5,textvariable=self.texto2)
        self.texto2.bind('<Return>',self.borrar_piso2)
        self.texto2.place(x=200,y=200)
        ################################################################################################################################
        #self.b1=tkinter.Button(self.frame2,text="Registrar",command=self.Registrar)
        #self.b1.place(x=200,y=230)
        self.frame2.grid(column=0,row=80)
        self.frame = tk.Frame(self.ventana)
        #######################################################################
        self.canvas1=tkinter.Canvas(self.frame,width=600, height=400)
        #######################################################################
        # self.piso7=self.canvas1.create_rectangle(20,40,190,15,fill="red")
        self.canvas1.create_line(10,50, 200,50, fill="black")
        # ##########################################################
        # self.piso6=self.canvas1.create_rectangle(20,90,190,60,fill="red")
        self.canvas1.create_line(10,100,200,100,fill="black")
        # ##########################################################
        # self.piso5=self.canvas1.create_rectangle(20,140,190,110,fill="red")
        self.canvas1.create_line(10,150,200,150,fill="black")
        # #########################################################
        # self.piso4=self.canvas1.create_rectangle(20,190,190,160,fill="red")
        self.canvas1.create_line(10,200,200,200,fill="black")
        # #########################################################
        # self.piso3=self.canvas1.create_rectangle(20,240,190,210,fill="red")
        self.canvas1.create_line(10,250,200,250,fill="black")
        # #########################################################
        # self.piso2=self.canvas1.create_rectangle(20,290,190,260,fill="red")
        self.canvas1.create_line(10,300,200,300,fill="black")
        # #########################################################
        # self.piso1=self.canvas1.create_rectangle(20,340,190,310,fill="red")
        self.canvas1.create_line(10,350,200,350,fill="black")
        #########################################################
        self.piso0=self.canvas1.create_rectangle(20,390,190,360,fill="red")
        self.canvas1.create_line(10,400,200,400,fill="black")
        #########################################################
        self.canvas1.create_rectangle(10,10,200,400)
        self.canvas1.grid()
        self.frame.grid(column=100,row=200,rowspan=15) 
        self.ventana.mainloop()
    
    
   
          
    def borrar_piso2(self,a):
        i=0
        self.canvas1.delete(self.piso0)
        # self.canvas1.delete(self.piso1)
        # self.canvas1.delete(self.piso2)
        # self.canvas1.delete(self.piso3)
        # self.canvas1.delete(self.piso4)
        # self.canvas1.delete(self.piso5)
        # self.canvas1.delete(self.piso6)
        # self.canvas1.delete(self.piso7)
        if self.texto2.get()=='0':
            self.piso0 = self.canvas1.create_rectangle(20,390,190,360,fill="red")
            i=0
        if self.texto2.get()=='1':
            self.piso0=self.canvas1.create_rectangle(20,340,190,310,fill="red")
            i=1
        if self.texto2.get()=='2':
            self.piso0=self.canvas1.create_rectangle(20,290,190,260,fill="red")
            i=2
        if self.texto2.get()=='3':
            self.piso0=self.canvas1.create_rectangle(20,240,190,210,fill="red")
            i=3
        if self.texto2.get()=='4':
            self.piso0=self.canvas1.create_rectangle(20,190,190,160,fill="red")
            i=4
        if self.texto2.get()=='5':
            self.piso0=self.canvas1.create_rectangle(20,140,190,110,fill="red")
            i=5
        if self.texto2.get()=='6':
            self.piso0=self.canvas1.create_rectangle(20,90,190,60,fill="red")
            i=6
        if self.texto2.get()=='7':
            self.piso0=self.canvas1.create_rectangle(20,40,190,15,fill="red")
            i=7
       
           
            
            
        with open ("Registro.txt", "a")as f:
            f.write(self.texto1.get()+"\t"+"Piso: "+str(i)+"\n")
            f.write(time.strftime('%H:%M:%S')+'\n')
            f.write("Fecha: "+time.strftime('%d/%m/%y')+"\n")
            f.close()
    
        
    def borrar_piso(self,a):
        i =0
        self.canvas1.delete(self.piso0)
        # self.canvas1.delete(self.piso1)
        # self.canvas1.delete(self.piso2)
        # self.canvas1.delete(self.piso3)
        # self.canvas1.delete(self.piso4)
        # self.canvas1.delete(self.piso5)
        # self.canvas1.delete(self.piso6)
        # self.canvas1.delete(self.piso7)
        if self.selecionpiso.current()==0:
            self.piso0 = self.canvas1.create_rectangle(20,390,190,360,fill="red")
            i=0
        if self.selecionpiso.current()==1:
            self.piso0=self.canvas1.create_rectangle(20,340,190,310,fill="red")
            i=1
        if self.selecionpiso.current()==2:
            self.piso0=self.canvas1.create_rectangle(20,290,190,260,fill="red")
            i=2
        if self.selecionpiso.current()==3:
            self.piso0=self.canvas1.create_rectangle(20,240,190,210,fill="red")
            i=3
        if self.selecionpiso.current()==4:
            self.piso0=self.canvas1.create_rectangle(20,190,190,160,fill="red")
            i=4
        if self.selecionpiso.current()==5:
            self.piso0=self.canvas1.create_rectangle(20,140,190,110,fill="red")
            i=5
        if self.selecionpiso.current()==6:
            self.piso0=self.canvas1.create_rectangle(20,90,190,60,fill="red")
            i=6
        if self.selecionpiso.current()==7:
            self.piso0=self.canvas1.create_rectangle(20,40,190,15,fill="red")
            i=7
            
        
        with open ("Registro.txt", "a")as f:
            f.write(time.strftime('%H:%M:%S')+'\n')
            f.write("Fecha: "+time.strftime('%d/%m/%y')+"\n")
            f.write(self.texto1.get()+"\t"+"Piso: "+str(i)+"\n")
            f.close()
        
        
        
        
        
        
        
    
    
    
a=Elevador()
      
                
                
                
                
                
                
        
      
        
    

