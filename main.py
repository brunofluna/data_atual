# importando bibliotecas
import calendar
from datetime import date

# exibindo a data atual
print(date.today())

#exibindo no formato Brasil
dia = date.today().day
mes = date.today().month
ano = date.today().year

# saida de dados
print(f'Data atual: {dia}/{mes}/{ano}.')

# Criando uma Tupla para exibir por extenso.
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#saída da data
print(f'Data atual: {dia} de {meses[mes -1]} de {ano}.\n')
print(f'{'-' *5} MÊS ATUAL')
print(calendar.month(ano, mes))


