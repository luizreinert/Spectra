import customtkinter as ctk
import tkinter
from tkinter import ttk
from PIL import Image
from tksheet import Sheet
from CTkScrollableDropdown import *
import os

ctk.set_appearance_mode("light")
root = ctk.CTk()
root.iconbitmap("icone.ico")
#primeira janela
root.resizable(False, False)
root.geometry("450x660+770+190")
root.title("Spectra")
fonte = ctk.CTkFont(family="Segoe UI", size=16, weight='bold')
fontegrande = ctk.CTkFont(family="Segoe UI", size=22, weight='bold')

graficoB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\graficoB.png"))
graficoR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\grafico_r.png"))
duvidasB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidasB.png"))
duvidasR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\duvidas_r.png"))
hisgraficosB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\historicograficosB.png"))
hisgraficosR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\historicograficos_r.png"))
casaB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\casaB.png"))
casaR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\casaR.png"))
angulo1 = ctk.CTkImage(size=[42, 42], light_image=Image.open("ícones\seta.png"))
angulo2 = ctk.CTkImage(size=[42, 42], light_image=Image.open("ícones\seta2.png"))
configB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\configB.png"))
configR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\configR.png"))
sairB = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\sairB.png"))
sairR = ctk.CTkImage(size=[22, 22], light_image=Image.open("ícones\sairR.png"))

def criarbotao_telainicial(texto, comando):
    botao = ctk.CTkButton(master=root, text=texto, cursor='@Aero.cur', hover_color="#6856CB", text_color="#6856CB", font=("Arial", 20),  width=288, height=66, corner_radius=32, fg_color="#FCFAFA", border_width=3, border_color='#E9DBEA', background_corner_colors=['#5E7DCA', '#C497E6', '#C497E6', '#5E7DCA'], command=comando)
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
    novajanela.geometry("1100x600+450+190")
    novajanela.resizable(False, False)
    novajanela.after(200, lambda: novajanela.iconbitmap("icone.ico"))
    novajanela.title("Spectra")
    criarbarralateral()
    janeladados()

def criarbotao_pLateral(root, icone, iconemouse):
    botao = ctk.CTkButton(master= root, cursor='@Aero.cur', width=40, height=40, image=icone, fg_color="#FFFFFF", text="", text_color="#E3E7F1", anchor="center")
    botao.bind('<Enter>', lambda e: botao.configure(image=iconemouse, fg_color="#E3E7F1", text_color="#FFFFFF", hover_color="#E3E7F1"))
    botao.bind('<Leave>', lambda e: botao.configure(image=icone, fg_color="#FFFFFF", text_color="#E3E7F1", hover_color="#FFFFFF"))
    return botao

def criarbarralateral():
    global barralateral, framebarra, botao_inicio, botao_dados, fundopreto, dados, inicio, dados
    barralateral = ctk.CTkFrame(master=novajanela, width=70, height=600, fg_color="#FFFFFF", bg_color="#E3E7F1")
    barralateral.pack(fill="y", side= "left")
    barralateral.pack_propagate(0)
    framebarra = ctk.CTkFrame(master=barralateral, width=70, height=325, fg_color="transparent")
    framebarra.pack(fill="none", anchor="center", expand="True")
    fundopreto = ctk.CTkTabview(master=novajanela, width=1100, height=600, fg_color="#E3E7F1", state="disabled", anchor="ne", bg_color="#E3E7F1", text_color="#E3E7F1", segmented_button_fg_color="#E3E7F1", segmented_button_unselected_color="#E3E7F1", segmented_button_selected_hover_color="#E3E7F1", segmented_button_unselected_hover_color="#E3E7F1", text_color_disabled="#E3E7F1", segmented_button_selected_color="#E3E7F1")
    fundopreto._outer_button_overhang = 0
    fundopreto._segmented_button.grid_forget()
    fundopreto._configure_grid()
    inicio = fundopreto.add("inicio")
    dados = fundopreto.add("dados")
    hist= fundopreto.add("hist")
    fundopreto.pack(after=barralateral, side= "right")
    fundopreto.pack_propagate(0)
    botao_inicio = criarbotao_pLateral(framebarra, casaB, casaR)
    botao_inicio.pack(anchor="center", pady=10)
    botao_inicio.configure(command=janelainicio)
    botao_dados = criarbotao_pLateral(framebarra, graficoB, graficoR)
    botao_dados.pack(anchor="center", pady=10)
    botao_dados.configure(command= lambda : fundopreto.set("dados"))
    botao_hist = criarbotao_pLateral(framebarra, hisgraficosB, hisgraficosR)
    botao_hist.pack(anchor="center", pady=10)
    botao_hist.configure(command= lambda : fundopreto.set("hist"))
    botao_duv = criarbotao_pLateral(framebarra, duvidasB, duvidasR)
    botao_duv.pack(anchor="center", pady=10)
    botao5 = criarbotao_pLateral(framebarra, duvidasB, duvidasR)
    botao5.pack(anchor="center", pady=10)
    botao6 = criarbotao_pLateral(framebarra, sairB, sairR)
    botao6.configure(command=sair)
    botao6.pack(anchor="center", pady=10)
    barralateral.configure(width=70)
    botao_config = criarbotao_pLateral(barralateral, configB, configR)
    botao_config.place(y=530, x=15)

