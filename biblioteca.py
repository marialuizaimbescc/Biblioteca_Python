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