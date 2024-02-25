import customtkinter as ctk
import tkinter
import tkinter.messagebox
from tkinter.filedialog import asksaveasfilename
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
from tksheet import Sheet
from assets.dropdown import *
import mplcursors
from json import load
from webbrowser import open_new
import ctypes
from matplotlib.backend_bases import KeyEvent, MouseEvent
import keyboard
from CTkColorPicker import *
from os.path import normpath
import csv

with open('textfile.txt', 'r', encoding='utf-8') as file:
    strings_txt = load(file)

controle = []
annotations = []
scale = ctypes.windll.shcore.GetScaleFactorForDevice(0)

ctk.set_appearance_mode("light")
root = ctk.CTk()
root.iconbitmap("assets\logos\icone_programa.ico")
root.resizable(False, False)
root.geometry("1300x600+450+190")
root.title("Spectra")
fonte_icones = ctk.CTkFont(family="Segoe UI", size=17, weight='bold')
fonte_iconesnormal = ctk.CTkFont(family="Segoe UI", size=14, weight='normal')
fonte = ctk.CTkFont(family="Segoe UI", size=15, weight='bold')
fontenormal = ctk.CTkFont(family="Segoe UI", size=18)
fontegrande = ctk.CTkFont(family="Segoe UI", size=22)
fontetitulos = ctk.CTkFont(family="Segoe UI", size=40, weight='bold')

imagemlogo = ctk.CTkImage(size=[150, 60], light_image=Image.open("assets\logos\logo_nome.png"))
tabelaB = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\gtabela_b.png"))
tabelaA = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\gtabela_a.png"))
duvidasB = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\duvidas_b.png"))
duvidasA = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\duvidas_a.png"))
graficoB = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\grafico_b.png"))
graficoA = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\grafico_a.png"))
configB = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\config_b.png"))
configA = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\config_a.png"))
sairB = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\sair_b.png"))
sairA = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\sair_a.png"))
infoB = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\duvidas_b.png"))
infoA = ctk.CTkImage(size=[22, 22], light_image=Image.open("assets\duvidas_a.png"))
pdf = ctk.CTkImage(size=[25, 25], light_image=Image.open("assets\pdf.png"))
png = ctk.CTkImage(size=[25, 25], light_image=Image.open("assets\png.png"))
jpg = ctk.CTkImage(size=[25, 25], light_image=Image.open("assets\jpg.png"))
svg = ctk.CTkImage(size=[25, 25], light_image=Image.open("assets\svg.png"))


####* Cria o layout geral da interface gráfica ####
def layout(): 
    global barralateral, barralateral, botao_dados, botao_grafico, botao_info, botao_config, botao_sair, fundocinza, janela_dados, janela_grafico, janela_info
    barralateral = ctk.CTkFrame(master=root, width=200, height=600, fg_color="#2B6AD0", bg_color="#2B6AD0")
    barralateral.grid(row=0, column=0, sticky="nsew")
    barralateral.grid_propagate(False)
    fundocinza = ctk.CTkTabview(master=root, width=1129, height=600, fg_color="#E3E7F1", state="disabled", anchor="ne", bg_color="#E3E7F1", text_color="#E3E7F1", segmented_button_fg_color="#E3E7F1", segmented_button_unselected_color="#E3E7F1", segmented_button_selected_hover_color="#E3E7F1", segmented_button_unselected_hover_color="#E3E7F1", text_color_disabled="#E3E7F1", segmented_button_selected_color="#E3E7F1")
    fundocinza._outer_button_overhang = 0
    fundocinza._segmented_button.grid_forget()
    janela_dados = fundocinza.add("dados")
    janela_grafico= fundocinza.add("janela_grafico")
    janela_info = fundocinza.add("informacoes")
    fundocinza.grid(row=0, column=1, sticky="nsew")

    fundocinza.grid_propagate(False)
    
    imglogo = ctk.CTkLabel(master=barralateral, image=imagemlogo, text="")
    imglogo.grid(row=0, pady=17, padx=10, sticky="n")

    espaço = ctk.CTkLabel(barralateral, text="\n\n\n\n")
    espaço.grid(row=1)

    botao_dados = criarbotao_pLateral(barralateral, tabelaB, "Inserir dados")
    botao_dados.grid(row=2, pady=8, padx=13)
    botao_dados.configure(command= lambda: tab_switch("dados"))

    botao_grafico = criarbotao_pLateral(barralateral, graficoB, "Gráfico")
    botao_grafico.grid(row=3, pady=8, padx=13)
    botao_grafico.configure(command= lambda : tab_switch("janela_grafico"))

    botao_info = criarbotao_pLateral(barralateral, infoB, "Informações")
    botao_info.grid(row=4, pady=8, padx=13)
    botao_info.configure(command= lambda: tab_switch("informacoes"))

    botao5 = criarbotao_pLateral(barralateral, infoB, "Null")
    botao5.grid(row=5, pady=8, padx=13)
    botao5.configure(state="disabled", command= lambda: tab_switch("informacoes"))

    botao_sair = criarbotao_pLateral(barralateral, sairB, "Sair")
    botao_sair.grid(row=6)
    botao_sair.configure(command= lambda: tab_switch("sair"))

    espaço2 = ctk.CTkLabel(barralateral, text="\n\n\n\n\n")
    espaço2.grid(row=7) 

    barralateral.configure(width=180)
    botao_config = criarbotao_pLateral(barralateral, configB, "Configurações")
    botao_config.grid(row=8, pady=10)
    botao_config.configure(command= lambda: tab_switch("config"))
    tab_switch("dados")

def criarbotao_pLateral(root, icon, texto): # Cria os botões de troca de aba na barra lateral.
    botao = ctk.CTkButton(master= root, cursor='hand2', width=150, height=40, image=icon, hover_color="#FBFBFE", font= fonte_icones, fg_color="#2B6AD0", text=texto, anchor="w")
    return botao

#####* Introduz os elementos gráficos da janela de dados #####
def janeladados(): # Widgets principais (frames, botões, tabela principal)
    global botao_dados, tabela, dados_tabela, valores_apagar, resultados_medias, porcentagens, mediasresazurina
    moldura = ctk.CTkFrame(janela_dados, height=320, width=1050, fg_color="#FFFFFF", corner_radius=12)
    moldura.grid(row=3, columnspan=3, sticky="nsew", padx=30, pady=25)
    moldura.grid_propagate(False)
    tabela = Sheet(moldura, align="center", max_column_width=77, total_columns=12, total_rows=8, column_width=82, height=300, width=1010, row_height=34, show_x_scrollbar=False, show_y_scrollbar=False, empty_horizontal=0, empty_vertical=0)
    tabela.create_header_dropdown(c = 10, values=["C+", "C-"])
    tabela.create_header_dropdown(c = 11, values=["C-", "C+"])
    Sheet.set_options(tabela, table_bg="#E3E7F1", table_grid_fg="#FFFFFF", table_selected_cells_bg="#C6CAD1", index_bg="#2B6AD0", index_grid_fg="#FFFFFF", header_bg="#2B6AD0", header_grid_fg="#FFFFFF", font=('Helvetica', 10, 'normal'), table_fg='#000000', index_fg='#E3E7F1', header_fg='#E3E7F1', table_selected_cells_border_fg="#2B6AD0", table_selected_rows_border_fg ="#2B6AD0", table_selected_columns_border_fg= "#2B6AD0")
    tabela.enable_bindings("all")
    tabela.disable_bindings("right_click_popup_menu", '<MouseWheel>', "column_height_resize", "column_width_resize", "row_width_resize", "row_height_resize")
    tabela.bind("<3>", popupmenu)
    tabela.grid(row=0, column=0, sticky="nsew", padx=20, pady= 10)
    tabela.grid_propagate(False)
    frame_corantes()
    frame_meio()
    frame_opcoes()
    dados_tabela = {'sc': [],'ttc': [], 'res_570': [], 'res_600': [], 'am': []}
    valores_apagar = []
    resultados_medias = {'sc': [],'ttc': [], 'res_570': [], 'res_600': [], 'am': []}
    porcentagens = {"sc": [], "ttc": [], "res_570": [], 'res_600': [], "am": []}
    mediasresazurina = {"res": []}

## FRAME 1 ##
def frame_opcoes(): # Cria os widgets do frame de opções, relacionado à escolha da bacteria e opção do cálculo de resazurina
    global op_s_aureus, bac_var, botaoresazurina, outra_bac
    titulo_inserirdados = ctk.CTkLabel(janela_dados, text="Inserir dados", font=fontetitulos, text_color="#2B6AD0")
    titulo_inserirdados.grid(row=0, sticky="nw", padx=27)
    titulo_inserirdados.grid_rowconfigure(0, pad=10)
    frame_escolhabac= ctk.CTkFrame(janela_dados, height=120, width=260, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=16)
    frame_escolhabac.grid(rowspan=2,row=1, column=0, sticky="wse", padx=30)
    frame_escolhabac.grid_propagate(False)
    bac_var= tkinter.StringVar(value="")
    op_s_aureus= ctk.CTkRadioButton(frame_escolhabac, width=30, height=30, fg_color="#2B6AD0", border_width_checked= 6, text= "Staphylococcus aureus", font=ctk.CTkFont(family="Segoe UI", size=18), text_color="#1c1d22", command=escolha_bac, variable=bac_var, value="Staphylococcus aureus")
    op_s_aureus.place( x= 10, y= 0)
    op_e_coli= ctk.CTkRadioButton(frame_escolhabac, width=30, height=30, fg_color="#2B6AD0", border_width_checked= 6, text= "Escherichia coli", font=ctk.CTkFont(family="Segoe UI", size=18), text_color="#1c1d22", command=escolha_bac, variable=bac_var, value="Escherichia coli")
    op_e_coli.place( x= 10, y= 30)
    outra_bac = ctk.CTkRadioButton(frame_escolhabac, width=30, height=30, fg_color="#2B6AD0", border_width_checked= 6, text= "Outra bactéria", font=ctk.CTkFont(family="Segoe UI", size=18), text_color="#1c1d22", command= escolha_bac, variable=bac_var, value="Outra bacteria")
    outra_bac.place( x= 10, y= 60)
    botaoresazurina = ctk.CTkSwitch(frame_escolhabac, switch_height= 15, progress_color="#2B6AD0", switch_width=30, width=40, height=10, text="Cálculo de resazurina", font=ctk.CTkFont(family="Segoe UI", size=18), command= linhas_resazurina, onvalue="on", offvalue="off")
    botaoresazurina.place(x=7, y=90)