def janelainicio():
    fundopreto.set("inicio")
    botao_dados.configure(state="normal")

def janeladados():
    global botao_inicio, botao_dados, tabela, dados_tabela, teste, valores_apagar, resultados_medias
    botao_inicio.unbind('<Enter>')
    botao_inicio.unbind('<Leave>')
    botao_dados.configure(state="disabled")
    moldura = ctk.CTkFrame(dados, height=320, width=970, fg_color="#FFFFFF", corner_radius=32)
    moldura.place(x=30, y=220)
    teste = ctk.CTkFrame(dados, height=300, width=1010, fg_color="#E3E7F1", bg_color="#E3E7F1")
    teste.place(x=65, y=247)
    tabela = Sheet(teste, align="center", total_columns=12, total_rows=8, column_width=73, height=265, width=900, row_height=30, show_x_scrollbar=False, show_y_scrollbar=False)
    tabela.create_header_dropdown(c = (10, 11), values=["C+", "C-"])
    Sheet.set_options(tabela, table_bg="#E3E7F1", table_grid_fg="#FFFFFF", table_selected_cells_bg="#C6CAD1", index_bg="#2B6AD0", index_grid_fg="#FFFFFF", header_bg="#2B6AD0", header_grid_fg="#FFFFFF", font=('Helvetica', 10, 'normal'), table_fg='#000000', index_fg='#E3E7F1', header_fg='#E3E7F1', table_selected_cells_border_fg="#2B6AD0", table_selected_rows_border_fg ="#2B6AD0", table_selected_columns_border_fg= "#2B6AD0")
    tabela.bind('<MouseWheel>', lambda a: scrollwheel)
    tabela.enable_bindings("all", "edit_header", "edit_index", "ctrl_select")
    tabela.grid(row = 0, column = 0)
    botoes_corantes()
    criarbotao_inserirlimparbac()
    criarbotao_gerardados()
    dados_tabela = {'sc': [],'ttc': [], 'res': [], 'am': []}
    valores_apagar = []
    resultados_medias = {'sc': [],'ttc': [], 'res': [], 'am': []}

def criarbotao_escolhaCor(cor):
    if cor == "sc":
        botao = ctk.CTkButton(frame_corantes, corner_radius=32, height=32, width=100, bg_color="#FBFBFE", fg_color="#999999", text="Sem corante", text_color="#FBFBFE", font=fonte, command= lambda a="sc": corante_escolhido(a))
    elif cor == "ttc":
        botao = ctk.CTkButton(frame_corantes, corner_radius=32, height=32, width=100, bg_color="#FBFBFE", fg_color="#FF6666", text="TTC 480 nm", text_color="#FBFBFE", font=fonte, command= lambda a="ttc": corante_escolhido(a))  
    elif cor == "res":
        botao = ctk.CTkButton(frame_corantes, corner_radius=32, height=32, width=100, bg_color="#FBFBFE", fg_color="#660099", text="Resazurina", text_color="#FBFBFE", font=fonte, command= lambda a="res": corante_escolhido(a))
    elif cor == "am":
        botao = ctk.CTkButton(frame_corantes, corner_radius=32, height=32, width=100, bg_color="#FBFBFE", fg_color="#64B1FF", text="Azul de Metileno 600 nm", font = fonte, text_color="#FBFBFE", command= lambda a="am": corante_escolhido(a))   
    return botao     

