# O Decorator @property

Para entender a profundidade do `@property`, precisamos olhar para um problema clássico da Engenharia de Software: a **Evolução do Código**.

Imagine que você criou uma classe `Retangulo` simples, onde a `largura` e a `altura` são atributos públicos. O código de quem usa sua classe seria assim:

```python
meu_retangulo.largura = 10
print(meu_retangulo.largura)
```

Meses depois, você percebe que precisa adicionar uma lógica extra: "Sempre que alguém ler a largura, eu preciso registrar isso num log" ou "A largura deve ser calculada dinamicamente baseada em outro fator".

Em linguagens como Java, você seria obrigado desde o dia 1 a criar métodos `getLargura()` e `setLargura()`, tornando o código verboso, só por precaução ("vai que um dia eu precise mudar a lógica").

O Python diz: **"Não faça isso. Comece simples."** Você começa usando atributos normais. Se um dia você precisar adicionar lógica ao acesso desse atributo, você usa o `@property`.

## O que o `@property` faz exatamente?

Ele transforma um **método** (uma função) em algo que se comporta externamente como um **atributo** (uma variável).

Quando você coloca `@property` em cima de um método, você está dizendo ao Python: *"Olha, eu sei que escrevi isso como uma função. Mas quando alguém tentar acessar isso lá fora (sem usar parênteses), execute esse código e entregue o valor retornado."*

Isso nos dá dois superpoderes:

1. **Encapsulamento Elegante (Getters):** Podemos expor um atributo como "somente leitura". Se você definir apenas o `@property` (que é o Getter) e não definir o Setter (que veremos depois), o usuário conseguirá ler o valor, mas receberá um erro se tentar alterá-lo (`objeto.valor = 10` falhará).
2. **Atributos Calculados (Computed Properties):** Esta é a aplicação mais comum. Muitas vezes, um dado não precisa ser armazenado na memória; ele pode ser calculado na hora (on-the-fly) com base em outros dados.

## Exemplo

Imagine um sistema bancário. Você tem `nome` e `sobrenome`. Você não precisa guardar uma variável `nome_completo` no banco de dados. Isso seria redundante e perigoso (se o `sobrenome` mudar, você teria que lembrar de atualizar o `nome_completo`).

Com `@property`, o `nome_completo` parece uma variável, mas na verdade é um cálculo em tempo real.

```python
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    # O decorator mágica
    @property
    def nome_completo(self):
        # Toda vez que alguém chamar 'pessoa.nome_completo', 
        # este código roda novamente.
        return f"{self.nome} {self.sobrenome}"

# Uso:
p = Pessoa("Ana", "Silva")

# Note que NÃO usamos parênteses () no final.
# O Python executa o método implicitamente.
print(p.nome_completo)  # Saída: Ana Silva
```

Se tentássemos fazer `p.nome_completo = "João Souza"`, daria erro, pois não dissemos ao Python como "setar" esse valor, apenas como "ler".