import csv
import os
import datetime

from datetime import *

def devolucaoLivro():
	if os.path.exists("EmprestimoCab.csv"):
		f = open("EmprestimoCab.csv", newline = "")
		f2 = open("UsuariosCab.csv", newline = "")
		f3 = open("LivrosCab.csv", newline = "")

		fa = open("a.csv", "w")
		fb = open("b.csv", "w")
		fc = open("c.csv", "w")

		camposEmprestimo = ["IDEmprestimo", "IDLivro", "CPF", "InicioEmprestimo", "DataMaximaEntrega", "DataDevolucao", "Renovacoes"]
		camposUsuario = ["CPF", "Nome", "Tipo", "QuantidadeEmprestado", "DataNovoEmprestimo"]
		camposLivro = ["IDLivro", "Titulo", "Autor", "Area", "Paginas", "Ano", "Palavra1", "Palavra2", "Palavra3", "Emprestado"]

		idemprestimo = input("Digite o ID do empréstimo: ")
		emprestimos = csv.DictReader(f, delimiter = ",")
		usuarios = csv.DictReader(f2, delimiter = ",")
		livros = csv.DictReader(f3, delimiter = ",")

		emprestimosWrite = csv.DictWriter(fa, fieldnames = camposEmprestimo)
		usuariosWrite = csv.DictWriter(fb, fieldnames = camposUsuario)
		livrosWrite = csv.DictWriter(fc, fieldnames = camposLivro)

		emprestimosWrite.writeheader()
		usuariosWrite.writeheader()
		livrosWrite.writeheader()

		i = 0
		j = 0
		k = 0
		for linhas in emprestimos:
			if idemprestimo == linhas["IDEmprestimo"]:
				i = 1
				for linhas2 in livros:
					if int(linhas2["IDLivro"]) == int(linhas["IDLivro"]):
						j = 1
						if linhas2["Emprestado"] == 'True':
							linhas2["Emprestado"] = False
							dia = int(input("Dia da devolução: "))
							mes = int(input("Mês da devolução: "))
							ano = int(input("Ano da devolução: "))
							t1 = date(year = ano, month = mes, day = dia)
							t2 = datetime.strptime(linhas["DataMaximaEntrega"], "%d/%m/%Y")
							if t2 < t1:
								print("Atraso na entrega do livro.")
								punicao = t1 - t2
								for linhas3 in usuarios:
									if linhas3["CPF"] == linhas["CPF"]:
										k = 1
										linhas3["DataNovoEmprestimo"] = t1 + 2*punicao
										if linhas3["QuantidadeEmprestado"] > 0:
											linhas3["QuantidadeEmprestado"] = int(linhas3["QuantidadeEmprestado"]) - 1
										else:
											print("Não há livros emprestados.")
									usuariosWrite.writerow(linhas3)
								if j == 0:
									print("Usuário não encontrado.")
							else:
								print("Devolução efetuada com sucesso.")
						else:
							print("Livro já devolvido.")
					livrosWrite.writerow(linhas2)
				if j == 0:
					print("Livro não encotrado.")
			emprestimosWrite.writerow(linhas)
		if i == 0:
			print("Empréstimo não encontrado.\n")
		os.remove("EmprestimoCab.csv")
		os.rename("a.csv", "EmprestimoCab.csv")
		fa.flush()
		fa.close()
		os.remove("LivrosCab.csv")
		os.rename("c.csv", "LivrosCab.csv")
		fc.flush()
		fc.close()
		os.remove("UsuariosCab.csv")
		os.rename("b.csv", "UsuariosCab.csv")
		fb.flush()
		fb.close()
	else:
		print("Não há empréstimos existentes.")