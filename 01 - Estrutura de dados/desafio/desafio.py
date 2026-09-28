import textwrap


# ==============================
# CONFIGURAÇÕES
# ==============================

AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500.00


# ==============================
# MENU
# ==============================

def menu():
    menu = """
    ================ MENU ================

    [d]    Depositar
    [s]    Sacar
    [e]    Extrato
    [nc]   Nova conta
    [lc]   Listar contas
    [nu]   Novo usuário
    [q]    Sair

    => """

    return input(textwrap.dedent(menu)).strip().lower()


# ==============================
# USUÁRIOS
# ==============================

def filtrar_usuario(cpf, usuarios):
    """
    Localiza um usuário pelo CPF.
    """

    usuarios_filtrados = [
        usuario
        for usuario in usuarios
        if usuario["cpf"] == cpf
    ]

    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios, cpfs_cadastrados):
    """
    Cria um novo usuário.
    """

    cpf = input("Informe o CPF (somente números): ").strip()

    if not cpf.isdigit():
        print("\n@@@ CPF inválido! Informe somente números. @@@")
        return

    if cpf in cpfs_cadastrados:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input(
        "Informe a data de nascimento (dd-mm-aaaa): "
    ).strip()
    endereco = input(
        "Informe o endereço "
        "(logradouro, nro - bairro - cidade/sigla estado): "
    ).strip()

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }

    usuarios.append(usuario)
    cpfs_cadastrados.add(cpf)

    print("\n=== Usuário criado com sucesso! ===")


# ==============================
# CONTAS
# ==============================

def criar_conta(agencia, numero_conta, usuarios, contas):
    """
    Cria uma nova conta para um usuário existente.
    """

    cpf = input("Informe o CPF do usuário: ").strip()

    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print(
            "\n@@@ Usuário não encontrado, "
            "fluxo de criação de conta encerrado! @@@"
        )
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0.0,
        "limite": LIMITE_SAQUE,
        "numero_saques": 0,
        "extrato": [],
    }

    contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

    return conta


def listar_contas(contas):
    """
    Lista todas as contas cadastradas.
    """

    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    print("\n================ CONTAS ================")

    for conta in contas:
        linha = f"""
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        CPF:\t\t{conta["usuario"]["cpf"]}
        Saldo:\t\tR$ {conta["saldo"]:.2f}
        """

        print(textwrap.dedent(linha))
        print("=" * 50)


def selecionar_conta(contas):
    """
    Solicita o CPF e retorna as contas pertencentes ao usuário.
    """

    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return None

    cpf = input("Informe o CPF do titular: ").strip()

    contas_usuario = [
        conta
        for conta in contas
        if conta["usuario"]["cpf"] == cpf
    ]

    if not contas_usuario:
        print("\n@@@ Nenhuma conta encontrada para esse CPF. @@@")
        return None

    if len(contas_usuario) == 1:
        return contas_usuario[0]

    print("\nContas encontradas:")

    for conta in contas_usuario:
        print(
            f"[{conta['numero_conta']}] "
            f"Agência: {conta['agencia']}"
        )

    numero_conta = input("Informe o número da conta: ").strip()

    for conta in contas_usuario:
        if str(conta["numero_conta"]) == numero_conta:
            return conta

    print("\n@@@ Número da conta inválido. @@@")
    return None


# ==============================
# OPERAÇÕES BANCÁRIAS
# ==============================

def depositar(conta, valor):
    """
    Realiza um depósito na conta.
    """

    if valor <= 0:
        print(
            "\n@@@ Operação falhou! "
            "O valor informado é inválido. @@@"
        )
        return False

    conta["saldo"] += valor

    conta["extrato"].append(
        ("Depósito", valor)
    )

    print("\n=== Depósito realizado com sucesso! ===")

    return True


def sacar(conta, valor):
    """
    Realiza um saque respeitando saldo, limite e quantidade máxima.
    """

    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    if valor <= 0:
        print(
            "\n@@@ Operação falhou! "
            "O valor informado é inválido. @@@"
        )
        return False

    if excedeu_saldo:
        print(
            "\n@@@ Operação falhou! "
            "Você não tem saldo suficiente. @@@"
        )
        return False

    if excedeu_limite:
        print(
            "\n@@@ Operação falhou! "
            "O valor do saque excede o limite de "
            f"R$ {conta['limite']:.2f}. @@@"
        )
        return False

    if excedeu_saques:
        print(
            "\n@@@ Operação falhou! "
            "Número máximo de saques excedido. @@@"
        )
        return False

    conta["saldo"] -= valor
    conta["numero_saques"] += 1

    conta["extrato"].append(
        ("Saque", valor)
    )

    print("\n=== Saque realizado com sucesso! ===")

    return True


def exibir_extrato(conta):
    """
    Exibe todas as movimentações da conta.
    """

    print("\n================ EXTRATO ================")

    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for operacao, valor in conta["extrato"]:
            print(
                f"{operacao}:\tR$ {valor:.2f}"
            )

    print(f"\nSaldo:\t\tR$ {conta['saldo']:.2f}")

    print(
        f"Saques realizados: "
        f"{conta['numero_saques']}/{LIMITE_SAQUES}"
    )

    print("==========================================")


# ==============================
# RELATÓRIOS
# ==============================

def exibir_resumo(contas):
    """
    Exibe um resumo geral do banco.
    """

    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    total_saldo = sum(
        conta["saldo"]
        for conta in contas
    )

    total_contas = len(contas)

    titulares = {
        conta["usuario"]["cpf"]
        for conta in contas
    }

    print("\n============== RESUMO DO BANCO ==============")
    print(f"Total de contas: {total_contas}")
    print(f"Total de titulares: {len(titulares)}")
    print(f"Saldo total do banco: R$ {total_saldo:.2f}")
    print("==============================================")


# ==============================
# OPERAÇÕES DO SISTEMA
# ==============================

def realizar_deposito(contas):
    conta = selecionar_conta(contas)

    if not conta:
        return

    try:
        valor = float(
            input("Informe o valor do depósito: ")
        )
    except ValueError:
        print("\n@@@ Valor inválido. @@@")
        return

    depositar(conta, valor)


def realizar_saque(contas):
    conta = selecionar_conta(contas)

    if not conta:
        return

    try:
        valor = float(
            input("Informe o valor do saque: ")
        )
    except ValueError:
        print("\n@@@ Valor inválido. @@@")
        return

    sacar(conta, valor)


def realizar_extrato(contas):
    conta = selecionar_conta(contas)

    if conta:
        exibir_extrato(conta)


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

def main():
    usuarios = []
    contas = []

    # Conjunto utilizado para garantir
    # que não existam CPFs duplicados.
    cpfs_cadastrados = set()

    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            realizar_deposito(contas)

        elif opcao == "s":
            realizar_saque(contas)

        elif opcao == "e":
            realizar_extrato(contas)

        elif opcao == "nu":
            criar_usuario(
                usuarios,
                cpfs_cadastrados
            )

        elif opcao == "nc":
            criar_conta(
                AGENCIA,
                numero_conta,
                usuarios,
                contas
            )

            numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "r":
            exibir_resumo(contas)

        elif opcao == "q":
            print("\n=== Obrigado por utilizar o sistema! ===")
            break

        else:
            print(
                "\n@@@ Operação inválida! "
                "Selecione uma opção disponível. @@@"
            )


if __name__ == "__main__":
    main()