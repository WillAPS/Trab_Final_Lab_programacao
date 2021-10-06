import csv
import os
import datetime

from datetime import *

def renovacaoEmprestimo():
	if os.path.exists("EmprestimoCab.csv"):
		f = open("EmprestimoCab.csv", newline = '')
		f2 = open("a.csv", "w")
		f3 = open ("UsuariosCab.csv", newline = '')
		idemprestimo = input("Digite o ID do empréstimo: ")

		campos = ["IDEmprestimo", "IDLivro", "CPF", "InicioEmprestimo", "DataMaximaEntrega", "DataDevolucao", "Renovacoes"]
		camposUsuario = ["CPF", "Nome", "Tipo", "QuantidadeEmprestado", "DataNovoEmprestimo"]

		usuarios = csv.DictReader(f3, delimiter=",")
		emprestimoWrite = csv.DictWriter(f2, fieldnames = campos )
		emprestimoWrite.writeheader()
		emprestimos = csv.DictReader(f, delimiter = ",")

		i = 0
		for linhas in emprestimos:
			if linhas["IDEmprestimo"] == idemprestimo:
				i = 1
				if int(linhas["Renovacoes"]) < 2:
					linhas["Renovacoes"] = int(linhas["Renovacoes"]) + 1
					t1 = 0
					for  linhas2 in usuarios:
						if linhas["CPF"] == linhas2["CPF"]:
							if linhas2["Tipo"].lower() == "estudante":
								t1 = timedelta(days = 7)
							else:
								t1 = timedelta(days = 15)
					t2 = datetime.strptime(linhas["DataMaximaEntrega"], "%d/%m/%Y")
					t3 = t2 + t1
					linhas["DataMaximaEntrega"] = t3.strftime("%d/%m/%Y")
					print("Renovacao efetuada com sucesso")
				else:
					print("O empréstimo já atingiu o máximo de renovações.")
			emprestimoWrite.writerow(linhas)
		if i == 0:
			print("Empréstimo não encontrado.")
		os.remove("EmprestimoCab.csv")
		os.rename("a.csv", "EmprestimoCab.csv")
		f2.flush()
		f2.close()
	else:
		print("Não há empréstimos existentes.")