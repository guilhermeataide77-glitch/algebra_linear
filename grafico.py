# Google Colab: comparação do custo de A(B + C) e AB + AC
# Usa PyTorch com GPU (CUDA), se disponível.
# O gráfico mede o número de operações aritméticas, não o tempo de execução.

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import torch

# Seleciona GPU se disponível
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Dispositivo utilizado:", device)

# Ordens testadas: A é m x n; B e C são n x p.
# Inclui matrizes quadradas e retangulares.
ordens = [
    (2, 3, 2),
    (4, 4, 4),
    (8, 8, 8),
    (16, 16, 16),
    (32, 32, 32),
    (64, 64, 64),
    (128, 128, 128),
    (256, 256, 256),
    (512, 512, 512),
    (1024, 1024, 1024),
]

resultados = []

for m, n, p in ordens:
  # Matrizes diferentes, geradas na GPU quando disponível
  A = torch.randint(1, 10, (m, n), device=device, dtype=torch.float64)
  B = torch.randint(1, 10, (n, p), device=device, dtype=torch.float64)
  C = torch.randint(1, 10, (n, p), device=device, dtype=torch.float64)

  # Lado esquerdo: A(B + C)
  # B + C: n*p adições
  # A @ (B+C): m*p*n multiplicações e m*p*(n-1) adições
  ops_esquerdo = n * p + m * p * n + m * p * (n - 1)

  # Lado direito: AB + AC
  # AB e AC: cada uma tem m*p*n multiplicações e m*p*(n-1) adições
  # Soma final: m*p adições
  ops_direito = 2 * m * p * n + 2 * m * p * (n - 1) + m * p

  # Calcula os dois lados na GPU/CPU para validar a igualdade
  lado_esquerdo = A @ (B + C)
  lado_direito = (A @ B) + (A @ C)

  iguais = torch.allclose(lado_esquerdo, lado_direito)

  percentual_a_mais = (
      (ops_direito - ops_esquerdo) / ops_esquerdo
  ) * 100

  resultados.append({
      "dimensoes": f"{m}x{n} · {n}x{p}",
      "m": m,
      "n": n,
      "p": p,
      "ops_esquerdo": ops_esquerdo,
      "ops_direito": ops_direito,
      "percentual_a_mais": percentual_a_mais,
      "iguais": iguais,
  })

# Exibe os resultados na tabela
print("\nComparação do custo computacional")
print("-" * 110)
print(
    f"{'Dimensões (A; B/C)':<22} {'Ops [A*(B+C)]':>16}"
    f" {'Ops [(A*B)+(A*C)]':>20} {'Diferença (%)':>18} {'Igualdade':>12}"
)
print("-" * 110)

for r in resultados:
  print(
      f"{r['dimensoes']:<22} {r['ops_esquerdo']:>16,}"
      f" {r['ops_direito']:>20,} {r['percentual_a_mais']:>17.2f}%"
      f" {str(r['iguais']):>12}"
  )

# --- CONFIGURAÇÃO E ORGANIZAÇÃO DO GRÁFICO ---
rotulos = [r["dimensoes"] for r in resultados]
percentuais = [r["percentual_a_mais"] for r in resultados]

fig, ax = plt.subplots(figsize=(11, 6), dpi=100)

# Linha principal com estilo aprimorado
ax.plot(
    rotulos,
    percentuais,
    marker="o",
    color="#1f77b4",
    linewidth=2.5,
    markersize=7,
    label="Ops adicionais de (AB + AC) em relação a A(B + C)",
)

# Adiciona os rótulos numéricos sobre os pontos no gráfico
for i, val in enumerate(percentuais):
  ax.annotate(
      f"{val:.1f}%",
      (rotulos[i], percentuais[i]),
      textcoords="offset points",
      xytext=(0, 8),
      ha="center",
      fontsize=9,
      fontweight="bold",
      color="#333333",
  )

# Títulos e rótulos organizados
ax.set_title(
    "Custo Computacional Adicional da Forma Expandida: (AB + AC) vs A(B + C)",
    fontsize=13,
    pad=15,
    fontweight="bold",
)
ax.set_xlabel("Dimensões das Matrizes: A (m×n), B e C (n×p)", fontsize=11, labelpad=10)
ax.set_ylabel("Operações Aritméticas a Mais (%)", fontsize=11, labelpad=10)

# Formatação do Eixo Y como porcentagem
ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))

# Ajustes do grid e limites dos eixos
ax.grid(True, linestyle="--", alpha=0.5, which="both")
ax.set_ylim(min(percentuais) - 5, max(percentuais) + 12)
plt.xticks(rotation=35, ha="right", fontsize=9.5)
plt.yticks(fontsize=9.5)

# Remoção de bordas desnecessárias
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()