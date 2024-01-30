import chess
import numpy as np
import time
import random

class Engine:
    def __init__(self, tab, profmax, cor):
        self.tab = tab
        self.cor = cor
        self.nodes_processed = 0
        self.profmax = profmax

    valorPeaoBranco = np.array([
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05,
        0.05, -0.05, -0.1, 0.0, 0.0, -0.1, -0.05, 0.05,
        0.0, 0.0, 0.0, 0.6, 0.6, 0.0, 0.0, 0.0,
        0.05, 0.05, 0.1, 0.65, 0.65, 0.1, 0.05, 0.05,
        0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1,
        0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ])

    valorPeaoPreto = np.array(list(reversed(valorPeaoBranco)))

    valorCavaloBranco = np.array([
        -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5,
        -0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4,
        -0.3, 0.0, 0.1, 0.15, 0.15, 0.1, 0.0, -0.3,
        -0.3, 0.05, 0.15, 0.2, 0.2, 0.15, 0.05, -0.3,
        -0.3, 0.0, 0.15, 0.2, 0.2, 0.15, 0.0, -0.3,
        -0.3, 0.05, 0.1, 0.15, 0.15, 0.1, 0.05, -0.3,
        -0.4, -0.2, 0.0, 0.05, 0.05, 0.0, -0.2, -0.4,
        -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5
    ])

    valorCavaloPreto = np.array(list(reversed(valorCavaloBranco)))

    valorBispoBranco = np.array([
    -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2,
    -0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.05, -0.1,
    -0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1,
    -0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0, -0.1,
    -0.1, 0.05, 0.05, 0.1, 0.1, 0.05, 0.05, -0.1,
    -0.1, 0.0, 0.05, 0.1, 0.1, 0.05, 0.0, -0.1,
    -0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1,
    -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2
])

    valorBispoPreto = np.array(list(reversed(valorBispoBranco)))

    valorTorreBranca = np.array([
        0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ])

    valorTorrePreta = np.array(list(reversed(valorTorreBranca)))

    valorDamaBranca = np.array([
        -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2,
        -0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1,
        -0.1, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1,
        -0.05, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05,
        0.0, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05,
        -0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1,
        -0.1, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, -0.1,
        -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2
    ])

    valorDamaPreta = np.array(list(reversed(valorDamaBranca)))

    valorReiBranco = np.array([
        0.02, 0.03, 0.01, 0.0, 0.0, 0.1, 0.3, 0.2,
        0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2,
        -0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1,
        0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3
    ])

    valorReiPreto = np.array(list(reversed(valorReiBranco)))

    valorReiBrancoFinal = np.array([
        0.5, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.5,
        -0.3, -0.3,  0.0,  0.0,  0.0,  0.0, -0.3, -0.3,
        -0.3, -0.1,  0.2,  0.3,  0.3,  0.2, -0.1, -0.3,
        -0.3, -0.1,  0.3,  0.4,  0.4,  0.3, -0.1, -0.3,
        -0.3, -0.1,  0.3,  0.4,  0.4,  0.3, -0.1, -0.3,
        -0.3, -0.1,  0.2,  0.3,  0.3,  0.2, -0.1, -0.3,
        -0.3, -0.2, -0.1,  0.0,  0.0, -0.1, -0.2, -0.3,
        -0.5, -0.4, -0.3, -0.2, -0.2, -0.3, -0.4, -0.5
    ])

    valorReiPretoFinal = np.array(list(reversed(valorReiBrancoFinal)))

    def ordenarJogadas(self):
        def ordenador(jog):
            self.tab.push(jog)
            valor = self.avalTab()
            self.tab.pop()
            return valor  
	    
        if self.cor == chess.WHITE:
            in_order = np.array(sorted(self.tab.legal_moves, key=ordenador, reverse=self.tab.turn==chess.BLACK))
        elif self.cor == chess.BLACK:
            in_order = np.array(sorted(self.tab.legal_moves, key=ordenador, reverse=self.tab.turn==chess.WHITE))

        if self.tab.fullmove_number < 4:
            filter = np.array(in_order[-10:])
        else:
            filter = np.array(in_order[-12:])

        return list(filter)

    def melhorJogada(self):
        return self.minimax(None, 1)

    def valorPecas(self, quad):
        valorPeca = 0

        if self.tab.piece_type_at(quad) == chess.PAWN:
            valorPeca = 1
        
        elif self.tab.piece_type_at(quad) == chess.KNIGHT:
            valorPeca = 3.3

        elif self.tab.piece_type_at(quad) == chess.BISHOP:
            valorPeca = 3.4
        
        elif self.tab.piece_type_at(quad) == chess.ROOK:
            valorPeca = 5
        
        elif self.tab.piece_type_at(quad) == chess.QUEEN:
            valorPeca = 9
        
        if self.tab.color_at(quad) == chess.BLACK:
            return valorPeca
        
        else:
            return -valorPeca

    def verificarFinal(self):
        damas = 0
        pecasmen = 0
        for i in chess.SQUARES:
            if self.tab.piece_type_at(i) == chess.BISHOP:
                pecasmen += 1
            
            elif self.tab.piece_type_at(i) == chess.KNIGHT:
                pecasmen += 1
            
            elif self.tab.piece_type_at(i) == chess.QUEEN:
                damas += 1
        
        if damas == 0 and pecasmen <= 2:
            return True
        
        else:
            return False

    def mapeamento(self):
        valor = 0
        final = self.verificarFinal()

        for i in chess.SQUARES:
            if self.tab.color_at(i) == chess.WHITE:    
                if self.tab.piece_type_at(i) == chess.PAWN:
                    valor += self.valorPeaoBranco[i]
                elif self.tab.piece_type_at(i) == chess.KNIGHT:
                    valor += self.valorCavaloBranco[i]
                elif self.tab.piece_type_at(i) == chess.BISHOP:
                    valor += self.valorBispoBranco[i]
                elif self.tab.piece_type_at(i) == chess.ROOK:
                    valor += self.valorTorreBranca[i]
                elif self.tab.piece_type_at(i) == chess.QUEEN:
                    valor += self.valorDamaBranca[i]
                elif self.tab.piece_type_at(i) == chess.KING and final == False:
                    valor += self.valorReiBranco[i]

                elif self.tab.piece_type_at(i) == chess.KING and final == True:
                    valor += self.valorReiBrancoFinal[i]
            else:
                if self.tab.piece_type_at(i) == chess.PAWN:
                    valor += self.valorPeaoPreto[i]
                elif self.tab.piece_type_at(i) == chess.KNIGHT:
                    valor += self.valorCavaloPreto[i]
                elif self.tab.piece_type_at(i) == chess.BISHOP:
                    valor += self.valorBispoPreto[i]
                elif self.tab.piece_type_at(i) == chess.ROOK:
                    valor += self.valorTorrePreta[i]
                elif self.tab.piece_type_at(i) == chess.QUEEN:
                    valor += self.valorDamaPreta[i]
                elif self.tab.piece_type_at(i) == chess.KING and final == False:
                    valor += self.valorReiPreto[i]
                
                elif self.tab.piece_type_at(i) == chess.KING and final == True:
                    valor += self.valorReiPretoFinal[i]

        return valor
    
    def abertura(self):
        if self.tab.fullmove_number <= 4:
            ab = 1/30 * self.tab.legal_moves.count()
        else:
            ab = 0

        return ab
    
    def avalTab(self):
        valor = 0

        for i in range(64):
            valor += self.valorPecas(chess.SQUARES[i])
        valor += self.mate() + self.abertura() + self.mapeamento() + 0.001 * random.random()
        
        return valor
    
    def mate(self):
        if self.tab.is_checkmate():
            if self.tab.turn == chess.WHITE:
                return 9999
            else:
                return -9999
        else:
            return 0
           
    def minimax(self, cand, prof, alpha=float("-inf"), beta=float("inf")):
        if (prof == self.profmax or self.tab.legal_moves.count() == 0):
            self.nodes_processed += 1
            return self.avalTab()
    
        else:
            jogadas = self.ordenarJogadas()
    
            novoCand = None
    
            if prof % 2 != 0:
                novoCand = float("-inf")
                for i in jogadas:
                    self.tab.push(i)
                    valor = self.minimax(novoCand, prof + 1, alpha, beta)
    
                    if valor > novoCand:
                        if prof == 1:
                            jog = i
                        novoCand = valor
    
                    alpha = max(alpha, novoCand)
    
                    if beta <= alpha:
                        self.tab.pop()
                        break
                    
                    self.tab.pop()
    
                if prof > 1:
                    return novoCand
                else:
                    return jog
    
            else:
                novoCand = float("inf")
                for i in jogadas:
                    self.tab.push(i)
                    valor = self.minimax(novoCand, prof + 1, alpha, beta)
    
                    if valor < novoCand:
                        novoCand = valor
    
                    beta = min(beta, novoCand)
    
                    if beta <= alpha:
                        self.tab.pop()
                        break
                    
                    self.tab.pop()
    
                if prof > 1:
                    return novoCand
                else:
                    return jog
    
def generateMove(fen, profmax, cor):
    tab = chess.Board(fen)
    engine = Engine(tab, profmax, cor)
    start_time = time.time()
    jog = engine.melhorJogada()
    end_time = time.time()

    duracao = end_time - start_time

    nodes_per_second = engine.nodes_processed / duracao

    print(f"Nodes per second: {nodes_per_second:.2f}")

    return jog
