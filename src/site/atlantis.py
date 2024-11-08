import chess
import random

class Engine:
    def __init__(self, tab, profmax, cor):
        self.tab = tab
        self.cor = cor
        self.profmax = profmax

     valorPeaoBranco = [
	    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
	    0.98, 1.34, 0.61, 0.95, 0.68, 1.26, 0.34, -0.11,
	    -0.06, 0.07, 0.26, 0.31, 0.65, 0.56, 0.25, -0.20,
	    -0.14, 0.13, 0.06, 0.21, 0.23, 0.12, 0.17, -0.23,
	    -0.27, -0.02, -0.05, 0.12, 0.17, 0.06, 0.10, -0.25,
	    -0.26, -0.04, -0.04, -0.10, 0.03, 0.03, 0.33, -0.12,
	    -0.35, -0.01, -0.20, -0.23, -0.15, 0.24, 0.38, -0.22,
	    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
     ]
	
     valorPeaoPreto = list(reversed(valorPeaoBranco))
	
     valorCavaloBranco = [
	    -1.67, -0.89, -0.34, -0.49, 0.61, -0.97, -0.15, -1.07,
	    -0.73, -0.41, 0.72, 0.36, 0.23, 0.62, 0.07, -0.17,
	    -0.47, 0.60, 0.37, 0.65, 0.84, 1.29, 0.73, 0.44,
	    -0.09, 0.17, 0.19, 0.53, 0.37, 0.69, 0.18, 0.22,
	    -0.13, 0.04, 0.16, 0.13, 0.28, 0.19, 0.21, -0.08,
	    -0.23, -0.09, 0.12, 0.10, 0.19, 0.17, 0.25, -0.16,
	    -0.29, -0.53, -0.12, -0.03, -0.01, 0.18, -0.14, -0.19,
	    -1.05, -0.21, -0.58, -0.33, -0.17, -0.28, -0.19, -0.23
     ]
	
     valorCavaloPreto = list(reversed(valorCavaloBranco))
	
     valorBispoBranco = [
	    -0.29, 0.04, -0.82, -0.37, -0.25, -0.42, 0.07, -0.08,
	    -0.26, 0.16, -0.18, -0.13, 0.30, 0.59, 0.18, -0.47,
	    -0.16, 0.37, 0.43, 0.40, 0.35, 0.50, 0.37, -0.02,
	    -0.04, 0.05, 0.19, 0.50, 0.37, 0.37, 0.07, -0.02,
	    -0.06, 0.13, 0.13, 0.26, 0.34, 0.12, 0.10, 0.04,
	    0.00, 0.15, 0.15, 0.15, 0.14, 0.27, 0.18, 0.10,
	    0.04, 0.15, 0.16, 0.00, 0.07, 0.21, 0.33, 0.01,
	    -0.33, -0.03, -0.14, -0.21, -0.13, -0.12, -0.39, -0.21
     ]
	
     valorBispoPreto = list(reversed(valorBispoBranco))
	
     valorTorreBranca = [
	    0.32, 0.42, 0.32, 0.51, 0.63, 0.09, 0.31, 0.43,
	    0.27, 0.32, 0.58, 0.62, 0.80, 0.67, 0.26, 0.44,
	    -0.05, 0.19, 0.26, 0.36, 0.17, 0.45, 0.61, 0.16,
	    -0.24, -0.11, 0.07, 0.26, 0.24, 0.35, -0.08, -0.20,
	    -0.36, -0.26, -0.12, -0.01, 0.09, -0.07, 0.06, -0.23,
	    -0.45, -0.25, -0.16, -0.17, 0.03, 0.00, -0.05, -0.33,
	    -0.44, -0.16, -0.20, -0.09, -0.01, 0.11, -0.06, -0.71,
	    -0.19, -0.13, 0.01, 0.17, 0.16, 0.07, -0.37, -0.26
     ]
	
     valorTorrePreta = list(reversed(valorTorreBranca))
	
     valorDamaBranca = [
	    -0.28, 0.00, 0.29, 0.12, 0.59, 0.44, 0.43, 0.45,
	    -0.24, -0.39, -0.05, 0.01, -0.16, 0.57, 0.28, 0.54,
	    -0.13, -0.17, 0.07, 0.08, 0.29, 0.56, 0.47, 0.57,
	    -0.27, -0.27, -0.16, -0.16, -0.01, 0.17, -0.02, 0.01,
	    -0.09, -0.26, -0.09, -0.10, -0.02, -0.04, 0.03, -0.03,
	    -0.14, 0.02, -0.11, -0.02, -0.05, 0.02, 0.14, 0.05,
	    -0.35, -0.08, 0.11, 0.02, 0.08, 0.15, -0.03, 0.01,
	    -0.01, -0.18, -0.09, 0.10, -0.15, -0.25, -0.31, -0.50
     ]
	
     valorDamaPreta = list(reversed(valorDamaBranca))
	
     valorPeaoPreto_eg = [
	    0, 0, 0, 0, 0, 0, 0, 0,
	    1.78, 1.73, 1.58, 1.34, 1.47, 1.32, 1.65, 1.87,
	    0.94, 1.00, 0.85, 0.67, 0.56, 0.53, 0.82, 0.84,
	    0.32, 0.24, 0.13, 0.05, -0.02, 0.04, 0.17, 0.17,
	    0.13, 0.09, -0.03, -0.07, -0.07, -0.08, 0.03, -0.01,
	    0.04, 0.07, -0.06, 0.01, 0.00, -0.05, -0.01, -0.08,
	    0.13, 0.08, 0.08, 0.10, 0.13, 0.00, 0.02, -0.07,
	    0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00
     ]
	
     valorPeaoBranco_eg = list(reversed(valorPeaoPreto_eg))
	
     valorCavaloPreto_eg = [
	    -0.58, -0.38, -0.13, -0.28, -0.31, -0.27, -0.63, -0.99,
	    -0.25, -0.08, -0.25, -0.02, -0.09, -0.25, -0.24, -0.52,
	    -0.24, -0.20,  0.10,  0.09, -0.01, -0.09, -0.19, -0.41,
	    -0.17,  0.03,  0.22,  0.22,  0.22,  0.11,  0.08, -0.18,
	    -0.18, -0.06,  0.16,  0.25,  0.16,  0.17,  0.04, -0.18,
	    -0.23, -0.03, -0.01,  0.15,  0.10, -0.03, -0.20, -0.22,
	    -0.42, -0.20, -0.10, -0.05, -0.02, -0.20, -0.23, -0.44,
	    -0.29, -0.51, -0.23, -0.15, -0.22, -0.18, -0.50, -0.64
     ]
	
     valorCavaloBranco_eg = list(reversed(valorCavaloPreto_eg))
	
     valorBispoPreto_eg = [
	    -0.14, -0.21, -0.11, -0.08, -0.07, -0.09, -0.17, -0.24,
	    -0.08, -0.04,  0.07, -0.12, -0.03, -0.13, -0.04, -0.14,
	     0.02, -0.08,  0.00, -0.01, -0.02,  0.06,  0.00,  0.04,
	    -0.03,  0.09,  0.12,  0.09,  0.14,  0.10,  0.03,  0.02,
	    -0.06,  0.03,  0.13,  0.19,  0.07,  0.10, -0.03, -0.09,
	    -0.12, -0.03,  0.08,  0.10,  0.13,  0.03, -0.07, -0.15,
	    -0.14, -0.18, -0.07, -0.01,  0.04, -0.09, -0.15, -0.27,
	    -0.23, -0.09, -0.23, -0.05, -0.09, -0.16, -0.05, -0.17
     ]
	
     valorBispoBranco_eg = list(reversed(valorBispoPreto_eg))
	
	# Endgame Rook Table
     valorTorrePreto_eg = [
	    0.13,  0.10,  0.18,  0.15,  0.12,  0.12,  0.08,  0.05,
	    0.11,  0.13,  0.13,  0.11, -0.03,  0.03,  0.08,  0.03,
	    0.07,  0.07,  0.07,  0.05,  0.04, -0.03, -0.05, -0.03,
	    0.04,  0.03,  0.13,  0.01,  0.02,  0.01, -0.01,  0.02,
	    0.03,  0.05,  0.08,  0.04, -0.05, -0.06, -0.08, -0.11,
	   -0.04,  0.00, -0.05, -0.01, -0.07, -0.12, -0.08, -0.16,
	   -0.06, -0.06,  0.00,  0.02, -0.09, -0.09, -0.11, -0.03,
	   -0.09,  0.02,  0.03, -0.01, -0.05, -0.13,  0.04, -0.20
     ]
	
     valorTorreBranco_eg = list(reversed(valorTorrePreto_eg))
	
	# Endgame Queen Table
     valorDamaPreto_eg = [
	    -0.09,  0.22,  0.22,  0.27,  0.27,  0.19,  0.10,  0.20,
	    -0.17,  0.20,  0.32,  0.41,  0.58,  0.25,  0.30,  0.00,
	    -0.20,  0.06,  0.09,  0.49,  0.47,  0.35,  0.19,  0.09,
	     0.03,  0.22,  0.24,  0.45,  0.57,  0.40,  0.57,  0.36,
	    -0.18,  0.28,  0.19,  0.47,  0.31,  0.34,  0.39,  0.23,
	    -0.16, -0.27,  0.15,  0.06,  0.09,  0.17,  0.10,  0.05,
	    -0.22, -0.23, -0.30, -0.16, -0.16, -0.23, -0.36, -0.32,
	    -0.33, -0.28, -0.22, -0.43, -0.05, -0.32, -0.20, -0.41
     ]
	
     valorDamaBranco_eg = list(reversed(valorDamaPreto_eg))
	
	# Endgame King Table
     valorReiPreto_eg = [
	    -0.74, -0.35, -0.18, -0.18, -0.11,  0.15,  0.04, -0.17,
	    -0.12,  0.17,  0.14,  0.17,  0.21,  0.31,  0.28,  0.04,
	     0.12,  0.13,  0.15,  0.14,  0.21,  0.28,  0.37,  0.40,
	     0.27,  0.17,  0.23,  0.25,  0.34,  0.37,  0.46,  0.38,
	     0.20,  0.28,  0.39,  0.52,  0.56,  0.64,  0.68,  0.72,
	     0.59,  0.65,  0.62,  0.73,  0.79,  0.78,  0.79,  0.89,
	     0.85,  0.81,  0.83,  0.81,  0.84,  0.88,  0.91,  0.88,
	     0.92,  0.92,  0.87,  0.85,  0.80,  0.76,  0.67,  0.61
     ]

     valorReiBranco_eg = list(reversed(valorReiPreto_eg))

     def ordenarJogadas(self):
        def ordenador(jog):
            self.tab.push(jog)
            valor = self.avalTab()
            self.tab.pop()
            return valor  
	    
        if self.cor == chess.WHITE:
            in_order = sorted(self.tab.legal_moves, key=ordenador, reverse=self.tab.turn==chess.BLACK)
        elif self.cor == chess.BLACK:
            in_order = sorted(self.tab.legal_moves, key=ordenador, reverse=self.tab.turn==chess.WHITE)

        if self.tab.fullmove_number < 10:
            filter = in_order[-7:]
        else:
            filter = in_order[-10:]

        return list(filter)

    def melhorJogada(self):
        return self.minimax(None, 1)

    def valorPecas(self, quad):
        valorPeca = 0

        if self.tab.piece_type_at(quad) == chess.PAWN:
            valorPeca = 1
        
        elif self.tab.piece_type_at(quad) == chess.KNIGHT:
            valorPeca = 3.2

        elif self.tab.piece_type_at(quad) == chess.BISHOP:
            valorPeca = 3.33
        
        elif self.tab.piece_type_at(quad) == chess.ROOK:
            valorPeca = 5.1
        
        elif self.tab.piece_type_at(quad) == chess.QUEEN:
            valorPeca = 8.8
        
        if self.tab.color_at(quad) != self.cor:
            return -valorPeca
        
        else:
            return valorPeca

    def mapeamento(self):
        valor = 0
        
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
                elif self.tab.piece_type_at(i) == chess.KING:
                    valor += self.valorReiBranco[i]
            
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
                elif self.tab.piece_type_at(i) == chess.KING:
                    valor += self.valorReiPreto[i]

        return valor
    
    def abertura(self):
        if self.tab.fullmove_number <= 10:
            if self.tab.turn == chess.WHITE:
                ab = 1/30 * self.tab.legal_moves.count()
            else:
                ab = 1/30 * self.tab.legal_moves.count()
        else:
            ab = 0
	
    
        return ab
    
    def avalTab(self):
        valor = 0

        for i in range(64):
            valor += self.valorPecas(chess.SQUARES[i])
        valor += self.mate() + self.abertura() + self.mapeamento() + 0.01 * random.random()
        
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
    jog = engine.melhorJogada()
    print(engine.abertura())
    return jog