def botoes_corantes():
    global frame_corantes
    frame_corantes = ctk.CTkFrame(dados, height=198, width=350, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=32)
    frame_corantes.place(x=370)
    frame_corantes.propagate(False)
    botao_sc = criarbotao_escolhaCor("sc")
    botao_sc.pack(in_= frame_corantes ,expand="True", ipadx=95)
    botao_ttc = criarbotao_escolhaCor("ttc")
    botao_ttc.pack(in_= frame_corantes ,expand="True", ipadx=98)
    botao_res = criarbotao_escolhaCor("res")
    botao_res.pack(in_= frame_corantes ,expand="True", ipadx=100)
    botao_am = criarbotao_escolhaCor("am")
    botao_am.pack(in_= frame_corantes , expand="True", ipadx=48)
    botao_pv = ctk.CTkButton(frame_corantes, corner_radius=32, height=35, width=100, bg_color="#FBFBFE", fg_color="#54546B", hover=False, text="Poço vazio/Resetar", text_color="#FBFBFE", font=fonte, command= lambda a="pv": corante_escolhido(a))
    botao_pv.pack(in_= frame_corantes , expand="True", ipadx=70)

def corante_escolhido(a):
    if a == "sc":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#999999", fg = "#000000", redraw = True, overwrite = True)
        sc_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
        for ro, co in sc_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["sc"].append(data)
        print(dados_tabela["sc"])
        for i in range(0, len(dados_tabela["sc"]), 2):
            valor = dados_tabela["sc"][i]
            proximo = dados_tabela["sc"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["sc"].append(resultado)       
        print(resultados_medias["sc"])
    if a == "ttc":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#FF6666", fg = "#000000", redraw = True, overwrite = True)      
        ttc_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
        for ro, co in ttc_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["ttc"].append(data)
        print(dados_tabela["ttc"])
        for i in range(0, len(dados_tabela["ttc"]), 2):
            valor = dados_tabela["ttc"][i]
            proximo = dados_tabela["ttc"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["ttc"].append(resultado)
        print(resultados_medias["ttc"])  
    if a == "res":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#660099", fg = "#000000", redraw = True, overwrite = True)
        res_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
        for ro, co in res_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["res"].append(data)
        print(dados_tabela["res"])
        for i in range(0, len(dados_tabela["res"]), 2):
            valor = dados_tabela["res"][i]
            proximo = dados_tabela["res"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["res"].append(resultado) 
        print(resultados_medias["res"])    
    if a == "am":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#64B1FF", fg = "#000000", redraw = True, overwrite = True)
        am_cr = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = True)
        for ro, co in am_cr:
            data = float(Sheet.get_cell_data(tabela, r=ro, c=co))
            dados_tabela["am"].append(data)
        print(dados_tabela["am"])
        for i in range(0, len(dados_tabela["am"]), 2):
            valor = dados_tabela["am"][i]
            proximo = dados_tabela["am"][i+1]
            resultado = (valor + proximo) / 2 
            resultados_medias["am"].append(resultado)
        print(resultados_medias["am"])
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
    frame_inslimp = ctk.CTkFrame(dados, height=198, width=300, fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=32)
    frame_inslimp.pack(anchor="w", padx=35)
    frame_inslimp.propagate(False)
    botao_inserir= ctk.CTkButton(frame_inslimp, width=270, height=40, corner_radius=32, cursor='@Aero.cur', text="Inserir dados", border_color="#C6CAD1", border_width=3, font=fontegrande, fg_color="#FBFBFE", text_color='#2B6AD0', command= inserir)
    botao_inserir.pack(pady=12)
    botao_inserir.bind('<Enter>', lambda e: botao_inserir.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_inserir.bind('<Leave>', lambda e: botao_inserir.configure(text_color="#2B6AD0", fg_color="#FBFBFE"))
    botao_limpar= ctk.CTkButton(frame_inslimp, width=270, height=40, corner_radius=32, cursor='@Aero.cur', hover_color="#2B6AD0", border_color="#C6CAD1", border_width=3, text="Limpar dados", font=fontegrande, fg_color="#FBFBFE", text_color='#2B6AD0', command= limpar)
    botao_limpar.pack(pady=8)
    botao_limpar.bind('<Enter>', lambda e: botao_limpar.configure(text_color="#FBFBFE", fg_color="#2B6AD0"))
    botao_limpar.bind('<Leave>', lambda e: botao_limpar.configure(text_color="#2B6AD0", fg_color="#FBFBFE"))
    tipo_bac= ctk.CTkOptionMenu(frame_inslimp, width=270, height=40, cursor='@Aero.cur', corner_radius=32, values=["Selecione a bacteria"], font=fonte, fg_color="#FBFBFE", text_color='#2B6AD0', button_color='#FBFBFE', anchor="center", button_hover_color="#2B6AD0")
    CTkScrollableDropdown(tipo_bac, width=270, height=105, button_height=20, frame_border_width=3, cursor='@Aero.cur', values=["Staphylococcus aureus", "Escherichia coli"], hover=False, font=fonte, fg_color="#FBFBFE", text_color='#2B6AD0', scrollbar=False, resize=False, alpha=0.90, button_color="#FBFBFE", justify="Center", frame_border_color="#C6CAD1")
    tipo_bac.pack(pady=8)

def limpar():
    del dados_tabela["am"][:]
    del dados_tabela["sc"][:]
    del dados_tabela["ttc"][:]
    del dados_tabela["res"][:]
    del resultados_medias["am"][:]
    del resultados_medias["sc"][:]
    del resultados_medias["ttc"][:]
    del resultados_medias["res"][:]
    tabela.set_sheet_data(data=([]), redraw=False, reset_col_positions=False, reset_row_positions=False)
    tabela.refresh

def inserir():
    tabela.paste(tabela.select_cell(row=0, column=0))

def criarbotao_gerardados():
    frame_gerardados = ctk.CTkFrame(dados, height=150, width=270, cursor='@Aero.cur', fg_color="#FBFBFE", bg_color="#E3E7F1", corner_radius=32)
    frame_gerardados.place(x=800)
    frame_gerardados.propagate(False)
    botao_gerardados= ctk.CTkButton(frame_gerardados, width=270, height=40, cursor='@Aero.cur', hover_color="#54546B", text="Gerar dados", font=fontegrande, fg_color="#FFFFFF", text_color='#44519e')
    botao_gerardados.pack(pady=1)
    botao_gerardados2= ctk.CTkButton(frame_gerardados, width=270, height=40, cursor='@Aero.cur', hover_color="#54546B", text="Gerar dados", font=fontegrande, fg_color="#FFFFFF", text_color='#44519e')
    botao_gerardados2.pack(pady=10)

def scrollwheel(event):
    return 'break'

def sair():
    novajanela.withdraw()
    root.deiconify()
   





#botaoseta = ctk.CTkButton(master=fundopreto, cursor='@Aero.cur', width=45, height=45, hover_color="#FCFAFA", image=angulo1, fg_color="#FCFAFA", text="", command=expandir)
#botaoseta.place(x=5, y=280)
#return botaoseta
#def expandir():
#barralateral.configure(width=180)
#botaoseta.configure(command=barradiminuida, image=angulo2)
#botao1.configure(text="Início", font=("circular-std-medium-500.ttf", 16, 'bold'), width=180, height=55, anchor="center")
#botao_graficos.configure(text="Importar dados", font=("circular-std-medium-500.ttf", 15, 'bold'), width=180, height=55, anchor="center")
#botao_hist.configure(text="Gráficos gerados", font=("circular-std-medium-500.ttf", 15, 'bold'), width=180, height=55, anchor="center")
#botao4.configure(text="Ajuda", font=("circular-std-medium-500.ttf", 16, 'bold'), width=180, height=55, anchor="center")
    

telainicial()

root.mainloop()
