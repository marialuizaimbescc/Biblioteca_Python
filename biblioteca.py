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
    for l in biblioteca: #mudei para poder separar o que quer mudar, ao invés de tudo junto
        if l.codigo == cod:
            print("Alterando:", l.titulo)
            print("1 - Título")
            print("2 - Autor")
            print("3 - Ano")
            opcao = input("O que deseja alterar? ")
            
            if opcao == "1":
                l.titulo = input("Novo título: ")
            elif opcao == "2":
                l.autor = input("Novo autor: ")
            elif opcao == "3":
                l.ano = input("Novo ano: ")
            else:
                print("Opção inválida!")
                
            print("Dados alterados!")
            encontrou = 1
            break # interrompe o loop após encontrar o livro
            
    if encontrou == 0:
        print("Livro não encontrado")


def busca_rapida():
    print("\n--- Busca Rápida (Opção 4) ---")
    cod = input("Digite o código: ")
    encontrou = 0 #te copiei
    for l in biblioteca:
        if l.codigo == cod:
            print("Título:", l.titulo)
            print("Número de exemplares (Total):", l.exemplares)
            print("Número de exemplares (Disponíveis):", l.disponiveis)
            encontrou = 1
    
    if encontrou == 0:
        print("Livro não encontrado")

def remover_livro():
    cod = input("Digite o código: ")
    encontrou = False  
    posicao_para_remover = 0
    
    for i in range(len(biblioteca)):
        if biblioteca[i].codigo == cod:
            posicao_para_remover = i
            encontrou = True 
            
    if encontrou == True:
        biblioteca.pop(posicao_para_remover) #remove pela posição
        print("Livro removido!")
    else:
        print("Livro não encontrado")

def listar_todos():
    print("\n--- Lista de Livros Disponíveis ---")

    disponiveis = []

    for l in biblioteca:
        if l.disponiveis > 0:
            disponiveis.append(l)

    if len(disponiveis) == 0:
        print("Nenhum livro disponível.")
    else:
    for i in range(len(disponiveis)): #ordernar sem sort pelo título
        for j in range(len(disponiveis)-1): #percorre a lista comparando com os elementos do lado
            if disponiveis[j].titulo > disponiveis[j+1].titulo:
                guarda = disponiveis[j] #guarda serve para a gnt não perder o livro enquanto ordena
                disponiveis[j] = disponiveis[j+1]
                disponiveis[j+1] = guarda

    for l in disponiveis:
        print("Título:", l.titulo, "| Ano:", l.ano, "| Na estante:", l.disponiveis)

def realizar_emprestimo():
    print("\n--- Empréstimo ---")
    cod = input("Digite o código: ")
    
    encontrou = 0
    for l in biblioteca:
        if l.codigo == cod:
            encontrou = 1
            if l.disponiveis > 0:
                l.disponiveis = l.disponiveis - 1
                print("Empréstimo realizado! Restam", l.disponiveis, "na estante.")
            else:
                print("Livro já emprestado (todos os exemplares estão fora)")
                
    if encontrou == 0:
        print("Livro não encontrado")
