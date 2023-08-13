
#criando as variáveis 
menu = """
                 
=====BANCO DIO=====

Seja bem vindo!

Escolha uma opcao:

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair
------------------
-> """

saldo = 1320
deposito = 0
numero_depositos = 0
saque = 0
limite_saque = 0
extrato = ""
op = True

#estrutura de repetição while para navegar pelo menu e operações subjacentes
while op == True:
    operacao = int(input(menu))
    
    if operacao == 1:
        deposito = float(input("""

Digite o valor do deposito
R$: """))
        saldo += deposito
        extrato += f"Deposito               R${deposito:.2f}\n"

        print(f"""
Deposito realizado com sucesso!""")
        deposito = 0
        numero_depositos += 1
    
    if operacao == 2:
        if limite_saque < 3:
            while (saque > 500) or (saque <= 0) or (saque > saldo):
                saque = float(input("""
SAQUE
Digite o valor do saque
R$: """))
                if (saque > 500) and (saque <= saldo):
                    print("Limite de R$ 500.00 excedido! Tente novamente.")
                elif saque <= 0:
                    print("Valor invalido! Tente novamente.")
                elif saque > saldo:
                    print("Saldo insuficiente! Tente novamente.")
                else:
                    saldo -= saque
                    extrato += f"Saque                  R${saque:.2f}\n"
                    limite_saque += 1
                    print(f"""
Saque realizado com sucesso!
Saques restantes: {3 - limite_saque} """)
                
        else:
            print("Limite de n° de saques excedido!")
    
    if operacao == 3:
        print(f"""
              
           EXTRATO
******************************
Limite de saques     3
Saques realizados    {limite_saque}
Depositos            {numero_depositos}
-------------------------------""")
        print(f"SALDO ANTERIOR        R$1320.00")
        print("-------------------------------")
        print("\nNenhuma movimentação realizada.\n" if not extrato else extrato)
        print("_______________________________")
        print(f"SALDO ATUAL           R${saldo:.2f}\n")
        print("_______________________________")
        
        
    
    if operacao == 0:
        op = False
        break

    if (operacao < 0) and (operacao > 4):
        print("Operação invalida! Tente novamente.")


        


