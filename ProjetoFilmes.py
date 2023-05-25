filmes = []
opcao = 2


print('---Bem vindo a locadora!!---')

while opcao != 6:
    print()
    print('''
   (1) Adicionar filmes
   (2) Modificar lista de filmes
   (3) Listar filmes
   (4) Apagar todos os filmes
   (5) Apagar filmes por id
   (6) Sair
    ''')
    print()
    
    opcao = int(input('Qual opção você deseja? '))
    
    if opcao == 1:
        print()
        filme = input('Fale qual filme você deseja adicionar: ')
        filmes.append(filme)
        print()
        print('Filme adicionado com sucesso.')
    elif opcao == 2:
        print()
        if len(filmes) == 0:
            print('Não existe nenhum filme na sua lista para editar.')
        else:
            for i in range(len(filmes)):
                print(str(i+1), '-Filme: ', filmes[i])
            valor = int(input('Informe o ID do filme que deseja editar: '))
            if valor > 0 and valor <= len(filmes):
                novo_filme = input('Digite o novo filme: ')
                filmes[valor - 1] = novo_filme
                print('Filme alterado com sucesso!!')
    elif opcao == 3:
        print()
        if len(filmes) == 0:
            print('Nenhum filme foi adicionado na lista!!')
        else:
            for i in range(len(filmes)):
                print(str(i+1), '-Filmes:',filmes[i])
    elif opcao == 4:
        if len(filmes) == 0:
            print('Não existe filmes para ser apagados!')
        elif len(filmes) != 0:
            print()
            desejo = int(input('Você realmente deseja deletar toda sua lista? Sim(1)  Não(2)'))
            print()
            if desejo == 1:
                filmes.clear()
                print('Todos os filmes apagados.')
            else:
                print('Ação cancelada')
    elif opcao == 5:
        if len(filmes) == 0:
            print('Não existem filmes para serem apagados!!')
        else:
            for i in range(len(filmes)):
                print(str(i+1), '-Filmes:', filmes[i])
            apagar = int(input('Qual filme deseja apagar? '))
            if apagar > 0 and apagar <= len(filmes):
                filmes.pop(apagar - 1)
                print('Filme apagado com sucesso!!')
            else:
                print('Opção inválida!')
    elif opcao == 6:
        print()
        print('Obrigado por usar nosso sis1tema.')
    else:
        print()
        print('Opção invalida!')


