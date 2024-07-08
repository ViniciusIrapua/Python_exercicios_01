# receber a idade do usuario como inteiro em uma variável
var_idade = int(input("qual a sua idade?"))
#testa se a idade é maior ou igual a 16 anos
if var_idade >= 16:
    #se é maior ou igual (verdade = true)
    #mostre a mensagem abaixo no terminal
    print("você pode votar")
else:
    #se é menor (mentira = false)
    print("você não pode votar")
   