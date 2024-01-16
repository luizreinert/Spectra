import customtkinter as ctk
import tkinter
from tkinter import ttk
from PIL import Image
from tksheet import Sheet
from CTkScrollableDropdown import *

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.iconbitmap("icone.ico")
#primeira janela
root.resizable(False, False)
root.geometry("450x660+770+190")
root.title("Spectra")
fonte = ctk.CTkFont(family="Segoe UI", size=16, weight='bold')
fontegrande = ctk.CTkFont(family="Segoe UI", size=24, weight='normal')

graficoB = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\grafico_b.png"))
graficoR = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\grafico_r.png"))
duvidasB = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\duvidas_b.png"))
duvidasR = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\duvidas_r.png"))
hisgraficosB = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\historicograficos_b.png"))
hisgraficosR = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\historicograficos_r.png"))
casaB = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\casaB.png"))
casaR = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\casaR.png"))
angulo1 = ctk.CTkImage(size=[42, 42], light_image=Image.open("ícones\seta.png"))
angulo2 = ctk.CTkImage(size=[42, 42], light_image=Image.open("ícones\seta2.png"))
configB = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\configB.png"))
configR = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\configR.png"))
sairB = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\sairB.png"))
sairR = ctk.CTkImage(size=[21, 21], light_image=Image.open("ícones\sairR.png"))

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
    botao = ctk.CTkButton(master= root, cursor='@Aero.cur', width=40, height=40, image=icone, fg_color="#28283C", text="", text_color="#141428", anchor="center")
    botao.bind('<Enter>', lambda e: botao.configure(image=iconemouse, fg_color="#141428", text_color="#28283C", hover_color="#141428"))
    botao.bind('<Leave>', lambda e: botao.configure(image=icone, fg_color="#28283C", text_color="#141428", hover_color="#28283C"))
    return botao

def criarbarralateral():
    global barralateral, framebarra, botao_inicio, botao_dados, fundopreto, dados, inicio, dados
    barralateral = ctk.CTkFrame(master=novajanela, width=70, height=600, fg_color="#28283C", bg_color="#141428")
    barralateral.pack(fill="y", side= "left")
    barralateral.pack_propagate(0)
    framebarra = ctk.CTkFrame(master=barralateral, width=70, height=325, fg_color="transparent")
    framebarra.pack(fill="none", anchor="center", expand="True")
    fundopreto = ctk.CTkTabview(master=novajanela, width=1100, height=600, fg_color="#141428", state="disabled", anchor="ne", bg_color="#54546B", text_color="#141428", segmented_button_fg_color="#141428", segmented_button_unselected_color="#141428", segmented_button_selected_hover_color="#141428", segmented_button_unselected_hover_color="#141428", text_color_disabled="#141428", segmented_button_selected_color="#141428")
    fundopreto._outer_button_overhang = 0
    fundopreto._segmented_button.grid_forget()
    fundopreto._configure_grid()
    inicio = fundopreto.add("inicio")
    dados = fundopreto.add("dados")
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
    botao_duv = criarbotao_pLateral(framebarra, duvidasB, duvidasR)
    botao_duv.pack(anchor="center", pady=10)
    botao5 = criarbotao_pLateral(framebarra, duvidasB, duvidasR)
    botao5.pack(anchor="center", pady=10)
    botao6 = criarbotao_pLateral(framebarra, sairB, sairR)
    botao6.pack(anchor="center", pady=10)
    barralateral.configure(width=70)
    botao_config = criarbotao_pLateral(barralateral, configB, configR)
    botao_config.place(y=530, x=15)

def janelainicio():
    fundopreto.set("inicio")
    botao_dados.configure(state="normal")

