#Exercício 1: Informações do Aluno
# Crie um dicionário para armazenar o nome, a idade, o curso e a cidade de um estudante. 
# Em seguida, imprima cada uma dessas informações.

aluno = {'nome' : 'Juca', 'idade' : 32, 'curso' : 'Gastronomia', 'cidade' : 'Belo Horizonte'}

for chave,  valor in aluno.items():
    print(f'{chave.capitalize()}: {valor}')