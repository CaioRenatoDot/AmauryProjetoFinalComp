# Validador de Bootstrapping com Diagramas em T

## Descrição do Projeto

Este projeto implementa um **Validador de Bootstrapping utilizando Diagramas em T**, conceito utilizado na área de Compiladores para representar tradutores de linguagens e verificar a viabilidade de processos de compilação e bootstrapping.

O sistema permite:

- Criar Diagramas em T contendo Linguagem Fonte, Linguagem Alvo e Linguagem Base;
- Verificar se um processo de bootstrapping é viável;
- Validar encadeamentos de múltiplos Diagramas em T;
- Exibir justificativas detalhadas para cada validação realizada.

O projeto foi desenvolvido em **Python 3**, utilizando apenas bibliotecas padrão da linguagem.

---

## Estrutura do Projeto

```text
projeto/
│
├── main.py
├── models.py
├── validador.py
└── README.md
```

### Arquivos

| Arquivo | Descrição |
|---|---|
| `main.py` | Interface principal para entrada de dados pelo usuário |
| `models.py` | Implementação das estruturas de dados e regras de validação |
| `validador.py` | Casos de teste pré-definidos para validação do algoritmo |
| `README.md` | Documentação do projeto |

---

## Requisitos

- Python 3.10 ou superior

Verifique a instalação com:

```bash
python --version
```

---

## Como Executar

```bash
python main.py
```

---

## Exemplo de Uso

**Entrada:**

```text
Linguagem Fonte: C
Linguagem Alvo: ASM
Linguagem Base: C
```

**Saída:**

```text
Diagrama informado:
  Fonte: C
  Alvo:  ASM
  Base:  C

Resultado: VIAVEL

Justificativa:
Existe um compilador escrito/executavel em C capaz de traduzir C para ASM.
Como a base coincide com a linguagem disponivel, a compilacao cruzada e viavel.
```

---

## Casos de Teste

Execute os casos pré-definidos com:

```bash
python validador.py
```

Cenários testados:

1. Caso viável
2. Caso inviável
3. Caso de entrada inválida

---

## Funcionalidades

- Representação de Diagramas em T através de classes
- Normalização automática dos nomes das linguagens
- Validação de bootstrapping
- Validação de encadeamento entre compiladores
- Tratamento de entradas inválidas
- Mensagens explicativas para os resultados

---

## Autores

Projeto desenvolvido para a disciplina de **Compiladores**.

- Caio Gabriel Pereira de Menezes Correia
- Caio Renato dos Santos Claudino
- José Francisco de Araújo Neto 
