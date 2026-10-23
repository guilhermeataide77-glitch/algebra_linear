import random

def multiplicar_matrizes(matriz_A, matriz_B):
    total_linhas_A = len(matriz_A)
    total_colunas_A = len(matriz_A[0])
    total_linhas_B = len(matriz_B)
    total_colunas_B = len(matriz_B[0])

    if total_colunas_A != total_linhas_B:
        raise ValueError("Multiplicação impossível: Colunas de A != Linhas de B")

    matriz_resultado = [
        [0 for _ in range(total_colunas_B)] for _ in range(total_linhas_A)
    ]
    contador_multiplicacoes = 0
    contador_adicoes = 0

    for i_linha in range(total_linhas_A):
        for j_coluna in range(total_colunas_B):
            soma_produto_escalar = 0
            for k_indice in range(total_colunas_A):
                elemento_A = matriz_A[i_linha][k_indice]
                elemento_B = matriz_B[k_indice][j_coluna]

                produto_parcial = elemento_A * elemento_B
                contador_multiplicacoes += 1

                if k_indice == 0:
                    soma_produto_escalar = produto_parcial
                else:
                    soma_produto_escalar = soma_produto_escalar + produto_parcial
                    contador_adicoes += 1

            matriz_resultado[i_linha][j_coluna] = soma_produto_escalar

    total_operacoes = contador_multiplicacoes + contador_adicoes
    return matriz_resultado, total_operacoes


def somar_matrizes(matriz_A, matriz_B):
    total_linhas = len(matriz_A)
    total_colunas = len(matriz_A[0])

    matriz_resultado = []
    contador_adicoes = 0

    for i_linha in range(total_linhas):
        linha_resultante = []
        for j_coluna in range(total_colunas):
            soma = matriz_A[i_linha][j_coluna] + matriz_B[i_linha][j_coluna]
            linha_resultante.append(soma)
            contador_adicoes += 1
        matriz_resultado.append(linha_resultante)

    return matriz_resultado, contador_adicoes


def processar_e_exibir(A, B, C):
    # --- LADO ESQUERDO: A * (B + C) ---
    B_mais_C, ops_soma_bc = somar_matrizes(B, C)
    A_mult_BC, ops_mult_A_bc = multiplicar_matrizes(A, B_mais_C)
    total_ops_esquerdo = ops_soma_bc + ops_mult_A_bc

    # --- LADO DIREITO: (A * B) + (A * C) ---
    A_mult_B, ops_mult_ab = multiplicar_matrizes(A, B)
    A_mult_C, ops_mult_ac = multiplicar_matrizes(A, C)
    soma_AB_AC, ops_soma_final = somar_matrizes(A_mult_B, A_mult_C)
    total_ops_direito = ops_mult_ab + ops_mult_ac + ops_soma_final

    # --- CÁLCULO PERCENTUAL ---
    if total_ops_esquerdo > 0:
        percentual_a_mais = ((total_ops_direito - total_ops_esquerdo) / total_ops_esquerdo) * 100
    else:
        percentual_a_mais = 0.0

    # --- EXIBIÇÃO ---
    print("=" * 60)
    print(f"Lado Esquerdo [A * (B + C)] -> Total de Operações: {total_ops_esquerdo}")
    print(f"Lado Direito [(A * B) + (A * C)] -> Total de Operações: {total_ops_direito}")
    print(f"Diferença Percentual Exata: {percentual_a_mais:.1f}%")
    print("=" * 60)


def main():
    tamanhos_quadrados = {
        '2': 4,
        '3': 8,
        '4': 16,
        '5': 32,
        '6': 64,
        '7': 128,
        '8': 256,
        '9': 512,
        '10': 1024
    }

    while True:
        print("\n==============================")
        print("       MENU DE MATRIZES       ")
        print("==============================")
        print("1. A (2x3), B (3x2), C (3x2)")
        print("2. Quadradas 4x4")
        print("3. Quadradas 8x8")
        print("4. Quadradas 16x16")
        print("5. Quadradas 32x32")
        print("6. Quadradas 64x64")
        print("7. Quadradas 128x128")
        print("8. Quadradas 256x256")
        print("9. Quadradas 512x512")
        print("10. Quadradas 1024x1024")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '0':
            print("Saindo...")
            break
        elif opcao == '1':
            print("\n--- Executando: A(2x3), B(3x2), C(3x2) ---")
            A = [[random.randint(0, 9) for _ in range(3)] for _ in range(2)]
            B = [[random.randint(0, 9) for _ in range(2)] for _ in range(3)]
            C = [[random.randint(0, 9) for _ in range(2)] for _ in range(3)]
            processar_e_exibir(A, B, C)
        elif opcao in tamanhos_quadrados:
            n = tamanhos_quadrados[opcao]
            print(f"\n--- Executando: Matrizes Quadradas de {n}x{n} ---")
            if n >= 512:
                print("(Aviso: Dimensões grandes em Python puro podem levar alguns minutos...)")
            A = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
            B = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
            C = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
            processar_e_exibir(A, B, C)
        else:
            print("Opção inválida! Escolha um número entre 0 e 10.")


if __name__ == "__main__":
    main()