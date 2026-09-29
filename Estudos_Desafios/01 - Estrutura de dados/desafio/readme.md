# 🏦 Sistema Bancário com Python 2

Projeto desenvolvido como parte de um desafio de programação em **Python**, com o objetivo de evoluir um sistema bancário simples aplicando os principais conceitos de estruturas de dados e funções.

O projeto permite cadastrar usuários, criar contas bancárias e realizar operações como depósitos, saques e consultas de extrato.

## 🎯 Objetivo

O objetivo do desafio é praticar os conceitos fundamentais da linguagem Python por meio da construção de um sistema bancário funcional.

Durante o desenvolvimento foram utilizadas:

* Listas
* Tuplas
* Conjuntos
* Dicionários
* Funções
* Estruturas condicionais
* Estruturas de repetição
* Compreensão de listas
* Manipulação de strings
* Tratamento de exceções

## ⚙️ Funcionalidades

O sistema possui as seguintes operações:

| Opção | Funcionalidade         |
| ----- | ---------------------- |
| `d`   | Realizar depósito      |
| `s`   | Realizar saque         |
| `e`   | Consultar extrato      |
| `nc`  | Criar nova conta       |
| `lc`  | Listar contas          |
| `nu`  | Cadastrar novo usuário |
| `r`   | Exibir resumo do banco |
| `q`   | Encerrar o sistema     |

## 📚 Estruturas de dados utilizadas

### 📋 Listas

As listas são utilizadas para armazenar os usuários e as contas cadastradas.

```python
usuarios = []
contas = []
```

O extrato de cada conta também é armazenado como uma lista de movimentações.

```python
"extrato": []
```

### 🔢 Tuplas

As tuplas são utilizadas para representar cada movimentação realizada na conta.

```python
("Depósito", valor)
```

ou:

```python
("Saque", valor)
```

Essa estrutura permite armazenar o tipo da operação e o respectivo valor.

### 🔵 Conjuntos

Um `set` é utilizado para armazenar os CPFs já cadastrados.

```python
cpfs_cadastrados = set()
```

Antes de cadastrar um usuário, o sistema verifica se o CPF já está presente no conjunto:

```python
if cpf in cpfs_cadastrados:
    print("Já existe usuário com esse CPF!")
```

Dessa forma, o sistema evita o cadastro de usuários com CPF duplicado.

### 📦 Dicionários

Os dicionários representam os usuários e as contas bancárias.

Um usuário é armazenado da seguinte forma:

```python
usuario = {
    "nome": nome,
    "data_nascimento": data_nascimento,
    "cpf": cpf,
    "endereco": endereco,
}
```

Uma conta possui informações próprias e também uma referência ao seu titular:

```python
conta = {
    "agencia": agencia,
    "numero_conta": numero_conta,
    "usuario": usuario,
    "saldo": 0.0,
    "limite": 500.00,
    "numero_saques": 0,
    "extrato": [],
}
```

## 🧩 Funções

O sistema foi dividido em funções para separar as responsabilidades do programa.

### Usuários

```python
criar_usuario()
filtrar_usuario()
```

Responsáveis pelo cadastro e localização de usuários.

### Contas

```python
criar_conta()
listar_contas()
selecionar_conta()
```

Responsáveis pela criação, consulta e seleção de contas.

### Operações bancárias

```python
depositar()
sacar()
exibir_extrato()
```

Responsáveis pelas principais operações financeiras.

### Relatórios

```python
exibir_resumo()
```

Apresenta informações gerais sobre as contas cadastradas.

## 💰 Regras para depósitos

Os depósitos precisam possuir um valor maior que zero.

Exemplo:

```text
Informe o valor do depósito: 1000

=== Depósito realizado com sucesso! ===
```

O valor é adicionado ao saldo e a movimentação é registrada no extrato.

## 💸 Regras para saques

O sistema possui três regras principais para saques:

1. O valor deve ser maior que zero.
2. O cliente precisa possuir saldo suficiente.
3. O saque não pode ultrapassar o limite de `R$ 500,00`.
4. São permitidos no máximo `3` saques por conta.

Exemplo:

```text
Informe o valor do saque: 200

=== Saque realizado com sucesso! ===
```

## 👤 Cadastro de usuários

Para criar uma conta, primeiro é necessário cadastrar um usuário.

O sistema solicita:

* CPF
* Nome completo
* Data de nascimento
* Endereço

O CPF funciona como identificador do usuário e não pode ser cadastrado duas vezes.

## 🏦 Criação de contas

Uma conta só pode ser criada para um usuário previamente cadastrado.

Cada conta possui:

* Agência
* Número da conta
* Titular
* Saldo
* Limite de saque
* Quantidade de saques
* Extrato

O número da conta é gerado automaticamente pelo sistema.

## 📄 Extrato

O extrato apresenta todas as movimentações realizadas na conta.

Exemplo:

```text
================ EXTRATO ================
Depósito:       R$ 1000.00
Saque:          R$ 200.00
Depósito:       R$ 500.00

Saldo:          R$ 1300.00
Saques realizados: 1/3
==========================================
```

## 📊 Resumo do banco

A opção `r` apresenta informações gerais do sistema:

```text
============== RESUMO DO BANCO ==============
Total de contas: 3
Total de titulares: 2
Saldo total do banco: R$ 3500.00
==============================================
```

Nesse relatório são utilizados recursos como `len()`, `sum()` e conjuntos para obter informações agregadas.

## ▶️ Como executar

Execute o programa:

```bash
python desafio.py
```

## 🗂️ Estrutura do projeto

```text
sistema-bancario/
│
├── sistema_bancario.py
└── README.md
```

## 🧠 Conceitos praticados

Este desafio permite praticar conceitos importantes do Python:

* Variáveis
* Tipos de dados
* `if`, `elif` e `else`
* `while`
* `for`
* Listas
* Tuplas
* Conjuntos
* Dicionários
* List comprehensions
* Funções
* Parâmetros e argumentos
* Retorno de funções
* `try/except`
* F-strings
* Manipulação de strings
* `textwrap`
* Organização e modularização de código

## 🚀 Possíveis melhorias

Como evolução futura do projeto, podem ser adicionados:

* Persistência dos dados em arquivos JSON;
* Banco de dados SQLite;
* Autenticação de usuários;
* Transferência entre contas;
* Pagamento de boletos;
* Histórico de transações com data e hora;
* Chave Pix;
* Depósito em conta;
* Encerramento de contas;
* Alteração dos dados do usuário;
* Interface gráfica;
* API REST utilizando Flask ou FastAPI;
* Testes automatizados com `pytest`.

## 📝 Conclusão

O projeto demonstra a aplicação prática de diferentes estruturas de dados do Python em um sistema que simula operações bancárias.

A principal evolução em relação à versão inicial é a separação das informações por conta, permitindo que diferentes usuários possuam diferentes contas, saldos e históricos de movimentações.

Além disso, o projeto utiliza **listas, tuplas, conjuntos, dicionários e funções** de maneira integrada, reforçando os fundamentos de Python aprendidos durante o curso.
