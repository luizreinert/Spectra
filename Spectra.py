import customtkinter as ctk
import tkinter
import tkinter.messagebox
from tkinter.filedialog import asksaveasfilename
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
from tksheet import Sheet
from CTkScrollableDropdown import *
import mplcursors
import json

with open('textfile.txt', 'r', encoding='utf-8') as file:
    strings_txt = json.load(file)
annotations = []

ctk.set_appearance_mode("light")
novajanela = ctk.CTk()
novajanela.iconbitmap("ícones\logos\icone_programa.ico")
novajanela.resizable(False, False)
novajanela.geometry("1300x600+450+190")
novajanela.title("Spectra")
fonte_icones = ctk.CTkFont(family="Segoe UI", size=17, weight='bold')
fonte_iconesnormal = ctk.CTkFont(family="Segoe UI", size=14, weight='normal')
fonte = ctk.CTkFont(family="Segoe UI", size=16, weight='bold')
fontenormal = ctk.CTkFont(family="Segoe UI", size=18)
fontegrande = ctk.CTkFont(family="Segoe UI", size=22)
fontetitulos = ctk.CTkFont(family="Segoe UI", size=40, weight='bold')

imagemlogo = ctk.CTkImage(size=[150, 60], light_image=Image.open("ícones\logos\logo_nome.png"))
tabelaB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\gtabela_b.png"))
tabelaA = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\gtabela_a.png"))
duvidasB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidas_b.png"))
duvidasA = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidas_a.png"))
graficoB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\grafico_b.png"))
graficoA = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\grafico_a.png"))
configB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\config_b.png"))
configA = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\config_a.png"))
sairB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\sair_b.png"))
sairA = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\sair_a.png"))
infoB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidas_b.png"))
infoA = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidas_a.png"))
pdf = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\pdf.png"))
png = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\png.png"))
jpg = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\jpg.png"))
svg = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\svg.png"))

def criarbotao_pLateral(root, icon, texto):
    botao = ctk.CTkButton(master= root, cursor='hand2', width=150, height=40, image=icon, hover_color="#FBFBFE", font= fonte_icones, fg_color="#2B6AD0", text=texto, anchor="w")
    return botao

def criarbarralateral():
    global barralateral, framebarra, botao_dados, botao_grafico, botao_info, botao_config, botao_sair, fundocinza, janela_dados, janela_grafico, janela_info
    barralateral = ctk.CTkFrame(master=novajanela, width=200, height=600, fg_color="#2B6AD0", bg_color="#2B6AD0")
    barralateral.pack(fill="y", side= "left")
    barralateral.pack_propagate(0)
    framebarra = ctk.CTkFrame(master=barralateral, width=200, height=325, fg_color="transparent")
    framebarra.pack(fill="none", anchor="center", expand="True")
    fundocinza = ctk.CTkTabview(master=novajanela, width=1129, height=600, fg_color="#E3E7F1", state="disabled", anchor="ne", bg_color="#E3E7F1", text_color="#E3E7F1", segmented_button_fg_color="#E3E7F1", segmented_button_unselected_color="#E3E7F1", segmented_button_selected_hover_color="#E3E7F1", segmented_button_unselected_hover_color="#E3E7F1", text_color_disabled="#E3E7F1", segmented_button_selected_color="#E3E7F1")
    fundocinza._outer_button_overhang = 0
    fundocinza._segmented_button.grid_forget()
    fundocinza._configure_grid()
    janela_dados = fundocinza.add("dados")
    janela_grafico= fundocinza.add("janela_grafico")
    janela_info = fundocinza.add("informacoes")
    fundocinza.pack(after=barralateral, side= "right")
    fundocinza.pack_propagate(0)
    imglogo = ctk.CTkLabel(master=barralateral, image=imagemlogo, text="")
    imglogo.place(x=10, y=20)
    botao_dados = criarbotao_pLateral(framebarra, tabelaB, "Inserir dados")
    botao_dados.pack(anchor="center", pady=10)
    botao_dados.configure(command= lambda: tab_switch("dados"))

    botao_grafico = criarbotao_pLateral(framebarra, graficoB, "Gráfico")
    botao_grafico.pack(anchor="center", pady=10)
    botao_grafico.configure(command= lambda : tab_switch("janela_grafico"))

    botao_info = criarbotao_pLateral(framebarra, infoB, "Informações")
    botao_info.pack(anchor="center", pady=10)
    botao_info.configure(command= lambda: tab_switch("informacoes"))

    botao5 = criarbotao_pLateral(framebarra, infoB, "Null")
    botao5.pack(anchor="center", pady=10)
    botao5.configure(state="disabled", command= lambda: tab_switch("informacoes"))

    botao_sair = criarbotao_pLateral(framebarra, sairB, "Sair")
    botao_sair.pack(anchor="center", pady=10)
    botao_sair.configure(command= lambda: tab_switch("sair"))
    

    barralateral.configure(width=180)
    botao_config = criarbotao_pLateral(barralateral, configB, "Configurações")
    botao_config.place(y=530, x=10)
    botao_config.configure(command= lambda: tab_switch("config"))
    tab_switch("dados")

