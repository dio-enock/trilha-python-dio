# Desafio — Programação Orientada a Objetos

Este projeto contém dois exercícios desenvolvidos durante o curso de **Programação Orientada a Objetos com Python**, com o objetivo de aplicar conceitos fundamentais de POO na construção de um sistema bancário simples.

Os desafios evoluem de uma implementação básica das classes e transações para uma aplicação completa com interação via terminal.

## 📁 Estrutura do projeto

```text
02 - Programação Orientada a Objetos/
└── 10 - desafio/
    ├── desafio_v1.py
    ├── desafio_v2.py
    ├── requirements.txt
    └── README.md
```

### Versão 1 — `desafio_v1.py`

Implementação da estrutura principal do sistema bancário, contemplando:

* Cliente;
* Pessoa Física;
* Conta;
* Conta Corrente;
* Histórico de transações;
* Depósito;
* Saque;
* Abstração de transações;
* Herança;
* Encapsulamento;
* Polimorfismo;
* Controle de saldo;
* Limite de saque;
* Quantidade máxima de saques.

### Versão 2 — `desafio_v2.py`

Evolução da primeira versão, adicionando uma interface interativa via terminal.

A aplicação permite:

* Criar clientes;
* Criar contas correntes;
* Realizar depósitos;
* Realizar saques;
* Consultar extrato;
* Listar contas;
* Encerrar a aplicação.

## 🧠 Conceitos de POO aplicados

Os desafios utilizam diferentes conceitos de **Programação Orientada a Objetos**.

### Classes e objetos

O sistema é estruturado por classes que representam as principais entidades do domínio bancário:

```python
class Cliente:
    ...

class Conta:
    ...

class ContaCorrente(Conta):
    ...

class Deposito(Transacao):
    ...

class Saque(Transacao):
    ...
```

### Encapsulamento

A classe `Conta` utiliza atributos privados por convenção, com acesso controlado por propriedades:

```python
self._saldo
self._numero
self._agencia
self._cliente
self._historico
```

E disponibiliza propriedades como:

```python
@property
def saldo(self):
    return self._saldo
```

### Herança

`PessoaFisica` herda de `Cliente`:

```python
class PessoaFisica(Cliente):
```

Enquanto `ContaCorrente` herda de `Conta`:

```python
class ContaCorrente(Conta):
```

As classes `Saque` e `Deposito` também herdam da classe abstrata `Transacao`.

### Abstração

A classe `Transacao` define uma interface comum para as operações de transação:

```python
class Transacao(ABC):
```

Ela exige que suas subclasses implementem:

```python
@property
@abstractproperty
def valor(self):
    pass

@abstractclassmethod
def registrar(self, conta):
    pass
```

Assim, `Saque` e `Deposito` possuem implementações específicas para o registro das suas respectivas operações.

### Polimorfismo

A classe `ContaCorrente` sobrescreve o comportamento do método `sacar()` definido em `Conta`.

Isso permite que a conta corrente aplique regras adicionais, como:

* limite máximo por saque;
* quantidade máxima de saques.

Depois de validar essas regras, a implementação reutiliza o comportamento da classe base:

```python
return super().sacar(valor)
```

### Composição e associação

Uma `Conta` possui um objeto `Historico`:

```python
self._historico = Historico()
```

O cliente também mantém uma coleção de suas contas:

```python
self.contas = []
```

Dessa forma, o sistema representa os relacionamentos entre clientes, contas e transações.

## ⚙️ Requisitos

* Python 3.10 ou superior;
* `pip`;

O projeto não possui dependências externas. Todos os módulos utilizados pertencem à biblioteca padrão do Python.

## ▶️ Executando o desafio

### Versão 1

Execute:

```bash
python desafio_v1.py
```

A versão 1 contém a implementação das entidades e operações bancárias, servindo como base para a evolução do sistema.

### Versão 2

Execute:

```bash
python desafio_v2.py
```

A versão 2 inicia o menu interativo:

```text
================ MENU ================
[d]    Depositar
[s]    Sacar
[e]    Extrato
[nc]   Nova conta
[lc]   Listar contas
[nu]   Novo usuário
[q]    Sair
=>
```

Digite a opção desejada e pressione `Enter`.

## 💰 Operações disponíveis

### Novo usuário

Utilize:

```text
nu
```

O sistema solicitará:

* CPF;
* nome completo;
* data de nascimento;
* endereço.

O CPF é utilizado para verificar se o cliente já está cadastrado.

### Nova conta

Utilize:

```text
nc
```

O sistema solicita o CPF de um cliente existente e cria uma nova conta corrente vinculada a ele.

### Depósito

Utilize:

```text
d
```

Informe o CPF e o valor que deseja depositar.

Apenas valores positivos são aceitos.

### Saque

Utilize:

```text
s
```

Informe o CPF e o valor do saque.

A operação verifica:

* existência do cliente;
* existência de conta;
* saldo disponível;
* limite máximo por saque;
* quantidade máxima de saques.

A conta corrente possui, por padrão:

```text
Limite por saque: R$ 500,00
Quantidade máxima de saques: 3
```

### Extrato

Utilize:

```text
e
```

O sistema apresenta as movimentações realizadas e o saldo atual da conta.

### Listar contas

Utilize:

```text
lc
```

O sistema apresenta as contas cadastradas, incluindo:

* agência;
* número da conta;
* titular.

### Sair

Utilize:

```text
q
```

para encerrar a aplicação.

## 📚 Objetivo do desafio

O objetivo dos exercícios é praticar a modelagem de um problema utilizando **Programação Orientada a Objetos**, aplicando:

* Classes e objetos;
* Construtores;
* Atributos e métodos;
* Encapsulamento;
* Properties;
* Herança;
* Abstração;
* Classes abstratas;
* Polimorfismo;
* Métodos de classe;
* Composição;
* Associação entre objetos;
* Sobrescrita de métodos;
* Reutilização de código com `super()`;
* Coleções de objetos;
* Organização de responsabilidades entre classes.

## 🛠️ Tecnologias

* Python 3
* Programação Orientada a Objetos
* Biblioteca padrão do Python

## 📄 Licença

Projeto desenvolvido para fins educacionais durante o curso de Programação Orientada a Objetos.
