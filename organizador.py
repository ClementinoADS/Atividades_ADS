
import os
import shutil

# 1. Define o caminho da pasta que você quer organizar
# (Substitua pelo caminho do seu computador. Ex: "C:/Users/Nome/Downloads")
pasta_baguncada = "C:/Users/julio/Downloads"

formatos = {
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Programas": [".exe", ".msi"]
}

for arquivo in os.listdir(pasta_baguncada):
    caminho_completo = os.path.join(pasta_baguncada, arquivo)
    
    if os.path.isfile(caminho_completo):
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        pasta_destino = None
        
        for categoria, extensoes_da_categoria in formatos.items():
            if extensao in extensoes_da_categoria:
                pasta_destino = categoria
                break
        
        if pasta_destino:
            nova_pasta_caminho = os.path.join(pasta_baguncada, pasta_destino)
            
            if not os.path.exists(nova_pasta_caminho):
                os.makedirs(nova_pasta_caminho)
                print(f"Pasta '{pasta_destino}' criada com sucesso!")
            
            shutil.move(caminho_completo, os.path.join(nova_pasta_caminho, arquivo))
            print(f"Arquivo '{arquivo}' movido para {pasta_destino}.")

print("\nOrganização concluída!")