def escolha_bac(): # Define a bactéria escolhida no frame de opções
    global bac_escolhida, outrabac_toplevel, nome_bac, tabela_diluicoes
    bac_escolhida = ''
    if bac_var.get() == "Staphylococcus aureus":
        bac_escolhida = "Staphylococcus aureus"
    if bac_var.get() == "Escherichia coli":
        bac_escolhida = "Escherichia coli"
    if bac_var.get() == "Outra bacteria":
        try:
            if outrabac_toplevel.winfo_exists() == True:
                outrabac_toplevel.deiconify()
        except NameError:
            outra_bac.configure(state="disabled")
            outrabac_toplevel = ctk.CTkToplevel()
            outrabac_toplevel.focus()
            outrabac_toplevel.geometry("900x350+450+190")
            outrabac_toplevel.title("Configurar bactéria")
            outrabac_toplevel.resizable(False,False)
            outrabac_toplevel.after(200, outrabac_toplevel.lift)
            outrabac_toplevel.after(200, lambda: outrabac_toplevel.iconbitmap("assets\logos\icone_programa.ico"))

            # Strings / Entrada do nome da bactéria
            titulo = ctk.CTkLabel(outrabac_toplevel, text="Configurar bactéria utilizada\n――――――――――――――――――――――――――――", justify="left", font=ctk.CTkFont(family="Segoe UI", size=30), text_color="#2B6AD0").pack(anchor="w", padx=20, pady=7)
            nome_bac = ctk.CTkEntry(outrabac_toplevel, placeholder_text="Digite o nome da bactéria utilizada", width=500, height= 40, font=ctk.CTkFont(family="Segoe UI", size=16))
            nome_bac.pack(anchor="w", pady=5, padx=20)
            desc = ctk.CTkLabel(outrabac_toplevel, text="• Introduza abaixo os 10 valores de diluição do antibiótico, iniciando pela concentração mais alta e seguindo\npara as menores.", justify="left", font=ctk.CTkFont(family="Segoe UI", size=17), text_color="#2B6AD0")
            desc.pack(anchor="w", padx=20, pady=9)
            desc2 = ctk.CTkLabel(outrabac_toplevel, text="Exemplo: Diluição de Ciprofloxacino em Staphylococcus aureus: 8 → 4 → 2 → 1 → 0,5 → 0,25 → 0,125 → 0,06 → 0,03 → 0,02", justify="left", font=ctk.CTkFont(family="Segoe UI", size=15), text_color="#1c1d22")
            desc2.place(x=20, y=200)
        
            # Tabela de entrada dos valores de diluição
            tabela_diluicoes = Sheet(outrabac_toplevel, show_header=False, show_top_left=False, row_index=["Concentração\nde antibiótico (µg)"], header_align="center", headers=["Diluições"], align="center", width=900, row_index_width=125, height=43, total_columns=10, total_rows=1, row_height=40, column_width=77, show_x_scrollbar=False, show_y_scrollbar=False, empty_horizontal=0, empty_vertical=0)
            Sheet.set_options(tabela_diluicoes, max_column_width=77, index_selected_cells_bg="#2B6AD0", index_selected_cells_fg="#FFFFFF", header_selected_cells_bg="#2B6AD0",header_selected_cells_fg="#FFFFFF", table_bg="#E3E7F1", table_grid_fg="#FFFFFF", table_selected_cells_bg="#C6CAD1", index_bg="#2B6AD0", index_grid_fg="#FFFFFF", header_bg="#2B6AD0", header_grid_fg="#FFFFFF", font=('Helvetica', 10, 'normal'), table_fg='#000000', index_fg='#E3E7F1', header_fg='#E3E7F1', table_selected_cells_border_fg="#2B6AD0", table_selected_rows_border_fg ="#2B6AD0", table_selected_columns_border_fg= "#2B6AD0")
            tabela_diluicoes.enable_bindings("all")
            tabela_diluicoes.disable_bindings("column_height_resize", "<MouseWheel>", "column_width_resize", "row_width_resize", "row_height_resize")
            if scale == 100:
                Sheet.configure(tabela_diluicoes, width=845)
                Sheet.set_all_column_widths(tabela_diluicoes, 71)
                tabela_diluicoes.place(x=10, y=240)
            elif scale == 125:
                Sheet.configure(tabela_diluicoes, width=1010)
                Sheet.set_all_column_widths(tabela_diluicoes, 88)
                tabela_diluicoes.place(x=20, y=300)
            botao_cofirmar = ctk.CTkButton(outrabac_toplevel, cursor='hand2', width=170, height=40, hover=False, font=ctk.CTkFont(family="Segoe UI", size=17, weight='bold'), text="Confirmar", fg_color="#2B6AD0", corner_radius=10, command = confirmar_bac)
            botao_cofirmar.place(x=340, y=295)
            outrabac_toplevel.protocol("WM_DELETE_WINDOW", lambda : outra_bac.configure(state='normal') or outrabac_toplevel.withdraw())

def confirmar_bac(): # Função relacionada ao botão "confirmar", na janela da opção "Outra bactéria". Oculta a janela.
    global bac_escolhida
    outrabac_toplevel.withdraw()
    outra_bac.configure(state='normal')
    bac_escolhida = "Outra bacteria"

def linhas_resazurina(): # Função relacionada ao botão "cálculo de resazurina". Adiciona 2 novas linhas na tabela
    if botaoresazurina.get() == "on":
        tabela.sheet_data_dimensions(total_rows=10)
        if scale == 100:
            tabela.set_all_row_heights(27)
        elif scale == 125:
            tabela.set_all_row_heights(34)
    if botaoresazurina.get() == "off":    
        tabela.sheet_data_dimensions(total_rows=8)
        if scale == 100:
            tabela.set_all_row_heights(34)
        elif scale == 125:
            tabela.set_all_row_heights(43)


