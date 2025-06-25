#Exercício 5: Chaves de Dicionário com Tuplas 
# Crie um dicionário chamado estoque onde as chaves são tuplas que representam (produto, tamanho) 
# e os valores são a quantidade em estoque. 
# Por exemplo: estoque = {("camiseta", "M"): 50, ("calça", "G"): 30}.
# Adicione um novo item ao estoque.
# Escreva um código para consultar a quantidade em estoque de um item específico 
# (ex: "camiseta" tamanho "M").

estoque = {
    ('agasalho', 'G'): 120, 
    ('blusa', 'P') : 30, 
    ('moleton', 'M') : 78, 
    ('short', 'GG') : 45
    }

roupa = input('Informe a peça de roupa: ').lower()
tamanho = input('Informe o tamanho: ').upper()

if (roupa, tamanho) in estoque:
    print(f'Quantidade: {estoque.get((roupa, tamanho))}')
else:
    print('Peça não disponivel.')
