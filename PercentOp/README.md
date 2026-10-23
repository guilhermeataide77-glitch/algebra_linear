# Analisador de Custo Operacional em Matrizes — Lei Distributiva

Projeto em Python para analisar e comparar o custo operacional da propriedade distributiva da multiplicação de matrizes:

**A × (B + C) = (A × B) + (A × C)**

O objetivo é comparar o número de adições e multiplicações escalares realizadas em cada abordagem, considerando diferentes dimensões de matrizes.

## 📂 Estrutura do repositório

```text
.
├── verificacaomanual.py
├── grafico.py
└── README.md
```

| Arquivo | Descrição |
|---|---|
| `verificacaomanual.py` | Executa testes manuais por meio de um menu interativo no terminal. |
| `grafico.py` | Automatiza testes para diferentes dimensões e gera gráficos comparativos. |

## 1. Verificação manual

O arquivo `verificacaomanual.py` implementa operações matriciais utilizando listas aninhadas nativas do Python, contabilizando as adições e multiplicações realizadas.

### Como executar

É necessário ter o Python 3 instalado.

```bash
python verificacaomanual.py
```

### Opções disponíveis

| Opção | Dimensões |
|---:|---|
| 0 | Encerrar o programa |
| 1 | A: 2 × 3; B e C: 3 × 2 |
| 2 | Matrizes 4 × 4 |
| 3 | Matrizes 8 × 8 |
| 4 | Matrizes 16 × 16 |
| 5 | Matrizes 32 × 32 |
| 6 | Matrizes 64 × 64 |
| 7 | Matrizes 128 × 128 |
| 8 | Matrizes 256 × 256 |
| 9 | Matrizes 512 × 512 |
| 10 | Matrizes 1024 × 1024 |

## 2. Análise gráfica

O arquivo `grafico.py` automatiza a comparação entre as duas expressões para diferentes tamanhos de matrizes e gera gráficos para visualizar os resultados.

### Como executar no Google Colab

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Crie um novo notebook.
3. Copie o conteúdo de `grafico.py` para uma célula de código.
4. Execute a célula para obter os resultados e os gráficos.

### Execução local

Se as dependências utilizadas pelo script estiverem instaladas, execute:

```bash
python grafico.py
```

Caso utilize Matplotlib e NumPy, instale as bibliotecas com:

```bash
pip install matplotlib numpy
```

## 3. Fundamento matemático

A propriedade distributiva da multiplicação de matrizes estabelece que:

**A × (B + C) = (A × B) + (A × C)**

Embora as duas expressões sejam matematicamente equivalentes, elas podem apresentar custos operacionais diferentes.

Considere três matrizes quadradas de ordem `n`.

### Abordagem 1 — A × (B + C)

Primeiro, calcula-se a soma `B + C`. Depois, multiplica-se o resultado por `A`.

- Multiplicações escalares: `n³`
- Adições escalares: `n³`
- **Total: 2n³ operações**

### Abordagem 2 — (A × B) + (A × C)

Primeiro, calculam-se os produtos `A × B` e `A × C`. Em seguida, somam-se os resultados.

- Multiplicações escalares: `2n³`
- Adições escalares: `2n³ − n²`
- **Total: 4n³ − n² operações**

### Comparação teórica

| Operação | A × (B + C) | (A × B) + (A × C) |
|---|---:|---:|
| Multiplicações | n³ | 2n³ |
| Adições | n³ | 2n³ − n² |
| **Total** | **2n³** | **4n³ − n²** |

*As contagens consideram o algoritmo convencional de multiplicação de matrizes, sem otimizações algorítmicas.*

## 4. Objetivos

- Verificar a equivalência matemática das duas expressões.
- Comparar o número de adições e multiplicações escalares.
- Analisar o crescimento do custo operacional conforme as dimensões aumentam.
- Gerar gráficos para facilitar a interpretação dos resultados.
- Comparar os resultados experimentais com as previsões teóricas.

## 5. Tecnologias utilizadas

- Python 3
- Google Colab
- Matplotlib

## 6. Considerações finais

A análise permite observar como a escolha da expressão utilizada influencia a quantidade de operações aritméticas necessárias para realizar um mesmo cálculo matricial.

É importante distinguir a contagem de operações do tempo de execução: o desempenho real também depende da implementação, do gerenciamento de memória e do hardware utilizado.

