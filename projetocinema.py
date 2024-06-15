filmes = [
    {'Título': 'Guilherme e Rene: lutando pela tecnologia', 'Sala': '1', 'Horário': '14:00', 'Capacidade': '100', 'Valor': '25.00', 'Gênero': 'Ação', 'Quantidade Restante': '100'}, 
    {'Título': 'renan: o salvador de lagoa', 'Sala': '2', 'Horário': '16:00', 'Capacidade': '80', 'Valor': '20.00', 'Gênero': 'Aventura', 'Quantidade Restante': '80'}, 
    {'Título': 'Messi: O Goat', 'Sala': '3', 'Horário': '18:00', 'Capacidade': '50', 'Valor': '25.00', 'Gênero': 'Drama', 'Quantidade Restante': '50'}
]
usuarios = []
import re
import qrcode
 
def menu_principal():
    print('\033[94mSeja Bem vindo ao Menu Principal do Cine Lagoa!\033[0m')
    print('\033[94m1- Gerenciamento do Cine Lagoa\033[0m (ADM)')
    print('\033[94m2- Menu do Cliente\033[0m (CLIENTE)')
    print('\033[94m3- Cadastre-se\033[0m (ADM ou CLIENTE)')
    print('\033[94m4- Sobre nós\033[0m')
    print('\033[94m0- Sair\n\033[0m')

def menu_adm(nome_adm):
    print(f'Seja bem-vindo, ADM {nome_adm}.')
    while True:
        print('\nMenu do Administrador:')
        print('1- Cadastrar Filme')
        print('2- Buscar Filme')
        print('3- Atualizar Filme')
        print('4- Remover Filme')
        print('5- Visualizar Ingressos Vendidos')
        print('6- Visualizar as Avaliações dos Filmes')
        print("0- Sair")
        opcao_adm = input("Escolha uma opção: ")
        if opcao_adm == '1':
            cadastrar_filme()
        elif opcao_adm == '2':
            buscar_filme()
        elif opcao_adm == '3':
            atualizar_filme()
        elif opcao_adm == '4':
            remover_filme()
        elif opcao_adm == '5':
            visualizar_ingressos_vendidos()
        elif opcao_adm == '6':
            visualizar_avaliacoes_filmes()
        elif opcao_adm == '0':
            break
        else:
            print('\033[91mOpção inválida. Tente novamente.\033[0m')

def menu_cliente(nome_cliente):
    print(f'Seja bem-vindo, Cliente {nome_cliente}!')
    while True:
        print('\nÁrea do Cliente:')
        print('1- Comprar Ingressos')
        print('2- Avaliar Filmes')
        print('3- Ver Ingressos Comprados')
        print('0- Sair')
        opcao_cliente = input('Escolha uma opção: ')
        if opcao_cliente == '1':
            comprar_ingressos(nome_cliente)
        elif opcao_cliente == '2':
            avaliar_filme(nome_cliente)
        elif opcao_cliente == '3':
            ver_ingressos_comprados(nome_cliente)
        elif opcao_cliente == '0':
            break
        else:
            print('\033[91mOpção escolhida é inválida. Tente novamente.\033[0m')

def cadastrar_filme():
    print('\033[94mCadastro de Filme')
    titulo = input('\033[94mDigite o título do filme: ')
    while True:
        sala = input('\033[94mDigite o número da sala: ')
        if not sala.isdigit() or int(sala) <= 0:
            print('\033[91mNúmero de sala inválido. Por favor, digite um número inteiro positivo.\033[0m')
        else:
            break

    while True:
        capacidade = input('\033[94mDigite a capacidade da sala: ')
        if not capacidade.isdigit() or int(capacidade) <= 0:
            print('\033[91mCapacidade inválida. Por favor, digite um número inteiro positivo.\033[0m')
        else:
            break

    valor_valido = False
    while not valor_valido:
        valor = input('Digite o valor do ingresso: ')
        if valor.replace('.', '', 1).isdigit() and float(valor) > 0:
            valor_valido = True
        else:
            print('\033[91mValor inválido. Por favor, digite um número positivo.\033[0m')

    while True:
        horario = input('Digite o horário de exibição (formato HH:MM): ')
        if not re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', horario):
            print('\033[91mFormato de horário inválido. Por favor, use o formato HH:MM.\033[0m')
        else:
            break

    filme = {'Título': titulo, 'Sala': sala, 'Horário': horario, 'Capacidade': capacidade, 'Valor': valor, 'Quantidade Restante': capacidade}
    filmes.append(filme)
    print('\033[92mFilme cadastrado com sucesso!\033[0m')

def buscar_filme():
    titulo = input('Digite o título do filme que deseja buscar: ')
    encontrados = [filme for filme in filmes if filme['Título'].lower() == titulo.lower()]
    if encontrados:
        print('Filme encontrado:')
        for filme in encontrados:
            print(filme)
    else:
        print('Nenhum filme encontrado com esse título.')

