import os
import time
from datetime import datetime
from typing import Dict, Tuple

class CalculadoraIMC:

    CORES = {
        'ciano': '\033[96m',
        'verde': '\033[92m', 
        'amarelo': '\033[93m',
        'vermelho': '\033[91m',
        'azul': '\033[94m',
        'magenta': '\033[95m',
        'branco': '\033[97m',
        'reset': '\033[0m',
        'negrito': '\033[1m'
    }
    
    TABELA_IMC: Dict[float, Tuple[str, str, str]] = {
        18.5: ("Magreza", "amarelo", "⚠️"),
        24.9: ("Normal", "verde", "✅"),
        29.9: ("Sobrepeso", "magenta", "⚠️"),
        34.9: ("Obesidade Grau I", "vermelho", "🚨"),
        39.9: ("Obesidade Grau II", "vermelho", "🚨🚨"),
        float('inf'): ("Obesidade Grau III", "vermelho", "🚨🚨🚨")
    }
    
    def __init__(self):
        self.historico = []
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def cor(self, texto: str, cor: str) -> str:
        return f"{self.CORES.get(cor, '')}{self.CORES['negrito']}{texto}{self.CORES['reset']}"
    
    def banner(self):
        self.limpar_tela()
        print(f"""
{self.cor('╔══════════════════════════════════════════════════════╗', 'ciano')}
{self.cor('║              🩺 CALCULADORA DE IMC 🩺                ║', 'ciano')}
{self.cor('║                    PROFISSIONAL v2.0                  ║', 'ciano')}
{self.cor('╚══════════════════════════════════════════════════════╝', 'ciano')}
        """)
    
    def obter_dados(self) -> Tuple[float, float]:
        while True:
            try:
                print(f"{self.cor('📏 INSIRA SEUS DADOS:', 'ciano')}")
                
                peso = float(input(f"{self.cor('   ➤ Peso (kg): ', 'branco')}{self.cor('', 'reset')}"))
                if peso <= 0:
                    print(f"{self.cor('❌ Peso deve ser maior que 0!', 'vermelho')}")
                    time.sleep(1)
                    continue
                
                altura = float(input(f"{self.cor('   ➤ Altura (m): ', 'branco')}{self.cor('', 'reset')}"))
                if altura <= 0 or altura > 3:
                    print(f"{self.cor('❌ Altura deve estar entre 0.1m e 3m!', 'vermelho')}")
                    time.sleep(1)
                    continue
                
                return peso, altura
                
            except ValueError:
                print(f"{self.cor('❌ Digite apenas números válidos!', 'vermelho')}")
                time.sleep(1)
    
    def calcular_imc(self, peso: float, altura: float) -> float:
        return peso / (altura ** 2)
    
    def classificar_imc(self, imc: float) -> Tuple[str, str, str]:
        for limite, (categoria, cor, emoji) in self.TABELA_IMC.items():
            if imc < limite:
                return categoria, cor, emoji
        return "Erro na classificação", "vermelho", "❌"
    
    def exibir_resultado(self, peso: float, altura: float, imc: float):
        categoria, cor_nome, emoji = self.classificar_imc(imc)
        
        print(f"\n{self.cor('═' * 60, 'ciano')}")
        print(f"{self.cor('                  RESULTADO FINAL                  ', 'ciano')}")
        print(f"{self.cor('═' * 60, 'ciano')}")
        print()
        
        print(f"{self.cor('📊 DADOS INFORMADOS:', 'branco')}")
        print(f"   Peso: {self.cor(f'{peso:.1f} kg', 'ciano')}")
        print(f"   Altura: {self.cor(f'{altura:.2f} m', 'ciano')}")
        print()
        
        print(f"{self.cor('🎯 SEU IMC: ', 'branco')}", end="")
        print(self.cor(f'{imc:.1f}', 'ciano'))
        print()
        
        print(f"{self.cor('🏷️  CLASSIFICAÇÃO: ', 'branco')}", end="")
        print(f"{self.cor(emoji + ' ' + categoria, cor_nome)}")
        print()
        
        # Dicas personalizadas
        self.dicas_personalizadas(categoria)
    
    def dicas_personalizadas(self, categoria: str):
        dicas = {
            "Magreza": " Consuma mais calorias saudáveis e consulte um nutricionista!",
            "Normal": " Parabéns! Continue mantendo hábitos saudáveis!",
            "Sobrepeso": " Reduza calorias e pratique exercícios regularmente!",
            "Obesidade Grau I": " Consulte um médico e nutricionista urgentemente!",
            "Obesidade Grau II": " Procure ajuda médica especializada IMEDIATAMENTE!",
            "Obesidade Grau III": " EMERGÊNCIA MÉDICA - Busque atendimento especializado!"
        }
        
        print(f"{self.cor('💡 DICAS: ', 'branco')}")
        print(f"   {dicas.get(categoria, 'Consulte um profissional de saúde!')}")
        print()
    
    def salvar_historico(self, peso: float, altura: float, imc: float, categoria: str):
        resultado = {
            'data': datetime.now().strftime("%d/%m/%Y %H:%M"),
            'peso': peso,
            'altura': altura,
            'imc': round(imc, 1),
            'categoria': categoria
        }
        self.historico.append(resultado)
    
    def mostrar_historico(self):
        if not self.historico:
            print(f"{self.cor('📝 Nenhum cálculo no histórico ainda!', 'amarelo')}")
            return
        
        print(f"\n{self.cor('═' * 70, 'ciano')}")
        print(f"{self.cor('                    HISTÓRICO DE CÁLCULOS                    ', 'ciano')}")
        print(f"{self.cor('═' * 70, 'ciano')}")
        
        for i, calc in enumerate(self.historico[-5:], 1):  # Últimos 5
            cor = self.classificar_imc(calc['imc'])[1]
            print(f"{self.cor(f'{i:2d}. ', 'branco')}{calc['data']} | "
                  f"IMC: {self.cor(f'{calc['imc']:5.1f}', cor)} | "
                  f"{calc['categoria']}")
    
    def menu_principal(self):
        while True:
            self.banner()
            
            print(f"{self.cor('1️⃣  Calcular IMC', 'verde')}")
            print(f"{self.cor('2️⃣  Ver Histórico', 'azul')}")
            print(f"{self.cor('3️⃣  Limpar Histórico', 'amarelo')}")
            print(f"{self.cor('0️⃣  Sair', 'vermelho')}")
            print()
            
            opcao = input(f"{self.cor('➤ Escolha uma opção: ', 'branco')}{self.cor('', 'reset')}")
            
            if opcao == "1":
                peso, altura = self.obter_dados()
                imc = self.calcular_imc(peso, altura)
                categoria, _, _ = self.classificar_imc(imc)
                
                self.exibir_resultado(peso, altura, imc)
                self.salvar_historico(peso, altura, imc, categoria)
                
                input(f"\n{self.cor('⏸️  Pressione ENTER para continuar...', 'ciano')}")
            
            elif opcao == "2":
                self.mostrar_historico()
                input(f"\n{self.cor('⏸️  Pressione ENTER para continuar...', 'ciano')}")
            
            elif opcao == "3":
                self.historico.clear()
                print(f"{self.cor('✅ Histórico limpo!', 'verde')}")
                time.sleep(1)
            
            elif opcao == "0":
                print(f"\n{self.cor('👋 Obrigado por usar a Calculadora de IMC! Volte sempre!', 'verde')}")
                time.sleep(1)
                break
            
            else:
                print(f"{self.cor('❌ Opção inválida!', 'vermelho')}")
                time.sleep(1)

def main():
    try:
        app = CalculadoraIMC()
        app.menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{app.cor('👋 Programa interrompido pelo usuário!', 'amarelo')}")
    except Exception as e:
        print(f"\n{app.cor(f'❌ Erro inesperado: {str(e)}', 'vermelho')}")

if __name__ == "__main__":
    main()
