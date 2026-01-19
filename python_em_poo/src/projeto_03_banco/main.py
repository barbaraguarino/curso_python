from python_em_poo.src.projeto_03_banco.banco import Conta

def menu():
    print("-"*15)
    print("1 - Saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")
    print("-"*15)

def main():
    print("Vamos iniciar nossas operações no banco.")

    nome = str(input("Digite o nome do titular: "))
    saldo = float(input("Digite o valor do saldo: "))

    banco = Conta(nome, saldo)

    while True:
        menu()
        op = int(input("Digite a opção escolhida:"))
        if op == 1:
            print(f"O valor atual na conta é {banco.saldo}")
        elif op == 2:
            valor = float(input("Valor para saque: "))
            banco.sacar(valor)
        elif op == 3:
            valor = float(input("Valor para deposito: "))
            banco.depositar(valor)
        elif op == 4:
            break

if __name__ == "__main__":
    main()