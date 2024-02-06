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
import webbrowser

ctk.set_appearance_mode("light")
root = ctk.CTk()
root.iconbitmap("ícones\logos\icone_programa.ico")
#primeira janela
root.resizable(False, False)
root.geometry("450x660+770+190")
root.title("Spectra")
fonte_icones = ctk.CTkFont(family="Segoe UI", size=15, weight='bold')
fonte_iconesnormal = ctk.CTkFont(family="Segoe UI", size=14, weight='normal')
fonte = ctk.CTkFont(family="Segoe UI", size=16, weight='bold')
fontenormal = ctk.CTkFont(family="Segoe UI", size=18)
fontegrande = ctk.CTkFont(family="Segoe UI", size=22)
fontetitulos = ctk.CTkFont(family="Segoe UI", size=44, weight='bold')

imagemlogo = ctk.CTkImage(size=[150, 60], light_image=Image.open("ícones\logos\logo_nome.png"))
graficoB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\gtabela_b.png"))
graficoR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\gtabela_a.png"))
duvidasB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidas_b.png"))
duvidasR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidas_a.png"))
hisgraficosB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\grafico_b.png"))
hisgraficosR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\grafico_a.png"))
configB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\config_b.png"))
configR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\config_a.png"))
sairB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\sair_b.png"))
sairR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\sair_a.png"))
infoB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\info_b.png"))
infoR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\info_r.png"))
pdf = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\pdf.png"))
png = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\png.png"))
jpg = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\jpg.png"))
svg = ctk.CTkImage(size=[25, 25], light_image=Image.open("ícones\svg.png"))

def criarbotao_telainicial(texto, comando):
    botao = ctk.CTkButton(master=root, text=texto, cursor='@Aero.cur', hover_color="#6856CB", text_color="#6856CB", font=("Arial", 20), width=288, height=66, corner_radius=16, fg_color="#FCFAFA", border_width=3, border_color='#E9DBEA', background_corner_colors=['#5E7DCA', '#C497E6', '#C497E6', '#5E7DCA'], command=comando)
    botao.pack(expand=False, pady=37)
    botao.bind('<Enter>', lambda e: botao.configure(text_color="#FCFAFA", fg_color="#6856CB"))
    botao.bind('<Leave>', lambda e: botao.configure(text_color="#6856CB", fg_color="#FCFAFA"))
    return botao

def telainicial():
    logotelainicial = ctk.CTkImage(size=[450, 200], light_image=Image.open("Now Open!.png"))
    framesuperior = ctk.CTkFrame(master=root, width=450, height=280, fg_color="#FCFAFA")
    framesuperior.place(relx= 1, rely=0)
    framesuperior.pack()
    inserirlogotelainicial = ctk.CTkLabel(master=framesuperior, image=logotelainicial, text="")
    inserirlogotelainicial.place(relx= 434, rely=0)
    inserirlogotelainicial.pack()
    imagemdefundo = ctk.CTkImage(size=[450, 460], light_image=Image.open("1-fundo.png"))
    label = ctk.CTkLabel(master=root, image=imagemdefundo, text="")
    label.pack(fill="both")
    label.place(relx=0.5, rely=0.651, anchor="center")
    versao = ctk.CTkLabel(master=root, text="v1.0", font=("Arial", 20), bg_color="#4777C3", text_color="#FCFAFA")
    versao.pack()
    versao.place(relx=0.02, rely=0.95)
    criarbotao_telainicial("Iniciar", telaprincipal)
    criarbotao_telainicial("Ajuda", telaprincipal)
    criarbotao_telainicial("Sobre", telaprincipal)

def telaprincipal():
    global novajanela
    root.withdraw()
    novajanela = ctk.CTkToplevel()
    novajanela.geometry("1300x600+450+190")
    novajanela.resizable(False, False)
    novajanela.after(200, lambda: novajanela.iconbitmap("ícones\logos\icone_programa.ico"))
    novajanela.title("Spectra")
    criarbarralateral()
    janeladados()
    janelagrafico()
    janelainformacoes()

def criarbotao_pLateral(root, icone, iconemouse, texto):
    botao = ctk.CTkButton(master= root, cursor='@Aero.cur', width=150, height=40, image=icone, font= fonte_icones, fg_color="#2B6AD0", text=texto, text_color="#E3E7F1", anchor="w")
    botao.bind('<Enter>', lambda e: botao.configure(image=iconemouse, fg_color="#FBFBFE", text_color="#2B6AD0", hover_color="#FBFBFE"))
    botao.bind('<Leave>', lambda e: botao.configure(image=icone, fg_color="#2B6AD0", text_color="#FBFBFE", hover_color="#2B6AD0"))
    return botao

