## 📦 Módulo 1: Fundamentos e Anatomia da Classe

O objetivo aqui é entender a sintaxe básica e como o Python enxerga objetos, sem a burocracia de outras linguagens.

- [x]  **A Classe, o Objeto e o `__init__`**: Entenda a diferença entre o molde (Classe) e a peça fabricada (Objeto). Aprenda que o `__init__` é o método inicializador (construtor) onde definimos o estado inicial do objeto.
- [x]  **Exercício 01**: Crie uma classe chamada `Livro` que receba `titulo`, `autor` e `ano` no método `__init__`. Instancie 3 objetos diferentes dessa classe e imprima seus atributos no terminal.
- [x]  **O parâmetro `self`**: Entenda por que o `self` deve ser explícito na definição do método, mas implícito na chamada. Ele é a referência à própria instância que está sendo manipulada.
- [x]  **Exercício 02:** Adicione um método na classe `Livro` chamado `descrever()`. Esse método deve usar o `self` para retornar uma string formatada: "O livro [titulo] foi escrito por [autor]". Chame esse método para suas instâncias.
- [x]  **Atributos de Instância vs. Atributos de Classe**: Diferencie variáveis que pertencem a um objeto específico (dentro do `__init__` com `self`) de variáveis que pertencem à classe inteira (compartilhadas por todos).
- [x]  **Exercício 03:** Crie uma classe `Carro` com um atributo de classe `quantidade_rodas = 4`. No `__init__`, receba `modelo` e `cor`. Instancie dois carros e mostre que ambos compartilham a mesma `quantidade_rodas`, mas têm modelos diferentes.
- [x]  **Tudo é um Objeto:** Compreenda que em Python, números, funções e até as próprias classes são objetos e podem ser passados como argumentos.
- [x]  **Exercício 04:** Crie uma função externa que receba um objeto `Carro` como argumento e mude a cor dele. Prove que a alteração persistiu no objeto original.

### 🧪 Projetos:

- [x]  **Sistema de Cadastro de Alunos**: Crie um sistema simples onde você possa criar alunos (Nome, Matrícula), armazená-los em uma lista e exibir um relatório de todos os alunos cadastrados.
- [x]  **A lâmpada Inteligente**: Crie uma classe `Lampada` com estado (ligada/desligada) e luminosidade (0 a 100). Crie métodos para ligar, desligar e ajustar a intensidade.

## 🛡️ Módulo 2: Encapsulamento e Proteção de Dados

Aqui você aprende a proteger seus dados usando as convenções do Python ("nós somos todos adultos aqui") e propriedades.

- [x]  **Convenções de Visibilidade (`_` e `__`):** Entenda que `_variavel` é um aviso de "uso interno/protected" e `__variavel` ativa o *Name Mangling* (o Python altera o nome da variável para dificultar o acesso).
- [x]  **Exercício 05**: Crie uma classe `Cofre`. Tente criar um atributo com `_` e outro com `__`. Tente acessar ambos de fora da classe e veja o que acontece (e o erro que ocorre no segundo caso).
- [x]  **O Decorator `@property` (Getters):** Aprenda a criar métodos que são acessados como se fossem atributos, permitindo lógica (cálculos) ao ler um valor.
- [x]  **Exercício 06**: Crie uma classe `Retangulo` com `largura` e `altura`. Crie uma `@property` chamada `area` que calcula e retorna a área automaticamente, sem precisar armazenar esse valor.
- [x]  **Setters Pythonicos (`@var.setter`):** Aprenda a validar dados no momento da atribuição sem criar métodos `setValor()`.
- [x]  **Exercício 07**: Crie uma classe `Produto` com um preço. Use o setter para impedir que o preço seja negativo (lance um `ValueError` se for menor que zero).

### 🧪 Projetos:

- [x]  **Conta Bancária Segura:** Implemente uma classe `Conta` com saldo privado (`__saldo`). Use `@property` para ver o saldo e métodos `depositar` e `sacar` que validam se há fundos suficientes.
- [x]  **Sistema de Login:** Crie uma classe `Usuario` que armazena a senha de forma privada. Use um setter para validar se a nova senha tem no mínimo 8 caracteres antes de salvar.

## 🧬 Módulo 3: Herança e Polimorfismo

Como reutilizar código e fazer objetos diferentes responderem aos mesmos comandos.

