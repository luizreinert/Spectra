import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
root = ctk.CTk()
root.iconbitmap("icone.ico")
#primeira janela
root.resizable(False, False)
root.geometry("450x660")
root.title("Spectra")

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
    novajanela.geometry("1100x600")
    novajanela.resizable(False, False)
    novajanela.after(200, lambda: novajanela.iconbitmap("icone.ico"))
    novajanela.title("Spectra")
    novajanela2()

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

def criarbotao_pLateral(root, icone, iconemouse):
    botao = ctk.CTkButton(master= root, cursor='@Aero.cur', width=40, hover_color="#FCFAFA", height=40, image=icone, fg_color="#6856CB", bg_color="#6856CB", text="", text_color="#FCFAFA", anchor="center")
    botao.bind('<Enter>', lambda e: botao.configure(image=iconemouse, fg_color="#FCFAFA", text_color="#6856CB", hover_color="#FCFAFA"))
    botao.bind('<Leave>', lambda e: botao.configure(image=icone, fg_color="#6856CB", text_color="#FCFAFA", hover_color="#6856CB"))
    return botao

def novajanela2():
    criarbarralateral()

def criarbarralateral():
    global barralateral, framebarra
    barralateral = ctk.CTkFrame(master=novajanela, width=70, height=600, fg_color="#6856CB")
    barralateral.pack(fill="y", side= "left")
    barralateral.pack_propagate(0)
    framebarra = ctk.CTkFrame(master=barralateral, width=70, height=325, fg_color="transparent")
    framebarra.pack(fill="none", anchor="center", expand="True")
    fundobranco = ctk.CTkLabel(master=novajanela, width=1100, height=600, fg_color="#FCFAFA", text="")
    fundobranco.pack(after=barralateral, side= "right")
    botao_inicio = criarbotao_pLateral(framebarra, casaB, casaR)
    botao_inicio.pack(anchor="center", pady=10)
    botao_graficos = criarbotao_pLateral(framebarra, graficoB, graficoR)
    botao_graficos.pack(anchor="center", pady=10)
    botao_hist = criarbotao_pLateral(framebarra, hisgraficosB, hisgraficosR)
    botao_hist.pack(anchor="center", pady=10)
    botao_duv = criarbotao_pLateral(framebarra, duvidasB, duvidasR)
    botao_duv.pack(anchor="center", pady=10)
    botao5 = criarbotao_pLateral(framebarra, duvidasB, duvidasR)
    botao5.pack(anchor="center", pady=10)
    botao6 = criarbotao_pLateral(framebarra, duvidasB, duvidasR)
    botao6.pack(anchor="center", pady=10)
    barralateral.configure(width=70)
    botao_config = criarbotao_pLateral(barralateral, configB, configR)
    botao_config.place(y=530, x=15)
    






#botaoseta = ctk.CTkButton(master=fundobranco, cursor='@Aero.cur', width=45, height=45, hover_color="#FCFAFA", image=angulo1, fg_color="#FCFAFA", text="", command=expandir)
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