def criarbarralateral():
    global barralateral, framebarra, botao_dados, fundocinza, janela_dados, janela_grafico, janela_info
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
    botao_dados = criarbotao_pLateral(framebarra, graficoB, graficoR, "Inserir dados")
    botao_dados.pack(anchor="center", pady=10)
    botao_dados.configure(command= lambda: (fundocinza.set("dados"), botao_dados.configure(image=graficoR, fg_color="#FBFBFE", text_color="#2B6AD0", hover_color="#FBFBFE") if fundocinza.get() == "dados" else None))
    botao_hist = criarbotao_pLateral(framebarra, hisgraficosB, hisgraficosR, "Gráfico")
    botao_hist.pack(anchor="center", pady=10)
    botao_hist.configure(command= lambda : fundocinza.set("janela_grafico"))
    botao_duv = criarbotao_pLateral(framebarra, duvidasB, duvidasR, "Informações")
    botao_duv.pack(anchor="center", pady=10)
    botao_duv.configure(command= lambda: fundocinza.set("informacoes"))
    botao5 = criarbotao_pLateral(framebarra, duvidasB, duvidasR, "Null")
    botao5.pack(anchor="center", pady=10)
    botao6 = criarbotao_pLateral(framebarra, sairB, sairR, "Null")
    botao6.configure(command=sair)
    botao6.pack(anchor="center", pady=10)
    barralateral.configure(width=180)
    botao_config = criarbotao_pLateral(barralateral, configB, configR, "Configurações")
    botao_config.place(y=530, x=10)

def janeladados():
    global botao_dados, tabela, dados_tabela, teste, valores_apagar, resultados_medias, porcentagens, mediasresazurina
    moldura = ctk.CTkFrame(janela_dados, height=320, width=1030, fg_color="#FFFFFF", corner_radius=16)
    moldura.place(x=30, y=220)
    teste = ctk.CTkFrame(janela_dados, height=300, width=1100, fg_color="#E3E7F1", bg_color="#E3E7F1")
    teste.place(x=65, y=247)
    tabela = Sheet(teste, align="center", total_columns=12, total_rows=8, column_width=77, height=265, width=950, row_height=30, show_x_scrollbar=False, show_y_scrollbar=False, empty_horizontal=0, empty_vertical=0)
    tabela.create_header_dropdown(c = 10, values=["C+", "C-"])
    tabela.create_header_dropdown(c = 11, values=["C-", "C+"])
    Sheet.set_options(tabela, table_bg="#E3E7F1", table_grid_fg="#FFFFFF", table_selected_cells_bg="#C6CAD1", index_bg="#2B6AD0", index_grid_fg="#FFFFFF", header_bg="#2B6AD0", header_grid_fg="#FFFFFF", font=('Helvetica', 10, 'normal'), table_fg='#000000', index_fg='#E3E7F1', header_fg='#E3E7F1', table_selected_cells_border_fg="#2B6AD0", table_selected_rows_border_fg ="#2B6AD0", table_selected_columns_border_fg= "#2B6AD0")
    tabela.bind('<MouseWheel>', lambda a: scrollwheel)
    tabela.enable_bindings("all")
    tabela.disable_bindings("right_click_popup_menu")
    tabela.bind("<3>", popupmenu)
    tabela.pack(expand="True")
    botoes_corantes()
    criarbotao_inserirlimparbac()
    criarbotao_escolhabac()
    dados_tabela = {'sc': [],'ttc': [], 'res_570': [], 'res_600': [], 'am': []}
    valores_apagar = []
    resultados_medias = {'sc': [],'ttc': [], 'res_570': [], 'res_600': [], 'am': []}
    porcentagens = {"sc": [], "ttc": [], "res_570": [], 'res_600': [], "am": []}
    mediasresazurina = {"res": []}

