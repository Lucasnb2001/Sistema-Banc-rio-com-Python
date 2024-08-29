# Exibe o menu de opções para o usuário e captura sua escolha 
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

# Realiza a operação de depósito no saldo do usuário
def depositar(saldo, extrato):
    # Lê e guarda o valor de depósito do usuário
    valor = float(input("Informe o valor do depósito: "))
    # Caso o depósito seja positivo
    if valor > 0:
        # Itera sobre o valor do salso (inicialmente 0)
        saldo += valor
        # Guarda o valor depositado na variável extrato
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    # Caso contrário
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Realiza a operação de saque, verificando o saldo, o limite e o número de saques permitidos
def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    # Lê e guarda o valor de saque do usuário
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

# Exibe o extrato das movimentações e o saldo atual do usuário
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    # Extrato das transações
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