def janeladados():
    global botao_inicio, botao_dados, tabela
    botao_inicio.unbind('<Enter>')
    botao_inicio.unbind('<Leave>')
    botao_dados.configure(state="disabled")
    moldura = ctk.CTkFrame(dados, height=320, width=970, fg_color="#28283C", corner_radius=32, border_width=3, border_color="#54546B")
    moldura.place(x=35, y=230)
    teste = ctk.CTkFrame(dados, height=300, width=1010, fg_color="#141428", bg_color="#141428")
    teste.place(x=65, y=257)
    tabela = Sheet(teste, align="center", total_columns=12, total_rows=8, column_width=73, height=265, width=900, row_height=30, show_x_scrollbar=False, show_y_scrollbar=False)
    tabela.create_header_dropdown(c = (10, 11), values=["C+", "C-"])
    Sheet.set_options(tabela, table_bg="#141428", table_grid_fg="#28283C", table_selected_cells_bg="#E4E3E6", index_bg="#505078", index_grid_fg="#28283C", header_bg="#505078", header_grid_fg="#28283C", outline_color="#505078", font=('Helvetica', 10, 'normal'), table_fg='#E4E3E6', index_fg='#E4E3E6', header_fg='#E4E3E6', table_selected_cells_border_fg="#54546B")
    tabela.bind('<MouseWheel>', lambda a: scrollwheel)
    tabela.enable_bindings("all", "edit_header", "edit_index", "ctrl_select")
    tabela.grid(row = 0, column = 0)
    botoes_corantes()
    criarbotao_inserirlimparbac()

def criarbotao_escolhaCor(cor):
    if cor == "sc":
        botao = ctk.CTkButton(frame_corantes, corner_radius=20, height=15, width=100, bg_color="#28283C", fg_color="#54546B", text="Sem corante", text_color="#E4E3E6", font=fonte, command= lambda a="sc": corante_escolhido(a))
        botao.bind('<Enter>', lambda e: botao.configure(fg_color="#999999", text_color="#54546B"))
        botao.bind('<Leave>', lambda e: botao.configure(fg_color="#54546B", text_color="#E4E3E6"))
    elif cor == "ttc":
        botao = ctk.CTkButton(frame_corantes, corner_radius=20, height=15, width=100, bg_color="#28283C", fg_color="#54546B", text="TTC 480 nm", text_color="#E4E3E6", font=fonte, command= lambda a="ttc": corante_escolhido(a))  
        botao.bind('<Enter>', lambda e: botao.configure(fg_color="#FF6666", text_color="#54546B"))
        botao.bind('<Leave>', lambda e: botao.configure(fg_color="#54546B", text_color="#E4E3E6"))
    elif cor == "res":
        botao = ctk.CTkButton(frame_corantes, corner_radius=20, height=15, width=100, bg_color="#28283C", fg_color="#54546B", text="Resazurina", text_color="#E4E3E6", font=fonte, command= lambda a="res": corante_escolhido(a))
        botao.bind('<Enter>', lambda e: botao.configure(fg_color="#660099", text_color="#54546B"))
        botao.bind('<Leave>', lambda e: botao.configure(fg_color="#54546B", text_color="#E4E3E6"))
    elif cor == "am":
        botao = ctk.CTkButton(frame_corantes, corner_radius=20, height=15, width=100, bg_color="#28283C", fg_color="#54546B", text="Azul de Metileno 600 nm",text_color="#E4E3E6", font=fonte, command= lambda a="am": corante_escolhido(a)) 
        botao.bind('<Enter>', lambda e: botao.configure(fg_color="#64B1FF", text_color="#54546B"))
        botao.bind('<Leave>', lambda e: botao.configure(fg_color="#54546B", text_color="#E4E3E6"))
    elif cor == "pv":
        botao = ctk.CTkButton(frame_corantes, corner_radius=20, height=15, width=100, bg_color="#28283C", fg_color="#54546B", hover=False, text="Poço vazio/Resetar",text_color="#E4E3E6", font=fonte, command= lambda a="pv": corante_escolhido(a))  
    return botao     