def popupmenu(event):
    menu = tkinter.Menu(root, tearoff=0)
    menu.add_command(label="Sem corante", command=lambda a="sc": corante_escolhido(a), activebackground="#999999", font=fonte_iconesnormal)
    menu.add_command(label="TTC", command=lambda a="ttc": corante_escolhido(a), activebackground="#FF6666", font=fonte_iconesnormal)
    menu.add_command(label="Resazurina 570nm", command=lambda a="res_570": corante_escolhido(a), activebackground="#660099", font=fonte_iconesnormal)
    menu.add_command(label="Resazurina 600nm", command=lambda a="res_600": corante_escolhido(a), activebackground="#6900EF", font=fonte_iconesnormal)
    menu.add_command(label="Azul de Metileno", command=lambda a="am": corante_escolhido(a), activebackground="#64B1FF", font=fonte_iconesnormal)
    menu.add_command(label="Sem corante/Deletar", command=lambda a="pv": corante_escolhido(a), activebackground="#54546B", font=fonte_iconesnormal)
    menu.post(event.x_root, event.y_root)

def criarbotao_escolhaCor(cor):
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

def botoes_corantes():
    global frame_corantes
    frame_corantes = ctk.CTkFrame(janela_dados, height=198, width=300, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=16)
    frame_corantes.pack(anchor="ne", padx= 50)
    frame_corantes.propagate(False)
    botao_sc = criarbotao_escolhaCor("sc")
    botao_sc.pack(in_= frame_corantes ,expand="True")
    botao_ttc = criarbotao_escolhaCor("ttc")
    botao_ttc.pack(in_= frame_corantes ,expand="True")
    botao_res = criarbotao_escolhaCor("res_570")
    botao_res.pack(in_= frame_corantes ,expand="True")
    botao_res2 = criarbotao_escolhaCor("res_600")
    botao_res2.pack(in_= frame_corantes ,expand="True")
    botao_am = criarbotao_escolhaCor("am")
    botao_am.pack(in_= frame_corantes , expand="True")
    botao_pv = ctk.CTkButton(frame_corantes, corner_radius=10, height=35, width=250, bg_color="#FBFBFE", fg_color="#54546B", hover=False, text="Poço vazio/Resetar", text_color="#FBFBFE", font=fonte, command= lambda a="pv": corante_escolhido(a))
    botao_pv.pack(in_= frame_corantes , expand="True")