def hover_fix(tab, botao, icon):
    if tab == "sair":
        novajanela.destroy()
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
            tkinter.messagebox.showerror(title="Erro", message="Nenhum gráfico encontrado!")
            fundocinza.set(fundocinza.get())

def tab_switch(botao):
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

def janeladados():
    global botao_dados, tabela, dados_tabela, teste, valores_apagar, resultados_medias, porcentagens, mediasresazurina
    moldura = ctk.CTkFrame(janela_dados, height=320, width=1030, fg_color="#FFFFFF", corner_radius=16)
    moldura.place(x=30, y=220)
    teste = ctk.CTkFrame(janela_dados, height=300, width=1100, fg_color="#E3E7F1", bg_color="#E3E7F1")
    teste.place(x=65, y=247)
    tabela = Sheet(teste, align="center", max_column_width=77, total_columns=12, total_rows=8, column_width=77, height=282, width=970, row_height=32, show_x_scrollbar=False, show_y_scrollbar=False, empty_horizontal=0, empty_vertical=0)
    tabela.create_header_dropdown(c = 10, values=["C+", "C-"])
    tabela.create_header_dropdown(c = 11, values=["C-", "C+"])
    Sheet.set_options(tabela, table_bg="#E3E7F1", table_grid_fg="#FFFFFF", table_selected_cells_bg="#C6CAD1", index_bg="#2B6AD0", index_grid_fg="#FFFFFF", header_bg="#2B6AD0", header_grid_fg="#FFFFFF", font=('Helvetica', 10, 'normal'), table_fg='#000000', index_fg='#E3E7F1', header_fg='#E3E7F1', table_selected_cells_border_fg="#2B6AD0", table_selected_rows_border_fg ="#2B6AD0", table_selected_columns_border_fg= "#2B6AD0")
    tabela.bind('<MouseWheel>', lambda a: scrollwheel)
    tabela.enable_bindings("all")
    tabela.disable_bindings("right_click_popup_menu", "column_height_resize", "column_width_resize", "row_width_resize", "row_height_resize")
    tabela.bind("<3>", popupmenu)
    tabela.pack(expand="True")
    frame_corantes()
    frame_inserir()
    frame_bacteria()
    dados_tabela = {'sc': [],'ttc': [], 'res_570': [], 'res_600': [], 'am': []}
    valores_apagar = []
    resultados_medias = {'sc': [],'ttc': [], 'res_570': [], 'res_600': [], 'am': []}
    porcentagens = {"sc": [], "ttc": [], "res_570": [], 'res_600': [], "am": []}
    mediasresazurina = {"res": []}

def popupmenu(event):
    menu = tkinter.Menu(novajanela, tearoff=0)
    menu.add_command(label="Sem corante", command=lambda a="sc": corante_escolhido(a), activebackground="#999999", font=fonte_iconesnormal)
    menu.add_command(label="TTC", command=lambda a="ttc": corante_escolhido(a), activebackground="#FF6666", font=fonte_iconesnormal)
    menu.add_command(label="Resazurina 570nm", command=lambda a="res_570": corante_escolhido(a), activebackground="#660099", font=fonte_iconesnormal)
    menu.add_command(label="Resazurina 600nm", command=lambda a="res_600": corante_escolhido(a), activebackground="#6900EF", font=fonte_iconesnormal)
    menu.add_command(label="Azul de Metileno", command=lambda a="am": corante_escolhido(a), activebackground="#64B1FF", font=fonte_iconesnormal)
    menu.add_command(label="Sem corante/Deletar", command=lambda a="pv": corante_escolhido(a), activebackground="#54546B", font=fonte_iconesnormal)
    menu.post(event.x_root, event.y_root)


