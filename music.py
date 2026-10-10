import time
import sys
import random

class MusicPlayer:
    def __init__(self):
        self.frases = [
            "Diga pra mim que é real,",
            "Que eu te prometo o meu melhor",
            "Fala pra mim que eu quero ouvir,",
            "que tu sentiu oque eu senti."
        ]
        self.efeitos = ['normal']
    
    def limpar_tela(self):
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
    
    def print_com_efeito(self, texto, efeito, velocidade=0.12):
        
        if efeito == 'normal':
            for char in texto:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(velocidade)
 
        print()
    
    def intro(self):
        self.limpar_tela()
        print("🎵 MÚSICA INICIANDO EM 3... 2... 1... 🎵")
        for i in range(3, 0, -1):
            print(f"\r{' '*40}🎵 {i} 🎵{' '*40}", end="", flush=True)
            time.sleep(1)
        self.limpar_tela()
    
    def separador(self):
        print("\n" + "━" * 60 + "\n")
        time.sleep(0.5)
    
    def tocar(self):
        self.intro()
        
        for i, frase in enumerate(self.frases):
            efeito = random.choice(self.efeitos)
            
            if i == 0: velocidade = 0.15  
            elif i == 1: velocidade = 0.12  
            elif i == 2: velocidade = 0.10  
            else: velocidade = 0.13  
            
            self.print_com_efeito(frase, efeito, velocidade)
            self.separador()

player = MusicPlayer()
player.tocar()