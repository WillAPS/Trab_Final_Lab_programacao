import csv
import datetime
import os


def cadastraUsuario():
    if os.path.exists("UsuariosCab.csv"):
        header_exists = True
    else:
        header_exists = False

    f = open("UsuariosCab.csv", "a")

    print("BEM VINDO AO CADASTRO DE USUARIO")
    print("Insira as informações necessarias")

    campos = ['CPF', 'Nome', 'Tipo', 'QuantidadeEmprestado', 'DataNovoEmprestimo']
    usuarios = csv.DictWriter(f, fieldnames=campos)

    if not header_exists:
        usuarios.writeheader()


    cpf = input("Insira seu cpf -> ")
    nome = input("Insira seu nome -> ").title()

    tipo = input("Insira seu tipo (Professor ou Estudante ) -> ")
    while(tipo.lower() != 'professor') and (tipo.lower() != 'estudante'):
        tipo = input(" Por favor insira novamente o seu tipo -> ")
    if tipo.lower() == 'professor':
        tipo = 'Professor'
    elif tipo.lower() == 'estudante':
        tipo = 'Estudante'

    quantidadeEmprestado = 0

    dataNovoEmprestimo = datetime.datetime.now()
    dataNovoEmprestimo = dataNovoEmprestimo.strftime('%d/%m/%Y')

    inf = dict(CPF=cpf, Nome=nome, Tipo=tipo, QuantidadeEmprestado=quantidadeEmprestado, DataNovoEmprestimo=dataNovoEmprestimo)

    if usuarios.writerow(inf):
        print("\nUsuario Cadastrado com sucesso")

    f.flush()
    f.close()

