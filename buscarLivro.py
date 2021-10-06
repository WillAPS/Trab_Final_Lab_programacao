import csv
import os


def mostraLivro(linha):
    print(" ID Livro:", linha['IDLivro'], '\n', "Título: ", linha['Titulo'], '\n', "Autor: ", linha['Autor'], '\n',
          "Área: ", linha['Area'], '\n',
          "Páginas: ", linha['Paginas'], '\n', "Ano: ", linha['Ano'], '\n', "Emprestado: ", linha['Emprestado'],"\n")


def buscaLivro():
    if os.path.exists("EmprestimoCab.csv"):
        f = open("LivrosCab.csv", newline='')

        cont = 0

        inf = input("Insira o metodo de busca (Palavra Chave / Titulo / Autor / Area) -> ").title()
        while(inf != 'Palavra Chave') and (inf != 'Titulo') and (inf != 'Autor') and (inf != 'Area'):
            inf = input("Insira o metodo de busca novamente (Palavra Chave / Titulo / Autor / Area) -> ").title()

        if inf == 'Palavra Chave':
            busca = input(' Insira a Palavra Chave -> ').title()
            print('\n')
            livros = csv.DictReader(f, delimiter=",")
            for linha in livros:
                if (busca.lower() == linha['Palavra1'].lower()) or (busca == linha['Palavra2'].lower()) or (busca == linha['Palavra3'].lower()):
                    cont += 1
                    mostraLivro(linha)

        elif inf == 'Area':

            print('\n[1] = Ciencias Sociais')
            print('[2] = Ciencias Humanas')
            print('[3] = Ciencias Sociais e Aplicadas')
            print('[4] = Engenharias')
            print('[5] = Linguisticas')
            print('[6] = Letras e Artes')
            print('[7] = Multidisciplinar\n')

            busca = int(input('Insira a Area -> '))
            while (busca > 7) or (busca < 1):
                busca = int(input('Insira novamente a area desejada -> '))

            print('\n')
            livros = csv.DictReader(f, delimiter=',')
            for linha in livros:
                if busca == 1 and linha['Area'] == 'Ciências Sociais':
                    cont += 1
                    mostraLivro(linha)

                elif busca == 2 and linha['Area'] == 'Ciências Humanas':
                    cont += 1
                    mostraLivro(linha)

                elif busca == 3 and linha['Area'] == 'Ciências Sociais e Aplicadas':
                    cont += 1
                    mostraLivro(linha)

                elif busca == 4 and linha['Area'] == 'Engenharias':
                    cont += 1
                    mostraLivro(linha)

                elif busca == 5 and linha['Area'] == 'Linguisticas':
                    cont += 1
                    mostraLivro(linha)

                elif busca == 6 and linha['Area'] == 'Letras e Artes':
                    cont += 1
                    mostraLivro(linha)

                elif busca == 7 and linha['Area'] == 'Multidisciplinar':
                    cont += 1
                    mostraLivro(linha)

        elif inf == 'Titulo':
            busca = input('Insira o Titulo(ou palavra) para busca -> ').title()
            print('\n')
            livros = csv.DictReader(f, delimiter=",")
            for linha in livros:
                if linha['Titulo'].find(busca) != -1:
                    cont += 1
                    mostraLivro(linha)

        elif inf == 'Autor':
            busca = input('Insira o nome do Autor para busca -> ').title()
            print('\n')
            livros = csv.DictReader(f, delimiter=",")
            for linha in livros:
                if linha['Autor'].find(busca) != -1:
                    cont += 1
                    mostraLivro(linha)

        if cont == 0:
            print("\nLivro Nao Encontrado")

        f.flush()
        f.close()