#função saque
def saque(*, saque, saldo, valor, extrato, numero_saques):
    if numero_saques < 3:
        while (valor > 500) or (valor <= 0) or (valor > saldo):
            if (valor > 500) and (valor <= saldo):
                print("Limite de R$ 500.00 excedido! Tente novamente.")
                return saldo, extrato, numero_saques

            elif valor <= 0:
                print("Valor invalido! Tente novamente.")
                return saldo, extrato, numero_saques
                    
            elif valor > saldo:
                print("Saldo insuficiente!")
                return saldo, extrato, numero_saques
            else:
                saldo -= valor
                extrato += f"Saque                  R${saque:.2f}\n"
                numero_saques += 1
                print(f"""
                Saque de R${saque:.2f} realizado com sucesso!
                Saques restantes: {3 - numero_saques}
                
                Saldo atual: R${saldo:.2f} """)
     
                return saldo, extrato, numero_saques            
    else:
        print("Limite de n° de saques excedido!")
        return saldo, extrato, numero_saques

#função deposito
def deposito(saldo, valor, extrato, /, ):
    if(valor < 0):
        print('Valor invalido! Tente novamente.')
        return saldo, extrato
    else:
        saldo += valor
        extrato += f"Deposito               R${valor:.2f}\n"
        numero_depositos += 1
        print(f"""
        Deposito de R${valor:.2f} realizado com sucesso!
        
        Saldo atual: R${saldo:.2f}""")
        return saldo, extrato
        
#função extrato
def ext(saldo, numero_saques, numero_depositos, /, *, extrato):
    print(f"""
            EXTRATO
    ******************************
    Limite de saques     3
    Saques realizados    {numero_saques}
    Depositos            {numero_depositos}
    -------------------------------""")
    print(f"SALDO ANTERIOR        R$1320.00")
    print("-------------------------------")
    print("\nNenhuma movimentacao realizada.\n" if not extrato else extrato)
    print("_______________________________")
    print(f"SALDO ATUAL           R${saldo:.2f}\n")
    print("_______________________________")

#função criar_usuario
def cadastro(usuarios):
    cpf = input('Informe o CPF (apenas numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nCPF ja cadastrado!')
    else:
        nome = input('Informe o nome completo: ')
        data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
        endereco = input('Informe o endereco completo (rua, número - bairro - cidade/sigla estado): ')
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("\nUsuario cadastrado com sucesso!\n")

#função filtrar_usuario
def filtrar_usuario(cpf, usuarios):
    lista_aux = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return lista_aux[0] if lista_aux else None

#função criar_conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('\nInforme o CPF (somente numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print('\nUsuario nao encontrado! Volte ao menu e tente novamente.\n')

#função listar_contas
def listar_contas(contas):
    print("\nCONTAS:\n")
    for conta in contas:
        lista = f"""
        Agencia:        {conta[agencia]}
        Conta Corrente: {conta[numero_conta]}
        Titular:        {conta[usuario]}
        _____________________________________ """

#módulo principal (main)
def main():
    AGENCIA = "0001"
    valor = 0
    saldo = 0
    numero_depositos = 0
    numero_conta = 0
    conta = {}
    extrato = ""
    usuarios = []
    contas = []
    continuar = True

    while continuar == True:

        op = int(input("""
        ========MENU========
        1. Depositar
        2. Sacar
        3. Extrato
        4. Nova Conta
        5. Cadastrar Usuário
        6. Listar Contas
        0. Sair
        ____________________
        => """))

        if op === 1:
            valor = float(input('Digite o valor do deposito: '))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif op === 2:
            valor = float(input('Digite o valor do saque: '))
            saldo, extrato, numero_saques = sacar(
                saque = saque, 
                saldo = saldo, 
                valor = valor, 
                extrato = extrato, 
                numero_saques = numero_saques,
            )
        
        elif op == 3:
            ext(saldo, numero_saques, numero_depositos, extrato)
        
        elif op == 4:
            cadastro(usuarios)
        
        elif op == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif op == 6:
            listar_contas(contas)
        
        elif op == 0:
            continuar = False
            break
        
        else:
            print('Operacao invalida! Volte ao menu e tente novamente.')


