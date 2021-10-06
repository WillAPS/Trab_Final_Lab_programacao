import csv
import os
import datetime

from datetime import *

def atualizaCadastroUsuario():
	if os.path.exists("UsuariosCab.csv"):
		f = open("UsuariosCab.csv", newline = "")
		f2 = open("a.csv", "w")

		campos = ["CPF", "Nome", "Tipo", "QuantidadeEmprestado", "DataNovoEmprestimo"]

		usuario = input("Digite o CPF do cadastro que deseja modificar: ")
		pessoas = csv.DictReader(f, delimiter=",")
		usuarioWrite = csv.DictWriter(f2, fieldnames = campos)
		usuarioWrite.writeheader()

		achou = 0
		for linha in pessoas:
			if usuario == linha["CPF"]:
				achou += 1
				opcao = input("Escreva a opção que deseja atualizar(CPF//Nome//Tipo//QuantidadeEmprestado):  ")
				if opcao.lower() == "cpf":
					linha["CPF"] = input("Digite o novo CPF: ")
				elif opcao.lower() == "nome":
					nome = input("Digite o novo nome: ")
					linha["Nome"] = nome.title()
				elif opcao.lower() == "tipo":
					tipo = input("Digite o novo tipo(Estudante/Professor): ")
					linha["Tipo"] = tipo.title()
				elif opcao.lower() == "quantidadeemprestado":
					linha["QuantidadeEmprestado"] = input("Digite a nova quantidade de livros emprestados: ")
				elif opcao.lower() == "datanovoemprestimo":
					dia = int(input("Digite o dia do novo empréstimo: "))
					mes = int(input("Digite o mês do novo empréstimo: "))
					ano = int(input("Digite o mês do novo empréstimo: "))
					t = date(year = ano, month = mes, day = dia)
					t = t.strftime("%d/%m/%Y")
					linha["DataNovoEmprestimo"] = t
				else:
					print("Opção inválida")
			usuarioWrite.writerow(linha)
		os.remove("UsuariosCab.csv")
		os.rename("a.csv", "UsuariosCab.csv")
		f2.flush()
		f2.close()

		print("Usuario Atualizado com sucesso")

		if achou == 0:
			print("Usuário não encontrado.")
	else:
		print("Não há usuários existentes.")