## FRAME 2 ##
def frame_meio(): # Cria o frame superior, com os botões de inserir os dados, limpar e gerar o gráfico #
    global frame2
    frame2 = ctk.CTkFrame(janela_dados, height=55, width=610, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=13)
    frame2.grid(row=1, column=1, sticky="new")
    frame2.rowconfigure(0, pad=10)
    frame2.grid_propagate(False)
    botao_inserir= ctk.CTkButton(frame2, width=215, height=45, corner_radius=10, cursor='hand2',hover=False, text="Colar dados", border_color="#dadada", border_width=2, font=fontegrande, fg_color="#FBFBFE", text_color="#1c1d22", command= lambda : tabela.paste(tabela.select_cell(row=0, column=0)))
    botao_inserir.grid(row=0, column=0, padx=15)
    botao_inserir.bind('<Enter>', lambda e: botao_inserir.configure(text_color="#2B6AD0", fg_color="#e8effd"))
    botao_inserir.bind('<Leave>', lambda e: botao_inserir.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    botao_limpar= ctk.CTkButton(frame2, width=215, height=45, corner_radius=10, cursor='hand2',hover=False, border_color="#dadada", border_width=2, text="Limpar tabela", font=fontegrande, fg_color="#FBFBFE", text_color="#1c1d22", command= limpar)
    botao_limpar.grid(row=0, column=1, padx=10)
    botao_limpar.bind('<Enter>', lambda e: botao_limpar.configure(text_color="#2B6AD0", fg_color="#e8effd"))
    botao_limpar.bind('<Leave>', lambda e: botao_limpar.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    botao_gerardados= ctk.CTkButton(frame2, width=215, height=45, corner_radius=10, cursor='hand2',hover=False, border_color="#dadada", border_width=2, text="Gerar gráfico", font=fontegrande, fg_color="#FBFBFE", text_color="#1c1d22", command= verificar_dados)
    botao_gerardados.grid(row=0, column=2, padx=10)
    botao_gerardados.bind('<Enter>', lambda e: botao_gerardados.configure(text_color="#2B6AD0", fg_color="#e8effd"))
    botao_gerardados.bind('<Leave>', lambda e: botao_gerardados.configure(text_color="#1c1d22", fg_color="#FBFBFE"))

def limpar(): # Limpa os dados da tabela #
    del dados_tabela["am"][:], dados_tabela["sc"][:], dados_tabela["ttc"][:], dados_tabela["res_570"][:], dados_tabela["res_600"][:]
    del resultados_medias["am"][:], resultados_medias["sc"][:], resultados_medias["ttc"][:], resultados_medias["res_570"][:], resultados_medias["res_600"][:]
    del porcentagens["am"][:], porcentagens["sc"][:], porcentagens["ttc"][:], porcentagens["res_570"][:], porcentagens["res_600"][:]
    del mediasresazurina["res"][:]
    del controle[:]
    tabela.set_sheet_data(data=([]), redraw=False, reset_col_positions=False, reset_row_positions=False, reset_highlights=True)
    tabela.refresh

## FRAME 3 ##
def frame_corantes(): # Cria o frame dos corantes, incorporando os botões referentes aos corantes.
    global quadro_corantes
    quadro_corantes = ctk.CTkFrame(janela_dados, height=58, width=690, fg_color="#E3E7F1", bg_color="#E3E7F1", corner_radius=13)
    quadro_corantes.grid(row=2, column=1, sticky="sew")
    quadro_corantes.rowconfigure(0, pad=8)
    quadro_corantes.grid_propagate(False)
    botao_sc = criar_botao_corantes("sc")
    botao_sc.grid(row=0 , column=0, padx=10, pady=2)
    botao_ttc = criar_botao_corantes("ttc")
    botao_ttc.grid(row=0, column=1, padx=5, pady=2)
    botao_res = criar_botao_corantes("res_570")
    botao_res.grid(row=0 , column=2, padx=5, pady=2)
    botao_res2 = criar_botao_corantes("res_600")
    botao_res2.grid(row=0 , column=3, padx=5, pady=2)
    botao_am = criar_botao_corantes("am")
    botao_am.grid(row=0 , column=4, padx=5, pady=2)
    botao_pv = criar_botao_corantes("pv")
    botao_pv.grid(row=0 , column=5, padx=5, pady=2)

def criar_botao_corantes(cor): # Cria os botões dos corantes
    if cor == "sc":
        botao = ctk.CTkButton(quadro_corantes, corner_radius=10, height=32, width=100, border_color=cores_corantes("sc"), hover=False, text_color="#1c1d22", border_width=0, fg_color="#FBFBFE", text="Sem\ncorante", font=fonte, command= lambda a="sc": corante_escolhido(a))
        botao.bind('<Enter>', lambda e: botao.configure(text_color="#FBFBFE", fg_color=cores_corantes("sc")))
        botao.bind('<Leave>', lambda e: botao.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    elif cor == "ttc":
        botao = ctk.CTkButton(quadro_corantes, corner_radius=10, height=32, width=100, border_color=cores_corantes("sc"), hover=False, text_color="#1c1d22", border_width=0, fg_color="#FBFBFE", text="TTC\n480nm", font=fonte, command= lambda a="ttc": corante_escolhido(a))  
        botao.bind('<Enter>', lambda e: botao.configure(text_color="#FBFBFE", fg_color=cores_corantes("ttc")))
        botao.bind('<Leave>', lambda e: botao.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    elif cor == "res_570":
        botao = ctk.CTkButton(quadro_corantes, corner_radius=10, height=32, width=100, border_color=cores_corantes("sc"), hover=False, text_color="#1c1d22", border_width=0, fg_color="#FBFBFE", text="Resazurina\n570nm", font=fonte, command= lambda a="res_570": corante_escolhido(a))
        botao.bind('<Enter>', lambda e: botao.configure(text_color="#FBFBFE", fg_color="#660099"))
        botao.bind('<Leave>', lambda e: botao.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    elif cor == "res_600":
        botao = ctk.CTkButton(quadro_corantes, corner_radius=10, height=32, width=100, border_color=cores_corantes("sc"), hover=False, text_color="#1c1d22", border_width=0, fg_color="#FBFBFE", text="Resazurina\n600nm", font = fonte, command= lambda a="res_600": corante_escolhido(a))   
        botao.bind('<Enter>', lambda e: botao.configure(text_color="#FBFBFE", fg_color="#6900EF"))
        botao.bind('<Leave>', lambda e: botao.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    elif cor == "am":
        botao = ctk.CTkButton(quadro_corantes, corner_radius=10, height=32, width=100, border_color=cores_corantes("sc"), hover=False, text_color="#1c1d22", border_width=0, fg_color="#FBFBFE", text="Azul de Metileno\n600nm", font = fonte, command= lambda a="am": corante_escolhido(a))
        botao.bind('<Enter>', lambda e: botao.configure(text_color="#FBFBFE", fg_color="#64B1FF"))
        botao.bind('<Leave>', lambda e: botao.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    elif cor == "pv":
        botao = ctk.CTkButton(quadro_corantes, corner_radius=10, height=32, width=100, border_color="#54546B", hover=False, text_color="#1c1d22", border_width=0, fg_color="#FBFBFE", text="Poço vazio\nResetar", font = fonte, command= lambda a="pv": corante_escolhido(a))
        botao.bind('<Enter>', lambda e: botao.configure(text_color="#FBFBFE", fg_color="#54546B"))
        botao.bind('<Leave>', lambda e: botao.configure(text_color="#1c1d22", fg_color="#FBFBFE"))
    return botao     

def corante_escolhido(a): # Função vinculada ao botão dos corantes. Permite a entrada de valores decimais com vírgula ou ponto, muda a cor das células referente ao corante, calcula a média das duplicatas, etc.
    try:
        if a == "sc":
            if len(dados_tabela["sc"]) >= 1:
                del dados_tabela["sc"][:]
                del resultados_medias["sc"][:] 
            Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = cores_corantes("sc"), fg = "#000000", redraw = True, overwrite = True)
            sc_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
            if len(sc_cr) > 24:
                tkinter.messagebox.showerror(title="Erro", message="Só é possível selecionar uma duplicata por corante.")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            if len(sc_cr) < 24:
                tkinter.messagebox.showerror(title="Erro", message="Deve ser selecionada ao menos uma duplicata.")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            for ro, co in sc_cr:
                data = str(Sheet.get_cell_data(tabela, r=ro, c=co))
                trocar_virgula = data.replace(',', ".")
                dados_tabela["sc"].append(float(trocar_virgula))
            for i in range(0, len(dados_tabela["sc"]), 2):
                valor = dados_tabela["sc"][i]
                proximo = dados_tabela["sc"][i+1]
                resultado = (valor + proximo) / 2 
                resultados_medias["sc"].append(resultado)
            if resultados_medias["sc"] == resultados_medias["ttc"]:
                del resultados_medias["ttc"][:]
            if resultados_medias["sc"] == resultados_medias["am"]:
                del resultados_medias["am"][:]
            if resultados_medias["sc"] == resultados_medias["res_570"]:
                del resultados_medias["res_570"]
            if resultados_medias["sc"] == resultados_medias["res_600"]:
                del resultados_medias["res_600"]
        if a == "ttc":
            if len(dados_tabela["ttc"]) >= 1:
                del dados_tabela["ttc"] [:]
                del resultados_medias["ttc"][:]
            Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = cores_corantes("ttc"), fg = "#000000", redraw = True, overwrite = True)      
            ttc_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
            if len(ttc_cr) > 24:
                tkinter.messagebox.showerror(title="Erro", message="Erro: Você só pode selecionar uma duplicata por corante.")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            if len(ttc_cr) < 24:
                tkinter.messagebox.showerror(title="Erro", message="Deve ser selecionada ao menos uma duplicata")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            for ro, co in ttc_cr:
                data = str(Sheet.get_cell_data(tabela, r=ro, c=co))
                trocar_virgula = data.replace(',', ".")
                dados_tabela["ttc"].append(float(trocar_virgula))
            for i in range(0, len(dados_tabela["ttc"]), 2):
                valor = dados_tabela["ttc"][i]
                proximo = dados_tabela["ttc"][i+1]
                resultado = (valor + proximo) / 2 
                resultados_medias["ttc"].append(resultado)
            if resultados_medias["ttc"] == resultados_medias["sc"]:
                del resultados_medias["sc"][:]
            if resultados_medias["ttc"] == resultados_medias["am"]:
                del resultados_medias["am"][:]
            if resultados_medias["ttc"] == resultados_medias["res_570"]:
                del resultados_medias["res_570"]
            if resultados_medias["ttc"] == resultados_medias["res_600"]:
                del resultados_medias["res_600"]
        if a == "res_570":
            if len(dados_tabela["res_570"]) >= 1:
                del dados_tabela["res_570"] [:]
                del resultados_medias["res_570"][:]
            Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#660099", fg = "#000000", redraw = True, overwrite = True)
            res_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
            if len(res_cr) > 24:
                tkinter.messagebox.showerror(title="Erro", message="Erro: Você só pode selecionar uma duplicata por corante.")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            if len(res_cr) < 24:
                tkinter.messagebox.showerror(title="Erro", message="Deve ser selecionada ao menos uma duplicata")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            for ro, co in res_cr:
                data = str(Sheet.get_cell_data(tabela, r=ro, c=co))
                trocar_virgula = data.replace(',', ".")
                dados_tabela["res_570"].append(float(trocar_virgula))
            for i in range(0, len(dados_tabela["res_570"]), 2):
                valor = dados_tabela["res_570"][i]
                proximo = dados_tabela["res_570"][i+1]
                resultado = (valor + proximo) / 2 
                resultados_medias["res_570"].append(resultado)
            if resultados_medias["res_570"] == resultados_medias["sc"]:
                del resultados_medias["sc"][:]
            if resultados_medias["res_570"] == resultados_medias["am"]:
                del resultados_medias["am"][:]
            if resultados_medias["res_570"] == resultados_medias["ttc"]:
                del resultados_medias["ttc"][:]     
            if resultados_medias["res_570"] == resultados_medias["res_600"]:
                del resultados_medias["res_600"]
        if a == "res_600":
            if len(dados_tabela["res_600"]) >= 1:
                del dados_tabela["res_600"] [:]
                del resultados_medias["res_600"][:]
            Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#6900EF", fg = "#000000", redraw = True, overwrite = True)
            res2_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
            if len(res2_cr) > 24:
                tkinter.messagebox.showerror(title="Erro", message="Erro: Você só pode selecionar uma duplicata por corante.")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            if len(res2_cr) < 24:
                tkinter.messagebox.showerror(title="Erro", message="Deve ser selecionada ao menos uma duplicata")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            for ro, co in res2_cr:
                data = str(Sheet.get_cell_data(tabela, r=ro, c=co))
                trocar_virgula = data.replace(',', ".")
                dados_tabela["res_600"].append(float(trocar_virgula))
            for i in range(0, len(dados_tabela["res_600"]), 2):
                valor = dados_tabela["res_600"][i]
                proximo = dados_tabela["res_600"][i+1]
                resultado = (valor + proximo) / 2 
                resultados_medias["res_600"].append(resultado)  
            if resultados_medias["res_600"] == resultados_medias["sc"]:
                del resultados_medias["sc"][:]
            if resultados_medias["res_600"] == resultados_medias["am"]:
                del resultados_medias["am"][:]
            if resultados_medias["res_600"] == resultados_medias["ttc"]:
                del resultados_medias["ttc"][:]  
            if resultados_medias["res_600"] == resultados_medias["res_570"]:
                del resultados_medias["res_570"][:]     
        if a == "am":
            if len(dados_tabela["am"]) >= 1:
                del dados_tabela["am"] [:]
                del resultados_medias["am"][:]
            Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#64B1FF", fg = "#000000", redraw = True, overwrite = True)
            am_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
            if len(am_cr) > 24:
                tkinter.messagebox.showerror(title="Erro", message="Erro: Você só pode selecionar uma duplicata por corante.")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            if len(am_cr) < 24:
                tkinter.messagebox.showerror(title="Erro", message="Deve ser selecionada ao menos uma duplicata")
                tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
                return
            for ro, co in am_cr:
                data = str(Sheet.get_cell_data(tabela, r=ro, c=co))
                trocar_virgula = data.replace(',', ".")
                dados_tabela["am"].append(float(trocar_virgula))
            for i in range(0, len(dados_tabela["am"]), 2):
                valor = dados_tabela["am"][i]
                proximo = dados_tabela["am"][i+1]
                resultado = (valor + proximo) / 2 
                resultados_medias["am"].append(resultado)
            if resultados_medias["am"] == resultados_medias["sc"]:
                del resultados_medias["sc"][:]
            if resultados_medias["am"] == resultados_medias["ttc"]:
                del resultados_medias["ttc"][:]  
            if resultados_medias["am"] == resultados_medias["res_570"]:
                del resultados_medias["res_570"][:]     
            if resultados_medias["am"] == resultados_medias["res_600"]:
                del resultados_medias["res_600"]
    except ValueError:
        tkinter.messagebox.showerror(title="Dados inválidos", message="Dados inválidos!")
        tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
        Sheet.delete(tabela, tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))      
    if a == "pv":
        tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
        pv_apagar = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
        for ro, co in pv_apagar:
            data = str(Sheet.get_cell_data(tabela, r=ro, c=co))
            trocar_virgula = data.replace(',', ".")
            valores_apagar.append(float(trocar_virgula))
        funcao_botaoapagar("sc")
        funcao_botaoapagar("ttc")
        funcao_botaoapagar("res_570")
        funcao_botaoapagar("res_600")
        funcao_botaoapagar("am")
        Sheet.delete(tabela, tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))

def funcao_botaoapagar(corante): # Função vinculada especificamente ao botão "Poço vazio/Apagar dados". Deleta todos os valores selecionados.
    if valores_apagar == dados_tabela[corante] or valores_apagar in dados_tabela[corante]:
        del dados_tabela[corante][:]
        del resultados_medias[corante][:]
        del valores_apagar[:]


## Funções relacionadas ao cálculo dos dados ##
    
def verificar_dados(): # Induz o cálculo para todos os corantes, verificando se a bactéria foi escolhida #
    global bac_escolhida
    try:
        del controle[:]
        criar_grafico()
        cálculos('sc')
        cálculos('ttc')
        cálculos('res')
        cálculos('am')
        gerar_grafico(bac_escolhida)
    except NameError:
        tkinter.messagebox.showerror(title="Erro", message="Selecione a bactéria utilizada")

def cálculos(cor): # Realiza os cálculos principais, utilizando as médias dos valores obtidos na tabela e os valores dos controles #
    controle = Sheet.get_header_dropdown_value(tabela, c=10)
    controle2 = Sheet.get_header_dropdown_value(tabela, c=11)
    if cor == 'sc':
        for valor in resultados_medias["sc"]:
            try:
                if controle != controle2:
                    if controle == 'C+':
                        resultado = 100-(valor*100/resultados_medias["sc"][-2])
                    if controle == 'C-':
                        resultado = 100-(valor*100/resultados_medias["sc"][-1])
                else:
                    print('Os dois controles estão iguais!')
                    break
            except ZeroDivisionError:
                resultado = 0
            resultado_lim = round(resultado, 2)
            porcentagens["sc"].append(resultado_lim)
    if cor == 'ttc':
        for valor in resultados_medias["ttc"]:
            try:
                if controle != controle2:
                    if controle == 'C+':
                        resultado = 100-(valor*100/resultados_medias["ttc"][-2])
                    if controle == 'C-':
                        resultado = 100-(valor*100/resultados_medias["ttc"][-1])
                else:
                    print('Os dois controles estão iguais!')
                    break
            except ZeroDivisionError:
                resultado = 0
            resultado_lim = round(resultado, 2)
            porcentagens["ttc"].append(resultado_lim)
    if cor == 'res':
        for valor, valor2 in zip(resultados_medias["res_570"], resultados_medias["res_600"]):
            try:
                if controle != controle2:
                    if controle == 'C+':
                        formula = 100-(((117216*valor)-(80586*valor2))/((117216*resultados_medias["res_570"][-2])-(80568*resultados_medias["res_600"][-2])))*100
                    if controle == 'C-':
                        formula = 100-(((117216*valor)-(80586*valor2))/((117216*resultados_medias["res_570"][-1])-(80568*resultados_medias["res_600"][-1])))*100
                else:
                    print('Os dois controles estão iguais!')
                    break
            except ZeroDivisionError:
                formula = 0
            resultado_lim = round(formula, 2)
            mediasresazurina["res"].append(resultado_lim)
    if cor == 'am':
        for valor in resultados_medias["am"]:
            try:
                if controle != controle2:
                    if controle == 'C+':
                        resultado = 100-(valor*100/resultados_medias["am"][-1])
                    if controle == 'C-':
                        resultado = 100-(valor*100/resultados_medias["am"][-2])
                else:
                    print('Os dois controles estão iguais!')
                    break
            except ZeroDivisionError:
                resultado = 0
            resultado_lim = round(resultado, 2)
            porcentagens["am"].append(resultado_lim)

#####* Introduz os elementos gráficos da janela do gráfico #####
    
def janelagrafico():  # Widgets principais (frames, botões)
    global molduragraf, salvarcomo2, var_grid, var_valores, var_titulo, var_legenda, botao_config_adc, botao_valores
    var_grid = ctk.StringVar(value="Off")
    var_valores = ctk.StringVar(value="Off")
    var_titulo = ctk.StringVar(value="On")
    var_legenda = ctk.StringVar(value="On")

    molduraopcoes = ctk.CTkFrame(janela_grafico, height=70, width=1050, fg_color="#FFFFFF", corner_radius=16)
    molduraopcoes.grid(row=0, column=1, sticky="ne", padx=30)
    molduraopcoes.grid_propagate(False)
    molduraopcoes.columnconfigure(2, weight=1)
    molduraopcoes.rowconfigure([0,1], pad=5)

    molduragraf = ctk.CTkFrame(janela_grafico, height=460, width=1050, fg_color="#FFFFFF", corner_radius=16)
    molduragraf.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=15, padx=30)
    molduragraf.grid_propagate(False)
    molduragraf.grid_rowconfigure(0, weight=1)
    molduragraf.grid_columnconfigure(0, weight=1)

    checkbox_grid = ctk.CTkCheckBox(molduraopcoes, width=100, height=20, text="Linhas de grade",font=ctk.CTkFont(family="Segoe UI", size=17), checkmark_color="#FBFBFE", fg_color="#2B6AD0", hover=False, command= lambda: grid_grafico(),variable=var_grid, onvalue="On", offvalue="Off")
    checkbox_grid.grid(column=0, row=0, padx=10, sticky="w",pady=5)

    checkbox_valores = ctk.CTkCheckBox(molduraopcoes, width=100, height=20, text="Mostrar valores", font=ctk.CTkFont(family="Segoe UI", size=17), checkmark_color="#FBFBFE", fg_color="#2B6AD0", hover=False, command= lambda: mostrar_valores(),variable=var_valores, onvalue="On", offvalue="Off")
    checkbox_valores.grid(column=0, row=1, padx=10, sticky="w")

    checkbox_titulo = ctk.CTkCheckBox(molduraopcoes, width=100, height=20, text="Mostrar título", font=ctk.CTkFont(family="Segoe UI", size=17), checkmark_color="#FBFBFE", fg_color="#2B6AD0", hover=False, command= lambda: titulo_grafico("show"),variable=var_titulo, onvalue="On", offvalue="Off")
    checkbox_titulo.grid(column=1, row=0, padx=10, sticky="w")

    checkbox_legenda = ctk.CTkCheckBox(molduraopcoes, width=100, height=20, text="Mostrar legenda", font=ctk.CTkFont(family="Segoe UI", size=17), checkmark_color="#FBFBFE", fg_color="#2B6AD0", hover=False, command= lambda: titulo_grafico("legenda"),variable=var_legenda, onvalue="On", offvalue="Off")
    checkbox_legenda.grid(column=1, row=1, padx=10, sticky="w")

    botao_valores = ctk.CTkButton(molduraopcoes,width=215, height=45, corner_radius=10, cursor='hand2',hover=False, text="Obter dados", border_color="#dadada", border_width=2, font=fontenormal, fg_color="#FBFBFE", text_color="#1c1d22", command= toplevel_valores)
    botao_valores.grid(column=2, row=0, rowspan=2, sticky="e", padx=30)
    botao_valores.bind('<Enter>', lambda e: botao_valores.configure(text_color="#2B6AD0", fg_color="#e8effd"))
    botao_valores.bind('<Leave>', lambda e: botao_valores.configure(text_color="#1c1d22", fg_color="#FBFBFE"))

    botao_config_adc = ctk.CTkButton(molduraopcoes,width=215, height=45, corner_radius=10, cursor='hand2',hover=False, text="Configurações", border_color="#dadada", border_width=2, font=fontenormal, fg_color="#FBFBFE", text_color="#1c1d22", command=toplevel_config_adc)
    botao_config_adc.grid(column=3, row=0, rowspan=2, sticky="e", padx=10)
    botao_config_adc.bind('<Enter>', lambda e: botao_config_adc.configure(text_color="#2B6AD0", fg_color="#e8effd"))
    botao_config_adc.bind('<Leave>', lambda e: botao_config_adc.configure(text_color="#1c1d22", fg_color="#FBFBFE"))

    salvarcomo = ctk.CTkButton(molduraopcoes,width=215, height=45, corner_radius=10, cursor='hand2',hover=False, text="Salvar gráfico:", border_color="#dadada", border_width=2, font=fontenormal, fg_color="#FBFBFE", text_color="#1c1d22")
    salvarcomo.grid(column=4, row=0, rowspan=2, sticky="e", padx=10)
    salvarcomo2 = CTkScrollableDropdown(salvarcomo, values=[".jpg", ".png", ".pdf", ".svg"], font=fontenormal, scrollbar=False, alpha=0.97, height=223, resize=False, image_values=[jpg, png, pdf, svg], fg_color="#FBFBFE", button_color="#C6CAD1", text_color="#1c1d22", button_height=40, width=215, command= salvargrafico)
    salvarcomo2.configure(hover_color="#2B6AD0")
    salvarcomo.bind('<Enter>', lambda e: salvarcomo.configure(text_color="#2B6AD0", fg_color="#e8effd"))
    salvarcomo.bind('<Leave>', lambda e: salvarcomo.configure(text_color="#1c1d22", fg_color="#FBFBFE"))

def tabela_tabview():
    global tabela_valores, var_tabelas
    corante = tbv_valores_corantes.get()
    tabela_valores = Sheet(tbv_valores_corantes.tab(corante), show_row_index=False, show_top_left=False, headers=["Concentração de\nantibiótico (µg/mL)", "Inibição\nbacteriana (%)"], header_height=50, header_align="center", align="center", width=263, row_index_width=125, height=400, total_columns=2, total_rows=10, row_height=35, column_width=130, show_x_scrollbar=False, show_y_scrollbar=False, empty_horizontal=0, empty_vertical=0)
    Sheet.set_options(tabela_valores, max_column_width=90, index_selected_cells_bg="#2B6AD0", index_selected_cells_fg="#FFFFFF", header_selected_cells_bg="#2B6AD0",header_selected_cells_fg="#FFFFFF", table_bg="#E3E7F1", table_grid_fg="#FFFFFF", table_selected_cells_bg="#C6CAD1", index_bg="#2B6AD0", index_grid_fg="#FFFFFF", header_bg="#2B6AD0", header_grid_fg="#FFFFFF", font=('Helvetica', 10, 'normal'), table_fg='#000000', index_fg='#E3E7F1', header_fg='#E3E7F1', table_selected_cells_border_fg="#2B6AD0", table_selected_rows_border_fg ="#2B6AD0", table_selected_columns_border_fg= "#2B6AD0")
    tabela_valores.enable_bindings("all")
    tabela_valores.disable_bindings("column_height_resize", "<MouseWheel>", "column_width_resize", "row_width_resize", "row_height_resize")
    tabela_valores.place(x=15, y=10)

    var_tabelas = ctk.StringVar(value="Off")
    checkbox_tabelas = ctk.CTkCheckBox(tbv_valores_corantes, width=100, height=20, text="Mostrar valores", font=ctk.CTkFont(family="Segoe UI", size=17), checkmark_color="#FBFBFE", fg_color="#2B6AD0", hover=False, command= lambda: mostrar_tabelas(),variable=var_tabelas, onvalue="On", offvalue="Off")
    checkbox_tabelas.grid(row=3, sticky="s", pady=40)
    botao_salvar_csv = ctk.CTkButton(tbv_valores_corantes, cursor='hand2', width=140, height=37, hover=False, font=ctk.CTkFont(family="Segoe UI", size=17, weight='bold'), text="Salvar .csv", fg_color="#2B6AD0", corner_radius=10, command = salvar_csv)
    botao_salvar_csv.grid(row=3, sticky="s")

    if corante == "Sem corante":
        tbv_valores_corantes.configure(segmented_button_selected_color=cores_corantes("sc"), segmented_button_selected_hover_color=cores_corantes("sc"))
        tabela_valores.span("A", transposed=True, header=False).data = diluicao_escolhida
        tabela_valores.span("B", transposed=True, header=False).data = porcentagens["sc"][:-2][::-1]
    if corante == "TTC":
        tbv_valores_corantes.configure(segmented_button_selected_color=cores_corantes("ttc"), segmented_button_selected_hover_color=cores_corantes("ttc"))
        tabela_valores.span("A", transposed=True, header=False).data = diluicao_escolhida
        tabela_valores.span("B", transposed=True, header=False).data = porcentagens["ttc"][:-2][::-1]
    if corante == "Resazurina":
        tbv_valores_corantes.configure(segmented_button_selected_color=cores_corantes("res"), segmented_button_selected_hover_color=cores_corantes("res"))
        tabela_valores.span("A", transposed=True, header=False).data = diluicao_escolhida
        tabela_valores.span("B", transposed=True, header=False).data = mediasresazurina["res"][:-2][::-1]
    if corante == "Azul de Metileno":
        tbv_valores_corantes.configure(segmented_button_selected_color=cores_corantes("am"), segmented_button_selected_hover_color=cores_corantes("am"))
        tabela_valores.span("A", transposed=True, header=False).data = diluicao_escolhida
        tabela_valores.span("B", transposed=True, header=False).data = porcentagens["am"][:-2][::-1]

def mostrar_tabelas():
    global lista_tabelas, headers
    headers = ["Concentração de\nantibiótico (µg/mL)", f"Inibição bacteriana (%)\n{tbv_valores_corantes.get()}"]
    lista_tabelas = ax.get_legend_handles_labels()[1]
    tabelas = len(lista_tabelas)
    if var_tabelas.get() == "On":
        if tabelas > 1:
            tbv_valores_corantes.configure(width=300+135*(tabelas-1))
            obter_valores.geometry(f"{300+(70*tabelas-1)}x600")
            tabela_valores.configure(width=262+131*(tabelas-1))
            tabela_valores.insert_columns(tabelas-1)
            lista_tabelas.remove(tbv_valores_corantes.get())
            for i in range (4):
                iteracao("C")
                iteracao("D")
                iteracao("E")
                iteracao("F")
    tabela_valores.set_all_column_widths(150)

def iteracao(col):
    if "Sem corante" in lista_tabelas:
        tabela_valores.span(col, transposed=True, header=False).data = porcentagens["sc"][:-2][::-1]
        lista_tabelas.remove("Sem corante")
        headers.append("Inibição bacteriana (%)\nSem corante")
        tabela_valores.headers(newheaders=headers)
    elif "TTC" in lista_tabelas:
        tabela_valores.span(col, transposed=True, header=False).data = porcentagens["ttc"][:-2][::-1]
        lista_tabelas.remove("TTC")
        headers.append("Inibição bacteriana (%)\nTTC")
        tabela_valores.headers(newheaders=headers)
    elif "Resazurina" in lista_tabelas:
        tabela_valores.span(col, transposed=True, header=False).data = mediasresazurina["res"][:-2][::-1]
        lista_tabelas.remove("Inibição bacteriana (%)\nResazurina")
        headers.append("Inibição bacteriana (%)\nResazurina")
        tabela_valores.headers(newheaders=headers)
    elif "Azul de Metileno" in lista_tabelas:
        tabela_valores.span(col, transposed=True, header=False).data = porcentagens["am"][:-2][::-1] 
        lista_tabelas.remove("Azul de Metileno")  
        headers.append("Inibição bacteriana (%)\nAzul de Metileno")
        tabela_valores.headers(newheaders=headers)
    print(headers)
            

def toplevel_valores():
    global tbv_valores_corantes, valores_sc, valores_ttc, obter_valores
    try:
        if obter_valores.winfo_exists() == True:
                obter_valores.deiconify()
    except (NameError, UnboundLocalError):
        botao_valores.configure(state="disabled")
        obter_valores = ctk.CTkToplevel()
        obter_valores.focus()
        obter_valores.geometry("300x600+80+190")
        obter_valores.title("Configurar bactéria")
        obter_valores.resizable(False, False)
        obter_valores.after(200, obter_valores.lift)
        obter_valores.after(200, lambda: obter_valores.iconbitmap("assets\logos\icone_programa.ico"))
        obter_valores.protocol("WM_DELETE_WINDOW", lambda : botao_valores.configure(state='normal') or obter_valores.withdraw())
        obter_valores.grid_propagate(False)
        obter_valores.grid_rowconfigure(0, weight=0)
        titulo = ctk.CTkLabel(obter_valores, text=" Valores do gráfico\n―――――――――――", justify="left", font=ctk.CTkFont(family="Segoe UI", size=25), text_color="#2B6AD0")
        titulo.grid(row=0, sticky="nw", padx=10)
        titulo.propagate(False)

        tbv_valores_corantes = ctk.CTkTabview(obter_valores, width=300, height=530, text_color="black", fg_color="#ffffff", segmented_button_fg_color="#eeece9", segmented_button_unselected_color="#fbfbfe", segmented_button_unselected_hover_color="#e8effd", command=tabela_tabview)
        tbv_valores_corantes.grid(row=2, column=0, sticky="n")
        if len(porcentagens["sc"]) > 1:
            valores_sc = tbv_valores_corantes.add("Sem corante")
        if len(porcentagens["ttc"]) > 1:    
            valores_ttc = tbv_valores_corantes.add("TTC")
        if len(mediasresazurina["res"]) > 1:
            valores_res = tbv_valores_corantes.add("Resazurina")
        if len(porcentagens["am"]) > 1:
            valores_am = tbv_valores_corantes.add("Azul de Metileno")
        tabela_tabview()
    
def toplevel_config_adc():
    global config_adc, titulo_config, label_sc, bt_cor_sc, label_ttc, bt_cor_ttc, label_res, bt_cor_res, label_am, bt_cor_am, eixox_config, eixoy_config
    try:
        if config_adc.winfo_exists() == True:
                config_adc.deiconify()
    except NameError:
        botao_config_adc.configure(state="disabled")
        config_adc = ctk.CTkToplevel()
        config_adc.focus()
        config_adc.geometry("450x600+80+190")
        config_adc.title("Configurar bactéria")
        config_adc.resizable(False, False)
        config_adc.after(200, config_adc.lift)
        config_adc.after(200, lambda: config_adc.iconbitmap("assets\logos\icone_programa.ico"))
        config_adc.protocol("WM_DELETE_WINDOW", lambda : botao_config_adc.configure(state='normal') or config_adc.withdraw())
        config_adc.grid_propagate(False)

        titulo = ctk.CTkLabel(config_adc, text=" Configurações adicionais\n―――――――――――――――――――――――――――――", justify="left", font=ctk.CTkFont(family="Segoe UI", size=30), text_color="#2B6AD0")
        titulo.grid(columnspan=4, column=0, row=0, sticky="nw", padx=10, pady=5)
        titulo.propagate(False)

        label_config_textos =  ctk.CTkLabel(config_adc, text="• Configurar o título do gráfico e eixos X e Y", justify="left", font=ctk.CTkFont(family="Segoe UI", size=17), text_color="#2B6AD0")
        label_config_textos.grid(row=1, columnspan=2, sticky="nw", padx=10)

        titulo_config = ctk.CTkEntry(config_adc, placeholder_text="Mudar o título do gráfico", width=330, height= 40, font=ctk.CTkFont(family="Segoe UI", size=16))
        titulo_config.grid(row=2, columnspan=2, sticky="w", padx=10, pady=5)
        bt_redefinir = ctk.CTkButton(config_adc, text="Redefinir", cursor='hand2', width=80, height=30, hover=False,fg_color="#2B6AD0", font=ctk.CTkFont(family="Segoe UI", size=16, weight='bold'), command= lambda: redefinir_texto("titulo"))
        bt_redefinir.grid(row=2, columnspan=2, sticky="e", pady=5, padx=0)

        eixox_config = ctk.CTkEntry(config_adc, placeholder_text="Mudar o eixo X", width=330, height= 40, font=ctk.CTkFont(family="Segoe UI", size=16))
        eixox_config.grid(row=3, columnspan=2, sticky="w", padx=10, pady=5)
        bt_redefinir = ctk.CTkButton(config_adc, text="Redefinir", cursor='hand2', width=80, height=30, hover=False,fg_color="#2B6AD0", font=ctk.CTkFont(family="Segoe UI", size=16, weight='bold'), command= lambda: redefinir_texto("eixo_x"))
        bt_redefinir.grid(row=3, columnspan=2, sticky="e", pady=5, padx=0)

        eixoy_config = ctk.CTkEntry(config_adc, placeholder_text="Mudar o eixo Y", width=330, height= 40, font=ctk.CTkFont(family="Segoe UI", size=16))
        eixoy_config.grid(row=4, columnspan=2, sticky="w", padx=10, pady=5)
        bt_redefinir = ctk.CTkButton(config_adc, text="Redefinir", cursor='hand2', width=80, height=30, hover=False,fg_color="#2B6AD0", font=ctk.CTkFont(family="Segoe UI", size=16, weight='bold'), command=  lambda: redefinir_texto("eixo_y"))
        bt_redefinir.grid(row=4, columnspan=2, sticky="e", pady=15, padx=0)
        
        label_config_cores =  ctk.CTkLabel(config_adc, text="• Configurar a cor das linhas e valores do gráfico", justify="left", font=ctk.CTkFont(family="Segoe UI", size=17), text_color="#2B6AD0")
        label_config_cores.grid(row=5, columnspan=2, sticky="nw", padx=10)
        nome_sc= ctk.CTkLabel(config_adc, text= "Sem corante", font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"))
        nome_sc.grid(row=6, columnspan=2, sticky="w", padx=10)
        label_sc = ctk.CTkLabel(config_adc, text="#999999", fg_color="#999999", font=fonte, height= 35, width=120, corner_radius=3, text_color="white")
        label_sc.grid(row=6, columnspan=2, stick="e", padx=65)
        bt_cor_sc = ctk.CTkButton(config_adc, text="", height=40, width=40, fg_color="#999999", corner_radius=3, hover=False, border_width=2, command= lambda: color_picker("sc"))
        bt_cor_sc.grid(row=6, columnspan=2, sticky="e", padx=5, pady=10)
       
        nome_ttc= ctk.CTkLabel(config_adc, text= "TTC", font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"))
        nome_ttc.grid(row=7, columnspan=2, sticky="w", padx=10)
        label_ttc = ctk.CTkLabel(config_adc, text="#FF6666", fg_color="#FF6666", font=fonte, height= 35, width=120, corner_radius=3, text_color="white")
        label_ttc.grid(row=7, columnspan=2, stick="e", padx=65)
        bt_cor_ttc = ctk.CTkButton(config_adc, text="", height=40, width=40, corner_radius=3, fg_color="#FF6666", hover=False, border_width=2, command= lambda: color_picker("ttc"))
        bt_cor_ttc.grid(row=7, columnspan=2, sticky="e", padx=5, pady=10)

        nome_res= ctk.CTkLabel(config_adc, text= "Resazurina", font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"))
        nome_res.grid(row=8, columnspan=2, sticky="w", padx=10)
        label_res = ctk.CTkLabel(config_adc, text="#660099", fg_color="#660099", font=fonte, height= 35, width=120, corner_radius=3, text_color="white")
        label_res.grid(row=8, columnspan=2, stick="e", padx=65)
        bt_cor_res = ctk.CTkButton(config_adc, text="", height=40, width=40, corner_radius=3, hover=False, fg_color="#660099", border_width=2, command= lambda: color_picker("res"))
        bt_cor_res.grid(row=8, columnspan=2, sticky="e", padx=5, pady=10)

        nome_am= ctk.CTkLabel(config_adc, text= "Azul de Metileno", font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"))
        nome_am.grid(row=9, columnspan=2, sticky="w", padx=10)
        label_am = ctk.CTkLabel(config_adc, text="#64B1FF", fg_color="#64B1FF", font=fonte, height= 35, width=120, corner_radius=3, text_color="white")
        label_am.grid(row=9, columnspan=2, stick="e", padx=65)
        bt_cor_am = ctk.CTkButton(config_adc, text="", height=40, width=40, corner_radius=3, hover=False, fg_color="#64B1FF", border_width=2, command= lambda: color_picker("am"))
        bt_cor_am.grid(row=9, columnspan=2, sticky="e", padx=5, pady=15)

        botao_confirmar = ctk.CTkButton(config_adc, cursor='hand2', width=170, height=40, hover=False, font=ctk.CTkFont(family="Segoe UI", size=17, weight='bold'), text="Confirmar", fg_color="#2B6AD0", corner_radius=10, command = confirmar_config_adc)
        botao_confirmar.place(x=135, y=550)

def redefinir_texto(texto):
    if texto == "titulo":
        titulo_config.delete(0, tkinter.END)
        titulo_config.insert(1, "Concentração de antibiótico x Inibição bacteriana")
    elif texto == "eixo_x":
        eixox_config.delete(0, tkinter.END)
        eixox_config.insert(1, "Concentração de antibiótico (μL)")
    elif texto == "eixo_y":
        eixoy_config.delete(0, tkinter.END)
        eixoy_config.insert(1, "Inibição bacteriana (%)")
    
def color_picker(corante):
    global colorpicker
    config_adc.geometry("730x600")
    if corante == "sc":
        colorpicker = CTkColorPicker(config_adc, width=300, orientation="horizontal", initial_color=label_sc.cget("fg_color"), command=lambda e: (label_sc.configure(fg_color=e, text=e), bt_cor_sc.configure(fg_color=e)))
        colorpicker.grid(row=3, rowspan=6, column=2, columnspan=2, sticky="sw", padx=32)
    elif corante == "ttc":
        colorpicker = CTkColorPicker(config_adc, width=300, orientation="horizontal", initial_color=label_ttc.cget("fg_color"),command=lambda e: (label_ttc.configure(fg_color=e, text=e), bt_cor_ttc.configure(fg_color=e)))
        colorpicker.grid(row=3, rowspan=6, column=2, columnspan=2, sticky="sw", padx=32)  
    elif corante == "res":
        colorpicker = CTkColorPicker(config_adc, width=300, orientation="horizontal", initial_color=label_res.cget("fg_color"),command=lambda e: (label_res.configure(fg_color=e, text=e), bt_cor_res.configure(fg_color=e)))
        colorpicker.grid(row=3, rowspan=6, column=2, columnspan=2, sticky="sw", padx=32)   
    elif corante == "am":
        colorpicker = CTkColorPicker(config_adc, width=300, orientation="horizontal", initial_color=label_am.cget("fg_color"),command=lambda e: (label_am.configure(fg_color=e, text=e), bt_cor_am.configure(fg_color=e)))
        colorpicker.grid(row=3, rowspan=6, column=2, columnspan=2, sticky="sw", padx=32)   

def confirmar_config_adc():
    global sc_alt, ttc_alt, res_alt, am_alt
    botao_config_adc.configure(state="normal")
    try:
        colorpicker.destroy()
    except (NameError, AttributeError):
        pass
    config_adc.geometry("450x600")
    config_adc.withdraw()
    try:
        if len(gra.selections) > 5:
            for valor in gra.selections:
                gra.remove_selection(valor)
        if len(gra2.selections) > 5:
            for valor in gra2.selections:
                gra2.remove_selection(valor)
        if len(gra3.selections) > 5:
            for valor in gra3.selections:
                gra3.remove_selection(valor)      
        if len(gra4.selections) > 5:
            for valor in gra4.selections:
                gra4.remove_selection(valor)
    except NameError:
        pass
    del controle[:]
    sc_alt = label_sc.cget("fg_color")
    ttc_alt = label_ttc.cget("fg_color")
    res_alt = label_res.cget("fg_color")
    am_alt = label_am.cget("fg_color")
    gerar_grafico(bac_escolhida)
    plt.pause(0.5)

def criar_grafico(): # Cria o back-end do gráfico antecipadamente, possibilitando a atualização do mesmo ao gerar novos gráficos #
    global ax, grafico1, canvas, fonte_graf, fonte_tit, titulografico
    plt.ion()
    plt.pause(0.005)
    fonte_graf = {'family':'Segoe UI','color':"#1c1d22",'size':12, 'weight':"semibold"}
    fonte_tit = {'family':'Segoe UI','color':"#1c1d22",'size':16, 'weight':"semibold"}
    grafico1 = plt.figure(figsize=(10.2, 5), facecolor="#FFFFFF", edgecolor="#FFFFFF", num=1, clear=True)
    canvas = FigureCanvasTkAgg(master= molduragraf, figure=grafico1)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    ax = grafico1.subplots()
    grafico1.tight_layout(pad=3.4)
    plt.close()

def gerar_grafico(bac): # Gera o gráfico ou atualiza um gráfico pré-existente com novos dados #
    global dil_saureus, dil_ecoli, dil_outrabac, titulografico, legenda, ann_hover, diluicao_escolhida
    try:
        ax.cla()
    except NameError:
        pass
    dil_saureus = ["0.02", "0.03", "0.06", "0.125", "0.25", "0.5", "1.0", "2.0", "4.0", "8.0"]
    dil_ecoli = ["0.0005", "0.001", "0.002", "0.004", "0.008", "0.016", "0.032", "0.064", "0.128", "0.256"]
    try:
        dil_outrabac = tabela_diluicoes.get_row_data(r=0)
    except NameError:
        pass
    if bac == "Staphylococcus aureus":
        diluicao_escolhida = dil_saureus
        plotar_gráfico(dil_saureus)
    if bac == "Escherichia coli":
        diluicao_escolhida = dil_ecoli
        plotar_gráfico(dil_ecoli)
    if bac =="Outra bacteria":
        diluicao_escolhida = tabela_diluicoes.get_row_data(r=0)
        plotar_gráfico(dil_outrabac)
    plt.pause(0.05)
    legenda = ax.legend(loc=("upper left"))
    try:
        titulografico = ax.set_title(titulo_config.get(), fontdict=fonte_tit)
        if len(titulo_config.get()) == 0:
            ax.set_title("Concentração de antibiótico x Inibição bacteriana", fontdict=fonte_tit)
        eixox = ax.set_xlabel(eixox_config.get(), fontdict= fonte_graf)
        if len(eixox_config.get()) == 0:
            ax.set_xlabel("Concentração de antibiótico (μL)", fontdict=fonte_graf)
        eixoy = ax.set_ylabel(eixoy_config.get(), fontdict= fonte_graf)
        if len(eixoy_config.get()) == 0:
            ax.set_ylabel("Inibição bacteriana (%)", fontdict=fonte_graf)
    except NameError:
        titulografico = ax.set_title("Concentração de antibiótico x Inibição bacteriana", fontdict=fonte_tit)
        ax.set_xlabel("Concentração de antibiótico (μL)", fontdict=fonte_graf)
        ax.set_ylabel("Inibição bacteriana (%)", fontdict=fonte_graf)
    ann_hover = mplcursors.cursor(ax, multiple = False, hover=2).connect("add", annotations_config_hover)

def plotar_gráfico(diluicao): # Introduz as porcentagens de inibição calculadas no eixo X, e a diluição referente à bactéria escolhida no eixo Y #
    global gra, gra2, gra3, gra4
    if len(resultados_medias["sc"]) == 12:
        if len(porcentagens["sc"]) > 12:
            del porcentagens["sc"][:-12]
        ax.plot(diluicao, porcentagens["sc"][:-2][::-1], color=cores_corantes("sc"), label="Sem corante", marker='.')
        gra = mplcursors.cursor(ax, multiple = True)
        gra.connect("add", annotations_config)
        valores_grafico("sc")
    if len(resultados_medias["ttc"]) == 12:
        if len(porcentagens["ttc"]) > 12:
            del porcentagens["ttc"][:-12]
        ax.plot(diluicao, porcentagens["ttc"][:-2][::-1], color=cores_corantes("ttc"), label="TTC", marker='.')
        gra2 = mplcursors.cursor(ax, multiple = True)
        gra2.connect("add", annotations_config)
        valores_grafico("ttc")
    if len(resultados_medias["res_570"]) and len(resultados_medias["res_600"]):
        if len(mediasresazurina["res"]) > 12:
            del mediasresazurina["res"][:-12]
        ax.plot(diluicao, mediasresazurina["res"][:-2][::-1], color=cores_corantes("res"), label="Resazurina", marker='.')
        gra3 = mplcursors.cursor(ax, multiple = True)
        gra3.connect("add", annotations_config)
        valores_grafico("res")
    if len(resultados_medias["am"]) == 12:
        if len(porcentagens["am"]) > 12:
            del porcentagens["am"][:-12]
        ax.plot(diluicao, porcentagens["am"][:-2][::-1], color=cores_corantes("am"), label="Azul de Metileno", marker='.')
        gra4 = mplcursors.cursor(ax, multiple = True)
        gra4.connect("add", annotations_config)
        valores_grafico("am")

def _process_event(name, axu, coords, *args):
    ax.viewLim  # unstale viewLim.
    if name == "__mouse_click__" or name == "deselect":
        # So that the dragging callbacks don't go crazy.
        _process_event("button_press_event", axu, coords, *args)
        _process_event("button_release_event", axu, coords, *args)
        return
    display_coords = ax.transData.transform(coords)
    if name in ["button_press_event", "button_release_event",
                "motion_notify_event", "scroll_event"]:
        event = MouseEvent(name, axu.figure.canvas, *display_coords, *args)
    elif name in ["key_press_event", "key_release_event"]:
        event = KeyEvent(name, axu.figure.canvas, *args, *display_coords)
    else:
        raise ValueError(f"Unknown event name {name!r}")
    axu.figure.canvas.callbacks.process(name, event)

# Funções referentes aos botões e checkbox na moldura de opções  
def valores_grafico(cor): 
    try:
        if cor == "sc":
            if "sc" not in controle:
                for i in range(0, 10):
                    _process_event("__mouse_click__", ax, (i, porcentagens["sc"][:-2][::-1][i]), 1)
            controle.append("sc")
        elif cor == "ttc":
            if "ttc" not in controle:
                for i in range(0, 10):
                    _process_event("__mouse_click__", ax, (i, porcentagens["ttc"][:-2][::-1][i]), 1)
            controle.append("ttc")
        elif cor == "res":
            if "res" not in controle:
                for i in range(0, 10):
                    _process_event("__mouse_click__", ax, (i, mediasresazurina["res"][:-2][::-1][i]), 1)
            controle.append("res")
        elif cor == "am":
            if "am" not in controle:
                for i in range(0,10):
                    _process_event("__mouse_click__", ax, (i, porcentagens["am"][:-2][::-1][i]), 1)
            controle.append("am")
    except (NameError, IndexError):
        pass

def mostrar_valores(): # Função para ativar/desativar a exposição dos valores na linha do eixo X (porcentagem de inibição) no gráfico #
    if var_valores.get() == "Off":
        keyboard.press_and_release("v")
    if var_valores.get() == "On":
        keyboard.press_and_release("v")

def grid_grafico(): # Função para ativar/desativar as linhas de grade do gráfico #
    if var_grid.get() == "On":
        ax.grid(visible=True)
        canvas.draw()
    else:
        ax.grid(visible=False)

def titulo_grafico(state): # Função para ativar/desativar o título do gráfico #
    if state == 'show':
        if var_titulo.get() == "On":
            titulografico.set_visible(True)
        else:
            titulografico.set_visible(False)
    if state == "legenda":
        if var_legenda.get() == "On":
            legenda.set_visible(True)
        else:
            legenda.set_visible(False)

def salvargrafico(choice): # Função para salvar o gráfico em formato de arquivo #
    if choice == ".jpg":
        archive = asksaveasfilename(initialfile="Gráfico", initialdir="Gráficos", filetypes=(("JPG","*.jpg"),('all files','*.*')), defaultextension=".*", title="grafico")
        if archive:
            grafico1.savefig(archive, dpi=300)
            tkinter.messagebox.showinfo(title="Salvar gráfico", message= "Gráfico salvo com sucesso!")
        else:
            return
    elif choice == ".png":
        archive = asksaveasfilename(initialfile="Gráfico", initialdir="Gráficos", filetypes=(("PNG","*.png"),('all files','*.*')), defaultextension=".*", title="grafico")
        if archive:
            grafico1.savefig(archive, dpi=300)
            tkinter.messagebox.showinfo(title="Salvar gráfico", message= "Gráfico salvo com sucesso!")
        else:
            return
    elif choice == ".pdf":
        archive = asksaveasfilename(initialfile="Gráfico", initialdir="Gráficos", filetypes=(("PDF","*.pdf"),('all files','*.*')), defaultextension=".*", title="grafico")
        if archive:
            grafico1.savefig(archive)
            tkinter.messagebox.showinfo(title="Salvar gráfico", message= "Gráfico salvo com sucesso!")
    elif choice == ".svg":
        archive = asksaveasfilename(initialfile="Gráfico", initialdir="Gráficos", filetypes=(("SVG","*.svg"),('all files','*.*')), defaultextension=".*", title="grafico")
        if archive:
            grafico1.savefig(archive)
            tkinter.messagebox.showinfo(title="Salvar gráfico", message= "Gráfico salvo com sucesso!")
        else:
            return

def salvar_csv(): # Função para salvar o gráfico em .csv #
    archive = asksaveasfilename(initialfile="Dados", initialdir="Dados", filetypes=(("CSV","*.csv"),('all files','*.*')), defaultextension=".*", title="dados")
    if archive:
        hearders_format = []
        headers = tabela_valores.headers()
        for valor in headers:
            novo_valor = str(valor).replace("\n", " ")
            hearders_format.append(novo_valor)
        data = tabela_valores.get_sheet_data()
        with open(archive, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(hearders_format)
            writer.writerows(data)
            tkinter.messagebox.showinfo(title="Salvar gráfico", message= "Gráfico salvo com sucesso!")

#####* Introduz os elementos gráficos da janela de informações #####
                
def janelainformacoes(): # Widgets principais (frames, botões, janelas de texto) #
    global moldurabarra, moldurainfo, botao_sobre, botao_codigofonte, botao_tutorial, botao_prereq, botao_hyperlinkcodigo, botao_hyperlinksobre, textbox_sobre, textbox_codigo
    moldurabarra = ctk.CTkFrame(janela_info, height= 530, width=1050, fg_color="#2B6AD0", corner_radius=16)
    moldurabarra.place(x=20)
    moldurabarra.pack_propagate(False)
    moldurainfo=ctk.CTkTabview(master=janela_info, width=850, height=538, fg_color="#FBFBFE", state="disabled", anchor="ne", bg_color="#FBFBFE", segmented_button_fg_color="#FBFBFE", segmented_button_unselected_color="#FBFBFE", segmented_button_selected_hover_color="#FBFBFE", segmented_button_unselected_hover_color="#FBFBFE", text_color_disabled="#FBFBFE", segmented_button_selected_color="#FBFBFE")
    moldurainfo._outer_button_overhang = 0
    moldurainfo._segmented_button.grid_forget()
    moldurainfo._configure_grid()
    moldurainfo.place(x=220)
    moldurainfo.pack_propagate(False)

    sobre = moldurainfo.add("sobre")
    codigo_fonte = moldurainfo.add("codigo_fonte")
    tutorial = moldurainfo.add("tutorial")
    pre_requisitos = moldurainfo.add("pre_requisitos")

    botao_sobre = criarbotao_informacoes("> Sobre o projeto", lambda: tab_switch_info("sobre"))
    botao_sobre.place(x=15, y=120)
    ctk.CTkLabel(sobre, wraplength=840, anchor="center", font=ctk.CTkFont(family="Segoe UI", size=19, weight='bold'),justify="center", text_color="#2B6AD0", text="Este projeto faz parte do trabalho de conclusão de curso em Biomedicina realizado pelo aluno Luiz Henrique Reinert, sob orientação da Prof.ª Dr.ª Katiany Rizzieri Caleffi Ferracioli.").pack(anchor="w", pady=15)
    textbox_sobre = criartexto(sobre, strings_txt["sobre"])
    botao_hyperlinksobre = ctk.CTkButton(sobre, text="https://doi.org/10.46311/2318-0579.60.eUJ4398", font=ctk.CTkFont(family="Segoe UI", size=17), fg_color="#FBFBFE", hover=False, text_color="blue", command= lambda: hyperlink("https://doi.org/10.46311/2318-0579.60.eUJ4398"))
    if scale == 125:
        botao_hyperlinksobre.place(x=15, y=176)
    else:
        botao_hyperlinksobre.place(x=15, y=173)

    botao_codigofonte= criarbotao_informacoes("> Código-fonte", lambda: tab_switch_info("botao_codigofonte"))
    botao_codigofonte.place(x=15, y=200)
    ctk.CTkLabel(codigo_fonte, wraplength=840, font=ctk.CTkFont(family="Segoe UI", size=35, weight='bold'), text_color="#2B6AD0", justify="left", text="Sobre o código fonte\n―――――――――――――――――――――――――――").pack(anchor="nw", pady=15, padx=15)
    textbox_codigo = criartexto(codigo_fonte, strings_txt["codigo_fonte"])
    botao_hyperlinkcodigo = ctk.CTkButton(codigo_fonte, text="https://github.com/luizreinert/Spectra", border_color='#FBFBFE', font=ctk.CTkFont(family="Segoe UI", size=17), fg_color="#FBFBFE", hover=False, text_color="blue", command= lambda: hyperlink("https://github.com/luizreinert/Spectra"))
    if scale == 125:
        botao_hyperlinkcodigo.place(x=285, y=284)
    else:
        botao_hyperlinkcodigo.place(x=285, y=276)

    botao_prereq = criarbotao_informacoes("> Pré-requisitos", lambda: tab_switch_info("pre_requisitos"))
    botao_prereq.place(x=15, y=280)
    ctk.CTkLabel(pre_requisitos, wraplength=840, font=ctk.CTkFont(family="Segoe UI", size=35, weight='bold'), text_color="#2B6AD0", justify="left", text="O que preciso saber antes?\n―――――――――――――――――――――――――――").pack(anchor="nw", pady=15, padx=15)
    textbox_prereq = criartexto(pre_requisitos, strings_txt["pre_requisitos"])
    

    botao_tutorial = criarbotao_informacoes("> Tutorial", lambda: tab_switch_info("tutorial"))
    botao_tutorial.place(x=15, y=360)
    ctk.CTkLabel(tutorial, wraplength=840, font=ctk.CTkFont(family="Segoe UI", size=35, weight='bold'), justify="left", text_color="#2B6AD0", text="Como usar o Spectra?\n―――――――――――――――――――――――――――").pack(anchor="nw", pady=15, padx=15)
    textbox_tutorial = criartexto(tutorial, strings_txt["tutorial"])

    tab_switch_info("sobre")

def criarbotao_informacoes(texto, comando): # Cria o botão na barra lateral da janela de informações #
    botao = ctk.CTkButton(moldurabarra, cursor='hand2', width=170, height=50, hover_color="#FBFBFE", font=ctk.CTkFont(family="Segoe UI", size=17, weight='bold'), text=texto, fg_color="#2B6AD0", corner_radius=10, command = comando)
    return botao

def criartexto(main, texto): # Cria o texto pré-definido #
    if texto == strings_txt["sobre"]:
        textbox = ctk.CTkTextbox(main, wrap="word", width=800, height=420, font=ctk.CTkFont(family="Segoe UI", size=16), cursor="arrow")
        textbox.place(x=15, y=80) 
    else:
        textbox = ctk.CTkTextbox(main, wrap="word", width=800, height=410, font=ctk.CTkFont(family="Segoe UI", size=17), cursor="arrow")
        textbox.place(x=15, y=110) 
    textbox.insert("0.0", *texto)
    textbox.bindtags((str(textbox), str(textbox), "all"))
    textbox.bind('<Button-1>', text_break())

def hyperlink(link): # Cria o hyperlink ligado aos botões referentes ao link #
    if link == "https://github.com/luizreinert/Spectra":
        open_new(link)
    if link == "https://doi.org/10.46311/2318-0579.60.eUJ4398":
        open_new(link)

#####* Funções referentes à funcionalidades internas e ajustes #####
   
def hover_fix(tab, botao, icon): # Ajusta o hover dos botões, mantendo a cor do botão até mudar de aba. Também impede o acesso da aba "Gráficos" caso não seja gerado um gráfico #
    if tab == "sair":
        root.destroy()
    if tab != "config" and tab != "janela_grafico":
        fundocinza.set(tab)
        botao.unbind('<Enter>')
        botao.unbind('<Leave>')
        botao.configure(fg_color="#FBFBFE", image=icon, text_color="#2B6AD0")
    if tab == "janela_grafico":
        if all(not lista for lista in porcentagens.values()) == False or len(mediasresazurina["res"]) > 0:
            fundocinza.set(tab)
            botao.unbind('<Enter>')
            botao.unbind('<Leave>')
            botao.configure(fg_color="#FBFBFE", image=icon, text_color="#2B6AD0")
        else:
            fundocinza.set(tab)
            tkinter.messagebox.showerror(title="Erro", message="Nenhum gráfico encontrado!")
            fundocinza.set(fundocinza.get())

def tab_switch(botao): # Vincula os botões laterais à mudança de abas #
    if botao == "dados":
        hover_fix("dados", botao_dados, tabelaA)
    else:
        botao_dados.configure(fg_color="#2B6AD0", image=tabelaB, text_color="#FBFBFE")
        botao_dados.bind('<Enter>', lambda e: botao_dados.configure(image=tabelaA, fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_dados.bind('<Leave>', lambda e: botao_dados.configure(image=tabelaB, fg_color="#2B6AD0", text_color="#FBFBFE"))
    if botao == "janela_grafico":
        hover_fix("janela_grafico", botao_grafico, graficoA)
    else:
        botao_grafico.configure(fg_color="#2B6AD0", image=graficoB, text_color="#FBFBFE")
        botao_grafico.bind('<Enter>', lambda e: botao_grafico.configure(image=graficoA, fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_grafico.bind('<Leave>', lambda e: botao_grafico.configure(image=graficoB, fg_color="#2B6AD0", text_color="#FBFBFE"))
    if botao == "informacoes":
        hover_fix("informacoes", botao_info, infoA)
    else:
        botao_info.configure(fg_color="#2B6AD0", image=infoB, text_color="#FBFBFE")
        botao_info.bind('<Enter>', lambda e: botao_info.configure(image=infoA, fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_info.bind('<Leave>', lambda e: botao_info.configure(image=infoB, fg_color="#2B6AD0", text_color="#FBFBFE"))
    if botao == "sair":
        hover_fix("sair", botao_sair, sairA)
    else:
        botao_sair.configure(fg_color="#2B6AD0", image=sairB, text_color="#FBFBFE")
        botao_sair.bind('<Enter>', lambda e: botao_sair.configure(image=sairA, fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_sair.bind('<Leave>', lambda e: botao_sair.configure(image=sairB, fg_color="#2B6AD0", text_color="#FBFBFE"))
    if botao == "config":
        hover_fix("config", botao_config, configA)
    else:
        botao_config.configure(fg_color="#2B6AD0", image=configB, text_color="#FBFBFE")
        botao_config.bind('<Enter>', lambda e: botao_config.configure(image=configA, fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_config.bind('<Leave>', lambda e: botao_config.configure(image=configB, fg_color="#2B6AD0", text_color="#FBFBFE"))

def popupmenu(event): # Bind que vincula o menu de corantes ao botão direito do mouse na tabela principal #
    menu = tkinter.Menu(root, tearoff=0)
    menu.add_command(label="Sem corante", command=lambda a="sc": corante_escolhido(a), activebackground=cores_corantes("sc"), font=fonte_iconesnormal)
    menu.add_command(label="TTC", command=lambda a="ttc": corante_escolhido(a), activebackground=cores_corantes("ttc"), font=fonte_iconesnormal)
    menu.add_command(label="Resazurina 570nm", command=lambda a="res_570": corante_escolhido(a), activebackground="#660099", font=fonte_iconesnormal)
    menu.add_command(label="Resazurina 600nm", command=lambda a="res_600": corante_escolhido(a), activebackground="#6900EF", font=fonte_iconesnormal)
    menu.add_command(label="Azul de Metileno", command=lambda a="am": corante_escolhido(a), activebackground="#64B1FF", font=fonte_iconesnormal)
    menu.add_command(label="Sem corante/Deletar", command=lambda a="pv": corante_escolhido(a), activebackground="#54546B", font=fonte_iconesnormal)
    menu.post(event.x_root, event.y_root)

def hoverfix_info(tab, botao): # Ajusta o hover dos botões, mantendo a cor do botão até mudar de aba #
    moldurainfo.set(tab)
    botao.unbind('<Enter>')
    botao.unbind('<Leave>')
    botao.configure(fg_color="#FBFBFE",text_color="#2B6AD0")

def tab_switch_info(botao): #Ajusta o hover dos botões, mantendo a cor do botão até mudar de aba #
    if botao == "sobre":
        hoverfix_info("sobre", botao_sobre)
    else:
        botao_sobre.configure(fg_color="#2B6AD0", text_color="#FBFBFE")
        botao_sobre.bind('<Enter>', lambda e: botao_sobre.configure(fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_sobre.bind('<Leave>', lambda e: botao_sobre.configure(fg_color="#2B6AD0", text_color="#FBFBFE"))
    if botao == "botao_codigofonte":
        hoverfix_info("codigo_fonte", botao_codigofonte)
    else:
        botao_codigofonte.configure(fg_color="#2B6AD0", text_color="#FBFBFE")
        botao_codigofonte.bind('<Enter>', lambda e: botao_codigofonte.configure(fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_codigofonte.bind('<Leave>', lambda e: botao_codigofonte.configure(fg_color="#2B6AD0", text_color="#FBFBFE"))
    if botao == "tutorial":
        hoverfix_info("tutorial", botao_tutorial)
    else:
        botao_tutorial.configure(fg_color="#2B6AD0", text_color="#FBFBFE")
        botao_tutorial.bind('<Enter>', lambda e: botao_tutorial.configure(fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_tutorial.bind('<Leave>', lambda e: botao_tutorial.configure(fg_color="#2B6AD0", text_color="#FBFBFE"))
    if botao == "pre_requisitos":
        hoverfix_info("pre_requisitos", botao_prereq)
    else:
        botao_prereq.configure(fg_color="#2B6AD0", text_color="#FBFBFE")
        botao_prereq.bind('<Enter>', lambda e: botao_prereq.configure(fg_color="#FBFBFE", text_color="#2B6AD0"))
        botao_prereq.bind('<Leave>', lambda e: botao_prereq.configure(fg_color="#2B6AD0", text_color="#FBFBFE"))

def fix_scale(): # Conserta o tamanho da tabela quando a escala do windows é maior (125%) #
    if scale == 125:
            Sheet.configure(tabela, width=1270, height=370)
            tabela.set_all_column_widths(103)
            tabela.set_all_row_heights(43)

def text_break(): # Bind que impede a edição da textbox na aba informações #
    return "break"

def annotations_config(sel): # Customiza os valores do mplcursors (geral) # 
    sel.annotation.get_bbox_patch().set(boxstyle="square,pad=0.01", linewidth=0, alpha=0, edgecolor="#FFFFFF")
    if sel.artist.get_label() == "Sem corante":
        sel.annotation.set(text=(f'{sel.target[1]:.1f}'), color=cores_corantes("sc"), position=(sel.target[0], sel.target[1]-12))
    elif sel.artist.get_label() == "TTC":
        sel.annotation.set(text=(f'{sel.target[1]:.1f}'), color=cores_corantes("ttc"),position=(sel.target[0], sel.target[1]-14))
    elif sel.artist.get_label() == "Resazurina":
        sel.annotation.set(text=(f'{sel.target[1]:.1f}'), color=cores_corantes("res"),position=(sel.target[0], sel.target[1]-16))
    elif sel.artist.get_label() == "Azul de Metileno":
        sel.annotation.set(text=(f'{sel.target[1]:.1f}'), color=cores_corantes("am"),position=(sel.target[0], sel.target[1]-6))
    sel.annotation.arrow_patch.set(arrowstyle="-", fc="black")
    
def annotations_config_hover(sel1):
    sel1.annotation.get_bbox_patch().set(boxstyle="square,pad=0.01", linewidth=0, alpha=0, edgecolor="#FFFFFF")
    if sel1.artist.get_label() == "Sem corante":
        sel1.annotation.set(text=(f'{sel1.target[1]:.1f}'), color=cores_corantes("sc"),position=(sel1.target[0], sel1.target[1]-12))
    elif sel1.artist.get_label() == "TTC":
        sel1.annotation.set(text=(f'{sel1.target[1]:.1f}'), color=cores_corantes("ttc"),position=(sel1.target[0], sel1.target[1]-14))
    elif sel1.artist.get_label() == "Resazurina":
        sel1.annotation.set(text=(f'{sel1.target[1]:.1f}'), color=cores_corantes("res"),position=(sel1.target[0], sel1.target[1]-16))
    elif sel1.artist.get_label() == "Azul de Metileno":
        sel1.annotation.set(text=(f'{sel1.target[1]:.1}'), color=cores_corantes("am"),position=(sel1.target[0], sel1.target[1]-6))
    sel1.annotation.arrow_patch.set(arrowstyle="-", fc="black")
    sel1.annotation.set_visible(True)

def cores_corantes(cor_corante):
    if cor_corante == "sc":
        try:
            return sc_alt
        except NameError:
            return "#999999"
    if cor_corante == "ttc":
        try:
            return ttc_alt
        except NameError:
            return "#FF6666"
    if cor_corante == "res":
        try:
            return res_alt
        except:
            return "#660099"
    if cor_corante == "am":
        try:
            return am_alt
        except:
            return "#64B1FF"

layout()
janelagrafico()
janeladados()
janelainformacoes()
fix_scale()

root.mainloop()