def botoes_corantes():
    global frame_corantes
    frame_corantes = ctk.CTkFrame(dados, height=198, width=244, cursor='@Aero.cur', fg_color="#28283C", bg_color="#141428", corner_radius=32)
    frame_corantes.place(x=400)
    frame_corantes.propagate(False)
    botao_sc = criarbotao_escolhaCor("sc")
    botao_sc.pack(in_= frame_corantes,padx=15, pady= 5,anchor="w", fill="x", ipady=1)
    botao_ttc = criarbotao_escolhaCor("ttc")
    botao_ttc.pack(in_= frame_corantes,padx=15, pady= 5,anchor="w", fill="x", ipady=1)
    botao_res = criarbotao_escolhaCor("res")
    botao_res.pack(in_= frame_corantes,padx=15, pady= 5,anchor="w", fill="x", ipady=1)
    botao_am = criarbotao_escolhaCor("am")
    botao_am.pack(in_= frame_corantes,padx=15, pady= 5,anchor="w", fill="x", ipady=1)
    botao_pv = criarbotao_escolhaCor("pv")
    botao_pv.pack(in_= frame_corantes,padx=15, pady= 5,anchor="w", fill="x", ipady=1)

def corante_escolhido(a):
    if a == "sc":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#999999", fg = "#E4E3E6", redraw = True, overwrite = True)
    if a == "ttc":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#FF6666", fg = "#E4E3E6", redraw = True, overwrite = True)      
    if a == "res":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#660099", fg = "#E4E3E6", redraw = True, overwrite = True)
    if a == "am":
        Sheet.highlight_cells(tabela, cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False), bg = "#64B1FF", fg = "#E4E3E6", redraw = True, overwrite = True)
    if a == "pv":
        Sheet.delete(tabela, tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))
        tabela.dehighlight_cells(cells = tabela.get_selected_cells(get_rows = False, get_columns = False, sort_by_row = False, sort_by_column = False))

def criarbotao_inserirlimparbac():
    frame_inslimp = ctk.CTkFrame(dados, height=150, width=270, cursor='@Aero.cur', fg_color="#141428", bg_color="#141428", corner_radius=32)
    frame_inslimp.pack(anchor="w", padx=60)
    frame_inslimp.propagate(False)
    botao_inserir= ctk.CTkButton(frame_inslimp, width=270, height=40, cursor='@Aero.cur', hover_color="#54546B", text="Inserir dados", font=fontegrande, fg_color="#28283C", text_color='#E4E3E6', command= inserir)
    botao_inserir.pack(pady=1)
    botao_limpar= ctk.CTkButton(frame_inslimp, width=270, height=40, cursor='@Aero.cur', hover_color="#54546B", text="Limpar dados", font=fontegrande, fg_color="#28283C", text_color='#E4E3E6', command= limpar)
    botao_limpar.pack(pady=15)
    tipo_bac= ctk.CTkOptionMenu(frame_inslimp, width=270, height=40, cursor='@Aero.cur', values=["Selecione a bacteria"], font=("Segoe UI", 18, "italic"), fg_color="#28283C", text_color='#E4E3E6', button_color='#383854', anchor="center", button_hover_color="#54546B")
    CTkScrollableDropdown(tipo_bac, width=270, height=105, button_height=20, cursor='@Aero.cur', values=["Staphylococcus aureus", "Escherichia coli"], font=("Segoe UI", 15, "italic"), fg_color="#28283C", text_color='#E4E3E6', scrollbar=False, resize=False, alpha=0.90, button_color="#505078", justify="Center", frame_border_color='#383854')
    tipo_bac.pack(pady=1)

def limpar():
    tabela.set_sheet_data(data=([]), redraw=False, reset_col_positions=False, reset_row_positions=False)
    tabela.refresh(redraw_header=True, redraw_row_index=True)

def inserir():
    tabela.paste(tabela.select_cell(row=0, column=0))

def scrollwheel(event):
    return 'break'

def janelagraficos():
    botao_dados.unbind('<Enter>')
    botao_dados.unbind('<Leave>')
    botao_dados.configure(state="disabled", fg_color="#141428")


def sair():
    novajanela.destroy()
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
