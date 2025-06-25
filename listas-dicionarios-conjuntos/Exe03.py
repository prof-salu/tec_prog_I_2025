#Exercício 3: Contagem de Palavras 
# Dada a frase: "o python é uma linguagem de programação poderosa e versátil para a análise de 
# dados e desenvolvimento web". Crie um programa que conte a frequência de cada palavra na frase e 
# armazene o resultado em um dicionário onde a chave é a palavra e o valor é o número de vezes que ela 
# aparece.

frase = 'o python é uma linguagem de programação poderosa e versátil para a análise de dados e desenvolvimento web'

lista_palavras = frase.split()

dicionario_palavras = dict()

for palavra in lista_palavras:
    dicionario_palavras[palavra] = lista_palavras.count(palavra)
    print(f'{palavra}: {dicionario_palavras.get(palavra)}')