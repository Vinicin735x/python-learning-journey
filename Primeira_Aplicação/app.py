import os

restaurantes = [{'nome': 'la mama', 'categoria': 'comida brasileira', 'ativo':False},
                {'nome': 'america', 'categoria': 'pizza', 'ativo':True}]

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
    print("3. Alternar estado")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
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
            alternar_estado()
        elif opcao_escolhida == 4:
            finalizar_app()
        
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input("Informe o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            print(f"O Restaurante {nome_restaurante} já cadastrado meu fi\n")
            input("Digite uma tecla para tentar novamente: ")
            cadastrar_restaurante()
            return
    else:
        restaurantes.append(dados_restaurante)
        print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!!\n")
        input("Digite uma tecla para voltar à página inicial: ")
        main()

def listar_restaurantes():
    exibir_subtitulo('Listagem dos restaurantes')

    print(f"{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | 'Status'\n")
    for restaurante in restaurantes:
        nome_rest = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f".{nome_rest.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    input("\nDigite uma tecla para voltar à página inicial: ")
    main()

def alternar_estado():
    exibir_subtitulo("Alternando o estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    rest_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            rest_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f"\nO restaurante {nome_restaurante} foi ativado com sucesso!!") if restaurante['ativo'] else (f'\nO restaurante {nome_restaurante} foi desativado com sucesso')
            print(mensagem)
    if not rest_encontrado:
        print(f"\nO restaurante {nome_restaurante} não foi encontrado meu chapa")

    voltar_menu()

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