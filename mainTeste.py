from novoEmprestimo import *
from atualizaCadastroUsuario import *
from livrosEmprestados import *
from renovacaoEmprestimo import *
from devolucaoLivro import *
from buscarLivro import *
from buscarUsuario import *
from cadastrarLivro import *
from cadastrarUsuario import *
from menus import *

def main():
	i = 1
	
	while i != 0:
		menus()
		i = int(input("Digite a opção desejada: "))
		opcao = 1
		if i == 1:
			while opcao != 0:
				menuUsuario()
				opcao = int(input("Digite a opção desejada: "))
				if opcao == 1:
					atualizaCadastroUsuario()
				elif opcao == 2:
					buscaUsuario()
				elif opcao == 3:
					cadastraUsuario()
				elif opcao == 0:
					break
				else:
					print("Opção inválida.\n")
					
		elif i == 2:
			while opcao != 0:
				menuLivro()
				opcao = int(input("Digite a opção desejada: "))
				if opcao == 1:
					buscaLivro()
				elif opcao == 2:
					cadastraLivro()
				elif opcao == 3:
					novoEmprestimo()
				elif opcao == 0:
					break
				else:
					print("Opção inválida.\n")
				
		elif i == 3:
			while opcao != 0:
				menuEmprestimo()
				opcao = int(input("Digite a opção desejada: "))
				if opcao == 1:
					devolucaoLivro()
				elif opcao == 2:
					renovacaoEmprestimo()
				elif opcao == 3:
					livrosEmprestados()
				elif opcao == 0:
					break
				else:
					print("Opção inválida.\n")
		elif i == 0:
			break
		else:
			print("Opção inválida.\n")
		