# Cria os botões no frame de corantes
def criar_botao_corantes(cor):
    if cor == "sc":
        botao = ctk.CTkButton(frame_corantes, corner_radius=10, height=35, width=250, bg_color="#FBFBFE", fg_color="#999999", text="Sem corante", text_color="#FBFBFE", font=fonte, command= lambda a="sc": corante_escolhido(a))
    elif cor == "ttc":
        botao = ctk.CTkButton(frame_corantes, corner_radius=10, height=35, width=250, bg_color="#FBFBFE", fg_color="#FF6666", text="TTC 480 nm", text_color="#FBFBFE", font=fonte, command= lambda a="ttc": corante_escolhido(a))  
    elif cor == "res_570":
        botao = ctk.CTkButton(frame_corantes, corner_radius=10, height=35, width=250, bg_color="#FBFBFE", fg_color="#660099", text="Resazurina 570 nm", text_color="#FBFBFE", font=fonte, command= lambda a="res_570": corante_escolhido(a))
    elif cor == "res_600":
        botao = ctk.CTkButton(frame_corantes, corner_radius=10, height=35, width=250, bg_color="#FBFBFE", fg_color="#6900EF", text="Resazurina 600 nm", font = fonte, text_color="#FBFBFE", command= lambda a="res_600": corante_escolhido(a))   
    elif cor == "am":
        botao = ctk.CTkButton(frame_corantes, corner_radius=10, height=35, width=250, bg_color="#FBFBFE", fg_color="#64B1FF", text="Azul de Metileno 600 nm", font = fonte, text_color="#FBFBFE", command= lambda a="am": corante_escolhido(a))
    return botao     

def frame_corantes():
    global frame_corantes
    frame_corantes = ctk.CTkFrame(janela_dados, height=198, width=300, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=16)
    frame_corantes.pack(anchor="ne", padx= 50)
    frame_corantes.propagate(False)
    botao_sc = criar_botao_corantes("sc")
    botao_sc.pack(in_= frame_corantes ,expand="True")
    botao_ttc = criar_botao_corantes("ttc")
    botao_ttc.pack(in_= frame_corantes ,expand="True")
    botao_res = criar_botao_corantes("res_570")
    botao_res.pack(in_= frame_corantes ,expand="True")
    botao_res2 = criar_botao_corantes("res_600")
    botao_res2.pack(in_= frame_corantes ,expand="True")
    botao_am = criar_botao_corantes("am")
    botao_am.pack(in_= frame_corantes , expand="True")
    botao_pv = ctk.CTkButton(frame_corantes, corner_radius=10, height=35, width=250, bg_color="#FBFBFE", fg_color="#54546B", hover=False, text="Poço vazio/Resetar", text_color="#FBFBFE", font=fonte, command= lambda a="pv": corante_escolhido(a))
    botao_pv.pack(in_= frame_corantes , expand="True")

def corante_escolhido(a):
    try:
        if a == "sc":
            if len(dados_tabela["sc"]) >= 1:
                del dados_tabela["sc"][:]
                del resultados_medias["sc"][:] 
            Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#999999", fg = "#000000", redraw = True, overwrite = True)
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
            Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#FF6666", fg = "#000000", redraw = True, overwrite = True)      
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

def funcao_botaoapagar(corante):
    if valores_apagar == dados_tabela[corante] or valores_apagar in dados_tabela[corante]:
        del dados_tabela[corante][:]
        del resultados_medias[corante][:]
        del valores_apagar[:]
