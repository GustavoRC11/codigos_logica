############################################
# 2026.08.10.Funcoes\agenda_furreca.py     #
# AGENDA FURRECA.PY                        #
# Versão 2026.08.10                        #
# By Luferat - https://github.xonm/Luferat #
############################################

# Importa "subprocess" e "os" que permitem executar comandos do sistema
import subprocess
import os

import json

# Importa "random" para gerar números aleatórios
import random

# Banco de dados em memória (dict)
ARQUIVO_DATABASE = "database.json"

def carregar_database():
    if os.path.exists(ARQUIVO_DATABASE):
        with open(ARQUIVO_DATABASE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return {}


def salvar_database():
    with open(ARQUIVO_DATABASE, "w", encoding="utf-8") as arquivo:
        json.dump(database, arquivo, ensure_ascii=False, indent=4)


database = carregar_database()

# Limpa a tela


def cls():
    if os.name == "nt":
        # Se o sistema é Windows
        subprocess.run("cls", shell=True)
    else:
        # Outros sistemas como Linux e MacOS
        subprocess.run("clear", shell=True)

# Cadastra novo contato


def new_contact():
    # Limpa a tela
    cls()

    # Cabeçalho
    print("[ AGENDA FURRECA - NOVO CONTATO ]")
    print("\nDigite os dados do contato:\n")

    # Recebe os dados do usuário
    name = input(" • Nome: ")
    contact = input(" • Contato: ")

    # Gera o ID aleatório
    key = str(random.randint(1, 1000))

    def gerar_id():
    while True:
        key = str(random.randint(1, 1000))

        if key not in database:
            return key

            key = gerar_id()

database[key] = {
    "name": name,
    "contact": contact
}

salvar_database()

    # Salva o novo cadastro no formato "dict"
    database[key] = dict(name=name, contact=contact)

    ## Salva no arquivo JSON
    salvar_database()

    # Confirmação
    print(f"\nUsuário com ID {key} adicionado!")
    input("Tecle [Enter] para continuar")

    # Chama o menu principal
    main()

# Lista todos os registros


def list_contacts():
    # Limpa a tela
    cls()

    # Cabeçalho
    print("[ AGENDA FURRECA - LISTA CONTATOS ]")
    print()
    print(len(database), "usuários encontrados!")
    print()

    # Loop para iterar os registros usando o método `dict.items()`
    for key, value in database.items():
        # Formata a saída
        print("ID:", key)
        print(" • Nome:", value['name'])
        print(" • Contato:", value['contact'])
        print()

    # Confirma e chama o menu principal
    input("Tecle [Enter] para continuar")
    main()


def edit_contact():
    cls()
    print("[ AGENDA FURRECA - EDITA CONTATO ]")

    
    print()
    while True:
        key = input("Digite o ID do usuário: ")
        if key in database:
            break
        print("-----", "ID não encontrado!", "-----")

    print()
    print("ID:", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['contact'])
    print()

    print("Digite os novos dados:")

    # Recebe e valida o "name"
    while True:
        name = input(" • Nome: ")
        if name.strip() != "":
            break
        print("-----", "Digite um nome válido!", "-----")

    # Recebe e valida o "contact"
    while True:
        contact = input(" • Contato: ")
        if contact.strip() != "":
            break
        print("-----", "Digite um contato válido!", "-----")

    # Atualizar
    database[key] = dict(name=name, contact=contact)

    print()
    print("Contato atualizado!")
    input("Tecle [Enter] para continuar")
    main()



    input("Tecle [Enter] para continuar")
    main()


def delete_contact():
    cls()
    print("[ AGENDA FURRECA - APAGA CONTATO ]")

    # ...

    input("Tecle [Enter] para continuar")
    main()

def main(erro=str()):
    # Programa principal e "main loop"
    while True:
        # Limpa a tela
        cls()

        # Cabeçalho
        print("[ AGENDA FURRECA - MENU PRINCIPAL ]")

        # Exibe menu principal
        print('''
Opções:

1 - Novo contato
2 - Listar contatos
3 - Editar contato
4 - Apagar contato
0 - Sair do programa
    ''')

        # Exibe mensagem de erro se existir
        if erro:
            print("-----", erro, "-----")

        # Recebe opção do usuário
        opcao = input("Escolha uma opção: ")

        # Executa a opção selecionada
        match opcao:
            case "1":
                new_contact()
            case "2":
                list_contacts()
            case "3":
                edit_contact()
            case "4":
                delete_contact()
            case "0":
                # Limpa a tela, exibe confirmação e termina o programa
                cls()
                print("\nAcabou!")
                exit()
            case _:
                # Se escolheu uma opção inválida, chama o menu novamente, mas, com a mensagem de erro.
                erro = "Digite uma opção válida!"
                main(erro)


# "Roda" o programa
main()
