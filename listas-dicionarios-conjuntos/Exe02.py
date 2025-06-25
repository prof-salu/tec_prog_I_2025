#Exercício 2: Cardápio de Pizzaria 
# Crie um dicionário que represente o cardápio de uma pizzaria. 
# As chaves devem ser os sabores das pizzas (ex: "Calabresa") e os valores devem ser os preços. 
# Escreva um código que pergunte ao usuário um sabor de pizza e, se o sabor existir no cardápio, 
# exiba o preço. Caso contrário, exiba a mensagem "Sabor não disponível".

cardapio = {'muçarela' : 45, 'portuguesa' : 49, 'marguerita' : 40, 'presunto' : 42}

busca = input('Informe o sabor da pizza: ').lower()

if busca in cardapio:
    print(f'Preço: {cardapio[busca]}')
else:
    print('Sabor não disponível')
