from abc import ABC, abstractmethod

class Notificador(ABC):
    def validar_mensagem(self, mensagem):
        if not mensagem or not mensagem.strip():
            raise ValueError('Mensagem não pode ser vazia!')
        
    @abstractmethod    
    def enviar(self, destinatario, mensagem):
        pass

class NotificadorEmail(Notificador):
    def __init__(self, remetente):
        self.remetente = remetente

    def __repr__(self):
        return f"NotificadorEmail(remetente='{self.remetente}')"
    
    def __eq__(self, outro):
        if not isinstance(outro, NotificadorEmail):
            return False
        return self.remetente == outro.remetente

    def enviar(self, destinatario, mensagem):
        self.validar_mensagem(mensagem)
        print(f'Email de {self.remetente} para {destinatario}: {mensagem}')

class NotificadorSMS(Notificador):
    def enviar(self, destinatario, mensagem):
        self.validar_mensagem(mensagem)
        if len(mensagem) > 160:
            mensagem = mensagem[:160]
            print("Aviso, mensagem cortada para 160 caracteres!")
        print(f'SMS para {destinatario}: {mensagem}')

class NotificadorSlack(Notificador):
    def __init__(self, canal):
        self.canal = canal

    def enviar(self, destinatario, mensagem):
        self.validar_mensagem(mensagem)
        mensagem_formatada = f'[SLACK] {self.canal} → {destinatario}: {mensagem}'
        print(mensagem_formatada)

class GerenciadorNotificacoes:
    def __init__(self):
        self.canais = []

    def __str__(self):
        tipos = ", ".join([type(canal).__name__ for canal in self.canais])
        return f'Lista de canais com {len(self.canais)} canais e com esses tipos: {tipos}'

    def __len__(self):
        return len(self.canais)

    def adicionar_canal(self, notificador):
        if not isinstance(notificador, Notificador):
            raise TypeError('Precisa ser um Notificador!')
        self.canais.append(notificador)

    def notificar_todos(self, destinatario, mensagem):
        for canal in self.canais:
            canal.enviar(destinatario, mensagem)

    def notificar_canal(self, tipo, destinatario, mensagem):
        for canal in self.canais:
            if isinstance(canal, tipo):
                canal.enviar(destinatario, mensagem)

# Criando o gerenciador
gerenciador = GerenciadorNotificacoes()

gerenciador.adicionar_canal(NotificadorEmail("AgencyX@gmail.com"))
gerenciador.adicionar_canal(NotificadorSMS())
gerenciador.adicionar_canal(NotificadorSlack("#alerts"))
gerenciador.notificar_todos("juliodev7@gmail.com", "Pedido aprovado!")
gerenciador.notificar_canal(NotificadorSMS, "juliodev7@gmail.com", "Código: 6767")

print(gerenciador)      
print(len(gerenciador)) 

email1 = NotificadorEmail("AgencyX@gmail.com")
email2 = NotificadorEmail("AgencyX@gmail.com")
email3 = NotificadorEmail("outro@gmail.com")

print(email1 == email2)  # True
print(email1 == email3)  # False
print(repr(email1)) 