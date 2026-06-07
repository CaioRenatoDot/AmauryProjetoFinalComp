from models import criar_t_diagram, validar_bootstrapping


def ler_linguagem(rotulo):
    valor = input(f"{rotulo}: ").strip()
    if not valor:
        raise ValueError(f"{rotulo} nao pode ficar vazia.")
    return valor


def main():
    print("Validador de Bootstrapping com Diagramas em T")
    print("-" * 48)

    try:
        linguagem_fonte = ler_linguagem("Linguagem Fonte")
        linguagem_alvo = ler_linguagem("Linguagem Alvo")
        linguagem_base = ler_linguagem("Linguagem Base")

        diagrama = criar_t_diagram(
            linguagem_fonte,
            linguagem_alvo,
            linguagem_base,
        )
        resultado = validar_bootstrapping(diagrama)
        status = "VIAVEL" if resultado.viavel else "NAO VIAVEL"

        print()
        print("Diagrama informado:")
        print(f"  Fonte: {diagrama.linguagem_fonte}")
        print(f"  Alvo:  {diagrama.linguagem_alvo}")
        print(f"  Base:  {diagrama.linguagem_base}")
        print()
        print(f"Resultado: {status}")
        print(f"Justificativa: {resultado.justificativa}")
    except (TypeError, ValueError) as erro:
        print()
        print(f"Entrada invalida: {erro}")


if __name__ == "__main__":
    main()