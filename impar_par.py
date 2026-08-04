import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

def verificar():
    try:
        numero = int(entrada.get())
        
        if numero % 2 == 0:
            resultado.configure(text=f"O número {numero} é PAR", text_color="#2ECC71")
        else:
            resultado.configure(text=f"O número {numero} é ÍMPAR", text_color="#E74C3C")
    except ValueError:
        resultado.configure(text="Por favor, digite um número válido!", text_color="orange")

janela = ctk.CTk()
janela.title("Verificador de impar ou par")
janela.geometry("400x300")

titulo = ctk.CTkLabel(janela, text="Par ou Ímpar?", font=("Roboto", 24, "bold"))
titulo.pack(pady=20)

entrada = ctk.CTkEntry(janela, placeholder_text="Digite um número: ")
entrada.pack(pady=10)

botao = ctk.CTkButton(janela, text="Verificar", command=verificar)
botao.pack(pady=20)

resultado = ctk.CTkLabel(janela, text="", font=("Roboto", 16))
resultado.pack(pady=10)

janela.mainloop()