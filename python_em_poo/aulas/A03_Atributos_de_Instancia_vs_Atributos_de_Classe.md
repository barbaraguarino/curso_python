# Atributos de Instância vs. Atributos de Classe

Até agora, todos os dados que manipulamos (`titulo`, `autor`, `cor`) viviam dentro do método `__init__` e começavam com o prefixo `self`. Estes são chamados de **Atributos de Instância**.

Um **Atributo de Instância** pertence exclusivamente a *um* objeto específico. Quando criamos o `livro_1`, ele ganhou seu próprio espaço na memória para guardar o título "O Senhor dos Anéis". O `livro_2` tem seu próprio espaço separado para "1984". Se você alterar o título de um, o outro não é afetado. É como se fosse o RG de uma pessoa: cada um tem o seu.

Porém, existem dados que não variam de objeto para objeto; são constantes para *toda* a categoria. Esses são os **Atributos de Classe**.

## Atributo de Classe

Um **Atributo de Classe** é declarado diretamente no corpo da classe, fora de qualquer método (geralmente logo no topo). Ele pertence ao *molde*, não à peça fabricada. Por conta disso, ele é **compartilhado** entre todas as instâncias existentes. Se a classe fosse uma fábrica de robôs, o "número de série" seria um atributo de instância (cada robô tem o seu), mas o "nome da fábrica" seria um atributo de classe (é o mesmo para todos os robôs).

## Visualização no Código

Veja a diferença sintática:

```python
class Robo:
    # Atributo de Classe (Compartilhado)
    # Declarado fora do __init__
    leis_da_robotica = "Não ferir humanos"

    def __init__(self, nome):
        # Atributo de Instância (Exclusivo)
        # Declarado dentro do __init__ com self
        self.nome = nome
```

Para acessar um atributo de classe, a boa prática (o jeito "Pythonico") é usar o nome da própria classe (`Robo.leis_da_robotica`), embora o Python permita acessar via instância (`self.leis_da_robotica`), o que pode causar confusão se não soubermos o que estamos fazendo.

A grande vantagem aqui é a eficiência: o Python armazena a string "Não ferir humanos" apenas uma vez na memória, e todos os milhares de robôs que você criar apontarão para esse único lugar.