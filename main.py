from tools import functions, lib
from time import sleep

text = functions.Text
menu = functions.create_menu
options = ["Cadastro", "Usuários", "Livros", "Locação", "Devolução", "Sair"]


def logar(type: lib.Book) -> None:
    # requirements recebe os valores necessários para cadastrar o livro
    requirements = type.requirements() # [titulo, autor]
    text.clear()
    info = []

    print(text("Cadastro").title(style="rozzo"), end="")

    # Este for percorre todos os itens necessários para o cadastro do livro
    # salvando estes um a um na lista "info" e fazendo o cadastro logo após
    # a inserção de todos os dados
    for item in requirements:
        response = item[0](input(item[1]+": ")) # str(input("titulo: "))
        if response:
            info.append(response)
        else:
            print("A informação não pode estar vazia.")
            sleep(2)
            logar(type)
            return None
    
    if type == lib.Book:
        cadastro = lib.Book(titulo=info[0], autor=info[1], genero=info[2], estoque=info[3])
    else:
        cadastro = lib.User(nome=info[0], cpf=info[1], idade=info[2])

    text.clear()
    print(text("Cadastro").title(style="rozzo"), end="")
    view: dict = cadastro.view()

    for key, value in view.items():
        print(text(key + ":").yellow(), text(value).green())

    cadastro.registrar()
    print(text("REGISTRADO").green())
    sleep(3)


def cadastro():
    text.clear()
    cad = ["Usuário", "Livro"]

    print(text("Cadastro").title(), end="")
    print(text("[i]").yellow(), "-", text("digite qualquer outra tecla para voltar").green())
    print(menu(lista=cad))

    choice = int(input(text(":// ").yellow()))

    match(choice):
        case 1:
            logar(lib.User)
        case 2:
            logar(lib.Book)
        case _:
            print("Voltando...")
            sleep(2)


def livros():
    text.clear()
    print(text("acervo").title(), end="")
    
    acervo = lib.Book.acervo()
    print(menu(acervo.keys()))
    
    input()


def usuarios():
    text.clear()
    print(text("Users").title(), end="")

    users = lib.User.usuarios()
    
    cpf = input("CPF: ")
    if cpf in users.keys():
        pessoa: dict = users[cpf]
        for key, value in pessoa.items():
            print(f"{key}: {text(value).green()}")
    else:
        print(text("Usuário não encontrado").red())
    input()


def main():
    while True:
        text.clear()
        title = text("Pylib").title(style="cosmic")

        print(text(title).blue(), end="")
        print(text("Copyright © 2023 - Developed by Matheus & Paulo\n").yellow())
        print(menu(lista=options))
        choice = int(input(text(":// ").yellow()))

        match(choice):
            case 1:
                cadastro()
            case 2:
                usuarios()
            case 3:
                livros()
            case 4:
                pass
            case 5:
                pass
            case 6:
                break


if __name__ == "__main__":
    main()
