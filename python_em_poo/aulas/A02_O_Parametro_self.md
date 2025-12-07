# O Parâmetro self

Este é, sem dúvida, o ponto que mais causa estranheza em quem vem de outras linguagens (como Java ou C#, onde o `this` é mágico e implícito). No Python, seguimos uma regra do *Zen of Python*: “**Explicito é melhor que implícito**”.

## O que é o `self`?

O `self` é uma **referência à própria instância** que está a chamar o método.

Pense comigo: A classe `Livro` é apenas um modelo genérico. Quando você cria 100 livros na memória, todos eles partilham os **mesmos métodos** (o código da função não é duplicado), mas cada um tem os seus **próprios dados** (título, autor, etc.).

Quando você chama um método, como o Python sabe se deve usar o título do `livro_1` ou do `livro_2`? É através do `self`.

## A “Tradução” Invisível

Quando você escreve isso no seu código:

```python
livro_1.descrever()
```

Nos bastidores, o Python “traduz” e executa isto:

```python
Livro.descrever(livro_1)
```

O objeto à esquerda do ponto (`livro_1`) é passado automaticamente como **primeiro argumento** para a função definida na classe.

É por isso que:

1. **Na Definição (`def`):** Você **precisa** declarar o `self` como primeiro parâmetro, para “receber” essa injeção automática da instância.
2. **Na Chamada:** Você **não** passa o `self`, porque o Python faz isso por si.

Se você esquecer de colocar o `self` na definição do método e tentar chamá-lo através de um objetivo, receberá um erro famoso: `TypeError: ... takes 0 positional arguments but 1 was given`. Isso significa: "Você definiu uma função que não aceita nada, mas eu (Python) tentei empurrar o objeto para dentro dela e não cabia".