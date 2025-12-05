from lampada import Lampada


def usar_interruptor():
    minha_lampada = Lampada()

    while True:
        print("\n" + "=" * 30)
        print(minha_lampada.mostrar_estado())
        print("=" * 30)

        print("1. Ligar")
        print("2. Desligar")
        print("3. Ajustar Luminosidade")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            minha_lampada.ligar()

        elif opcao == '2':
            minha_lampada.desligar()

        elif opcao == '3':
            # Note que convertemos a entrada para inteiro
            novo_valor = int(input("Digite a intensidade (0-100): "))
            minha_lampada.ajustar_luminosidade(novo_valor)

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    usar_interruptor()