# Setters Pythonicos (@var.setter)

Agora que aprendemos a controlar a **leitura** de dados (com `@property`), precisamos controlar a **escrita** (atribuição).

Voltemos ao princípio de proteção. No seu código do `Retangulo`, nada me impede de fazer isso:

```python
retangulo.largura = -50
```

Matematicamente, uma largura negativa é impossível na geometria física, mas o Python aceita. Em linguagens antigas (Java pré-moderno), você criaria um método `setLargura(valor)` e colocaria um `if` dentro dele.

No Python, queremos continuar usando a sintaxe bonita de atribuição (`objeto.largura = 10`), mas queremos que uma validação ocorra nos bastidores. É aqui que entra o **Setter Decorado**.

## A Regra da Dependência

Para criar um setter, você **primeiro** precisa ter uma `@property` com o mesmo nome. O setter é um "anexo" da propriedade.

### A Sintaxe

```python
class Produto:
    def __init__(self, preco_inicial):
        # Aqui está o pulo do gato:
        # Não atribuímos direto ao self._preco.
        # Atribuímos ao self.preco (o setter), para validar desde o nascimento!
        self.preco = preco_inicial

    # 1. O Getter (Leitura)
    # Define como o valor é entregue ao mundo
    @property
    def preco(self):
        return self._preco

    # 2. O Setter (Escrita)
    # Define o que acontece quando alguém faz: objeto.preco = valor
    # O nome do decorator deve ser @nome_da_propriedade.setter
    @preco.setter
    def preco(self, novo_valor):
        if novo_valor < 0:
            # Em vez de aceitar o erro, lançamos uma exceção (um grito de alerta)
            raise ValueError("O preço não pode ser negativo!")
        
        # Se passou no teste, aí sim guardamos na variável interna (protegida)
        self._preco = novo_valor
```

### O Fluxo de Execução

Quando você escreve `p.preco = 50`, o Python:

1. Vê que existe um `@preco.setter`.
2. Captura o valor `50`.
3. Passa esse valor como argumento para o método `preco(self, novo_valor)`.
4. Executa sua lógica de `if`.
5. Se tudo der certo, salva na variável oculta `_preco`.

Isso mantém a interface limpa (parece uma variável simples), mas o comportamento seguro (tem validação por trás).