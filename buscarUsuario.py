import csv
import os

def buscaUsuario():
    if os.path.exists("UsuariosCab.csv"):
        f = open("UsuariosCab.csv", newline='')

        cont = 0
        inf = input("Insira seu nome ou cpf -> ").title()
        pessoas = csv.DictReader(f, delimiter=",")
        for linha in pessoas:
            if (inf == linha['Nome']) or (inf == linha['CPF']):
                cont += 1
                print("\n CPF: ",linha['CPF'], "\n","Nome: ", linha['Nome'], "\n","Tipo: ", linha['Tipo'], '\n',"Quantidade de livros emprestados: ", linha['QuantidadeEmprestado'], '\n',
                      "Data do novo empréstimo: ", linha['DataNovoEmprestimo'])

        if cont == 0:
            print("\nUSUARIO NAO ENCONTRADO")

        f.flush()
        f.close()