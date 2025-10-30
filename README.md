Jogo Campo Minado em Python
Objetivo
Desenvolver um jogo simples de Campo Minado (Minesweeper) em Python, utilizando
matrizes (listas bidimensionais) e funções para organizar o código.
Descrição do Problema
Você deverá implementar uma versão simplificada do Campo Minado em modo texto.
O tabuleiro é representado por uma matriz, onde algumas posições contêm minas e as demais
são espaços seguros.
O jogador deve escolher coordenadas (linha e coluna) e tentar abrir as posições sem explodir
uma mina.
Regras do Jogo
1. O jogo começa com um tabuleiro oculto (exemplo: 5x5).
2. As minas são distribuídas aleatoriamente no tabuleiro.
3. O jogador escolhe posições digitando linha e coluna.
4. Se o jogador abrir:
o Uma célula sem mina, ela mostra quantas minas há nas 8 posições vizinhas.
o Uma célula com mina, o jogo termina ( Game Over).
5. O jogo termina quando:
o O jogador abre todas as células seguras ( Vitória), ou
o Explode uma mina ( Derrota).
Requisitos Técnicos
• O tabuleiro deve ser representado por uma matriz (lista de listas).
• Devem ser usadas funções para modularizar o código, por exemplo:
o criar_tabuleiro(linhas, colunas, qtd_minas)
o mostrar_tabuleiro(tabuleiro, revelado)
o contar_minas_vizinhas(tabuleiro, linha, coluna)
o jogar(tabuleiro)
• Use o módulo random para posicionar minas aleatoriamente.
• Utilize try/except para tratar erros de entrada (ex: coordenadas inválidas).
• O jogador deve ver o progresso a cada jogada.
