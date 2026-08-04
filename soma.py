import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Soma")
        self.geometry("400x350")
        self.total = 0

        ctk.CTkLabel(self, text="Calculadora de Soma", font=("Arial", 20, "bold")).pack(pady=20)

        self.entrada = ctk.CTkEntry(self, placeholder_text="Digite um número: ", width=200)
        self.entrada.pack(pady=10)

        ctk.CTkButton(self, text="Adicionar à Soma", command=self.somar).pack(pady=10)
        ctk.CTkButton(self, text="Zerar (0)", fg_color="red", command=self.zerar).pack(pady=5)

        self.label_res = ctk.CTkLabel(self, text="total: 0", font=("Arial", 24))
        self.label_res.pack(pady=30)

    def somar(self):
        try:
            valor = float(self.entrada.get())
            if valor == 0:
                self.zerar()
            else:
                self.total += valor
                self.label_res.configure(text=f"Total: {self.total}")
                self.entrada.delete(0, 'end')
        except ValueError:
            self.label_res.configure(text="Erro: Valor Inválido")

    def zerar(self):
        self.total = 0
        self.label_res.configure(text="Total: 0")
        self.entrada.delete(0, 'end')

if __name__ == "__main__":
    app = App()
    app.mainloop()