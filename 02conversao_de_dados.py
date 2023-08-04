print(int(1.9))
print(int("10"))
print(float("10.10")) #conseguiu converter para float por causa do ponto

print(str(10.10)) #não apareceu com as aspas, mas temos como saber o seu tipo com o comando abaixo
print(type(str(10.10))) # a função type( ) indica o tipo (class) da variável

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str)) #como essa variavel armazenou uma conversao para string da variavel valor, seu tipo aparece como string

print(100 / 2) #com um operador de divisão apenas, o resultado sai em float
print(100 // 2) #com dois operadores de divisão, o resultado sai em int


