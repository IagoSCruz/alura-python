'''
1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
'''

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Numero é par')
else:
    print('Numero é impar')
    

'''
2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
'''

idade = int(input('Informe a sua idade: '))

if idade <= 12:
    print(f'A idade de {idade} é considerada como Criança.')
elif idade <= 18:
    print(f'A idade de {idade} é considerada de Adolescente')
else:
    print('Adulto')
    
    
    
