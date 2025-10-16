#!/bin/bash

def menu():
	print("/n=== CALCULADORA PYTHON ===")
	print("1. Soma (+)")
	print("2. Subtração (-)")
	print("3. Multiplicação (*)")
	print("4. Divisão (/)")
	print("5. Potência (^)")
	print("6. Sair")
	print("===========================")

def calculador(opcao):
	if opcao in ["1", "2", "3", "4", "5"]:
		try:
			num1 = float(input("Digite o primeiro número: "))
			num2 = float(input("Digite o segundo número: "))
		except ValueError:
			print("Entrada inválida. Digite apenas números.")
			return
		if opcao == "1":
			resultado = num1 + num2
			print(f" Resultado: {num1} + {num2} = {resultado}")
		elif opcao == "2":
			resultado = num1 - num2
			print(f" Resultado: {num1} - {num2} = {resultado}")
		elif opcao == "3":
			reultado = num1 * num2
			print(f" Resultado: {num1} * {num2} = {resultado}")
		elif opcao == "4":
			if num2 == 0:
				print("Erro divisão por zero não é permitida")
			else
				resultado = num1 / num2
				print(f" Resultado: {num1} / {num2} = {resultado}")
		elif opcao == "5":
			resultao = num1 ** num2
			print(f" Resultado: {num1} ^ {num2} = {resultado}")
	else:
		print("Opção Inválida. escolha de 1 a 6")

def main():
	while True:
		menu()
		opcao = input("Escolah uma opção:")
		if opcao == "6":
			print("Encerrando a calculadora. Até breve!")
			break

		calculadora(opcao)

if __name__ == "__main__":
	main()
