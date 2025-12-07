## Introdução

Até o momento, nossos programas exibiam apenas texto em branco (ou cinza) sobre um fundo preto. Para melhorar a experiência do usuário e destacar informações, utilizaremos as **Sequências de Escape ANSI** (ANSI Escape Sequences).

Embora existam bibliotecas externas (como `colorama` ou `termcolor`) que facilitam este processo, entender o padrão ANSI nativo é fundamental para ter controle total sobre o terminal sem depender de instalações extras.

## Estrutura do Código ANSI

Para o terminal interpretar que você quer uma cor, e não um texto, você deve enviar um comando especial. Todo código ANSI de cor em Python segue esta sintaxe rigorosa:

```python
\033[style;text;backm
```

**Detalhamento da Sintaxe:**

1. **`\033`**: É o código octal que representa o caractere **ESCAPE** (Esc) na tabela ASCII. Ele avisa ao terminal: *"Atenção, o que vem a seguir é um comando, não um texto para imprimir."*
2. **`[`**: Abre a sequência de formatação.
3. **`style;text;back`**: São códigos numéricos separados por ponto e vírgula (`;`).
    - **Style**: Estilo da fonte (negrito, sublinhado, etc).
    - **Text**: Cor do texto (foreground).
    - **Back**: Cor do fundo (background).
    - *Nota:* A ordem não é obrigatória, mas manter `estilo;texto;fundo` é uma boa prática.
4. **`m`**: Letra que indica o fim da sequência de formatação.

## Tabela de Códigos

Para montar suas cores, você precisa combinar os códigos abaixo.

### Códigos de Estilo (`style`)

| **Código** | **Efeito** | **Descrição** |
| --- | --- | --- |
| **0** | None | Sem estilo (padrão). |
| **1** | Bold | Negrito (deixa a cor mais viva/brilhante). |
| **4** | Underline | Sublinhado. |
| **7** | Negative | Inverte as cores (o que é letra vira fundo, e vice-versa). |

### Códigos de Texto (`text`)

As cores de texto variam do 30 ao 37.

| **Código** | **Cor** | **Código** | **Cor** |
| --- | --- | --- | --- |
| **30** | Branco/Cinza Escuro* | **34** | Azul Escuro |
| **31** | Vermelho | **35** | Magenta (Roxo) |
| **32** | Verde | **36** | Ciano (Azul Piscina) |
| **33** | Amarelo | **37** | Cinza/Branco (Padrão) |

***Nota**: Em muitos terminais, o código 30 pode ser preto ou cinza muito escuro. O 37 geralmente é o cinza claro/branco padrão.*

### Códigos de Fundo (`back`)

As cores de fundo seguem a mesma lógica, mas variam do 40 ao 47.

| **Código** | **Cor** | **Código** | **Cor** |
| --- | --- | --- | --- |
| **40** | Branco/Preto* | **44** | Azul |
| **41** | Vermelho | **45** | Magenta |
| **42** | Verde | **46** | Ciano |
| **43** | Amarelo | **47** | Cinza (Padrão) |

***Nota**: O código 40 geralmente representa o fundo preto (padrão do terminal) ou branco, dependendo da implementação do terminal, mas é comumente associado ao preto/escuro.*

## Implementação Prática

### O Problema do "Sangramento" de Cor

Ao ativar uma cor, o terminal mantém aquela configuração até que você mande parar. Se você pintar uma palavra de vermelho e não "limpar" a formatação, todo o resto do programa (e até o prompt do terminal) continuará vermelho.

Para evitar isso, usamos o código de **limpeza** ao final da string:
`\033[m` (Equivalente a `\033[0;37;40m` - volta ao padrão).

**Exemplos de `print` com Cores**

```python
# Exemplo 1: Texto Vermelho em Negrito
print('\033[1;31mOlá, Mundo!\033[m')

# Exemplo 2: Texto Branco, Fundo Violeta (Magenta)
print('\033[30;45mTeste de Cores\033[m')

# Exemplo 3: Texto Amarelo, Fundo Azul, Sublinhado
print('\033[4;33;44mCombinação Estranha\033[m')

# Exemplo 4: Inversão (Negative)
# Texto vira a cor do fundo, Fundo vira a cor do texto
print('\033[7;30mFundo Branco e Letra Preta (Invertido)\033[m')
```

## Organização Profissional (Dicionário de Cores)

Escrever `\033[1;31;43m` dentro de cada `print` torna o código ilegível e difícil de manter. A maneira profissional de lidar com isso em scripts simples é criar um dicionário de cores.

Isso centraliza a definição das cores. Se você precisar mudar o tom de vermelho do sistema inteiro, muda em apenas um lugar.

```python
# Definição do Dicionário de Cores
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'preto_branco': '\033[7;30m', # Invertido (Letra preta, fundo branco)
    'vermelho_bold': '\033[1;31m'
}

# Uso no código
nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelho_bold'], nome, cores['limpa']))

# Exemplo mais complexo
print('Os valores são {}{}{} e {}{}{}.'.format(
    cores['amarelo'], 3, cores['limpa'],
    cores['azul'], 5, cores['limpa']
))
```

## Resumo da Sintaxe

Para consulta rápida: `\033[` + **`ESTILO`** + `;` + **`TEXTO`** + `;` + **`FUNDO`** + `m`

| **Estilo** | **Texto** | **Fundo** |
| --- | --- | --- |
| 0 (Sem) | 30 (Branco) | 40 (Branco) |
| 1 (Negrito) | 31 (Vermelho) | 41 (Vermelho) |
| 4 (Subl.) | 32 (Verde) | 42 (Verde) |
| 7 (Invert) | 33 (Amarelo) | 43 (Amarelo) |
|  | 34 (Azul) | 44 (Azul) |
|  | 35 (Magenta) | 45 (Magenta) |
|  | 36 (Ciano) | 46 (Ciano) |
|  | 37 (Cinza) | 47 (Cinza) |