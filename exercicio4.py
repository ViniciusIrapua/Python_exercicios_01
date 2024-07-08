var_numero1 = float(input("Digite o primeiro valor:"))
var_operacao = str(input("Escolha a operação matematica:"))
var_numero2 = float(input("Digite o segumdo valor:"))

if var_operacao == "+":
   print(var_numero1 + var_numero2)

elif var_operacao == "-":
    print(var_numero1 - var_numero2)

elif var_operacao == "*":
    print(var_numero1 * var_numero2)

elif var_operacao == "/":
    if var_numero2 != 0:
        print(f"{var_numero1 / var_numero2:.2f}")
    else:
            print("Não pode ser dividida por ZERO")

else:
    print(" Operação inválida, só pode ser calculado com esses sinais ( +, -, *, /)")