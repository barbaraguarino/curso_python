from aluno import Aluno

def iniciar_sistema():
    banco_de_alunos = []

    print("Sistema de Cadastro Escolar")

    while True:
        nome_input = input("Digite o nome do aluno: ")
        matricula_input = input("Digite a matrícula: ")

        novo_aluno = Aluno(nome_input, matricula_input)
        banco_de_alunos.append(novo_aluno)

        print(f"Aluno {novo_aluno.nome} cadastrado com sucesso!")

        continuar = input("\nDeseja cadastrar outro? (S/N): ").strip().upper()
        if continuar != 'S':
            break

    print("\nRelatório de Alunos Cadastrados")

    for aluno_atual in banco_de_alunos:
        print(aluno_atual.exibir_info())


if __name__ == "__main__":
    iniciar_sistema()