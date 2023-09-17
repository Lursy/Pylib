def princial(cadastro, find, Lib, loc_dev):
    return {
        "Cadastro": cadastro,
        "Usuários": (find, Lib.User),
        "Livros": (find, Lib.Book),
        "Locação": (loc_dev, True),
        "Devolução": (loc_dev, False),
        "Sair": exit}


def search(Lib):
    return {
        Lib.User: {
            "title": "Users",
            "input": "CPF",
            "database": Lib.User.usuarios()
        },
        Lib.Book: {
            "title": "Acervo",
            "input": "ID",
            "database": Lib.Book.acervo()
            }
        }
