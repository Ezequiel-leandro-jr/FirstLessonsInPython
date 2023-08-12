
#for
VOGAIS = "AEIOU"
texto = input('Informe um texto: ')

for letra in texto: #o for vai passar por cada caractere do texto digitado, armazeando em letra a cada loop
    if letra.upper() in VOGAIS: #se cada caractere armazenado em letra, ao transformado em maiúsculo, esteja em VOGAIS
        print(letra, end=" ") #será impresso, com um espaço ao fim. Ou seja, se for vogal, será impresso.

print() #adiciona uma quebra de linha ao fim do for



# range(stop) -> range object
# range(start, stop[, step]) -> range object
list(range(4)) #o range tá dentro de list para converter a range em list e assim poder imprimi-la devidamente
#>>>[0,1,2,3] impressão da range acima

#utilizando range com FOR
for numero in range(0, 11):
    print(numero, end=" ")
#>>> 0 1 2 3 4 5 6 7 8 9 10 impressão do for

#exibindo a tabuada do cinco
for numero in range(0, 51, 5):
    print(numero, end=" ")
#>>> 0 5 10 15 20 25 30 35 40 45 50 impressão do for


#while
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n: "))

    if opcao ==1:
        print("sacando...")
    elif opcao == 2:
        print('Exibindo o extrato...')


#uso do BREAK
while True:
    numero = int(input('Informe um número: '))

    if numero == 10:
        break

print(numero)

#>>> esse while é um loop infinito. Porém, seu if numero == 10 traz um break que, ao digitar 10, o loop encerra


#uso do CONTINUE
for numero in range(100):
    if numero == 12:
        continue

    print(numero, end=" ")

#>>> esse for irá imprimir números de 0 a 99, porém como tem if == 12 trazendo um continue, não irá imprimir o 12