- [x]  **Herança Simples e `super()`:**Aprenda a sintaxe `class Filha(Mae):` e como usar `super().__init__()` para aproveitar o construtor da classe pai.
- [x]  **Exercício 08**: Crie uma classe `Funcionario` (nome, salario base). Crie uma classe filha `Gerente` que herda de funcionário e adiciona um atributo `bonus`.
- [x]  **Polimorfismo e Sobrescrita de Métodos:** Entenda como uma classe filha pode alterar completamente o comportamento de um método herdado da classe pai.
- [x]  **Exercício 09**: Na classe `Funcionario`, crie um método `calcular_pagamento()`. Na classe `Gerente`, sobrescreva esse método para retornar `salario + bonus`.
- [ ]  **Duck Typing:** "Se anda como pato e grasna como pato, é pato". Entenda que o Python não liga para o tipo do objeto, apenas se ele tem o método que está sendo chamado.
- [ ]  **Exercício 10**: Crie uma função `emitir_som(animal)` que chama `animal.fazer_som()`. Passe para ela objetos de classes totalmente distintas (ex: `Cachorro` e `Carro`), desde que ambos tenham o método `fazer_som`.

### 🧪 Projetos:

- [ ]  **Zoológico Virtual:** Crie uma classe base `Animal` e subclasses `Ave`, `Mamifero`, `Reptil`. Implemente métodos específicos e use uma lista para iterar sobre todos os animais chamando um método comum `alimentar()`.
- [ ]  **E-commerce com Frete:** Crie classes `Eletronico` e `Movel`. Ambas devem ter um método `calcular_frete()`, mas a lógica do cálculo é diferente para cada tipo.

## ✨ Módulo 4: Métodos Mágicos (Dunder Methods)

Dê superpoderes às suas classes, permitindo que elas se comportem como tipos nativos do Python.

- [ ]  **Representação em String (`__str__` e `__repr__`):** Aprenda a diferença entre uma string amigável para o usuário (`str`) e uma para o desenvolvedor (`repr`).
- [ ]  **Exercício 11**: Pegue a classe `Livro` do Módulo 1 e implemente o `__str__` para que, ao fazer `print(meu_livro)`, apareça algo bonito como "Título (Autor)".
- [ ]  **Operadores Aritméticos (`__add__`, `__sub__`, etc.):** Ensine sua classe a somar, subtrair ou multiplicar usando os sinais `+`, , .
- [ ]  **Exercício 12**: Crie uma classe `Ponto` (x, y). Implemente o `__add__` para que somar dois pontos resulte em um novo ponto com a soma das coordenadas (`p1 + p2`).
- [ ]  **Comparação e Ordenação (`__eq__`, `__lt__`, `__gt__`):** Permita que seus objetos sejam comparados com `==`, `<` ou `>` e que listas de objetos possam ser ordenadas com `sort()`.
- [ ]  **Exercício 13**: Crie uma classe `Carta` (naipe, valor). Implemente `__gt__` (maior que) para que você possa comparar qual carta vale mais num jogo.
- [ ]  **Comprimento e Coleção (`__len__`, `__contains__`):** Faça seu objeto responder à função `len()` e ao operador `in`.
- [ ]  **Exercício 14**: Crie uma classe `Turma` que guarda uma lista de alunos internamente. Implemente `__len__` para retornar quantos alunos existem na turma.

### 🧪 Projetos:

- [ ]  **Calculadora de Tempo:** Crie uma classe `Tempo` (horas, minutos). Permita somar dois tempos (`1h30 + 2h45 = 4h15`) usando o operador `+`.
- [ ]  **Baralho de Cartas:** Implemente um baralho completo onde você possa usar `len(baralho)`, iterar sobre ele num `for` e verificar se uma carta está presente (`carta in baralho`).

## 📐 Módulo 5: Abstração e Estruturas Avançadas

Aqui o foco é arquitetura: como definir contratos e compor classes complexas.

- [ ]  **Classes Abstratas (ABC):** Como usar o módulo `abc` e `@abstractmethod` para impedir que uma classe "modelo" seja instanciada e forçar as filhas a implementar certos métodos.
- [ ]  **Exercício 15**: Crie uma classe abstrata `FormaGeometrica` com o método abstrato `area()`. Tente instanciá-la (verifique o erro). Crie subclasses `Circulo` e `Quadrado` que implementam a área.
- [ ]  **Herança Múltipla e Mixins:** Entenda como herdar de duas classes ao mesmo tempo e o conceito de Mixin (classes que apenas adicionam uma funcionalidade extra).
- [ ]  **Exercício 16**: Crie um Mixin `LogavelMixin` com um método `log(mensagem)`. Faça uma classe `Usuario` herdar de `Pessoa` e de `LogavelMixin` para ganhar a habilidade de logar ações.
- [ ]  **MRO (Method Resolution Order):** Entenda a ordem que o Python procura os métodos quando há herança múltipla (o problema do diamante).
- [ ]  **Exercício 17**: Crie uma hierarquia de classes em formato de diamante (A herda de B e C, que herdam de D). Use `Classe.mro()` para visualizar a ordem de busca.
- [ ]  **Protocolos (Typing):** O jeito moderno de definir interfaces estruturais (similar a Go ou TypeScript) sem precisar de herança explícita.
- [ ]  **Exercício 18**: Defina um `Protocol` chamado `Renderizavel` que exige um método `render()`. Crie classes que não herdam desse protocolo, mas o implementam, e use checagem estática (tipo o MyPy ou IDE) para validar.

