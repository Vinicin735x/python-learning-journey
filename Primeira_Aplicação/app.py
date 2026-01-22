import os

restaurantes = []

def exibir_nome():
     print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def opcao_invalida():
    print("Opção inválida, favor escolher uma das disponíveis\n")
    voltar_menu()

def escolher_opc():
    try:
        opcao_escolhida = int(input("Selecione uma opção: "))
        print(f"Você escolheu a opção: {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            print("Ativar restaurante")

        elif opcao_escolhida == 4:
            finalizar_app()
        
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input("Informe o nome do restaurante: ")

    if nome_restaurante in restaurantes:
        print(f"O Restaurante {nome_restaurante} já cadastrado meu fi\n")
        input("Digite uma tecla para tentar novamente: ")
        cadastrar_restaurante()
        return
    
    else:
        restaurantes.append(nome_restaurante )
        print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!!\n")
        input("Digite uma tecla para voltar à página inicial: ")
        main()

def listar_restaurantes():
    exibir_subtitulo('Listagem dos restaurantes')

    for restaurante in restaurantes:
        print(f".{restaurante}")

    input("\nDigite uma tecla para voltar à página inicial: ")
    main()

def voltar_menu():
    input("Digite uma tecla para voltar a tela inicial: ")
    main()

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def main():
    os.system('clear')
    exibir_nome()
    exibir_opcoes()
    escolher_opc()



if __name__ == '__main__':
    main()