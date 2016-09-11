# Abre o arquivo 'name' e retorna uma lista com índices no
# formato [produto, quantidade, preço]
def openFile(name):
    try:
        l = []
        f = open(name)
        for i in f:
            l.append(i[0:len(i) - 1])
        l.append("\n")
        return l

    except:
        print("Erro: o arquivo", name, "nao foi encontrado")
        raise SystemExit


def linhaPraDados(lista):
    # Os 3 ultimos são '\n'      V
    lista = lista[0:len(lista) - 3].split("\n")
    l = []
    for i in lista:
        splited = i.split(", ")
        splited[1] = int(splited[1])
        splited[2] = float(splited[2])
        l.append(splited)
    return l
