import csv
import os

def buscaid():
    if os.path.exists("LivrosCab.csv"):
        ide = 0
        f1 = open("LivrosCab.csv", newline='')
        info = csv.DictReader(f1, delimiter=',')
        for linha in info:
                ide += 1
        return ide

    f1.flush()
    f1.close()


def cadastraLivro():
    if os.path.exists("LivrosCab.csv"):
        header_exists = True
    else:
        header_exists = False

    f = open("LivrosCab.csv", "a")

    print("BEM VINDO AO CADASTRO DE LIVROS")
    print("Insira as informações necessarias")

    areas = ('Ciencias Sociais', 'Ciencias Humanas', 'Ciencias Sociais e Aplicadas',
             'Engenharias', 'Linguisticas', 'Letras e Artes', 'Multidisciplinar')

    campos = ['IDLivro', 'Titulo', 'Autor', 'Area', 'Paginas', 'Ano',
              'Palavra1', 'Palavra2', 'Palavra3', 'Emprestado']

    livros = csv.DictWriter(f, fieldnames=campos)

    if not header_exists:
        livros.writeheader()

    idlivro = buscaid() + 1

    titulo = input("Insira o Titulo do Livro -> ").title()

    autor = input("Insira o Nome do Autor -> ").title()

    print('\n[1] = Ciencias Sociais')
    print('[2] = Ciencias Humanas')
    print('[3] = Ciencias Sociais e Aplicadas')
    print('[4] = Engenharias')
    print('[5] = Linguisticas')
    print('[6] = Letras e Artes')
    print('[7] = Multidisciplinar\n')
    opc = int(input("Insira a Area do Livro -> "))
    while (opc < 1) or (opc > 7):
        opc = int(input("Insira a Area novamente -> "))

    area = areas[opc-1]

    paginas = int(input("Insira a Quantidade de Paginas -> "))

    ano = int(input("Insira o Ano de Publicação -> "))

    palavra1 = input("Insira a palavra chave 1 -> ").title()

    palavra2 = input("Insira a palavra chave 2 -> ").title()

    palavra3 = input("Insira a palavra chave 3 -> ").title()

    emprestado = False

    inf = dict(IDLivro=idlivro, Titulo=titulo, Autor=autor, Area=area, Paginas=paginas, Ano=ano,
               Palavra1=palavra1, Palavra2=palavra2, Palavra3=palavra3,Emprestado=emprestado)

    if livros.writerow(inf):
        print("\nLivro Cadastrado com Sucesso")

    f.flush()
    f.close()
