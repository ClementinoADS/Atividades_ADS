import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def mostrar_proximos():
    try:
        inicio = int(entrada.get())
        
        sequencia = [str(n) for n in range(inicio + 1, inicio + 11)]
        
        resultado_texto = " , ".join(sequencia)
        label_resultado.configure(text=f"Próximos 10 números:\n{resultado_texto}", text_color="white")
        
    except ValueError:
        label_resultado.configure(text="Erro: Digite apenas números inteiros!", text_color="red")

app = ctk.CTk()
app.title("Contador")
app.geometry("500x300")

titulo = ctk.CTkLabel(app, text="Gerador de Sequência", font=("Roboto", 20, "bold"))
titulo.pack(pady=20)

entrada = ctk.CTkEntry(app, placeholder_text="Digite o número inicial", width=200)
entrada.pack(pady=10)

botao = ctk.CTkButton(app, text="Mostrar Próximos 10", command=mostrar_proximos)
botao.pack(pady=20)

label_resultado = ctk.CTkLabel(app, text="", font=("Roboto", 14), wraplength=450)
label_resultado.pack(pady=10)

app.mainloop()