### 🧪 Projetos:

- [ ]  **Sistema de Notificações:** Crie uma classe abstrata `Notificador` e implementações concretas: `EmailNotificador`, `SMSNotificador`. Use injeção de dependência para enviar mensagens sem saber qual o meio específico.
- [ ]  **Personagem de RPG Híbrido:** Crie classes `Guerreiro` (físico), `Mago` (mágico) e um `Paladino` que herda de ambos (Herança Múltipla), combinando atributos de força e mana.

## 🚀 Módulo 6: Python Moderno

Ferramentas que modernizaram a POO no Python 3.7+.

- [ ]  **Type Hinting:** Como usar anotações de tipo (`nome: str`, `> int`) para tornar o código legível e seguro para IDEs.
- [ ]  **Exercício 19**: Pegue o exercício da "Calculadora de Tempo" (Módulo 4) e adicione tipagem estática em todos os métodos e retornos.
- [ ]  **Dataclasses:** O decorator `@dataclass`. Como ele gera `__init__`, `__repr__` e `__eq__` automaticamente, economizando linhas de código.
- [ ]  **Exercício 20**: Reescreva a classe `Livro` ou `Produto` usando `@dataclass`. Compare o tamanho do código com a versão tradicional.
- [ ]  **Context Managers (`with`):** Como criar classes que usam `__enter__` e `__exit__` para gerenciar recursos (abrir/fechar arquivos ou conexões).
- [ ]  **Exercício 21**: Crie uma classe `Cronometro` que, ao ser usada num bloco `with`, mede quanto tempo o código dentro do bloco demorou para rodar e imprime no final.

### 🧪 Projetos:

- [ ]  **Validador de Configurações:** Use `Dataclasses` para criar uma estrutura de configuração de sistema (Host, Porta, DebugMode) e implemente um método `__post_init__` para validar se a Porta é um número válido.
- [ ]  **Gerenciador de Arquivos Customizado:** Crie um Context Manager que abre um arquivo, escreve um cabeçalho automaticamente ao abrir e um rodapé ao fechar.

## 🏗️ Módulo 7: SOLID e Arquitetura Limpa

A aplicação das boas práticas de engenharia de software na estrutura de classes.

- [ ]  **S - Princípio da Responsabilidade Única (SRP):** Uma classe deve ter apenas um motivo para mudar. Como detectar classes "Deusas" que fazem tudo.
- [ ]  **Exercício 22**: Refatoração: Pegue uma classe `Pedido` que calcula total, salva no banco e envia email. Quebre-a em `Pedido`, `PedidoRepository` e `EmailService`.
- [ ]  **O - Princípio Aberto/Fechado (OCP):** Classes devem estar abertas para extensão, mas fechadas para modificação.
- [ ]  **Exercício 23**: Crie um sistema de `Desconto` onde você possa adicionar novas regras de desconto (ex: Black Friday, Natal) criando novas classes, sem tocar no `if/else` da classe principal.
- [ ]  **L - Princípio de Substituição de Liskov (LSP):** Subclasses devem poder substituir as classes pai sem quebrar o código.
- [ ]  **Exercício 24**: Identifique um exemplo ruim (ex: classe `Quadrado` herdando de `Retangulo` e quebrando a lógica de setar largura/altura) e corrija a estrutura.
- [ ]  **I - Princípio da Segregação de Interface (ISP):** É melhor ter várias interfaces específicas do que uma genérica.
- [ ]  **Exercício 25**: Em vez de uma classe base `Trabalhador` com métodos `codar()` e `gerenciar()`, crie classes abstratas separadas `Dev` e `Gestor`.
- [ ]  **D - Injeção de Dependência (DIP):** Dependa de abstrações, não de implementações concretas.
- [ ]  **Exercício 26**: Crie uma classe `Interruptor` que recebe um objeto `Dispositivo` (qualquer coisa que tenha `ligar/desligar`) no construtor, em vez de criar uma `Lampada` internamente.

### 🧪 Projetos:

- [ ]  **Sistema de Biblioteca:** Implemente o sistema completo aplicando SOLID: Dataclasses para os modelos (Livro), Classes Abstratas para interfaces (Repositorio), Injeção de Dependência e tratamento de erros customizado.
- [ ]  **Refatoração de Código Legado:** Pegue um script Python "macarrônico" (tudo em um arquivo, sem classes) e transforme-o em um sistema Orientado a Objetos seguindo os princípios aprendidos.