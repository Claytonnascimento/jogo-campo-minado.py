import random

def criar_tabuleiro(linhas, colunas, qtd_minas):

    tabuleiro = [[0 for _ in range(colunas)] for _ in range(linhas)]
    
    minas_colocadas = 0
    while minas_colocadas < qtd_minas:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if tabuleiro[linha][coluna] != "M":
            tabuleiro[linha][coluna] = "M"
            minas_colocadas += 1
    return tabuleiro

def contar_minas_vizinhas(tabuleiro, linha, coluna):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    contador = 0
    for i in range(linha-1, linha+2):
        for j in range(coluna-1, coluna+2):
            if 0 <= i < linhas and 0 <= j < colunas:
                if tabuleiro[i][j] == "M":
                    contador += 1
    return contador

def mostrar_tabuleiro(tabuleiro, revelado):
    print("   " + " ".join([str(i) for i in range(len(tabuleiro[0]))]))
    for i, linha in enumerate(tabuleiro):
        display = []
        for j, celula in enumerate(linha):
            if revelado[i][j]:
                if celula == "M":
                    display.append("M")
                else:
                    display.append(str(contar_minas_vizinhas(tabuleiro, i, j)))
            else:
                display.append("-")
        print(f"{i}  " + " ".join(display))

def jogar():
    linhas, colunas, qtd_minas = 5, 5, 5
    tabuleiro = criar_tabuleiro(linhas, colunas, qtd_minas)
    revelado = [[False for _ in range(colunas)] for _ in range(linhas)]
    celulas_seguras = linhas * colunas - qtd_minas
    abertas = 0

    while True:
        mostrar_tabuleiro(tabuleiro, revelado)
        try:
            linha = int(input("Escolha a linha: "))
            coluna = int(input("Escolha a coluna: "))
            if not (0 <= linha < linhas and 0 <= coluna < colunas):
                print("Coordenadas inválidas! Tente novamente.")
                continue
            if revelado[linha][coluna]:
                print("Essa célula já foi aberta! Escolha outra.")
                continue
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")
            continue

        if tabuleiro[linha][coluna] == "M":
            print("BOOM! Você acertou uma mina. Game Over!")

            for i in range(linhas):
                for j in range(colunas):
                    if tabuleiro[i][j] == "M":
                        revelado[i][j] = True
            mostrar_tabuleiro(tabuleiro, revelado)
            break
        else:
            revelado[linha][coluna] = True
            abertas += 1
            if contar_minas_vizinhas(tabuleiro, linha, coluna) == 0:
                abrir_adjacentes(tabuleiro, revelado, linha, coluna)
        
        if abertas == celulas_seguras:
            print("Parabéns! Você abriu todas as células seguras. Vitória!")
            mostrar_tabuleiro(tabuleiro, revelado)
            break

def abrir_adjacentes(tabuleiro, revelado, linha, coluna):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    for i in range(linha-1, linha+2):
        for j in range(coluna-1, coluna+2):
            if 0 <= i < linhas and 0 <= j < colunas and not revelado[i][j]:
                revelado[i][j] = True
                if contar_minas_vizinhas(tabuleiro, i, j) == 0 and tabuleiro[i][j] != "M":
                    abrir_adjacentes(tabuleiro, revelado, i, j)

jogar()
