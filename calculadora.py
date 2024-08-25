from tkinter import *
import customtkinter,math 

root = customtkinter.CTk()
aparencia = customtkinter.set_appearance_mode("light")

class Calculadora():
    def __init__(self):
        print("Projeto Iniciado")
        self.textoVariado = StringVar()
        self.todos_valores = ""
        self.botaoToggle = False
        self.temp_todos_valores = ""
        self.janelaMain = root
        self.janelaMain._set_appearance_mode = aparencia
        self.janelaMain.title("Maiacalc")
        self.janelaMain.geometry("250x400")
        self.favicon = PhotoImage(file="icones/logo-16x16.png")
        self.janelaMain.iconphoto(True, self.favicon)
        self.janelaMain.resizable(False, False)
        pass
     
    def update(self):
        self.textoVariado.set(0)
        self.displayCalculadora = customtkinter.CTkEntry(self.janelaMain, width=243,height=50, textvariable=self.textoVariado, state="readonly", font=customtkinter.CTkFont(family="Arial", size=20), fg_color="#f4f4f4",justify="right", bg_color="#f4f4f4")
        self.displayCalculadora.place(x=5, y=5)
        self.displayCalculadora.focus()
        self.painel_buttons_up = customtkinter.CTkFrame(self.janelaMain,width=250)
        self.painel_buttons_up.place(x=5, y=60)
       
        self.btn_porcento = customtkinter.CTkButton(self.painel_buttons_up,width=50,height=50,text="%", command=lambda:self.EntraValor("%"))
        self.btn_porcento.grid(column=0,row=0)

        self.btn_cleaner = customtkinter.CTkButton(self.painel_buttons_up,width=110,height=50,text="Cleaner", command=lambda:self.EntraValor("C"))
        self.btn_cleaner.grid(column=1,row=0, padx=5)

        self.btn_eraser = customtkinter.CTkButton(self.painel_buttons_up,width=50,height=50,text="E",command=lambda:self.EntraValor("E"))
        self.btn_eraser.grid(column=2,row=0, padx=5)

        self.btn_num_ao_quadrado = customtkinter.CTkButton(self.painel_buttons_up,width=50,height=50,text="X²", command=lambda:self.EntraValor("X"))
        self.btn_num_ao_quadrado.grid(column=0,row=1, padx=5, pady=5)

        self.btn_raiz_quadrada = customtkinter.CTkButton(self.painel_buttons_up,width=110,height=50,text="Raiz²", command=lambda:self.EntraValor("R"))
        self.btn_raiz_quadrada.grid(column=1,row=1, padx=5, pady=5)

        self.btn_dividir = customtkinter.CTkButton(self.painel_buttons_up,width=50,height=50,text="/", command=lambda:self.EntraValor("/"))
        self.btn_dividir.grid(column=2, row=1, pady=5)

        self.painel_buttons_down = customtkinter.CTkFrame(self.janelaMain,width=250, height=235)
        self.painel_buttons_down.place(x=5, y=170)       

        self.btn_7 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="7", command=lambda:self.EntraValor("7"))
        self.btn_7.grid(column=0,row=2)

        self.btn_8 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="8", command=lambda:self.EntraValor("8"))
        self.btn_8.grid(column=1,row=2,padx=5)

        self.btn_9 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="9", command=lambda:self.EntraValor("9"))
        self.btn_9.grid(column=2,row=2,padx=5)

        self.btn_multiplicar = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="*", command=lambda:self.EntraValor("*"))
        self.btn_multiplicar.grid(column=3,row=2,padx=5)

        self.btn_4 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="4", command=lambda:self.EntraValor("4"))
        self.btn_4.grid(column=0,row=3,padx=5, pady=5)

        self.btn_5 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="5", command=lambda:self.EntraValor("5"))
        self.btn_5.grid(column=1,row=3,padx=5, pady=5)

        self.btn_6 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="6", command=lambda:self.EntraValor("6"))
        self.btn_6.grid(column=2,row=3, pady=5)

        self.btn_subtrair = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="-", command=lambda:self.EntraValor("-"))
        self.btn_subtrair.grid(column=3,row=3, pady=5)

        self.btn_1 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="1", command=lambda:self.EntraValor("1"))
        self.btn_1.grid(column=0,row=4, pady=5)

        self.btn_2 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="2", command=lambda:self.EntraValor("2"))
        self.btn_2.grid(column=1,row=4, pady=5)

        self.btn_3 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="3", command=lambda:self.EntraValor("3"))
        self.btn_3.grid(column=2,row=4, pady=5)

        self.btn_somar = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="+", command=lambda:self.EntraValor("+"))
        self.btn_somar.grid(column=3,row=4, pady=5)

        self.btn_mais_ou_menos = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="+ou-", command=lambda:self.EntraValor("* -1"))
        self.btn_mais_ou_menos.grid(column=0,row=5, pady=5)
        
        self.btn_0 = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="0", command=lambda:self.EntraValor("0"))
        self.btn_0.grid(column=1,row=5, pady=5)

        self.btn_virgula = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text=",", command=lambda:self.EntraValor("."))
        self.btn_virgula.grid(column=2,row=5, pady=5)

        self.btn_igual = customtkinter.CTkButton(self.painel_buttons_down,width=50,height=50,text="=", command=lambda:self.Calcular())
        self.btn_igual.grid(column=3,row=5,pady=5)

        self.displayCalculadora.bind("<Key>", self.Teclas)
       
        self.janelaMain.mainloop()    
        pass

    def EntraValor(self,parametro):
        if parametro=="%":
            parametro="/100"
        
        if parametro=="C" or parametro=="c":
            parametro=""
            self.todos_valores = ""
            self.textoVariado.set(0)
            
        if parametro=="E" or parametro=="e":
            parametro=""
            self.todos_valores = self.todos_valores[:-1]   
            self.textoVariado.set(self.todos_valores)

        if parametro=="X" or parametro=="x":
            parametro=""
            self.todos_valores = str(math.pow(eval(self.todos_valores),2))
            self.resultado = str(eval(self.todos_valores))
            self.textoVariado.set(self.resultado)

        if parametro=="R" or parametro=="r":
            parametro=""
            self.todos_valores = str(math.sqrt(eval(self.todos_valores)))
            self.resultado = str(eval(self.todos_valores))
            self.textoVariado.set(self.resultado)

        if parametro == "* -1":
            self.botaoToggle = not self.botaoToggle
            parametro=""
            if self.botaoToggle == True:
                parametro=" * -1 "
                self.textoVariado.set(parametro[:-1])
            else:
                parametro=" * -1 "
                self.textoVariado.set(parametro[:-1])
        
                            
        self.todos_valores = self.todos_valores + parametro
        self.textoVariado.set(self.todos_valores)
        
    def Calcular(self):
        try:
      
            self.resultado = str(eval(self.todos_valores))
            self.textoVariado.set(self.resultado)
            self.temp_todos_valores = self.textoVariado.get()
            self.todos_valores[:-1]
            
            # CODIGO ABAIXO PRA NÃO TER HISTÓRICO DAS OPERAÇÕES
            #self.todos_valores = ""
            #self.textoVariado.set(0)
            #self.textoVariado.set(self.temp_todos_valores)
            #print(self.textoVariado.get())
        except:
            windows_msn = customtkinter.CTk()
            windows_msn.title("Informativo")
            windows_msn.geometry("400x100")
            lbl_msn = customtkinter.CTkLabel(windows_msn,width=400,height=100,font=customtkinter.CTkFont(family="Comic_Sans_MS_Bold",size=24,weight="bold"),fg_color="#f4f4f4", bg_color="#131313", text="Por favor, check seu cálculo")
            lbl_msn.pack()
            windows_msn.after(2000,windows_msn.destroy)
            print("Por favor, confira o cálculo")
           

    def Teclas(self,event):
        tecla_com_nomes = event.keysym
        tecla = event.char
        #print(tecla_com_nomes)
 
        if tecla_com_nomes == "Return" or tecla_com_nomes == "KP_Enter":
            self.Calcular()

        if tecla_com_nomes == "Escape":
            self.janelaMain.quit()

        if tecla_com_nomes == "BackSpace":
            self.todos_valores = self.todos_valores[:-1]   
            self.textoVariado.set(self.todos_valores)

        if tecla_com_nomes == "comma" or tecla_com_nomes == "KP_Separator":
            self.EntraValor(".")
          
        if tecla.isnumeric() or tecla.isdigit() or tecla == "/" or tecla == "*" or tecla == "-" or tecla == "+" or tecla == ".":
            self.EntraValor(tecla)
           
        if tecla=="%" or tecla=="c" or tecla=="C" or tecla=="x" or tecla=="X" or tecla=="r" or tecla=="R":
            self.EntraValor(tecla)

            if tecla == "c" or tecla == "C":
                self.textoVariado.set(0)


if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.update()


# DOCUMENTAÇÃO DE TECLAS ATALHOS Maiacalc 1.0
# tecla              [ c ]   =   clean display           =   limpa visor
# tecla              [ x ]   =   number squared          =   número ao quadrado
# tecla              [ r ]   =   square root             =   raiz quadrada = sqrt()
# tecla      [ BackSpace ]   =   delete character        =   apaga caracter
# tecla         [ Escape ]   =   exit the program        =   sai do programa
# teclas        [ Numpad ]   =   digits and operators    =   digitos e operadores
# teclas  [ Return,Enter ]   =   does the calculation    =   faz o cálculo

