# classe simples
class livro:
    titulo = ''
    autor = ''
    ano = ''
    codigo = ''
    exemplares = 0 # Total de livros que a biblioteca comprou
    disponiveis = 0 # Quantos estão na estante agora

# Lista para guardar os livros
biblioteca = []

def cadastrar_livro():
    print("\n--- Cadastrar Livro ---") # Vamos deixar esse formato 
    cod = input("Digite o código do livro: ")
    
    # Verificar se o código já existe
    for l in biblioteca:
        if l.codigo == cod:
            print("Erro: Já existe um livro com este código!")
            return

    novo = livro()
    novo.codigo = cod #facilitou
    novo.titulo = input("Digite o título: ")
    novo.autor = input("Digite o autor (apenas o primeiro): ")
    novo.ano = input("Digite o ano de publicação: ")
    
    qtd = int(input("Quantidade de exemplares: "))
    novo.exemplares = qtd
    novo.disponiveis = qtd # todos estão disponíveis
    
    biblioteca.append(novo)
    print("Livro cadastrado com sucesso!")

def consultar_livro():
    print("\n--- Consultar Livro ---")
    print("1. Por código") #percorre a lista comparando o código
    print("2. Por autor") #percorre a lista pelo autor
    opcao = input("Escolha uma opção: ")

    encontrou = 0 #criei essa variável para saber se achou o livro
    if opcao == "1":
        cod = input("Digite o código: ")
        for l in biblioteca:
            if l.codigo == cod:
                print("Título:", l.titulo, "| Autor:", l.autor, "| Disponíveis:", l.disponiveis, "/", l.exemplares)
                encontrou = 1 #achou o livro
    
    if opcao == "2":
        aut = input("Digite o nome do autor: ")
        for l in biblioteca:
            if l.autor == aut:
                print("Código:", l.codigo, "| Título:", l.titulo, "| Disponíveis:", l.disponiveis)
                encontrou = 1 #achou o livro
    
    if encontrou == 0: #não achou
        print("Livro não encontrado")

def alterar_dados():
    print("\n--- Alterar Dados ---")
    cod = input("Digite o código do livro: ")
    
    encontrou = 0
    for l in biblioteca: #aqui vai percorrer e sobreescrever com os novos dados
        if l.codigo == cod:
            print("Alterando:", l.titulo)
            l.titulo = input("Novo título: ")
            l.autor = input("Novo autor: ")
            l.ano = input("Novo ano: ")
            print("Dados alterados!")
            encontrou = 1
            
    if encontrou == 0:
        print("Livro não encontrado")

