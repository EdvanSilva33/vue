def new_func():
    estoque = {}
    return __name__,estoque

__name__, estoque = new_func()

def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        print("Produto já cadastrado.")
    else:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        estoque[codigo] = {'nome': nome, 'quantidade': quantidade}
        print(f"Produto '{nome}' cadastrado com sucesso.")

def adicionar_quantidade():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        quantidade_adicional = int(input("Digite a quantidade a ser adicionada: "))
        estoque[codigo]['quantidade'] += quantidade_adicional
        print(f"{quantidade_adicional} unidades adicionadas ao estoque do produto '{estoque[codigo]['nome']}'.")
    else:
        print("Produto não encontrado no estoque.")

def remover_quantidade():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        quantidade_remover = int(input("Digite a quantidade a ser removida: "))
        estoque[codigo]['quantidade'] -= quantidade_remover
        if estoque[codigo]['quantidade'] < 0:
            estoque[codigo]['quantidade'] = 0
        print(f"{quantidade_remover} unidades removidas do estoque do produto '{estoque[codigo]['nome']}'.")
    else:
        print("Produto não encontrado no estoque.")

def editar_produto():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        novo_nome = input("Digite o novo nome do produto: ")
        estoque[codigo]['nome'] = novo_nome
        print("Nome do produto atualizado.")
    else:
        print("Produto não encontrado no estoque.")

def retirar_produto():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        del estoque[codigo]
        print("Produto removido do estoque.")
    else:
        print("Produto não encontrado no estoque.")

def mostrar_estoque():
    print("\nEstoque:")
    for codigo, produto in estoque.items():
        print(f"Código: {codigo}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")
    print()

def main():
    while True:
        print("\nOpções:")
        print("1 - Cadastrar produto")
        print("2 - Adicionar quantidade")
        print("3 - Remover quantidade")
        print("4 - Editar produto")
        print("5 - Retirar produto")
        print("6 - Mostrar estoque")
        print("0 - Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            adicionar_quantidade()
        elif opcao == 3:
            remover_quantidade()
        elif opcao == 4:
            editar_produto()
        elif opcao == 5:
            retirar_produto()
        elif opcao == 6:
            mostrar_estoque()
        elif opcao == 0:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
