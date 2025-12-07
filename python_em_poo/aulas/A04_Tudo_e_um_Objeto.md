# Tudo é um Objeto

Em linguagens como C ou Java, existe uma distinção clara entre “Tipos Primitivos” (como `int`, `float`, `char`, que são apenas valores crus na memória) e o “Objetos” (que são estruturas complexas).

No Python, essa distinção **não existe**.

- O número `10` é um objeto (instância da classe `int`).
- A string `"Olá"` é um objeto (instância da classe `str`).
- Uma função é um objeto.
- A própria classe `Carro` é um objeto (instância da classe `type`).

## O que isso muda na sua vida? (Passagem por Referência)

Como tudo é objeto, variáveis em Python não são "caixas" onde você guarda o valor. Elas são **etiquetas** (labels) que você cola em um objeto que está flutuando na memória.

Quando você passa um objeto (como o nosso `Carro`) para uma função, você não está enviando uma cópia dele. Você está entregando o **endereço de memória** onde aquele carro está estacionado.

Isso significa que, se a função alterar o objeto recebido, **o objeto original será alterado fora da função também**. Isso é chamado de *Side Effect* (Efeito Colateral) causado pela mutabilidade.