from cProfile import label
from sys import maxsize
from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_frame_1()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Ativos")
        self.root.configure(background="#F5F5F5")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.maxsize(width=1366, height=768)
        self.root.minsize(width=500, height=400)

    def frames_tela(self):
        self.frames_1 = Frame(self.root, bd=4, bg="#F5F5F5",
                              highlightbackground="#C0C0C0", highlightthickness=2)
        self.frames_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frames_2 = Frame(self.root, bd=4, bg="white",
                              highlightbackground="#C0C0C0", highlightthickness=2)
        self.frames_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    def widgets_frame_1(self):
        #Construindo os botões

        self.bt_limpar_frame1 = Button(self.frames_1, text = "Limpar", bd= 3, bg= "#1E90FF",fg= "white", font= ('Regular Oblique', 10, 'bold'))
        self.bt_limpar_frame1.place(relx=0.1, rely=0.1, relwidth=0.1,relheight=0.1)
        
        self.bt_buscar_frame1 = Button(self.frames_1, text = "Buscar", bd= 3, bg= "#1E90FF",fg= "white", font= ('Regular Oblique', 10, 'bold'))
        self.bt_buscar_frame1.place(relx=0.2, rely=0.1, relwidth=0.1,relheight=0.1)

        self.bt_novo_frame1 = Button(self.frames_1, text = "Novo", bd= 3, bg= "#1E90FF",fg= "white", font= ('Regular Oblique', 10, 'bold'))
        self.bt_novo_frame1.place(relx=0.4, rely=0.1, relwidth=0.1,relheight=0.1)

        self.bt_alterar_frame1 = Button(self.frames_1, text = "Alterar", bd= 3, bg= "#1E90FF",fg= "white", font= ('Regular Oblique', 10, 'bold'))
        self.bt_alterar_frame1.place(relx=0.5, rely=0.1, relwidth=0.1,relheight=0.1)

        self.bt_excluir_frame1 = Button(self.frames_1, text = "Excluir", bd= 3, bg= "#FF6347",fg= "white", font= ('Regular Oblique', 10, 'bold'))
        self.bt_excluir_frame1.place(relx=0.6, rely=0.1, relwidth=0.1,relheight=0.1)

        # Construindo as Labels e Entry

         #-----------------------Codigo----------------------------------
        self.lab_cod = Label(self.frames_1, text = "Codigo", bg="#F5F5F5", fg="#1E90FF", font= ('Titillium Web', 10, 'bold'))
        self.lab_cod.place(relx=0.01, rely=0.01)

        self.lab_cod_entry = Entry(self.frames_1,bg="white", border=3)
        self.lab_cod_entry.place(relx=0.01, rely=0.1, relwidth=0.08,relheight=0.1)
         
         #-----------------------Nome----------------------------------
        self.lab_name = Label(self.frames_1, text= "Nome", bg="#F5F5F5", fg="#1E90FF", font= ('Titillium Web', 10, 'bold'))
        self.lab_name.place(relx=0.01, rely=0.2)
        
        self.lab_name_entry = Entry(self.frames_1,bg="white", border=3)
        self.lab_name_entry.place(relx=0.01, rely=0.28, relwidth=0.6,relheight=0.1)
         
          #-----------------------Contato----------------------------------
        self.lab_contato = Label(self.frames_1, text= "Contato", bg="#F5F5F5", fg="#1E90FF", font= ('Titillium Web', 10, 'bold'))
        self.lab_contato.place(relx=0.62, rely=0.2)
        
        self.lab_name_entry = Entry(self.frames_1,bg="white", border=3)
        self.lab_name_entry.place(relx=0.62, rely=0.28, relwidth=0.2,relheight=0.1)
         
         #-----------------------Logradouro----------------------------------
        self.lab_logradouro = Label(self.frames_1, text= "Logradouro", bg="#F5F5F5", fg="#1E90FF", font= ('Titillium Web', 10, 'bold'))
        self.lab_logradouro.place(relx=0.01, rely=0.4)
        
        self.lab_logradouro_entry = Entry(self.frames_1,bg="white", border=3)
        self.lab_logradouro_entry.place(relx=0.01, rely=0.48, relwidth=0.6,relheight=0.1)
         
         #---------------------------------Numero---------------------------------------------
        self.lab_numero = Label(self.frames_1, text= "Numero", bg="#F5F5F5", fg="#1E90FF", font= ('Titillium Web', 10, 'bold'))
        self.lab_numero.place(relx=0.62, rely=0.4)
        
        self.lab_numero_entry = Entry(self.frames_1,bg="white", border=3)
        self.lab_numero_entry.place(relx=0.62, rely=0.48, relwidth=0.2,relheight=0.1)

     #---------------------------------C E P---------------------------------------------
        self.lab_cep = Label(self.frames_1, text= "CEP", bg="#F5F5F5", fg="#1E90FF", font= ('Titillium Web', 10, 'bold'))
        self.lab_cep.place(relx=0.01, rely=0.6)
        
        self.lab_cep_entry = Entry(self.frames_1,bg="white", border=3)
        self.lab_cep_entry.place(relx=0.01, rely=0.68, relwidth=0.2,relheight=0.1)





Application()
