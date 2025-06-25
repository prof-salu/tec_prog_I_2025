#Exercício 7: Inscrições em Eventos 
# Dois eventos de tecnologia ocorrerão simultaneamente: "Python Day" e "Data Science Summit".
# Crie dois conjuntos, python_day e data_science_summit, cada um contendo os nomes dos participantes 
# inscritos. Calcule e imprima:
                    # O número total de participantes únicos (sem contar duplicados).
                    # Os nomes dos participantes que se inscreveram em ambos os eventos.
                    # Os nomes dos participantes que se inscreveram apenas no "Python Day".

python_day = {'Juca', 'Ana', 'Pedro', 'Maria', 'Gabi', 'Joana'}
data_science_summit = {'Juca', 'Jonin', 'Harry', 'Gigi', 'Gabi'}

participantes_unicos = set.union(python_day,data_science_summit)

participantes_ambos_eventos = set.intersection(python_day, data_science_summit)
#participantes_ambos_eventos = python_day & data_science_summit

participantes_apenas_python_day = set.difference(python_day, data_science_summit)
#participantes_apenas_python_day = python_day - data_science_summit

print(f'Participantes unicos: {len(participantes_unicos)} --> {participantes_unicos}')
print(f'Participantes em Ambos os eventos: {participantes_ambos_eventos}')
print(f'Participantes apenas Python Day: {participantes_apenas_python_day}')
