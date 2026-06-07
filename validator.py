from models import criar_t_diagram, validar_encadeamento


def imprimir_caso(titulo, diagramas, linguagem_inicial):
    print("=" * 60)
    print(titulo)
    print(f"Linguagem inicial disponivel: {linguagem_inicial}")
    print("Entrada:")

    for indice, diagrama in enumerate(diagramas, start=1):
        print(
            f"  T{indice}: fonte={diagrama.linguagem_fonte}, "
            f"alvo={diagrama.linguagem_alvo}, base={diagrama.linguagem_base}"
        )

    resultado = validar_encadeamento(diagramas, linguagem_inicial)
    status = "VIAVEL" if resultado.viavel else "NAO VIAVEL"

    print(f"Resultado: {status}")
    print(f"Justificativa: {resultado.justificativa}")
    print()


def main():
    casos = [
        (
            "Caso viavel",
            [
                criar_t_diagram("C", "ASM", "C"),
                criar_t_diagram("MiniLang", "C", "ASM"),
            ],
            "C",
        ),
        (
            "Caso inviavel",
            [
                criar_t_diagram("Python", "C", "Python"),
                criar_t_diagram("MiniLang", "ASM", "Rust"),
            ],
            "Python",
        ),
        (
            "Caso de linguagem base incompatibilidade",
            [
                criar_t_diagram("Pascal", "C", "Java"),
            ],
            "Pascal",
        ),
    ]

    for titulo, diagramas, linguagem_inicial in casos:
        imprimir_caso(titulo, diagramas, linguagem_inicial)


if __name__ == "__main__":
    main()
