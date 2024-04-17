import os

def exibir_nome_programa():
    print("𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼")
    print()

def opcoes_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')


def finalizar_programa():
    os.system('clear')
    print('Finalizando o aplicativo\n')


def opcao_invalida():
    print('Opção Inválida\n')
    print('Digite uma tecla para voltar ao menu ')
    main()


def escolher_opcao():
    try:
        opcao = int(input('Selecione uma opção: '))
        print(f'Você escoheu a opção {opcao}')
    
        if opcao == 1:
            print('Cadastrar Restaurante')
        elif opcao == 2:
            print('Listar Restaurantes')
        elif opcao == 3:
            print('Ativar Restaurante')
        elif opcao == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
  
def main():
    os.system('clear')
    exibir_nome_programa()
    opcoes_menu()
    escolher_opcao()    
    
if __name__ == '__main__':
    main()