# Convenções de Visibilidade ( _ e __ )

Em Python, **todos** os atributos e métodos são públicos por padrão. Se você digitar `objeto.nome`, você acessa o valor. Pronto.

Porém, para proteger a integridade dos dados internos de um objeto, usamos convenções de nomenclatura para sinalizar “Privacidade”.

## O Underscore Simples (`_variavel`) - Protected

Quando você vê um atributo ou método começando com **um** sublinhado (ex: `self._saldo`), isso é um **aviso**.

- **Significado:** "Caro desenvolvedor, este atributo é de uso interno da classe ou de suas subclasses. Por favor, não o acesse ou modifique diretamente de fora."
- **Efeito Técnico:** Nenhum. O Python **não** impede o acesso. Se você quiser fazer `print(conta._saldo)`, vai funcionar. Mas você estará violando um contrato implícito e o código pode quebrar em futuras atualizações da biblioteca.

## O Underscore Duplo (`__variavel`) - Private (Name Mangling)

Quando usamos **dois** sublinhados (ex: `self.__senha`), a coisa muda de figura.

- **Significado:** "Este atributo é exclusivo desta classe específica. Nem mesmo as subclasses deveriam mexer nele."
- **Efeito Técnico:** O Python ativa um mecanismo chamado **Name Mangling** (Desfiguração de Nome).
    
    Internamente, o interpretador altera o nome da variável. O atributo `__senha` deixa de existir com esse nome e passa a se chamar `_NomeDaClasse__senha`.
    
    Isso faz com que, se você tentar acessar `objeto.__senha` no seu código, receberá um erro dizendo que o atributo não existe. É a forma mais próxima de "private" que temos, feita para evitar conflitos de nomes acidentais (especialmente em herança).