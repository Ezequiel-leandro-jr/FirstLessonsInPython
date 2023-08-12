#declaração e inicialização das variáveis utilizadas
saldo = 500
saque = 200
conta_normal = True
cheque_especial = 300
conta_universitaria = True
opcao = 0

#if
if saldo >= saque:
    print("realizando o saque!")


#if/else
if saldo >= saque:
    print("realizando o saque!")
else:
    print("saldo insuficiente!")


#elif
opcao = int(input("informe uma opção: [1]Sacar\n[2]Extrato\n: "))

if opcao == 1:
    valor = float(input('informe a quantia para o saque: '))
elif opcao == 2:
    print('Exibindo o extrato...')
else:
    sys.exit("Opção inválida.")


#if aninhado
if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso de cheque especial!')
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print('Saldo insuficiente!')


#if ternário
  #permite escrever uma condição em uma única linha. É composto por 3 partes 1°) retorno caso a expressão seja True
  #2°) expressão lógica e 3°) retorno caso a expressão não seja atendida
status = 'sucesso' if saldo >= saque else "Falha"
print(f"{status} ao retirar o saque!")