def frame_inserir():
    global frame_inslimp
    frame_inslimp = ctk.CTkFrame(janela_dados, height=198, width=300, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=16)
    frame_inslimp.place(x=422)
    frame_inslimp.propagate(False)
    botao_inserir= ctk.CTkButton(frame_inslimp, width=270, height=55, corner_radius=10, cursor='hand2', text="Colar dados", border_color="#999999", border_width=2, font=fontegrande, fg_color="#FBFBFE", text_color='black', command= lambda : tabela.paste(tabela.select_cell(row=0, column=0)))
    botao_inserir.pack(pady=6)
    botao_inserir.bind('<Enter>', lambda e: botao_inserir.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_inserir.bind('<Leave>', lambda e: botao_inserir.configure(text_color="black", fg_color="#FBFBFE"))
    botao_limpar= ctk.CTkButton(frame_inslimp, width=270, height=55, corner_radius=10, cursor='hand2', hover_color="#2B6AD0", border_color="#999999", border_width=2, text="Limpar tabela", font=fontegrande, fg_color="#FBFBFE", text_color='black', command= limpar)
    botao_limpar.pack(pady=6)
    botao_limpar.bind('<Enter>', lambda e: botao_limpar.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_limpar.bind('<Leave>', lambda e: botao_limpar.configure(text_color="black", fg_color="#FBFBFE"))
    botao_gerardados= ctk.CTkButton(frame_inslimp, width=270, height=55, corner_radius=10, cursor='hand2', hover_color="#2B6AD0", border_color="#999999", border_width=2, text="Gerar gráfico", font=fontegrande, fg_color="#FBFBFE", text_color='black', command= calculos)
    botao_gerardados.pack(pady=6)
    botao_gerardados.bind('<Enter>', lambda e: botao_gerardados.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_gerardados.bind('<Leave>', lambda e: botao_gerardados.configure(text_color="black", fg_color="#FBFBFE"))

def frame_bacteria():
    global op_s_aureus, bac_var, botaoresazurina, outra_bac
    titulo_inserirdados = ctk.CTkLabel(janela_dados, text="Inserir dados", font=fontetitulos, text_color="#2B6AD0")
    titulo_inserirdados.place(y=0, x=33)
    frame_escolhabac= ctk.CTkFrame(janela_dados, height=120, width=350, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=16)
    frame_escolhabac.place(y=80, x=33)
    frame_escolhabac.propagate(False)
    bac_var= tkinter.StringVar(value="")
    op_s_aureus= ctk.CTkRadioButton(frame_escolhabac, width=30, height=30, fg_color="#2B6AD0", border_width_checked= 6, text= "Staphylococcus aureus", font=ctk.CTkFont(family="Segoe UI", size=18), text_color="black", command=escolha_bac, variable=bac_var, value="Staphylococcus aureus")
    op_s_aureus.place( x= 10, y= 0)
    op_e_coli= ctk.CTkRadioButton(frame_escolhabac, width=30, height=30, fg_color="#2B6AD0", border_width_checked= 6, text= "Escherichia coli", font=ctk.CTkFont(family="Segoe UI", size=18), text_color="black", command=escolha_bac, variable=bac_var, value="Escherichia coli")
    op_e_coli.place( x= 10, y= 30)
    outra_bac = ctk.CTkRadioButton(frame_escolhabac, width=30, height=30, fg_color="#2B6AD0", border_width_checked= 6, text= "Outra bactéria", font=ctk.CTkFont(family="Segoe UI", size=18), text_color="black", command= escolha_bac, variable=bac_var, value="Outra bacteria")
    outra_bac.place( x= 10, y= 60)
    botaoresazurina = ctk.CTkSwitch(frame_escolhabac, switch_height= 15, progress_color="#2B6AD0", switch_width=30, width=40, height=10, text="Cálculo de resazurina", font=ctk.CTkFont(family="Segoe UI", size=18), command= linhas_resazurina, onvalue="on", offvalue="off")
    botaoresazurina.place(x=7, y=90)

# Adiciona 2 linhas na tabela
def linhas_resazurina():
    if botaoresazurina.get() == "on":
        tabela.sheet_data_dimensions(total_rows=10)
        tabela.set_all_row_heights(25)
    if botaoresazurina.get() == "off":    
        tabela.sheet_data_dimensions(total_rows=8)
        tabela.set_all_row_heights(32)

def escolha_bac():
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
            outrabac_toplevel.after(50, outrabac_toplevel.lift)
            outrabac_toplevel.after(200, lambda: outrabac_toplevel.iconbitmap("ícones\logos\icone_programa.ico"))

            # Strings / Entrada do nome da bactéria
            titulo = ctk.CTkLabel(outrabac_toplevel, text="Configurar bactéria utilizada\n――――――――――――――――――――――――――――", justify="left", font=ctk.CTkFont(family="Segoe UI", size=30), text_color="#2B6AD0").pack(anchor="w", padx=20, pady=7)
            nome_bac = ctk.CTkEntry(outrabac_toplevel, placeholder_text="Digite o nome da bactéria utilizada", width=500, height= 40, font=ctk.CTkFont(family="Segoe UI", size=16))
            nome_bac.pack(anchor="w", pady=5, padx=20)
            desc = ctk.CTkLabel(outrabac_toplevel, text="• Introduza abaixo os 10 valores de diluição do antibiótico, iniciando pela concentração mais alta e seguindo\npara as menores.", justify="left", font=ctk.CTkFont(family="Segoe UI", size=17), text_color="#2B6AD0")
            desc.pack(anchor="w", padx=20, pady=9)
            desc2 = ctk.CTkLabel(outrabac_toplevel, text="Exemplo: Diluição de Ciprofloxacino em Staphylococcus aureus: 8 → 4 → 2 → 1 → 0,5 → 0,25 → 0,125 → 0,06 → 0,03 → 0,02", justify="left", font=ctk.CTkFont(family="Segoe UI", size=15), text_color="black")
            desc2.place(x=20, y=200)
        
            # Tabela de entrada dos valores de diluição
            tabela_diluicoes = Sheet(outrabac_toplevel, show_header=False, show_top_left=False, row_index=["Concentração\nde antibiótico (µg)"], header_align="center", headers=["Diluições"], align="center", width=900, row_index_width=125, height=43, total_columns=10, total_rows=1, row_height=40, column_width=77, show_x_scrollbar=False, show_y_scrollbar=False, empty_horizontal=0, empty_vertical=0)
            Sheet.set_options(tabela_diluicoes, max_column_width=77, index_selected_cells_bg="#2B6AD0", index_selected_cells_fg="#FFFFFF", header_selected_cells_bg="#2B6AD0",header_selected_cells_fg="#FFFFFF", table_bg="#E3E7F1", table_grid_fg="#FFFFFF", table_selected_cells_bg="#C6CAD1", index_bg="#2B6AD0", index_grid_fg="#FFFFFF", header_bg="#2B6AD0", header_grid_fg="#FFFFFF", font=('Helvetica', 10, 'normal'), table_fg='#000000', index_fg='#E3E7F1', header_fg='#E3E7F1', table_selected_cells_border_fg="#2B6AD0", table_selected_rows_border_fg ="#2B6AD0", table_selected_columns_border_fg= "#2B6AD0")
            tabela_diluicoes.enable_bindings("all")
            tabela_diluicoes.disable_bindings("column_height_resize", "column_width_resize", "row_width_resize", "row_height_resize")
            tabela_diluicoes.place(y=240)
            botao_cofirmar = ctk.CTkButton(outrabac_toplevel, cursor='hand2', width=170, height=40, hover=False, font=ctk.CTkFont(family="Segoe UI", size=17, weight='bold'), text="Confirmar", fg_color="#2B6AD0", corner_radius=10, command = confirmar_bac)
            botao_cofirmar.place(x=340, y=295)
            outrabac_toplevel.protocol("WM_DELETE_WINDOW", lambda : outra_bac.configure(state='normal') or outrabac_toplevel.withdraw())

def confirmar_bac():
    global bac_escolhida
    outrabac_toplevel.withdraw()
    outra_bac.configure(state='normal')
    bac_escolhida = "Outra bacteria"

# Limpa os dados da tabela
def limpar():
    del dados_tabela["am"][:], dados_tabela["sc"][:], dados_tabela["ttc"][:], dados_tabela["res_570"][:], dados_tabela["res_600"][:]
    del resultados_medias["am"][:], resultados_medias["sc"][:], resultados_medias["ttc"][:], resultados_medias["res_570"][:], resultados_medias["res_600"][:]
    del porcentagens["am"][:], porcentagens["sc"][:], porcentagens["ttc"][:], porcentagens["res_570"][:], porcentagens["res_600"][:]
    del mediasresazurina["res"][:]
    tabela.set_sheet_data(data=([]), redraw=False, reset_col_positions=False, reset_row_positions=False, reset_highlights=True)
    tabela.refresh

def calculos():
    global bac_escolhida
    try:
        calculos2('sc')
        calculos2('ttc')
        calculos2('res')
        calculos2('am')
        gerar_grafico(bac_escolhida)
    except NameError:
        tkinter.messagebox.showerror(title="Erro", message="Selecione a bactéria utilizada")

# Cria o back-end do gráfico antecipadamente, possibilitando a atualização do mesmo ao gerar novos gráficos
def criar_grafico():
    global ax, grafico1, canvas, fonte_graf
    plt.ion()
    plt.pause(0.005)
    fonte_graf = {'family':'Segoe UI','color':'black','size':10, 'weight':"semibold"}
    grafico1 = plt.figure(figsize=(10, 5), facecolor="#FFFFFF", edgecolor="#FFFFFF", num=1, clear=True)
    grafico1.tight_layout()
    canvas = FigureCanvasTkAgg(master= molduragraf, figure=grafico1)
    canvas.get_tk_widget().pack()
    ax = grafico1.subplots()
    mplcursors.cursor(grafico1)
    plt.close()

def gerar_grafico(bac):
    global dil_saureus
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
        funcaobac(dil_saureus)
    if bac == "Escherichia coli":
        funcaobac(dil_ecoli)
    if bac =="Outra bacteria":
        funcaobac(dil_outrabac)
    plt.pause(0.05)
    canvas.draw()
    mplcursors.cursor(grafico1, hover=2)
    ax.legend(loc=("upper left"))
    ax.set_ylabel("Inibição bacteriana (%)", fontdict=fonte_graf)
    ax.set_xlabel("Concentração de antibiótico (μL)", fontdict=fonte_graf)


def funcao_anotacoes(dil, corante, cor):
    if corante != "res":
        for x, y in zip(dil, porcentagens[corante][:-2][::-1]):
            ann = ax.annotate(text= str(y), xy=(x, y), arrowprops = {'arrowstyle' : '-', 'shrinkB' : 10, 'facecolor' : cor})
            annotations.append(ann)
    else:
        for x, y in zip(dil, mediasresazurina[corante][:-2][::-1]):
            ann = ax.annotate(text= str(y), xy=(x, y), )
            annotations.append(ann)

def grid():
    if var_grid.get() == "On":
        ax.grid(visible=True)
        canvas.draw()
    else:
        ax.grid(visible=False)

def valores_grafico():
    if var_valores.get() == "On":
        for valor in annotations:
            valor.set_visible(True)
    else:
        for valor in annotations:
            valor.set_visible(False)

def funcaobac(diluicao):
    if len(resultados_medias["sc"]) == 12:
        if len(porcentagens["sc"]) > 12:
            del porcentagens["sc"][:-12]
        ax.plot(diluicao, porcentagens["sc"][:-2][::-1], color="#999999", label="Sem corante", marker='.')
        funcao_anotacoes(diluicao, "sc", "#999999")
    if len(resultados_medias["ttc"]) == 12:
        if len(porcentagens["ttc"]) > 12:
            del porcentagens["ttc"][:-12]
        ax.plot(diluicao, porcentagens["ttc"][:-2][::-1], color="#FF6666", label="TTC", marker='.')
        funcao_anotacoes(diluicao, "ttc", "#FF6666")
    if len(resultados_medias["res_570"]) and len(resultados_medias["res_600"]):
        if len(mediasresazurina["res"]) > 12:
            del mediasresazurina["res"][:-12]
        ax.plot(diluicao, mediasresazurina["res"][:-2][::-1], color="#660099", label="Resazurina", marker='.')
        funcao_anotacoes(diluicao, "res", "#660099")
    if len(resultados_medias["am"]) == 12:
        if len(porcentagens["am"]) > 12:
            del porcentagens["am"][:-12]
        ax.plot(diluicao, porcentagens["am"][:-2][::-1], color="#64B1FF", label="Azul de Metileno", marker='.')
        funcao_anotacoes(diluicao, "am", "#64B1FF")

def calculos2(cor):
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
    
def scrollwheel(event):
    return 'break'
    
def janelagrafico():
    global molduragraf, salvarcomo2, var_grid, var_valores
    molduragraf = ctk.CTkFrame(janela_grafico, height=410, width=1050, fg_color="#FFFFFF", corner_radius=16)
    molduragraf.place(x=25, y=115)
    molduragraf.pack_propagate("False")
    molduraopcoes = ctk.CTkFrame(janela_grafico, height=100, width=650, fg_color="#FFFFFF", corner_radius=16)
    molduraopcoes.pack(anchor="ne", padx=30)
    molduraopcoes.pack_propagate(False)
    salvarcomo = ctk.CTkButton(molduraopcoes, width=170, height=55, corner_radius=10, cursor='hand2', hover=False, text="Salvar como:", font=fonte, fg_color="#2B6AD0", text_color='#FBFBFE')
    salvarcomo.pack()
    salvarcomo2 = CTkScrollableDropdown(salvarcomo, values=[".jpg", ".png", ".pdf", ".svg"], font=fontenormal, scrollbar=False, alpha=0.97, height=223, resize=False, image_values=[jpg, png, pdf, svg], fg_color="#FBFBFE", button_color="#C6CAD1", text_color="black", button_height=40, width=160, command= salvargrafico)
    salvarcomo2.configure(hover_color="#2B6AD0")
    var_grid = ctk.StringVar(value="Off")
    var_valores = ctk.StringVar(value="Off")
    botao_grid = ctk.CTkCheckBox(molduraopcoes, width=100, height=20, text="Ativar grid", command= lambda: grid(),variable=var_grid, fg_color="#2B6AD0", onvalue="On", offvalue="Off")
    botao_grid.pack()
    botao_valores = ctk.CTkCheckBox(molduraopcoes, width=100, height=20, text="Ativar valores", command= lambda: (valores_grafico()),variable=var_valores, fg_color="#2B6AD0", onvalue="On", offvalue="Off")
    botao_valores.pack()

def salvargrafico(choice):
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

def criarbotao_informacoes(texto, comando):
    botao = ctk.CTkButton(moldurabarra, cursor='hand2', width=170, height=50, hover_color="#FBFBFE", font=ctk.CTkFont(family="Segoe UI", size=17, weight='bold'), text=texto, fg_color="#2B6AD0", corner_radius=10, command = comando)
    return botao

def criartexto(main, texto):
    if texto == strings_txt["sobre"]:
        textbox = tkinter.Text(main, wrap="word", relief="flat", blockcursor=True, width=86, height=17, font=ctk.CTkFont(family="Segoe UI", size=16), cursor="arrow")
        textbox.place(x=15, y=80) 
    else:
        textbox = tkinter.Text(main, wrap="word", relief="flat", blockcursor=True, width=90, height=17, font=ctk.CTkFont(family="Segoe UI", size=17), cursor="arrow")
        textbox.place(x=15, y=110) 
    textbox.insert("0.0", *texto)
    textbox.bindtags((str(textbox), str(textbox), "all"))

def janelainformacoes():
    global moldurabarra, moldurainfo, botao_sobre, botao_codigofonte, botao_tutorial, botao_prereq
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
    
    botao_codigofonte= criarbotao_informacoes("> Código-fonte", lambda: tab_switch_info("botao_codigofonte"))
    botao_codigofonte.place(x=15, y=200)
    ctk.CTkLabel(codigo_fonte, wraplength=840, font=ctk.CTkFont(family="Segoe UI", size=35, weight='bold'), text_color="#2B6AD0", justify="left", text="Sobre o código fonte\n―――――――――――――――――――――――――――").pack(anchor="nw", pady=15, padx=15)
    textbox_codigo = criartexto(codigo_fonte, strings_txt["codigo_fonte"])
    
    botao_prereq = criarbotao_informacoes("> Pré-requisitos", lambda: tab_switch_info("pre_requisitos"))
    botao_prereq.place(x=15, y=280)
    ctk.CTkLabel(pre_requisitos, wraplength=840, font=ctk.CTkFont(family="Segoe UI", size=35, weight='bold'), text_color="#2B6AD0", justify="left", text="O que preciso saber antes?\n―――――――――――――――――――――――――――").pack(anchor="nw", pady=15, padx=15)
    textbox_codigo = criartexto(pre_requisitos, strings_txt["pre_requisitos"])

    botao_tutorial = criarbotao_informacoes("> Tutorial", lambda: tab_switch_info("tutorial"))
    botao_tutorial.place(x=15, y=360)
    ctk.CTkLabel(tutorial, wraplength=840, font=ctk.CTkFont(family="Segoe UI", size=35, weight='bold'), justify="left", text_color="#2B6AD0", text="Como usar o Spectra?\n―――――――――――――――――――――――――――").pack(anchor="nw", pady=15, padx=15)
    textbox_tutorial = criartexto(tutorial, strings_txt["tutorial"])

    tab_switch_info("sobre")

def hoverfix_info(tab, botao):
    moldurainfo.set(tab)
    botao.unbind('<Enter>')
    botao.unbind('<Leave>')
    botao.configure(fg_color="#FBFBFE",text_color="#2B6AD0")

def tab_switch_info(botao):
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

criarbarralateral()
janeladados()
janelagrafico()
janelainformacoes()
criar_grafico()

novajanela.mainloop()
