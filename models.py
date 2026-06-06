from dataclasses import dataclass


@dataclass(frozen=True)
class TDiagram:
    linguagem_fonte: str
    linguagem_alvo: str
    linguagem_base: str

    def __post_init__(self):
        campos = {
            "linguagem_fonte": self.linguagem_fonte,
            "linguagem_alvo": self.linguagem_alvo,
            "linguagem_base": self.linguagem_base,
        }

        for nome, valor in campos.items():
            if not isinstance(valor, str) or not valor.strip():
                raise ValueError(f"{nome} deve ser uma string nao vazia.")


@dataclass(frozen=True)
class ResultadoValidacao:
    viavel: bool
    justificativa: str


def normalizar_linguagem(linguagem):
    if not isinstance(linguagem, str):
        raise ValueError("A linguagem deve ser informada como texto.")

    linguagem_normalizada = linguagem.strip()
    if not linguagem_normalizada:
        raise ValueError("A linguagem nao pode ser vazia.")

    return linguagem_normalizada.upper()


def criar_t_diagram(linguagem_fonte, linguagem_alvo, linguagem_base):
    return TDiagram(
        linguagem_fonte=normalizar_linguagem(linguagem_fonte),
        linguagem_alvo=normalizar_linguagem(linguagem_alvo),
        linguagem_base=normalizar_linguagem(linguagem_base),
    )


def validar_bootstrapping(diagrama, linguagem_disponivel=None):
    if not isinstance(diagrama, TDiagram):
        raise TypeError("diagrama deve ser uma instancia de TDiagram.")

    linguagem_base = normalizar_linguagem(diagrama.linguagem_base)
    linguagem_fonte = normalizar_linguagem(diagrama.linguagem_fonte)
    linguagem_alvo = normalizar_linguagem(diagrama.linguagem_alvo)

    if linguagem_disponivel is None:
        linguagem_disponivel = linguagem_fonte

    linguagem_disponivel = normalizar_linguagem(linguagem_disponivel)

    if linguagem_base != linguagem_disponivel:
        return ResultadoValidacao(
            viavel=False,
            justificativa=(
                "A linguagem base do compilador precisa existir no ambiente "
                f"disponivel. Esperado: {linguagem_disponivel}. "
                f"Recebido: {linguagem_base}."
            ),
        )

    if linguagem_fonte == linguagem_alvo:
        return ResultadoValidacao(
            viavel=True,
            justificativa=(
                "O compilador roda na base disponivel e traduz a linguagem "
                "para ela mesma, portanto o encadeamento e direto."
            ),
        )

    return ResultadoValidacao(
        viavel=True,
        justificativa=(
            f"Existe um compilador escrito/executavel em {linguagem_base} "
            f"capaz de traduzir {linguagem_fonte} para {linguagem_alvo}. "
            "Como a base coincide com a linguagem disponivel, a compilacao "
            "cruzada e viavel."
        ),
    )


def validar_encadeamento(diagramas, linguagem_inicial):
    if not diagramas:
        raise ValueError("Informe pelo menos um T-diagram para validar.")

    linguagem_atual = normalizar_linguagem(linguagem_inicial)
    etapas = []

    for indice, diagrama in enumerate(diagramas, start=1):
        resultado = validar_bootstrapping(diagrama, linguagem_atual)
        etapas.append(resultado.justificativa)

        if not resultado.viavel:
            return ResultadoValidacao(
                viavel=False,
                justificativa=(
                    f"Etapa {indice} falhou. "
                    + " ".join(etapas)
                ),
            )

        linguagem_atual = normalizar_linguagem(diagrama.linguagem_alvo)

    return ResultadoValidacao(
        viavel=True,
        justificativa=(
            "Todas as etapas respeitam a regra dos T-diagrams: a linguagem "
            "base de cada compilador coincide com a linguagem disponivel "
            "naquele ponto do encadeamento."
        ),
    )
