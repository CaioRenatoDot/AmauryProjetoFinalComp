# Projeto: Validador de Bootstrapping - Divisao de Tarefas

> **Avaliacao PBL:** Componentes de Compiladores
> **Grupo:** 3 pessoas | **Prazo:** 7 dias

---

## Sobre o Projeto

Este projeto implementa um validador de bootstrapping usando **Diagramas em T**. O programa recebe as linguagens **fonte**, **alvo** e **base** de um compilador e verifica se a compilacao cruzada e viavel conforme as regras modeladas.

O codigo foi desenvolvido em **Python** e nao possui dependencias externas.

---

## Como Executar

Na raiz do repositorio, execute no Windows:

```bash
py -3 main.py
```

Para rodar os casos de teste demonstrativos:

```bash
py -3 validator.py
```

Em ambientes onde o comando `python` ou `python3` esteja configurado, tambem e possivel executar:

```bash
python main.py
python validator.py
python3 main.py
python3 validator.py
```

---

## Exemplo de Uso

Entrada:

```text
Linguagem Fonte: C
Linguagem Alvo: ASM
Linguagem Base: C
```

Saida esperada:

```text
Resultado: VIAVEL
Justificativa: Existe um compilador escrito/executavel em C capaz de traduzir C para ASM. Como a base coincide com a linguagem disponivel, a compilacao cruzada e viavel.
```

---

## Pessoa 1 - Logica Central e Codigo

**Responsabilidade:** Implementar o programa funcional do validador.

### Tarefas:
- Modelar as regras dos **Diagramas em T** (T-diagrams) para determinar viabilidade de compilacao cruzada
- Implementar a leitura das 3 entradas do usuario:
  - Linguagem Fonte
  - Linguagem Alvo
  - Linguagem Base
- Implementar a funcao de validacao que cruza as entradas com as regras
- Garantir saidas claras: `VIAVEL` / `NAO VIAVEL` com justificativa
- Escrever pelo menos **3 casos de teste** com entradas e saidas esperadas documentadas no codigo

### Entregavel:
- Arquivo principal do programa funcionando (`main.py`) e estruturas auxiliares (`models.py`, `validator.py`)

---

## Pessoa 2 - README e Estrutura do Repositorio

**Responsabilidade:** Garantir que o pacote entregue esteja organizado e que o `README.md` contenha as instrucoes exigidas pela rubrica.

### Tarefas:
- Criar e organizar o repositorio GitHub ou arquivo `.zip`
- Escrever o `README.md` contendo:
  - Descricao do projeto
  - **Comandos exatos de terminal** para executar o programa
  - Exemplo de uso com input e output esperado
  - Rubrica de avaliacao
- Definir a linguagem de programacao usada em conjunto com a Pessoa 1
- Testar se o passo a passo do README funciona em uma maquina limpa

### Entregavel:
- `README.md` completo e repositorio/zip organizado

---

## Pessoa 3 - Relatorio Tecnico (PDF)

**Responsabilidade:** Produzir o relatorio tecnico obrigatorio, seguindo as secoes exigidas pela rubrica.

### Tarefas:
- Escrever o relatorio em PDF com as **3 secoes obrigatorias**:

  **1. Introducao**
  - O que sao Diagramas em T
  - Qual problema o validador resolve

  **2. Metodologia de Implementacao**
  - Como a logica foi estruturada
  - Quais regras foram modeladas e por que

  **3. Casos de Teste**
  - Incluir prints ou blocos de codigo mostrando **inputs e outputs reais** do programa
  - Cobrir ao menos: caso viavel, caso inviavel e caso de entrada invalida

### Entregavel:
- Arquivo `relatorio.pdf` na raiz do repositorio/zip

> **Atencao:** A Pessoa 3 depende do codigo pronto para tirar os prints dos casos de teste.

---

# Rubrica de Avaliacao

A rubrica a seguir distribui os 80 pontos em criterios binarios ou parametricos estritos, facilitando a analise de presenca e conformidade dos artefatos entregues.

| Categoria | Criterio de Avaliacao Parametrico | Pontos |
|------------|----------------------------------|---------|
| **1. Conformidade e Formatacao (10 pts)** | **1.1. Estrutura do Pacote:** Presenca de arquivo `README.md` valido e codigo-fonte em pasta raiz ou acessivel (ZIP ou repositorio aberto). | 5 |
| | **1.2. Relatorio Tecnico:** Relatorio entregue obrigatoriamente no formato PDF. | 5 |
| **2. Compilacao e Execucao (20 pts)** | **2.1. Funcionalidade:** O codigo principal executa (interpreta) ou compila sem gerar erros fatais (`SyntaxError`, `CompileError`, `SegFault` no arranque). | 10 |
| | **2.2. Documentacao de Setup:** O arquivo `README.md` contem os comandos exatos de terminal exigidos para executar o projeto. | 10 |
| **3. Core do Projeto (30 pts)** | **3.1. Estrutura de Dados Especifica:** O codigo implementa explicitamente as estruturas teoricas requeridas pelo tema escolhido (ex.: classes para No/Grafo, Arrays como Pilha, Hash Maps). | 15 |
| | **3.2. Saida Esperada:** A execucao do programa imprime/retorna resultados compativeis com o problema proposto (ex.: estado da pilha impresso, lista de TAC, relatorio de nos coloridos, erros de tipagem). | 15 |
| **4. Relatorio Tecnico (20 pts)** | **4.1. Secoes Obrigatorias:** Presenca exata das 3 secoes: **Introducao**, **Metodologia de Implementacao** e **Casos de Teste**. | 10 |
| | **4.2. Evidencia de Testes:** A secao **Casos de Teste** inclui blocos de codigo ou capturas de tela demonstrando entradas (*inputs*) e saidas (*outputs*) do sistema criado. | 10 |
| **TOTAL** | A nota final deve ser a soma exata dos criterios atendidos. | **80** |
