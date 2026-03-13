def salvar_resultado_em_arquivo(nome, casa):
    # Salva o nome do jogador e a casa em um arquivo chamado 'resultados.txt'.
    try:
        # Abre o arquivo em modo de anexação ('a') para adicionar o novo registro
        with open('resultados.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"Nome: {nome} | Casa: {casa}\n")
        print(f"\nResultado salvo com sucesso em 'resultados.txt'.")
    except Exception as e:
        print(f"\nErro ao salvar o resultado no arquivo: {e}")

def exibir_historico_e_pontuacao():
    # Lê todos os resultados salvos, calcula a pontuação total por casa e imprime o histórico.
    pontuacao_total = {
        "Grifinoria": 0,
        "Sonserina": 0,
        "Corvinal": 0,
        "Lufa Lufa": 0
    }

    historico = []

    try:
        # Tenta ler o arquivo e processar os resultados
        with open('resultados.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                historico.append(linha.strip())

                # Procura o nome da casa na linha e incrementa o contador
                for casa in pontuacao_total.keys():
                    if f"Casa: {casa}" in linha:
                        pontuacao_total[casa] += 1
                        break

    except FileNotFoundError:
        print("\nO arquivo 'resultados.txt' não foi encontrado. Nenhum resultado anterior para mostrar.")
        return
    except Exception as e:
        print(f"\nErro ao ler ou processar o arquivo de resultados: {e}")
        return

    # --- Exibe o Histórico Detalhado ---
    print("\n================================================")
    print("=== HISTÓRICO DE CLASSIFICAÇÕES DO CHAPÉU SELETOR ===")
    if historico:
        for linha in historico:
            print(linha)
    else:
        print("Nenhum resultado foi salvo ainda.")
    print("================================================")

    # --- Exibe o Placar Total ---
    print("\n====== PLACAR TOTAL DAS CASAS (Contagem de Alunos) ======")
    # Ordena as casas por pontuação (do maior para o menor)
    casas_ordenadas = sorted(pontuacao_total.items(), key=lambda item: item[1], reverse=True)

    for casa, pontos in casas_ordenadas:
        print(f"{casa}: {pontos} pontos")
    print("=======================================================")

def menu(nome):
    print('==================================')
    print(f'Bem vindo ao CHAPÉU SELETOR, {nome}!')
    print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠒⠒⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡰⠋⠀⠈⡆⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⢠⠴⠊⠁⡏⠠⡀⢧⣀⠀⠀⠈⠑⠢⡀⠀⠄⠘⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡎⠁⠀⠀⠀⠀⠙⠦⡀⠀⠹⡷⠤⠭⠵⡄⢱⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠏⠀⠀⠀⠀⣀⣀⣀⠀⠈⠙⡎⠁⠀⠀⠀⠈⢦⡹⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠋⠁⠀⠀⠀⢠⣎⠭⠥⠤⢀⠀⠡⣇⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠴⠶⡾⢂⡀⠀⠀⢀⡰⠏⠁⢀⣮⣤⣄⠑⠖⠽⡄⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⢀⢰⣃⣤⡀⠈⠀⠀⡰⠊⠉⠀⣠⣶⣿⣿⣿⣿⡅⠘⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠂⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠈⠱⡽⣷⣆⠀⢸⡅⠀⣰⣾⣿⣿⣿⣿⡿⡟⡁⡄⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠳⠿⠿⠧⠼⠱⠞⠙⠛⠿⠭⠥⠴⠟⠊⠅⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⡠⠈⠀⠀⢀⡀⠀⠀⠀⠁⠀⠀⠀⠀⠀⢀⠀⡀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⢀⡎⣩⣴⣶⣶⣶⣷⣿⣿⣷⣿⣶⣶⡶⠶⠞⠒⠒⢍⡙⣾⣆⣀⠀⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠱⡄⠀⠀⠀⠀⠀⢀⢀⡗⠨⡻⢿⣿⣿⣿⡿⠿⠛⠋⢉⠁⠤⠀⠀⠀⠀⢉⠉⠕⢊⣉⡩⠭⠥⣖⣲⢄⡀⠀
⠀⠀⠀⠀⠈⠣⡙⢶⡲⡤⣄⢠⠴⢏⢀⡠⢔⠲⠮⢄⣀⣀⣈⡠⠔⠉⠉⠀⠀⠀⢀⣀⠥⠒⠈⠁⠀⠀⠀⠀⠀⠈⠑⢗⠆
⠀⠀⠀⠀⠀⠀⠈⠪⡱⢵⣌⠂⠀⠀⠀⠀⠀⠈⠀⠂⠀⠢⠁⠀⠀⠀⠐⣀⠤⠖⠛⠒⠒⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠎
⠀⠀⠀⠀⠀⠀⠀⠆⠈⠢⡉⠳⠦⠄⡀⠀⠀⠄⠀⠀⠀⠀⠁⢀⣠⣖⡉⠀⠀⣀⣀⣄⠠⠤⠤⠶⠤⠤⠤⠤⠖⠒⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠑⠦⠄⢀⣨⣀⣈⡡⠤⠴⠒⠊⡉⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """) # Mantendo o desenho simples, se quiser o detalhado troque pelo que enviamos
    print('==================================')
    print("Que tal descobrir sua casa em Hogwarts?")

def selecionar_casa(perguntas_list, jogador_nome):
    # Deixa as casas com a pontução em 0 no começo
    casas = {"grifinoria": 0, "sonserina": 0, "corvinal": 0, "lufalufa": 0}

    # Loop das perguntas para receber as respostas
    for pergunta_texto, respostas in perguntas_list:
        while True:
            try:
                pergunta = int(input(pergunta_texto))
                if pergunta in respostas:
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção existente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        casa = respostas.get(pergunta)
        if casa:
            casas[casa] += 1

    # Pontuação final das casas
    grifinoria = casas["grifinoria"]
    sonserina = casas["sonserina"]
    corvinal = casas["corvinal"]
    lufalufa = casas["lufalufa"]

    # Variável para armazenar a casa final para salvar no arquivo
    casa_final = None

    # Determine and print the final house
    if grifinoria > corvinal and grifinoria > sonserina and grifinoria > lufalufa:
        casa_final = "Grifinoria"
        print(f"{jogador_nome} sua casa é... \n{casa_final}!")
    elif corvinal > grifinoria and corvinal > sonserina and corvinal > lufalufa:
        casa_final = "Corvinal"
        print(f"{jogador_nome}, sua casa é... \n{casa_final}!")
    elif sonserina > grifinoria and sonserina > corvinal and sonserina > lufalufa:
        casa_final = "Sonserina"
        print(f"{jogador_nome}, sua casa é... \n{casa_final}!")
    elif lufalufa > grifinoria and lufalufa > corvinal and lufalufa > sonserina:
        casa_final = "Lufa Lufa"
        print(f"{jogador_nome}, sua casa é... \n{casa_final}!")
    else:
        casa_final = "Não decidida"
        print("o chapeu seletor não consegue decidir a sua casa")

    # CHAMA A FUNÇÃO PARA SALVAR O RESULTADO
    if casa_final != "Não decidida":
        salvar_resultado_em_arquivo(jogador_nome, casa_final)
    else:
        print("O resultado não foi salvo pois a casa não foi decidida.")

# --- Início da Execução Principal ---

# Pergunta se o usuário quer ver os resultados antes de começar, e exibe o histórico e placar total
opcao = input("Deseja ver o Histórico e Placar Total de testes anteriores (S/N)? ").strip().upper()
if opcao == 'S':
    exibir_historico_e_pontuacao()

nome_do_jogador = input("Digite seu nome: ").capitalize()

menu(nome_do_jogador)


# Lista de perguntas e suas respostas
perguntas = [
    ("Qual a sua estação preferida do ano ?\n1-Verão\n2-Inverno\n3-Outono\n4-Primavera\n", {1: "grifinoria", 2: "sonserina", 3: "corvinal", 4: "lufalufa"}),
    ("Você se considera uma pessoa: \n1-Determinada\n2-Ambiciosa\n3-Inteligênte\n4-Leal\n", {1: "grifinoria", 2: "sonserina", 3: "corvinal", 4: "lufalufa"}),
    ("Em um grupo de trabalho, quem você se considera? \n1-O criativo\n2-O Determinado\n3-O paciênte\n4-O líder\n", {2: "grifinoria", 4: "sonserina", 1: "corvinal", 3: "lufalufa"}),
    ("Se você for escolher um animal de estimação no mundo bruxo, qual seria? \n1-Gato\n2-Coruja\n3-Largato\n4-Coelho\n", {2: "grifinoria", 3: "sonserina", 1: "corvinal", 4: "lufalufa"}),
    ("O que te motiva? \n1-A busca de expandir conhecimentos\n2-A lealdade que posso dar as pessoas\n3-Expressar coragem e determinação\n4-Focar naquilo que me favoreça\n", {3: "grifinoria", 4: "sonserina", 1: "corvinal", 2: "lufalufa"}),
    ("Qual dos itens mágicos abaixo você escolheria? \n1-A Capa da Invizibilidade\n2-A Pedra da Ressurreição\n3-A Varinha das Varinhas\n4-Pedra Filosofal\n", {1: "grifinoria", 3: "sonserina", 4: "corvinal", 2: "lufalufa"}),
]


# Chama a função para rodar o código
selecionar_casa(perguntas, nome_do_jogador)