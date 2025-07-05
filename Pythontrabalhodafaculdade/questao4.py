# Função de boas vindas e menu da livraria
print('Olá, seja Bem-vindo à livraria de Marcelo Augusto! ')
print( 50 * ('-'))
print(18 * ('-') + 'MENU PRINCIPAL' + 18 * ('-'))

lista_livro= []
id_global = 0

def cadastra_livro(id):
#MENU DE CADASTRAMENTO DOS LIVROS
  nome = input('\nDigite o nome do livro: ')
  autor = input('\nDigite o nome do autor:')
  editor = input('\nDigite o nome do editora:')

  livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editor} #Feito um dicionario com as palavras chaves dentro dele
  lista_livro.append(livro)
  print(f'\nLivro "{nome}" Cadastrado com sucesso!')

def consultar_livro():
  print(18 * ('-') + 'CONSULTAR LIVRO' + 18 * ('-')) ## Menu de consultar livros
  while True:
    print('\nQual opção deseja?')
    print('1- Consultar todos os livros')
    print('2- Consultar por ID')
    print('3- Consultar por Autor')
    print('4- Retornar ao MENU')

    opcao = int(input('\nEscolha uma Opção: '))
    print(25 * ('-') + 25 * ('-'))

    if opcao == 1:
      if lista_livro:
         for livro in lista_livro:
          print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
      else:
        print('Nenhum livro cadastrado!') # Caso não tenha nenhum livro cadastrado

    elif opcao == 2:
            id_consulta = int(input("Digite o ID do livro: "))
            encontrado = False # Caso nao tenha o ID do livro
            for livro in lista_livro:
                if livro['id'] == id_consulta:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrado = True # Caso tenha algum ID do livro cadastrado
                    break
            if not encontrado:
                print("Livro não encontrado pelo ID.")
    elif opcao == 3:
            autor_consulta = input("Digite o nome do autor: ")
            encontrado = False # Caso nao tenha autor(a) cadastrado no sistema
            for livro in lista_livro:
                if livro['autor'].lower() == autor_consulta.lower():
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrado = True # Caso tenha autor(a) cadastrado
            if not encontrado:
                print("Nenhum livro encontrado para este autor.")

    elif opcao == 4:
            break

    else:
      print('Opção inválida!')

def remover_livro():
    print(18 * ('-') + 'REMOVER LIVRO' + 18 * ('-'))
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    encontrado = False # Caso não tenha nenhuma livro á ser removido
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print(f"Livro com ID {id_remover} removido com sucesso!")
            encontrado = True # Está removendo com sucesso o livro cadastrado
            break
    if not encontrado:
        print("Id inválido. Livro não encontrado.")

while True:
  print("\nMenu principal:")
  print("\n1. Cadastrar Livro")
  print("2. Consultar Livro")
  print("3. Remover Livro")
  print("4. Encerrar Programa")

  opcao = input("\nEscolha uma opção: ")

  if opcao == '1':
    id_global += 1
    cadastra_livro(id_global)
  elif opcao == '2':
    consultar_livro()
  elif opcao == '3':
    remover_livro()
  elif opcao == '4':
    print("Programa encerrado.")
    break
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

