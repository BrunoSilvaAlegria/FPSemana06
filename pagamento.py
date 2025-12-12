class Pagamento:
    
    def processar_pagamento(self, quantia):
        pass

class CartaoCredito(Pagamento):
    
    numero_cartao = "" #1234 5678 9012 3456
    nome_titular = ""  #João Silva
    validade = "" #12/25
    ccv = "" #123
    
    def __init__(self, numero_cartao, nome_titular, validade, ccv):
        self.numero_cartao = numero_cartao.strip()
        self.nome_titular = nome_titular.strip()
        self.validade = validade.strip()
        self.ccv = ccv.strip()
    
    def processar_pagamento(self, quantia):
        print(f"€{quantia:.2f} com Cartão de Crédito ({self.numero_cartao})")
        
class PayPal(Pagamento):
    
    email = "" #jonas@email.com

    def __init__(self, email):
        self.email = email.strip()
    
    def processar_pagamento(self, quantia):
        print(f"€{quantia:.2f} com Paypal (email: {self.email})")

class TransferenciaBancaria(Pagamento):
    
    banco = "" #Banco
    agencia = "" #4 ints
    conta = "" #8 ints
    
    def __init__(self, banco, agencia, conta):
        self.banco = banco.strip()
        self.agencia = agencia.strip()
        self.conta = conta.strip()
    
    def processar_pagamento(self, quantia):
        print(f"€{quantia:.2f} com Transferência Bancária (banco: {self.banco}, conta: {self.conta})")


def realizar_pagamento(tipo, quantia):
    tipo.processar_pagamento(quantia)

