# --- Saída de Dados ---

# Print de mensagens com aspas simples e aspas duplas.
print("Olá Mundo! Estou usando aspas duplas.")
print('Olá mundo! Estou usando aspas simples.')

# Print de dados numéricos
print(2+2)
print(27)

# --- Concatenação e Junção ---

# Diferença entre Vírgula e Mais
print('Olá', 5)    # Saída: Olá 5 (Aceita tipos mistos)
# print('Olá' + 5) # ERRO: TypeError (Não concatena str com int)
print('Olá' + '5') # Saída: Olá5 (Concatenação de strings)

# --- Variáveis e Atribuição

# Atribuição de Variáveis
nome = 'Guanabara'  # Tipo str
idade = 25          # Tipo int
peso = 75.8         # Tipo float

print(nome, idade, peso)

# --- Entradas de Dados ---

variavel = input('Mensagem de prompt: ')
print(variavel)