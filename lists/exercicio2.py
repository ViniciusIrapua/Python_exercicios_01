numeros = list(range(1,11))
print(numeros)
#pares = [num for num in numeros if num % 2 == 0]
pares = numeros[1::2]
print("Lista de números pares:", pares)
pares[2] = 15
print(pares)
print('o mumero "15" foi adicionado na terceira posiçãona lista. ')