def corante_escolhido(a):
    if a == "sc":
        if len(dados_tabela["sc"]) >= 1:
            del dados_tabela["sc"][:]
            del resultados_medias["sc"][:]
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#999999", fg = "#000000", redraw = True, overwrite = True)
        sc_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
        if len(sc_cr) > 24:
            tkinter.messagebox.showerror(title="Erro", message="Erro: Você só pode selecionar uma duplicata por corante.")
            tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
            return
        for ro, co in sc_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["sc"].append(data)
        for i in range(0, len(dados_tabela["sc"]), 2):
            valor = dados_tabela["sc"][i]
            proximo = dados_tabela["sc"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["sc"].append(resultado)
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
        for ro, co in ttc_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["ttc"].append(data)
        for i in range(0, len(dados_tabela["ttc"]), 2):
            valor = dados_tabela["ttc"][i]
            proximo = dados_tabela["ttc"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["ttc"].append(resultado)
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
        for ro, co in res_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["res_570"].append(data)
        for i in range(0, len(dados_tabela["res_570"]), 2):
            valor = dados_tabela["res_570"][i]
            proximo = dados_tabela["res_570"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["res_570"].append(resultado)  
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
        for ro, co in res2_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["res_600"].append(data)
        for i in range(0, len(dados_tabela["res_600"]), 2):
            valor = dados_tabela["res_600"][i]
            proximo = dados_tabela["res_600"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["res_600"].append(resultado)  
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
        for ro, co in am_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["am"].append(data)
        for i in range(0, len(dados_tabela["am"]), 2):
            valor = dados_tabela["am"][i]
            proximo = dados_tabela["am"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["am"].append(resultado)
    if a == "pv":
        tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
        pv_apagar = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
        for ro, co in pv_apagar:
            celulas_pv = (Sheet.get_cell_data(tabela, r=ro, c=co))
            valores_apagar.append(float(celulas_pv))
        if valores_apagar == dados_tabela["sc"] or valores_apagar in dados_tabela["sc"]:
            del dados_tabela["sc"][:]
            del valores_apagar[:]
        if valores_apagar == dados_tabela["ttc"] or valores_apagar in dados_tabela["ttc"]:
            del dados_tabela["ttc"][:]
            del valores_apagar[:]
        Sheet.delete(tabela, tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))

def criarbotao_inserirlimparbac():
    global frame_inslimp
    frame_inslimp = ctk.CTkFrame(janela_dados, height=198, width=300, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=16)
    frame_inslimp.place(x=422)
    frame_inslimp.propagate(False)
    botao_inserir= ctk.CTkButton(frame_inslimp, width=270, height=55, corner_radius=10, cursor='@Aero.cur', text="Colar dados", border_color="#999999", border_width=4, font=fontegrande, fg_color="#FBFBFE", text_color='black', command= lambda : tabela.paste(tabela.select_cell(row=0, column=0)))
    botao_inserir.pack(pady=6)
    botao_inserir.bind('<Enter>', lambda e: botao_inserir.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_inserir.bind('<Leave>', lambda e: botao_inserir.configure(text_color="black", fg_color="#FBFBFE"))
    botao_limpar= ctk.CTkButton(frame_inslimp, width=270, height=55, corner_radius=10, cursor='@Aero.cur', hover_color="#2B6AD0", border_color="#999999", border_width=4, text="Limpar tabela", font=fontegrande, fg_color="#FBFBFE", text_color='black', command= limpar)
    botao_limpar.pack(pady=6)
    botao_limpar.bind('<Enter>', lambda e: botao_limpar.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_limpar.bind('<Leave>', lambda e: botao_limpar.configure(text_color="black", fg_color="#FBFBFE"))
    botao_gerardados= ctk.CTkButton(frame_inslimp, width=270, height=55, corner_radius=10, cursor='@Aero.cur', hover_color="#2B6AD0", border_color="#999999", border_width=4, text="Gerar gráfico", font=fontegrande, fg_color="#FBFBFE", text_color='black', command= calculos)
    botao_gerardados.pack(pady=6)
    botao_gerardados.bind('<Enter>', lambda e: botao_gerardados.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_gerardados.bind('<Leave>', lambda e: botao_gerardados.configure(text_color="black", fg_color="#FBFBFE"))

def criarbotao_escolhabac():
    global op_s_aureus, bac_var
    titulo_inserirdados = ctk.CTkLabel(janela_dados, text="Inserir dados", font=fontetitulos, text_color="#2B6AD0")
    titulo_inserirdados.place(y=0, x=33)
    frame_escolhabac= ctk.CTkFrame(janela_dados, height=100, width=350, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=16)
    frame_escolhabac.place(y=100, x=33)
    frame_escolhabac.propagate(False)
    bac_var= tkinter.StringVar(value="")
    op_s_aureus= ctk.CTkRadioButton(frame_escolhabac, width=50, height=50, text= "Staphylococcus aureus", font=fontenormal, text_color="black", command=escolha_bac, variable=bac_var, value="Staphylococcus aureus")
    op_s_aureus.pack(anchor="w", padx=20)
    op_e_coli= ctk.CTkRadioButton(frame_escolhabac, width=50, height=50, text= "Escherichia coli", font=fontenormal, text_color="black", command=escolha_bac, variable=bac_var, value="Escherichia coli")
    op_e_coli.pack(anchor="w", padx=20)

def escolha_bac():
    global bac_escolhida
    bac_escolhida = ''
    if bac_var.get() == "Staphylococcus aureus":
        bac_escolhida = "Staphylococcus aureus"
    if bac_var.get() == "Escherichia coli":
        bac_escolhida = "Escherichia coli"

def limpar():
    del dados_tabela["am"][:], dados_tabela["sc"][:], dados_tabela["ttc"][:], dados_tabela["res_570"][:], dados_tabela["res_600"][:]
    del resultados_medias["am"][:], resultados_medias["sc"][:], resultados_medias["ttc"][:], resultados_medias["res_570"][:], resultados_medias["res_600"][:]
    del porcentagens["am"][:], porcentagens["sc"][:], porcentagens["ttc"][:], porcentagens["res_570"][:], porcentagens["res_600"][:]
    tabela.set_sheet_data(data=([]), redraw=False, reset_col_positions=False, reset_row_positions=False)
    tabela.refresh

def calculos():
    global bac_escolhida
    calculos2('sc')
    calculos2('ttc')
    calculos2('res')
    calculos2('am')
    if bac_escolhida == "Staphylococcus aureus":
        gerargraficos("s_aureus")
    if bac_escolhida == "Escherichia coli":
        gerargraficos("e_coli")

def gerargraficos(bac):
    global ax, canvas, grafico1
    dil_saureus = ["0.02", "0.03", "0.06", "0.125", "0.25", "0.5", "1.0", "2.0", "4.0", "8.0"]
    dil_ecoli = ["0.0005", "0.001", "0.002", "0.004", "0.008", "0.016", "0.032", "0.064", "0.128", "0.256"]
    fonte_graf = {'family':'Segoe UI','color':'black','size':10, 'weight':"semibold"}
    grafico1 = plt.figure(figsize=(10, 5), facecolor="#FFFFFF", edgecolor="#FFFFFF", num=1, clear=True)
    grafico1.tight_layout()
    canvas = FigureCanvasTkAgg(master= molduragraf, figure=grafico1)
    canvas.get_tk_widget().pack()
    ax = grafico1.subplots()
    if bac == "s_aureus":
        funcaobac(dil_saureus)
    if bac == "e_coli":
        funcaobac(dil_ecoli)
    ax.set_ylabel("Inibição bacteriana (%)", fontdict=fonte_graf)
    ax.set_xlabel("Concentração de antibiótico (μL)", fontdict=fonte_graf)
    ax.legend(loc=("upper left"))
    mplcursors.cursor(grafico1, hover=2)

def funcaobac(diluicao):
    if len(resultados_medias["sc"]) == 12:
        if len(porcentagens["sc"]) > 12:
            del porcentagens["sc"][:-12]
        ax.plot(diluicao, porcentagens["sc"][:-2][::-1], color="#999999", label="Sem corante", marker='.')
    if len(resultados_medias["ttc"]) == 12:
        if len(porcentagens["ttc"]) > 12:
            del porcentagens["ttc"][:-12]
        ax.plot(diluicao, porcentagens["ttc"][:-2][::-1], color="#FF6666", label="TTC", marker='.')
    if len(resultados_medias["res_570"]) and len(resultados_medias["res_600"]):
        if len(mediasresazurina["res"]) > 12:
            del mediasresazurina["res"][:-12]
        ax.plot(diluicao, mediasresazurina["res"][:-2][::-1], color="#660099", label="Resazurina", marker='.')
    if len(resultados_medias["am"]) > 5:
        if len(porcentagens["am"]) > 12:
            del porcentagens["am"][:-12]
        ax.plot(diluicao, porcentagens["am"][:-2][::-1], color="#64B1FF", label="Azul de Metileno", marker='.')

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
    global molduragraf, salvarcomo2
    molduragraf = ctk.CTkFrame(janela_grafico, height=410, width=1050, fg_color="#FFFFFF", corner_radius=16)
    molduragraf.place(x=25, y=115)
    molduragraf.pack_propagate("False")
    molduraopcoes = ctk.CTkFrame(janela_grafico, height=100, width=650, fg_color="#FFFFFF", corner_radius=16)
    molduraopcoes.pack(anchor="ne", padx=30)
    molduraopcoes.pack_propagate(False)
    salvarcomo = ctk.CTkButton(molduraopcoes, width=170, height=55, corner_radius=10, cursor='@Aero.cur', hover=False, text="Salvar como:", font=fonte, fg_color="#2B6AD0", text_color='#FBFBFE')
    salvarcomo.pack(anchor="w", padx=15, pady=15)
    salvarcomo2 = CTkScrollableDropdown(salvarcomo, values=[".jpg", ".png", ".pdf", ".svg"], font=fontenormal, scrollbar=False, alpha=0.97, height=223, resize=False, image_values=[jpg, png, pdf, svg], fg_color="#FBFBFE", button_color="#C6CAD1", frame_border_width=3, frame_border_color="#2B6AD0", text_color="black", button_height=40, width=160, command= salvargrafico)
    salvarcomo2.configure(hover_color="#2B6AD0")

def salvargrafico(choice):
    if choice == ".jpg":
        archive = asksaveasfilename(initialfile="Gráfico", initialdir="Gráficos", filetypes=(("JPG","*.jpg"),('all files','*.*')), defaultextension=".*", title="grafico")
        if archive:
            grafico1.savefig(archive)
            tkinter.messagebox.showinfo(title="Salvar gráfico", message= "Gráfico salvo com sucesso!")
        else:
            return
    elif choice == ".png":
        archive = asksaveasfilename(initialfile="Gráfico", initialdir="Gráficos", filetypes=(("PNG","*.png"),('all files','*.*')), defaultextension=".*", title="grafico")
        if archive:
            grafico1.savefig(archive)
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
    botao = ctk.CTkButton(moldurabarra, cursor='@Aero.cur', width=200, height=60, font=fonte, text=texto, fg_color="#2B6AD0", text_color="#FBFBFE", corner_radius=16, command = comando)
    botao.bind('<Enter>', lambda e: botao.configure(fg_color="#FBFBFE", text_color="#2B6AD0", hover_color="#FBFBFE"))
    botao.bind('<Leave>', lambda e: botao.configure(fg_color="#2B6AD0", text_color="#FBFBFE", hover_color="#2B6AD0"))
    botao.pack(anchor="nw", padx=15, pady= 15)
    return botao

def janelainformacoes():
    global moldurabarra
    moldurabarra = ctk.CTkFrame(janela_info, height= 530, width=1050, fg_color="#2B6AD0", corner_radius=16)
    moldurabarra.place(x=20)
    moldurabarra.pack_propagate(False)
    moldurainfo=ctk.CTkTabview(master=janela_info, width=850, height=538, fg_color="#FBFBFE", state="disabled", anchor="ne", bg_color="#FBFBFE", text_color="#FBFBFE", segmented_button_fg_color="#FBFBFE", segmented_button_unselected_color="#FBFBFE", segmented_button_selected_hover_color="#FBFBFE", segmented_button_unselected_hover_color="#FBFBFE", text_color_disabled="#FBFBFE", segmented_button_selected_color="#FBFBFE")
    moldurainfo._outer_button_overhang = 0
    moldurainfo._segmented_button.grid_forget()
    moldurainfo._configure_grid()
    moldurainfo.place(x=220)
    moldurainfo.pack_propagate(False)
    sobre = moldurainfo.add("sobre")
    teste = moldurainfo.add("teste")
    moldurainfo.set("sobre")
    criarbotao_informacoes("Sobre o projeto", lambda: moldurainfo.set("sobre"))
    ctk.CTkLabel(sobre, wraplength=840, anchor="center", font=ctk.CTkFont(family="Segoe UI", size=20, weight='bold'),justify="center", text_color="#2B6AD0", text="Este projeto faz parte do trabalho de conclusão de curso em Biomedicina realizado pelo aluno Luiz Henrique Reinert sob orientação da Professora Dra. Katiany Caleffi Ferracioli.").pack(anchor="w")
    ctk.CTkLabel(sobre, wraplength=840, anchor="center", font=ctk.CTkFont(family="Segoe UI", size=16, weight='bold'),justify="left", text_color="black", text="Inicialmente pensado como parte da disciplina de Atividade em Laboratório Clínico II (ALC II) na área da bacteriologia, o projeto consistia em uma planilha automatizada no Microsoft Excel."
    " Nessa abordagem, os cálculos eram realizados por fórmulas embutidas nas células, e os gráficos eram gerados usando as funcionalidades nativas do Excel. Esse projeto serviu como base para"
    " a elaboração de um artigo, que pode ser acessado em  https://doi.org/10.46311/2318-0579.60.eUJ4398").pack(anchor= "w", pady=15)
    ctk.CTkLabel(sobre, wraplength=840, anchor="center", font=ctk.CTkFont(family="Segoe UI", size=16, weight='bold'),justify="left", text_color="black", text="No entanto, a aplicação dessa planilha enfrentava desafios relacionados a erros de compatibilidade entre diferentes versões, além de apresentar limitações de interatividade no design do Excel."
    " Diante dessas questões, surgiu a ideia de aprimorar o projeto transformando a planilha em um programa executável. O principal objetivo dessa transformação era otimizar a execução de experimentos," 
    " superando as limitações das planilhas e possibilitando uma distribuição mais eficiente do programa entre usuários interessados.").pack(anchor= "w", pady=15)
    ctk.CTkLabel(sobre, wraplength=840, anchor="center", font=ctk.CTkFont(family="Segoe UI", size=16, weight='bold'),justify="left", text_color="black", text="Dessa forma, unindo o meu interesse no aprendizado em programação, decidi incorporar essa transformação como parte integrante do meu Trabalho de Conclusão de Curso (TCC)."
    " O novo formato executável visa proporcionar uma experiência mais intuitiva e interativa, com o objetivo de tornar a administração dos experimentos mais eficiente.").pack(anchor= "w", pady=15)
    criarbotao_informacoes("teste", lambda: moldurainfo.set("teste"))
    ctk.CTkLabel(teste, height=100, width=100, font=fontegrande, text="teste").pack(anchor="w")

def sair():
    novajanela.withdraw()
    root.deiconify()

telainicial()

root.mainloop()