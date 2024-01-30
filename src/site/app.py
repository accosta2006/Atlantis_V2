from flask import Flask
from flask import render_template
from flask import request
import chess
import atlantis

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/make_move', methods=['POST'])
async def make_move():
    fen = request.form.get('fen')
    board = chess.Board(fen)

    result = atlantis.generateMove(fen, 5, chess.BLACK)
    board.push(result)

    fen = board.fen()

    return {'fen': fen}

if __name__ == '__main__':
    app.run(port=5000,host="0.0.0.0", threaded=True)
