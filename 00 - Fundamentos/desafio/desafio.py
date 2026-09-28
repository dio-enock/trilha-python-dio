menu = """
================ BANCO DIO ================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

============================================
=> """

saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))

            if valor <= 0:
                print("\nOperação falhou! O valor informado é inválido.")
                continue

            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")

            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")

        except ValueError:
            print("\nOperação falhou! Informe um valor numérico válido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))

            if valor <= 0:
                print("\nOperação falhou! O valor informado é inválido.")
                continue

            if valor > saldo:
                print("\nOperação falhou! Você não tem saldo suficiente.")
                continue

            if valor > limite:
                print(
                    f"\nOperação falhou! "
                    f"O valor máximo por saque é de R$ {limite:.2f}."
                )
                continue

            if numero_saques >= LIMITE_SAQUES:
                print(
                    f"\nOperação falhou! "
                    f"Você atingiu o limite de {LIMITE_SAQUES} saques."
                )
                continue

            saldo -= valor
            numero_saques += 1
            extrato.append(f"Saque: R$ {valor:.2f}")

            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")

        except ValueError:
            print("\nOperação falhou! Informe um valor numérico válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")

        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in extrato:
                print(movimentacao)

        print("------------------------------------------")
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Saques realizados: {numero_saques}/{LIMITE_SAQUES}")
        print("==========================================")

    elif opcao == "q":
        print("\nObrigado por utilizar o Banco DIO!")
        break

    else:
        print(
            "\nOperação inválida, "
            "por favor selecione uma opção disponível."
        )