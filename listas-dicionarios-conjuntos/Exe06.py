#Exercício 6: Removendo Duplicados 
# Você recebeu uma lista de números com valores duplicados: 
# numeros = [10, 20, 30, 10, 20, 40, 50, 50, 60]. Use um conjunto para remover todos os elementos 
# duplicados da lista e, em seguida, imprima a nova lista de números únicos.

numeros = [10, 20, 30, 10, 20, 40, 50, 50, 60]

conjunto = set(numeros)

print(sorted(conjunto))
print(sorted(conjunto, reverse=True))