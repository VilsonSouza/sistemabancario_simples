class Banco:
    SAQUE_MAX = 3
    saqueDia = 1

    def __init__(self, agencia, conta, saldo=0, extrato=""):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extrato = extrato

    def __str__(self) -> str:
        return f"Agencia {self.agencia} Conta: {self.conta} Saldo R$:{self.saldo}"

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Saldo: R${self.saldo}")
            self.extrato += f"Saldo: R${self.saldo}\n"  # Adiciona o valor do saldo ao extrato com quebra de linha
        else:
            print("Valor Inválido")

    def saque(self, valor):
        if valor > self.saldo:
            print("Valor de saque Maior que o Saldo")
        elif valor > 500:
            print("Valor Maior que o Limite de Saque")
        elif self.saqueDia > self.SAQUE_MAX:
            print("Máximo de Saques Excedido")
        else:
            self.saldo -= valor
            self.extrato += f"Saque Realizado Saldo Atual: R${self.saldo}\n"  # Adiciona o valor do saque ao extrato com quebra de linha
            print(f"Saque Realizado Saldo Atual: R${self.saldo}")
            self.saqueDia += 1

    def imprimir_extrato(self):  # Renomeado o método para imprimir_extrato
        print("\n============Extrato============")
        print(self.extrato)


# Exemplo de uso:
b1 = Banco("1234", "5678")
b1.deposito(200)
b1.saque(70)
b1.saque(20)
b1.saque(10)

b1.imprimir_extrato()
