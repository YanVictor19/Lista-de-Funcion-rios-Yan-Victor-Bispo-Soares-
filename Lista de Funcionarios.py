# Sistema de gerenciamento de funcionários

funcionarios = []

def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    funcionarios.append({"nome": nome, "salario": salario})
    print(f"Funcionário {nome} adicionado com sucesso!\n")

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return
    print("\n--- Lista de Funcionários ---")
    for i, f in enumerate(funcionarios, start=1):
        print(f"{i}. Nome: {f['nome']} | Salário: R$ {f['salario']:.2f}")
    print()

def buscar_funcionario():
    nome_busca = input("Digite o nome do funcionário que deseja buscar: ")
    encontrados = [f for f in funcionarios if nome_busca.lower() in f['nome'].lower()]
    if encontrados:
        print("\n--- Funcionários encontrados ---")
        for f in encontrados:
            print(f"Nome: {f['nome']} | Salário: R$ {f['salario']:.2f}")
        print()
    else:
        print("Nenhum funcionário encontrado com esse nome.\n")

def calcular_media_salarial():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.\n")
        return
    media = sum(f['salario'] for f in funcionarios) / len(funcionarios)
    print(f"Média salarial: R$ {media:.2f}\n")

def menu():
    while True:
        print("=== Sistema de Funcionários ===")
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Buscar funcionário por nome")
        print("4. Calcular média salarial")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            buscar_funcionario()
        elif opcao == "4":
            calcular_media_salarial()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Executa o menu principal
menu()
