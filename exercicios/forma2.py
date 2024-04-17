print("𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼")
print()

lista_opcoes = ('1: Cadastrar Restaurante',
                '2: Listar Restaurantes',
                '3: Ativar Restaurante',
                '4: Sair')
                
for opcao in lista_opcoes:
    print(opcao)
print()

opcao_menu = int(input('Selecione uma opção: '))

if opcao_menu == 1:
    print(lista_opcoes[0])
elif opcao_menu == 2:
    print(lista_opcoes[1])
elif opcao_menu == 3:
    print(lista_opcoes[2])
else:
    print('Encerrando o programa')