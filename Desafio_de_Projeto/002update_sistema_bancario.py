#função saque
def saque(*, saldo, valor, extrato, numero_saques):
    if numero_saques < 3:
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
                extrato += f"Saque                  R${valor:.2f}\n"

                numero_saques += 1

                print(f"""
                Saque de R${valor:.2f} realizado com sucesso!

                limite de saque: 3
                Saques realizados: {numero_saques}
                
                Saldo atual: R${saldo:.2f} """)
     
                return saldo, extrato, numero_saques           
    else:
        print("Limite de n° de saques excedido!")
        return saldo, extrato, numero_saques

#função deposito
def deposito(saldo, valor, extrato, numero_depositos, /, ):
    if(valor < 0):
        print('\nValor invalido! Volte ao menu e tente novamente.')
        return saldo, extrato, numero_depositos
    else:
        saldo += valor
        extrato += f"Deposito               R${valor:.2f}\n"
        numero_depositos += 1

        print(f"""
        Deposito de R${valor:.2f} realizado com sucesso!
        
        Saldo atual: R${saldo:.2f}""")
        return saldo, extrato, numero_depositos
        
#função extrato
def ext(saldo, numero_depositos, /, *, numero_saques, extrato):
    print(f"""
            EXTRATO
    ******************************
    Limite de saques     3
    Saques realizados    {numero_saques}
    Depositos            {numero_depositos}
    -------------------------------""")
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
        return
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
       linha = f"""
        Agencia:        {conta['agencia']}
        Conta Corrente: {conta['numero_conta']}
        Titular:        {conta['usuario']['nome']}
        _____________________________________ """
       print(linha)

#módulo principal (main)
def main():
    AGENCIA = "0001"
    saldo = 0
    numero_depositos = 0
    numero_saques = 0
    extrato = ""
    usuarios = []
    contas = []
    continuar = True


    while continuar == True:

        op = int(input("""\n
        ========DIO BANK========
        1. Depositar
        2. Sacar
        3. Extrato
        4. Nova Conta
        5. Cadastrar Usuário
        6. Listar Contas
        0. Sair
        ____________________
        => """))

        if op == 1:
            valor = float(input('\nDigite o valor do deposito: '))
            saldo, extrato, numero_depositos = deposito(saldo, valor, extrato, numero_depositos)
        
        elif op == 2:
            valor = float(input('\nDigite o valor do saque: '))
            saldo, extrato, numero_saques = saque(saldo = saldo, valor = valor, extrato = extrato, numero_saques = numero_saques)
        
        elif op == 3:
            ext(saldo, numero_depositos, numero_saques = numero_saques, extrato = extrato)
        
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
        
        else:
            print('\nOperacao invalida! Volte ao menu e tente novamente.')

#chamando a função main
main()