def atualizar_filme():
    titulo = input('Digite o título do filme que deseja atualizar: ')
    encontrados = [filme for filme in filmes if filme["Título"].lower() == titulo.lower()]
    if encontrados:
        print('Filme encontrado:')
        for filme in encontrados:
            print(filme)
        novo_valor = input('Digite o novo valor do ingresso: ')
        if novo_valor.replace('.', '', 1).isdigit() and float(novo_valor) > 0:
            for filme in encontrados:
                filme['Valor'] = novo_valor
            print('\033[92mFilme atualizado com sucesso!\033[0m')
        else:
            print('\033[91mValor inválido. Por favor, digite um número positivo.\033[0m')
    else:
        print('Nenhum filme encontrado com esse título.')

def remover_filme():
    titulo = input('Digite o título do filme que deseja remover: ')
    encontrados = [filme for filme in filmes if filme["Título"].lower() == titulo.lower()]
    if encontrados:
        print('Filme encontrado:')
        for filme in encontrados:
            print(filme)
        confirmacao = input('Tem certeza que deseja remover este filme? (\033[92msim\033[0m/\033[91mnao): ')
        if confirmacao.lower() == 'sim':
            filmes.remove(encontrados[0])
            print('\033[92mFilme removido com sucesso!\033[0m')
    else:
        print('Nenhum filme encontrado com esse título.')

