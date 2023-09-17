from infoFlib import Functions, Lib
from utils.abbreviators import *

from time import sleep

text = Functions.Text
menu = Functions.Tools.create_menu
cpf_validate = Functions.Tools.cpf_validate


def logar(type: Lib.Book):
    requirements = type.requirements()
    text.clear()
    info = []

    print(text("Cadastro").title(style="rozzo"), end="")

    for item in requirements:
        response = item[0](input(item[1]+": ")) # int(input("Titulo"+": "))
        if response:
            info.append(response)
        else:
            print("A informação não pode estar vazia.")
            sleep(2)
            logar(type)
            return None
    
    if type == Lib.Book:
        cadastro = Lib.Book(id=info[0], titulo=info[1], autor=info[2], genero=info[3], estoque=info[4])
    else:
        if cpf_validate(info[1]):
            cadastro = Lib.User(nome=info[0], cpf=info[1], idade=info[2])
        else:
            print(text("CPF inválido").red())
            sleep(3)
            logar(type)
            return None

    if cadastro.registrar():
        text.clear()
        view: dict = cadastro.view()    
        print(text("Cadastro").title(style="rozzo"), end="")

        for key, value in view.items():
            print(text(key + ":").yellow(), text(value).green())

        print(text("REGISTRADO").green())
    else:
        print(text("Registro já encontrado na database").red())
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
            logar(Lib.User)
        case 2:
            logar(Lib.Book)
        case _:
            print("Voltando...")
            sleep(2)


def find(type):
    busca = search(Lib=Lib)
    busca = busca[type]
    text.clear()
    print(text(busca["title"]).title(), end="")

    database = busca["database"]
    
    choice = input(busca["input"] + ": ")
    if choice in database.keys():
        pessoa: dict = database[choice]
        for key, value in pessoa.items():
            print(f"{key}: {text(value).green()}")
    else:
        print(text("não encontrado na database").red())
    
    input(f'\n\n{text("[i]").yellow()} - {text("tecle ENTER para voltar").green()}')


def loc_dev(type: bool):
    text.clear()
    print(text("Locacao" if type else "Devolucao").title())
    user = input("Digite o CPF do usuário: ")
    livro = input("Digite o ID do livro: ")

    valid = Lib.Loc(id=livro, cpf=user)
    
    if valid.locar_devo(type=type):
        print(text("sucesso!").green())
        sleep(3)
    else:
        print(text("Não foi possivel concluir a " + ("locação" if type else "devolução")).red())
        sleep(3)


def main():
    options = princial(cadastro=cadastro, find=find, Lib=Lib, loc_dev=loc_dev)

    while True:
        text.clear()
        title = text("PyLib").title(style="univers")

        print(text(title).blue(), end="")
        print(text("Copyright © 2023 - Developed by Matheus & Paulo\n").yellow())
        print(menu(lista=options.keys()))

        choice = int(input(text(":// ").yellow()))
        choice = list(options.keys())[choice-1]
        item = options[choice]

        if item.__class__ == tuple:
            item[0](item[1])
        else:
            item()


if __name__ == "__main__":
    main()
