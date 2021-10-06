import csv
import os


def livrosEmprestados():
	if os.path.exists("EmprestimoCab.csv"):
		f = open("EmprestimoCab.csv", newline="")
		emprestados = csv.DictReader(f, delimiter=",")
		cpf = input(" Digite o cpf do usuário: ")

		i = 0
		print("\n")
		for linhas in emprestados:
			if cpf == linhas["CPF"]:
				i = 1
				print(" ID do empréstimo: ", linhas["IDEmprestimo"],)
				print(" ID livro: ", linhas["IDLivro"],)
				print(" Data do empréstimo: ", linhas["InicioEmprestimo"],)
				print(" Data de entrega: ", linhas["DataMaximaEntrega"],)
		if i == 0:
			print(" Empréstimo não encontrado.")
		f.close()
	else:
		print(" Não há empréstimos existentes.")