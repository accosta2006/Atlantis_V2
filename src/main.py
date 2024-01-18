import avaliacao as av
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board=board

    #play human move
    def jogHumana(self):
        try:
            jog = input("Insira uma jogada: ")
            self.board.push_san(jog)
        except:
            self.jogHumana()

    def jogEngine(self, profmax, cor):
        engine = av.Engine(self.board, profmax, cor)
        jogadaEngine = engine.melhorJogada()
        self.board.push(jogadaEngine)
        print("Jogada do engine: ", jogadaEngine, "\n")

    def startGame(self):
        cor=None
        while(cor!="b" and cor!="p"):
            cor = input("Escolhe a tua cor (b/p):\n")
        profmax=None
        while(isinstance(profmax, int)==False):
            profmax = int(input("Escolhe a profundidade:\n"))
        if cor=="p":
            while (self.board.is_checkmate()==False):
                self.jogEngine(profmax, ch.WHITE)
                self.jogHumana()   
        elif cor=="b":
            while (self.board.is_checkmate()==False):
                self.jogHumana()
                self.jogEngine(profmax, ch.BLACK)
                print()
        self.board.reset
        self.startGame()

novoTab= ch.Board()
game = Main(novoTab)
jogo = game.startGame()