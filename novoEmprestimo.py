import csv
import datetime
import os

from datetime import *

def novoEmprestimo():
	if os.path.exists("LivrosCab.csv"):
		if os.path.exists("EmprestimoCab.csv"):
			header_exists = True
		else:
			header_exists = False

		f = open("EmprestimoCab.csv", "a+", newline = '')
		f2 = open("LivrosCab.csv", newline = '')
		f3 = open("UsuariosCab.csv", newline = '')

		fb = open("b.csv", "w")
		fc = open("c.csv", "w")

		camposEmprestimo = ["IDEmprestimo", "IDLivro", "CPF", "InicioEmprestimo", "DataMaximaEntrega", "DataDevolucao", "Renovacoes"]
		camposUsuario = ["CPF", "Nome", "Tipo", "QuantidadeEmprestado", "DataNovoEmprestimo"]
		camposLivro = ["IDLivro", "Titulo", "Autor", "Area", "Paginas", "Ano", "Palavra1", "Palavra2", "Palavra3", "Emprestado"]

		emprestimoW = csv.DictWriter(f, fieldnames = camposEmprestimo)
		livroW = csv.DictWriter(fb, fieldnames = camposLivro)
		usuarioW = csv.DictWriter(fc, fieldnames = camposUsuario)

		if not header_exists:
			emprestimoW.writeheader()

		livroW.writeheader()
		usuarioW.writeheader()

		emprestimos = csv.DictReader(f, delimiter = ",")
		livros = csv.DictReader(f2, delimiter = ",")
		usuarios = csv.DictReader(f3, delimiter = ",")

		cpf = input("Digite o cpf do usuário: ")
		i = 0
		for linha3 in usuarios:
			if cpf == linha3["CPF"]:
				i = 1
				idlivro = int(input("Digite o ID do livro: "))
				for linha2 in livros:
					if int(linha2["IDLivro"]) == idlivro:
						if linha2["Emprestado"] == "True":
							print("Livro já emprestado.")
						else:
							linha2["Emprestado"] = True
							linha3["QuantidadeEmprestado"] = int(linha3["QuantidadeEmprestado"]) + 1
							ident = 0
							f.seek(0)
							for linha in emprestimos:
								ident = int(linha["IDEmprestimo"])
							ident += 1
							iniemprestimo = datetime.today()
							if linha3["Tipo"].lower() == "estudante":
								t1 = timedelta(days = 7)
							else:
								t1 = timedelta(days = 15)
							datamaxima = iniemprestimo + t1
							datamaxima = datamaxima.strftime("%d/%m/%Y")
							datadev = date.min
							datadev = datadev.strftime("%d/%m/%Y")
							iniemprestimo = iniemprestimo.strftime("%d/%m/%Y")
							renovacao = 0
							info = dict(IDEmprestimo = ident, IDLivro = idlivro, CPF = cpf, InicioEmprestimo = iniemprestimo, DataMaximaEntrega = datamaxima, DataDevolucao = datadev, Renovacoes = renovacao)
							emprestimoW.writerow(info)
							f.flush()
							f.close()
							print("Emprestimo realizado com sucesso.")
					livroW.writerow(linha2)
			usuarioW.writerow(linha3)
		if i == 0:
			print("Usuário não cadastrado.")
		os.remove("LivrosCab.csv")
		os.rename("b.csv", "LivrosCab.csv")
		fb.flush()
		fb.close()
		os.remove("UsuariosCab.csv")
		os.rename("c.csv", "UsuariosCab.csv")
		fc.flush()
		fc.close()
	else:
		print("Não há livros existentes.")