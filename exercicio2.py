#receber o numero do usuario converte para inteiro e armazena em uma variável
var_numero = int(input("digite um numero:"))
if var_numero % 2 == 0:
    print(f"{var_numero} par")
else:
    print(f"{var_numero} impar")
