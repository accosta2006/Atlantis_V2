import chess
import random

class Engine:
    def __init__(self, tab, profmax, cor):
        self.tab = tab
        self.cor = cor
        self.profmax = profmax

    valorPeaoBranco = [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05,
        0.05, -0.05, -0.1, 0.0, 0.0, -0.1, -0.05, 0.05,
        0.0, 0.0, 0.0, 0.6, 0.6, 0.0, 0.0, 0.0,
        0.05, 0.05, 0.1, 0.65, 0.65, 0.1, 0.05, 0.05,
        0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1,
        0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ]

    valorPeaoPreto = list(reversed(valorPeaoBranco))

    valorCavaloBranco = [
        -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5,
        -0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4,
        -0.3, 0.0, 0.1, 0.15, 0.15, 0.1, 0.0, -0.3,
        -0.3, 0.05, 0.15, 0.2, 0.2, 0.15, 0.05, -0.3,
        -0.3, 0.0, 0.15, 0.2, 0.2, 0.15, 0.0, -0.3,
        -0.3, 0.05, 0.1, 0.15, 0.15, 0.1, 0.05, -0.3,
        -0.4, -0.2, 0.0, 0.05, 0.05, 0.0, -0.2, -0.4,
        -0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5
    ]

    valorCavaloPreto = list(reversed(valorCavaloBranco))

    valorBispoBranco = [
        -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2,
        -0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.05, -0.1,
        -0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1,
        -0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0, -0.1,
        -0.1, 0.05, 0.05, 0.1, 0.1, 0.05, 0.05, -0.1,
        -0.1, 0.0, 0.05, 0.1, 0.1, 0.05, 0.0, -0.1,
        -0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1,
        -0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2
    ]

    valorBispoPreto = list(reversed(valorBispoBranco))

    valorTorreBranca = [
        0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        -0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05,
        0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ]

    valorTorrePreta = list(reversed(valorTorreBranca))

    valorDamaBranca = [
        -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2,
        -0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1,
        -0.1, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1,
        -0.05, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05,
        0.0, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05,
        -0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1,
        -0.1, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, -0.1,
        -0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2
    ]

    valorReiBranco = [
        0.02, 0.03, 0.01, 0.0, 0.0, 0.1, 0.3, 0.2,
        0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2,
        -0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1,
        0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3,
        -0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3
    ]
    valorReiPreto = list(reversed(valorReiBranco))

    valorDamaPreta = list(reversed(valorDamaBranca))

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
