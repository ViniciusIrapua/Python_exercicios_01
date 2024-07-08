#receber a temperatura em celsius do usuário como decimal em uma varável
var_celsius = float(input("digite a temperatuara em celsius"))

var_fahrenheit = var_celsius  * 9/5 + 32
print(f"a temperatura é {var_fahrenheit:.2f} °F")
