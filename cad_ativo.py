from cProfile import label
from email.utils import collapse_rfc2231_value
from sys import maxsize
from tkinter import *

root = Tk()
# -----------Cores do sistema--------------
col1 = "#403D3D"  # Letra PRETA (exceto letras Botoes)
col2 = "#3fb5a3"  # Letra VERDE
col3 = "#FFFFFF"  # BRANCA
col4 = '#1E90FF'  # Background Button AZUL
col5 = '#FF6347'  # Background Button VERMELHO


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_frame_1()
        root.mainloop()

    def tela(self):
        self.root.title("")
        self.root.configure(background=col3)
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.maxsize(width=1366, height=768)
        self.root.minsize(width=500, height=400)

    def frames_tela(self):

        self.frames_tit = Frame(self.root, bd=4, bg=col3)
        self.frames_tit.place(relx=0.025, rely=0.007,
                              relwidth=0.96, relheight=0.46)
        self.frames_rodape = Frame(self.root, bd=4, bg=col3)
        self.frames_rodape.place(relx=0.02, rely=0.925,
                                 relwidth=0.96, relheight=0.6)
        self.frames_1 = Frame(self.root, bd=4, bg=col3,
                              highlightbackground=col3, highlightthickness=2)
        self.frames_1.place(relx=0.02, rely=0.10,
                            relwidth=0.96, relheight=0.46)

        self.frames_2 = Frame(self.root, bd=4, bg="#F5F5F5",
                              highlightbackground="#7CC6FF", highlightthickness=2)
        self.frames_2.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.4)

    def widgets_frame_1(self):

        # Construindo os botões

        self.bt_limpar_frame1 = Button(
            self.frames_1, text="Limpar", bd=3, bg=col4, fg=col3, font=('Ivy Mode Regular', 10, 'bold'))
        self.bt_limpar_frame1.place(
            relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_buscar_frame1 = Button(
            self.frames_1, text="Buscar", bd=3, bg=col4, fg=col3, font=('Ivy Mode Regular', 10, 'bold'))
        self.bt_buscar_frame1.place(
            relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_novo_frame1 = Button(self.frames_1, text="Novo", bd=3,
                                     bg=col4, fg=col3, font=('Ivy Mode Regular', 10, 'bold'))
        self.bt_novo_frame1.place(
            relx=0.4, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_alterar_frame1 = Button(
            self.frames_1, text="Alterar", bd=3, bg=col4, fg=col3, font=('Ivy Mode Regular', 10, 'bold'))
        self.bt_alterar_frame1.place(
            relx=0.5, rely=0.1, relwidth=0.1, relheight=0.1)

        self.bt_excluir_frame1 = Button(
            self.frames_1, text="Excluir", bd=3, bg=col5, fg=col3, font=('Ivy Mode Regular', 10, 'bold'))
        self.bt_excluir_frame1.place(
            relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)

        # Construindo as Labels e Entry

        # -----------------------Cabeçalho ou Titulo----------------------------------

        self.tit_tela = Label(self.frames_tit, text="Cadastro de Ativos", bd=4, bg=col3,
                              fg=col1, font=('Ivy Mode Regular', 20))
        self.tit_tela.place(relx=0.001, rely=0.04)

        # -----------------------Codigo----------------------------------
        self.lab_cod = Label(self.frames_1, text="Codigo", bg=col3,
                             fg=col1, font=('Ivy Mode Regular', 10, 'bold'))
        self.lab_cod.place(relx=0.01, rely=0.01)

        self.lab_cod_entry = Entry(self.frames_1, bg=col3, border=3)
        self.lab_cod_entry.place(
            relx=0.01, rely=0.1, relwidth=0.08, relheight=0.1)

        # -----------------------Nome----------------------------------
        self.lab_name = Label(self.frames_1, text="Nome", bg=col3,
                              fg=col1, font=('Ivy Mode Regular', 10, 'bold'))
        self.lab_name.place(relx=0.01, rely=0.2)

        self.lab_name_entry = Entry(self.frames_1, bg=col3, border=3)
        self.lab_name_entry.place(
            relx=0.01, rely=0.28, relwidth=0.6, relheight=0.1)

        # -----------------------Contato----------------------------------
        self.lab_contato = Label(self.frames_1, text="Contato", bg=col3,
                                 fg=col1, font=('Ivy Mode Regular', 10, 'bold'))
        self.lab_contato.place(relx=0.62, rely=0.2)

        self.lab_name_entry = Entry(self.frames_1, bg=col3, border=3)
        self.lab_name_entry.place(
            relx=0.62, rely=0.28, relwidth=0.2, relheight=0.1)

        # -----------------------Logradouro----------------------------------
        self.lab_logradouro = Label(self.frames_1, text="Logradouro",
                                    bg=col3, fg=col1, font=('Ivy Mode Regular', 10, 'bold'))
        self.lab_logradouro.place(relx=0.01, rely=0.4)

        self.lab_logradouro_entry = Entry(self.frames_1, bg=col3, border=3)
        self.lab_logradouro_entry.place(
            relx=0.01, rely=0.48, relwidth=0.6, relheight=0.1)

        # ---------------------------------Numero---------------------------------------------
        self.lab_numero = Label(self.frames_1, text="Numero", bg=col3,
                                fg=col1, font=('Ivy Mode Regular', 10, 'bold'))
        self.lab_numero.place(relx=0.62, rely=0.4)

        self.lab_numero_entry = Entry(self.frames_1, bg=col3, border=3)
        self.lab_numero_entry.place(
            relx=0.62, rely=0.48, relwidth=0.2, relheight=0.1)

     # ---------------------------------C E P---------------------------------------------
        self.lab_cep = Label(self.frames_1, text="CEP", bg=col3,
                             fg=col1, font=('Ivy Mode Regular', 10, 'bold'))
        self.lab_cep.place(relx=0.01, rely=0.6)

        self.lab_cep_entry = Entry(self.frames_1, bg=col3, border=3)
        self.lab_cep_entry.place(relx=0.01, rely=0.68,
                                 relwidth=0.2, relheight=0.1)
    # ---------------------r o d a p e-----------------------------------------------------

        self.frames_rodape = Label(self.frames_rodape, text="Desenvolvido por: A A Dev - Todos os direitos reservados.", bd=4, bg=col3,
                                   fg=col4, font=('Ivy Mode Regular', 8))
        self.frames_rodape.place(relx=0.001, rely=0.06)


Application()
