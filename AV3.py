import os

usuarios = {}
registros = {}

def cadastrar_usuario():
    print("Cadastro de Novo Usuário:")
    nome_usuario = input("Nome de usuário: ")
    if nome_usuario in usuarios:
        print("Usuário já existe!")
        return
    senha = input("Senha: ")
    usuarios[nome_usuario] = senha
    print("Usuário cadastrado com sucesso!")

def login():
    print("Login:")
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
        print("Login bem-sucedido!")
        return nome_usuario
    else:
        print("Nome de usuário ou senha incorretos!")
        return None

def criar_registro(usuario):
    print(f"Criar Registro (Usuário: {usuario}):")
    nome_registro = input("Nome do registro: ")
    if nome_registro in registros:
        print("Registro já existe!")
        return
    dados = input("Digite os dados do registro: ")
    registros[nome_registro] = dados
    print("Registro criado com sucesso!")

def ler_registro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista de Registros:")
    if not registros:
        print("Nenhum registro encontrado.")
        return
    for nome_registro, dados in registros.items():
        print(f"{nome_registro}: {dados}")

def atualizar_registro():
    print("Atualizar Registro:")
    nome_registro = input("Nome do registro a ser atualizado: ")
    if nome_registro not in registros:
        print("Registro não encontrado!")
        return
    dados = input("Digite os novos dados do registro: ")
    registros[nome_registro] = dados
    print("Registro atualizado com sucesso!")

def deletar_registro():
    print("Deletar Registro:")
    nome_registro = input("Nome do registro a ser deletado: ")
    if nome_registro in registros:
        del registros[nome_registro]
        print("Registro deletado com sucesso!")
    else:
        print("Registro não encontrado!")

def menu_principal(usuario):
    while True:
        print(f"Bem-vindo, {usuario}!")
        print("Escolha uma opção:")
        print("1 - Criar Registro")
        print("2 - Ler Registros")
        print("3 - Atualizar Registro")
        print("4 - Deletar Registro")
        print("5 - Sair")
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            criar_registro(usuario)
        elif opcao == '2':
            ler_registro()
        elif opcao == '3':
            atualizar_registro()
        elif opcao == '4':
            deletar_registro()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        input("Pressione Enter para continuar...")

def main():
    while True:
        print("Sistema de Login e Cadastro")
        print("1 - Login")
        print("2 - Cadastrar Novo Usuário")
        print("3 - Sair")
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == '1':
            usuario = login()
            if usuario:
                menu_principal(usuario)
        elif opcao == '2':
            cadastrar_usuario()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