def pagar_com_pix(valor_total):
    chave_pix = '14567203410'
    pix_data = f'00020126360014BR.GOV.BCB.PIX0114{chave_pix}5204000053039865406{valor_total:.2f}5802BR5913Cine Lagoa6009SAO PAULO62070503***6304'
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(pix_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('pix_payment.png')
    print('\033[92mQR Code para pagamento via Pix gerado com sucesso! Escaneie o código para realizar o pagamento.\033[0m')
    print('pagamento feito com sucesso!')
    
def pagar_com_cartao(valor_total):
    while True:
        senha_cartao = input('Digite a senha do cartão (4 dígitos): ')
        if senha_cartao.isdigit() and len(senha_cartao) == 4:
            print(f'\033[92mPagamento efetuado com sucesso no cartão de crédito. O valor total é: R$ {valor_total:.2f} (com acréscimo de R$ 1,50). Obrigado pela compra, desejamos um otimo filme!\033[0m')
            print('Não esqueça de avaliar o filme em nosso programa após assisti-lo, assim saberemos se gostou. fechado?! Volte sempre!')
            return
        else:
            print('\033[91mSenha inválida. A senha deve conter 4 dígitos numéricos.\033[0m')     
       
def comprar_ingressos(nome_cliente):
    print(f'Seja bem-vindo, Cliente {nome_cliente}!')
    print('Comprar Ingressos:')
    if not filmes:
        print('\033[91mDesculpe, não há filmes disponíveis no momento.\033[0m')
        return

    while True:
        print('Filmes Disponíveis:')
        for index, filme in enumerate(filmes, start=1):
            print(f"{index}. Título: {filme['Título']}, Gênero: {filme['Gênero']}, Horário: {filme['Horário']}, Capacidade: {filme['Capacidade']}, Valor: {filme['Valor']}")

        escolha = input("Digite o número do filme que deseja assistir ou '0' para sair: ")

        if escolha == '0':
            print("Saindo do menu de compra de ingressos.")
            return

        if not escolha.isdigit():
            print("\033[91mOpção inválida. Por favor, escolha um filme em cartaz.\033[0m")
            continue

        escolha = int(escolha)
        if escolha < 1 or escolha > len(filmes):
            print("\033[91mOpção inválida. Por favor, escolha um número válido.\033[0m")
            continue

        filme_escolhido = filmes[escolha - 1]
        print(f"Você escolheu o filme '{filme_escolhido['Título']}'")

        while True:
            quantidade_ingressos = input("Digite a quantidade de ingressos que deseja comprar: ")

            if not quantidade_ingressos.isdigit() or int(quantidade_ingressos) <= 0:
                print("\033[91mQuantidade inválida. Por favor, digite um número inteiro positivo.\033[0m")
                continue

            quantidade_ingressos = int(quantidade_ingressos)

            if quantidade_ingressos > int(filme_escolhido["Quantidade Restante"]):
                print(f"\033[91mQuantidade inválida.\033[0m A capacidade máxima da sala é de {filme_escolhido['Quantidade Restante']} ingressos.")
            else:
                break

        valor_total_ingressos = quantidade_ingressos * float(filme_escolhido['Valor'])
        filme_escolhido['Quantidade Restante'] = str(int(filme_escolhido['Quantidade Restante']) - quantidade_ingressos)

        print(f"O valor total da compra é: R$ {valor_total_ingressos:.2f}")

        capacidade_atualizada = int(filme_escolhido['Capacidade']) - quantidade_ingressos
        filme_escolhido['Capacidade'] = str(capacidade_atualizada)

        with open(f"ingressos_{nome_cliente}.txt", "a") as file:
            file.write(f"Filme: {filme_escolhido['Título']}, Quantidade: {quantidade_ingressos}, Total: R$ {valor_total_ingressos:.2f}\n")

        print('\nFormas de Pagamento:')
        print('1 - Dinheiro')
        print('2 - Cartão de Crédito')
        print('3 - Pix')

        while True:
            forma_pagamento = input('Escolha uma forma de pagamento: ')

            if forma_pagamento == "1":
                print("\033[92mPagamento efetuado com sucesso no dinheiro. Obrigado pela compra, desejamos um ótimo filme!\033[0m")
                print('Não esqueça de avaliar o filme em nosso programa após assisti-lo, assim saberemos se gostou. fechado?! Volte sempre!')
                break
            elif forma_pagamento == "2":
                aproximacao_cartao = input("O seu cartão de crédito possui aproximação? (sim/não): ")
                if aproximacao_cartao.lower() == "sim":
                    print("\033[92mPagamento efetuado com aproximação. Obrigado pela compra, desejamos um ótimo filme!\033[0m")
                    print('Não esqueça de avaliar o filme em nosso programa após assisti-lo, assim saberemos se gostou. fechado?! Volte sempre!')
                    break
                elif aproximacao_cartao.lower() == "não":
                    pagar_com_cartao(valor_total_ingressos)
                    continue
                else:
                    print("\033[91mOpção inválida. Por favor, escolha 'sim' ou 'não'.\033[0m")
            elif forma_pagamento == "3":
                pagar_com_pix(valor_total_ingressos)
                break
            else:
                print("\033[91mOpção inválida. Por favor, escolha '1', '2' ou '3'.\033[0m")

        break

def cadastrar_usuario():
    while True:
        print("Cadastro de Usuário:")
        while True:
            nome = input("Digite seu nome: ").strip()
            if not nome:
                print("\033[91mNome não pode ser em branco. Por favor, digite seu nome.\033[0m")
                continue
            break

        while True:
            login = input("Digite um login: ").strip()
            if not login:
                print('\033[91mLogin não pode ser em branco. Por favor, digite um login.\033[0m')
                continue
            break

        while True:
            senha = input("Digite uma senha: ").strip()
            if not senha:
                print('\033[91mSenha não pode ser em branco. Por favor, digite uma senha.\033[0m')
                continue
            break

        for usuario in usuarios:
            if usuario['Login'] == login and usuario['Senha'] == senha:
                print('\033[91mErro: já existe um usuário cadastrado com esse login e senha.\033[0m')
                break
        else:
            while True:
                perfil = input('Digite seu perfil (ADM ou CLIENTE): ').upper()
                if perfil in ['ADM', 'CLIENTE']:
                    usuario = {'Nome': nome, 'Login': login, 'Senha': senha, 'Perfil': perfil}
                    usuarios.append(usuario)
                    print('\033[92mUsuário cadastrado com sucesso!\033[0m')
                    return
                else:
                    print("\033[91mOpção inválida: Perfil inválido.\033[0m Por favor, digite 'ADM' ou 'CLIENTE'.")

def realizar_login():
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    for usuario in usuarios:
        if usuario['Login'] == login:
            if usuario['Senha'] == senha:
                return usuario
            else:
                print('\033[91mSenha incorreta.')
                return None
    print('Usuário não encontrado.')
    return None

def visualizar_avaliacoes_filmes():
    print('Avaliações dos Filmes:')
    for filme in filmes:
        if 'Avaliação' in filme:
            print(f"Título: {filme['Título']}, Avaliação: {filme['Avaliação']} estrelas")
        else:
            print(f"Título: {filme['Título']}, Avaliação: Sem avaliação")

def visualizar_ingressos_vendidos():
    print('Visualizar Ingressos Vendidos por Filme:')
    for index, filme in enumerate(filmes, start=1):
        print(f"{index}. Título: {filme['Título']}, Sala: {filme['Sala']}, Horário: {filme['Horário']}")

    escolha = input("Digite o número do filme para visualizar os ingressos vendidos ou '0' para sair: ")

    if escolha == '0':
        print("Saindo do menu de visualização de ingressos vendidos por filme.")
        return

    if not escolha.isdigit():
        print("\033[91mOpção inválida. Por favor, escolha um filme em cartaz.\033[0m")
        return

    escolha = int(escolha)
    if escolha < 1 or escolha > len(filmes):
        print("\033[91mOpção inválida. Por favor, escolha um filme em cartaz.\033[0m")
        return

    filme_escolhido = filmes[escolha - 1]

    print(f"Ingressos Vendidos para o Filme '{filme_escolhido['Título']}':")
    ingressos_vendidos = int(filme_escolhido["Capacidade"]) - int(filme_escolhido["Quantidade Restante"])
    print(f"{ingressos_vendidos} de {filme_escolhido['Capacidade']} ingressos vendidos na sala {filme_escolhido['Sala']}")

    with open(f"ingressos_filme_{filme_escolhido['Título'].replace(' ', '_')}.txt", "w") as file:
        file.write(f"Ingressos Vendidos para o Filme: {filme_escolhido['Título']}\n")
        file.write(f"{ingressos_vendidos} de {filme_escolhido['Capacidade']} ingressos vendidos na sala {filme_escolhido['Sala']}\n")


def ver_ingressos_comprados(nome_cliente):
    print(f'Ingressos Comprados por {nome_cliente}:')
    arquivo_ingressos = f'ingressos_{nome_cliente}.txt'
    try:
        with open(arquivo_ingressos, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print('Nenhum ingresso comprado encontrado.')

def avaliar_filme(nome_cliente):
    print('Avaliar Filmes')

    print('Filmes Disponíveis para Avaliação:')
    for index, filme in enumerate(filmes, start=1):
        print(f"{index}. Título: {filme['Título']}, Sala: {filme['Sala']}, Horário: {filme['Horário']}")

    escolha = input("Digite o número do filme que deseja avaliar ou '0' para sair: ")

    if escolha == '0':
        print('Saindo do menu de avaliação de filmes.')
        return

    if not escolha.isdigit():
        print('\033[91mOpção inválida. Por favor, escolha um filme em cartaz.\033[0m')
        return

    escolha = int(escolha)
    if escolha < 1 or escolha > len(filmes):
        print('\033[91mOpção inválida. Por favor, escolha um filme em cartaz.\033[0m')
        return

    filme_escolhido = filmes[escolha - 1]
    if 'Avaliação' in filme_escolhido and filme_escolhido['Avaliação']['Usuário'] == nome_cliente:
        print('\033[91mVocê já avaliou este filme anteriormente.\033[0m')
        return

    avaliacao = input('Digite sua avaliação para o filme (de 1 a 5 estrelas): ')

    if not avaliacao.isdigit() or int(avaliacao) < 1 or int(avaliacao) > 5:
        print('\033[91mAvaliação inválida. Por favor, escolha um número de 1 a 5.\033[0m')
        return

    comentario = input('Digite um comentário sobre o filme (opcional): ')

    filme_escolhido['Avaliação'] = {'Usuário': nome_cliente, 'Estrelas': int(avaliacao), 'Comentário': comentario}
    print('\033[92mAvaliação registrada com sucesso!\033[0m')

def menu_sobre_nos():
    print('\nCriação do cine Lagoa: O Cine Lagoa nasceu da paixão do seu proprietario, pedro e de seu socio renan, por filmes e da vontade de criar um espaço onde as pessoas pudessem se  divertir e se emocionar juntas. inspirado pela magia do cinema, nosso objetivo é proporcionar experiencias memoraveis, reunindo amigos e familias para desfrutar de histórias unicas no telão.')
    print('Precisa de ajuda e quer falar conosco?')
    print('WhatsApp: (83 996941127)')
    print('Instagram: @cinelagoaoficial')
    print('Email: Cinelagoaofc@gmail.com')
    print('\nDeseja:')
    print('1 - Voltar para o Menu Principal')
    print('2 - Cadastrar-se')
    opcao = input('Escolha uma opção: ')
    return opcao    

def iniciar_cinema():
    while True:
        menu_principal()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            usuario = realizar_login()
            if usuario and usuario['Perfil'] == 'ADM':
                menu_adm(usuario['Nome'])
            else:
                print('\033[91mAcesso negado. Apenas administradores podem acessar este menu.\033[0m')
        elif opcao == '2':
            usuario = realizar_login()
            if usuario and usuario['Perfil'] == 'CLIENTE':
                menu_cliente(usuario['Nome'])
            else:
                print('\033[91mAcesso negado. Apenas clientes podem acessar este menu.\033[0m')
        elif opcao == '3':
            cadastrar_usuario()
        elif opcao == '4':
            opcao_sobre_nos = menu_sobre_nos()
            if opcao_sobre_nos == '1':
                continue
            elif opcao_sobre_nos == '2':
                cadastrar_usuario()
            else:
                print('\033[91mOpção inválida. Retornando ao menu principal.\033[0m')
        elif opcao == "0":
            print('Saindo... Obrigado por utilizar o Cine Lagoa!')
            break
        else:
            print('\033[91mOpção inválida. Tente novamente.\033[0m')

iniciar_cinema()
